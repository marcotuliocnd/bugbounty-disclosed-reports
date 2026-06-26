# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is **not an application** — it is a research corpus plus a set of skills that mine it. Two parts:

- `reports/` — ~10,000 publicly disclosed HackerOne bug bounty reports, one Markdown file per report. Filenames are `<reportID>_<slugified_title>.md`. This is the data; it is read, never "built" or "tested".
- `.claude/skills/` — the working tooling. A set of bug-bounty skills (hunt, poc, severity, write-report, report-search, recon-playbook, program-intel) that ground their output in the corpus via a single shared search helper.

`targets/` holds working copies of code/sourcemaps for whatever target is currently being audited. It is **gitignored** — do not assume its contents are tracked or permanent, and do not commit them.

## Report file format (relied on by the tooling)

Every file in `reports/` follows the same structure, and the search helper parses these exact fields with regexes — preserve them when adding or editing reports:

```
# <Title>

## Report Details
- **Report ID**: <id>
- **URL**: https://hackerone.com/reports/<id>
- **State**: <Open/Closed>
- **Severity**: <critical|high|medium|low|none>
- **Submitted**: <ISO date>
- **Disclosed**: <ISO date>

## Reporter
- **Username**: ...

## Team
- **Handle**: <program handle, e.g. shopify, tiktok, gitlab>

## Vulnerability Information
<Summary / Steps To Reproduce / Impact — may be empty for some reports>
```

`Severity` and `Handle` are the two filterable fields. Many reports have an empty `Vulnerability Information` body (only metadata) — don't treat that as a parse failure.

## The search helper is the backbone

All corpus access goes through one script. Run it from the repo root:

```bash
python3 .claude/skills/_lib/search_reports.py "<query terms>" [options]
```

Options: `--severity critical,high` · `--handle shopify` · `--limit 20` · `--full` (print body excerpts inline) · `--titles-only` (high precision).

Scoring weighs title/filename matches ~10x over body matches, adds a coverage bonus for hitting more distinct query terms, and a bonus for verbatim phrase hits. There is no index/database — it scans all files on every run, which is fine at this corpus size.

Every skill (hunt, severity, write-report, etc.) calls this same helper to find precedent before producing output. When extending a skill, reuse the helper rather than re-globbing `reports/` yourself.

## Working conventions for this corpus

- **Always cite report IDs.** Claims about "how X was exploited" must link to a specific `reports/<file>` and `#<id>` (`https://hackerone.com/reports/<id>`). Never invent a report the search didn't return — fabricated precedent defeats the point of the corpus.
- **Synonyms matter** for recall: try both `ssrf` / `server side request forgery`, `idor` / `insecure direct object`, `ato` / `account takeover`.
- Corpus skew (useful for knowing what precedent exists): RCE, XSS, auth/bypass, CSRF, memory-safety, cache deception, SQLi, SSRF, IDOR, account-takeover, info-disclosure, rate-limit, subdomain-takeover.

## Skills overview

Skills live in `.claude/skills/<name>/SKILL.md`. Each is invoked via the Skill tool / `/<name>`. They compose: `report-search` is the foundation the others build on. `hunt` audits a target for a vuln class primed with corpus patterns; `recon-playbook` produces a methodology/checklist; `program-intel` summarizes a program's historical bug patterns; `severity` calibrates CVSS against how similar findings were rated; `write-report` / `poc` produce disclosure-quality writeups and reproductions styled on real corpus entries.
