---
name: write-report
description: Write a disclosure-quality bug bounty report for a finding, matching the HackerOne report format used in this repo's corpus. Use when the user has a vulnerability and wants it written up — "write a report for this", "draft a HackerOne submission", "turn this finding into a report". Produces title, summary, steps to reproduce, impact, severity, and remediation, few-shot styled on real disclosed reports.
---

# write-report

Draft a clear, triager-friendly bug bounty report that matches the structure of
the disclosed reports in `reports/`.

## Workflow

1. **Collect the finding details** from the user / conversation: target asset, vuln
   class, where it lives, how to trigger it, what the impact is, any PoC artifacts
   (requests, responses, screenshots). Ask only for what's genuinely missing.

2. **Find a style/structure exemplar.** Pull 2–3 strong same-class reports to match
   tone and detail level:
   ```bash
   python3 .claude/skills/_lib/search_reports.py "<vuln class>" --severity high,critical --full --limit 8
   ```
   Read one or two in full to mirror how good reports phrase impact and steps.

3. **Write the report** in this structure (Markdown):

   ```
   # <Concise, specific title: vuln + where + impact>

   ## Summary
   What the bug is, where, and why it matters — in 2–4 sentences.

   ## Steps To Reproduce
   1. Numbered, exact, copy-pasteable. Include full HTTP requests in code blocks,
      concrete URLs/params, and account/role pre-conditions.
   2. ...

   ## Proof of Concept
   Requests/responses, payloads, or a short script. (Use the `poc` skill to build.)

   ## Impact
   Concrete attacker capability and blast radius. Tie to business risk. Note
   pre-conditions and whether it's one-click / unauthenticated / cross-account.

   ## Severity
   Proposed rating + CVSS vector (use the `severity` skill to calibrate).

   ## Remediation
   Specific, actionable fix(es).
   ```

## Rules
- Be precise and reproducible: a triager must be able to follow the steps verbatim.
- Lead the title and summary with impact, not mechanism.
- No exaggeration — claim only what the PoC demonstrates; state pre-conditions.
- Keep it self-contained. Redact real secrets/PII from any captured artifacts.
- Don't fabricate steps or responses you haven't actually established.
