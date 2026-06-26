---
name: program-intel
description: Summarize the historical bug patterns for a specific bug bounty program/team using the local disclosed-report corpus. Use when the user names a program (e.g. shopify, gitlab, nextcloud, nodejs, uber, tiktok) and wants to know what's been found there, recurring weak spots, hot endpoints/assets, and what to avoid duplicating. Helps focus hunting and avoid dupes.
---

# program-intel

Profile a program from its disclosed reports so the user knows where to look and
what's already been reported.

## Workflow

1. **Resolve the handle.** Programs are identified by `Handle` in each report. List
   what's available / find the closest handle:
   ```bash
   grep -h "^- \*\*Handle\*\*:" reports/*.md | sort | uniq -c | sort -rn | grep -i "<name>"
   ```
   High-coverage handles include: deptofdefense, ibb, nextcloud, security, shopify,
   nodejs-ecosystem, gitlab, curl, x, vkcom, uber, shopify-scripts, tiktok, brave.

2. **Pull the program's reports:**
   ```bash
   python3 .claude/skills/_lib/search_reports.py "<broad term or *>" --handle <handle> --limit 60
   ```
   (Or to enumerate all of a program's reports, grep filenames after finding their
   IDs.) Read the highest-severity / most-disclosed ones in full.

3. **Synthesize an intel brief:**
   - **Volume & severity mix** — how many reports, breakdown by severity.
   - **Recurring vuln classes** — what keeps getting found (rank by frequency).
   - **Hot assets / endpoints / features** — subdomains, APIs, app areas that
     repeatedly show up.
   - **Notable chains** — high-impact reports worth studying, with `#<id>`.
   - **Where to hunt next** — under-tested adjacent surface, variations of past
     bugs, classes that appear elsewhere but not yet here.
   - **Dupe risk** — patterns already well-covered (likely to be dupes now).

## Rules
- Cite report IDs and `reports/<file>` for every claim.
- Distinguish "frequently found here" (mature, dupe-prone) from "found on similar
  programs but not here" (opportunity).
- Note the date range of the reports — old patterns may be patched.
