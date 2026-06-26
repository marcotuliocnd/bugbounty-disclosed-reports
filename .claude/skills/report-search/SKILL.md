---
name: report-search
description: Search the local corpus of ~10k disclosed HackerOne bug bounty reports by vulnerability class, technique, program, or keyword. Use when the user wants precedent / prior art for a vuln type, asks "how was X exploited", wants examples of a bug class, or any other skill needs to ground itself in real disclosed reports. Returns ranked matches with report IDs, severity, program handle, and excerpts.
---

# report-search

Search the disclosed-report corpus in `reports/` (one Markdown file per HackerOne
report, format: title, Report Details, Reporter, Team/Handle, Vulnerability
Information / Summary / Steps To Reproduce / Impact).

This is the foundation skill — other bug-bounty skills call the same search helper.

## How to search

Use the shared helper. Always run it from the repo root:

```bash
python3 .claude/skills/_lib/search_reports.py "<query terms>" [options]
```

Options:
- `--severity critical,high` — filter by severity (critical/high/medium/low/none)
- `--handle shopify` — filter by program handle (substring match)
- `--limit 20` — max results (default 20)
- `--full` — include a body excerpt for each hit (read precedent without extra Reads)
- `--titles-only` — match only titles/filenames (high-precision, less recall)

Scoring weighs title/filename matches above body matches, rewards covering more
distinct query terms, and bonuses verbatim phrase hits.

## Workflow

1. Run a broad query first (e.g. `"cache deception"`, `"oauth account takeover"`).
2. If too many/noisy results, add `--titles-only` or a `--handle` / `--severity`
   filter. If too few, drop filters or use broader synonyms.
3. Pick the most relevant 3–8 reports and `Read` their full files for technique
   detail, or pass `--full` to skim excerpts inline.
4. Synthesize: report the patterns, link each claim to a specific `reports/<file>`
   and `#<id>` (`https://hackerone.com/reports/<id>`) so the user can verify.

## Tips
- Vuln-class synonyms matter: try both `ssrf` and `server side request forgery`,
  `idor` and `insecure direct object`, `ato` and `account takeover`.
- The corpus skews toward RCE, XSS, bypasses, CSRF, memory-safety, cache, SQLi,
  SSRF, IDOR, account-takeover, info-disclosure, rate-limit, subdomain-takeover.
- Always cite report IDs. Never invent a report that search didn't return.
