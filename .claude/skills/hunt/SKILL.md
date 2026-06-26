---
name: hunt
description: Hunt a target codebase or web app for a specific vulnerability class, primed with real exploitation patterns from the local disclosed-report corpus. Use when the user wants to find real vulnerabilities — "look for IDOR/SSRF/XSS/auth bypass in this code", "audit this for <vuln class>", "find bugs in <target>". Combines corpus-derived patterns with source/endpoint analysis and reports concrete candidate findings.
---

# hunt

Find real vulnerabilities of a given class in a target (source code, or a running
app's endpoints), using the disclosed-report corpus to know exactly what to look
for and how it gets exploited.

## Workflow

1. **Scope.** Confirm the target (which repo/dir, or which host/endpoints) and the
   vuln class(es) to hunt. If the user named a target host, confirm they have
   authorization (bug bounty scope, pentest, own asset) before active testing.

2. **Prime from precedent.** Pull real exploitation patterns:
   ```bash
   python3 .claude/skills/_lib/search_reports.py "<vuln class>" --full --limit 25
   ```
   Read the most detailed reports to learn the source/sink patterns, dangerous
   APIs, and bypasses that worked in the wild.

3. **Map the attack surface.**
   - Source: grep for the sinks/sources the corpus flagged (e.g. for SSRF: HTTP
     client calls taking user input; for SQLi: string-built queries; for XSS:
     unescaped output, `dangerouslySetInnerHTML`, `v-html`, template injection;
     for IDOR: object lookups by user-supplied id without authz checks).
   - Running app: enumerate endpoints/params and probe the patterns from the
     playbook (use `recon-playbook` if a full methodology helps).

4. **Investigate candidates.** For each potential finding, trace data flow from
   source to sink. Confirm the missing control. Distinguish real exploitability
   from false positives — verify the guard truly isn't there.

5. **Report findings** as a ranked list. For each:
   - **Title**, **vuln class**, **severity** (rough), **confidence**.
   - **Location** — `file:line` or endpoint.
   - **Why it's exploitable** — the data flow and the missing/insufficient control.
   - **Closest precedent** — `#<id> — <title>` from the corpus.
   - **Next step** — how to confirm / build a PoC (hand off to `poc`).

## Rules
- Only do active testing against targets the user is authorized to test.
- Prefer precision: a few well-traced, exploitable findings beat a wall of grep
  hits. Mark anything unconfirmed as "needs verification".
- Tie each finding to a concrete code path or request, not a vague suspicion.
- Hand off confirmed findings to `write-report`, and PoC building to `poc`.
