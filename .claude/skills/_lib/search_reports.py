#!/usr/bin/env python3
"""
Shared search helper over the disclosed-report corpus in reports/.

Used by the bug-bounty skills (report-search, recon-playbook, hunt,
program-intel, severity, write-report, poc). Ranks reports by how well their
title + body match the query terms, with optional filters on severity and
program handle.

Usage:
  search_reports.py "ssrf internal netblock" [--severity high,critical]
                    [--handle shopify] [--limit 20] [--full] [--titles-only]

Output: ranked list of matches. By default prints a compact line per report
(score, id, severity, handle, title). --full prints the matching report body
excerpts so the model can read precedent without extra file reads.
"""
import argparse
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
REPORTS_DIR = os.path.join(ROOT, "reports")

META_RE = {
    "id": re.compile(r"^- \*\*Report ID\*\*:\s*(.+)$", re.M),
    "url": re.compile(r"^- \*\*URL\*\*:\s*(.+)$", re.M),
    "severity": re.compile(r"^- \*\*Severity\*\*:\s*(.+)$", re.M),
    "handle": re.compile(r"^- \*\*Handle\*\*:\s*(.+)$", re.M),
    "state": re.compile(r"^- \*\*State\*\*:\s*(.+)$", re.M),
}


def meta(text, key):
    m = META_RE[key].search(text)
    return m.group(1).strip() if m else "N/A"


def title_of(text, fallback):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else fallback


def tokenize(s):
    return [t for t in re.split(r"[^a-z0-9]+", s.lower()) if len(t) > 1]


def iter_reports():
    for name in os.listdir(REPORTS_DIR):
        if not name.endswith(".md"):
            continue
        yield name, os.path.join(REPORTS_DIR, name)


def score(query_terms, title, body, filename):
    """Title/filename matches weigh more than body matches."""
    title_l = (title + " " + filename).lower()
    body_l = body.lower()
    s = 0
    matched = set()
    for term in query_terms:
        in_title = title_l.count(term)
        in_body = body_l.count(term)
        if in_title:
            s += 10 * min(in_title, 3)
            matched.add(term)
        if in_body:
            s += min(in_body, 5)
            matched.add(term)
    # phrase bonus: full query appears verbatim
    phrase = " ".join(query_terms)
    if phrase in body_l or phrase in title_l:
        s += 15
    # coverage bonus: rewards reports hitting many distinct query terms
    s += 8 * len(matched)
    return s


def excerpt(body, query_terms, width=350):
    body_l = body.lower()
    for term in query_terms:
        i = body_l.find(term)
        if i != -1:
            start = max(0, i - width // 3)
            chunk = body[start:start + width].replace("\n", " ")
            return "…" + chunk.strip() + "…"
    return body[:width].replace("\n", " ").strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="+", help="search terms")
    ap.add_argument("--severity", default="",
                    help="comma list: critical,high,medium,low,none")
    ap.add_argument("--handle", default="", help="program handle filter (substring)")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--full", action="store_true",
                    help="print body excerpts for top matches")
    ap.add_argument("--titles-only", action="store_true",
                    help="only match titles/filenames, ignore body")
    args = ap.parse_args()

    query = " ".join(args.query)
    query_terms = tokenize(query)
    if not query_terms:
        print("empty query", file=sys.stderr)
        sys.exit(1)

    sev_filter = {s.strip().lower() for s in args.severity.split(",") if s.strip()}
    handle_filter = args.handle.strip().lower()

    results = []
    for name, path in iter_reports():
        try:
            with open(path, "r", errors="replace") as f:
                text = f.read()
        except OSError:
            continue
        sev = meta(text, "severity").lower()
        handle = meta(text, "handle").lower()
        if sev_filter and sev not in sev_filter:
            continue
        if handle_filter and handle_filter not in handle:
            continue
        title = title_of(text, name)
        body = "" if args.titles_only else text
        sc = score(query_terms, title, body, name)
        if sc <= 0:
            continue
        results.append((sc, name, title, sev, handle, text))

    results.sort(key=lambda r: r[0], reverse=True)
    top = results[:args.limit]

    print(f"# {len(results)} matches for: {query}"
          + (f"  [severity={','.join(sev_filter)}]" if sev_filter else "")
          + (f"  [handle~{handle_filter}]" if handle_filter else ""))
    print()
    for sc, name, title, sev, handle, text in top:
        rid = meta(text, "id")
        print(f"[{sc:>3}] #{rid} ({sev}, {handle}) — {title}")
        print(f"      reports/{name}")
        if args.full:
            print(f"      {excerpt(text, query_terms)}")
        print()

    if not top:
        print("No matches. Try broader terms or drop filters.")


if __name__ == "__main__":
    main()
