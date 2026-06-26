---
name: severity
description: Estimate the severity of a vulnerability finding and produce a CVSS 3.1 vector + impact framing, calibrated against how similar findings were rated in the local disclosed-report corpus. Use when the user asks "how severe is this", "what CVSS score", "how should I rate this", or needs an impact statement for a report.
---

# severity

Rate a finding and justify it, anchored to how comparable disclosed reports were
scored.

## Workflow

1. **Understand the finding:** vuln class, pre-conditions (auth required? user
   interaction? cross-account?), what the attacker gains, and blast radius.

2. **Calibrate against precedent.** Pull similar reports and see how they were rated:
   ```bash
   python3 .claude/skills/_lib/search_reports.py "<vuln class + key qualifiers>" --full --limit 15
   ```
   Note the `Severity` field on the closest analogues. Adjust for differences in
   pre-conditions and impact.

3. **Score with CVSS 3.1.** Build the vector explicitly:
   - AV (Network/Adjacent/Local/Physical), AC (Low/High), PR (None/Low/High),
     UI (None/Required), S (Unchanged/Changed), C/I/A (None/Low/High).
   - Give the vector string, the base score, and the qualitative band.

4. **Output:**
   - **Proposed severity** (critical/high/medium/low) + numeric CVSS + vector.
   - **Justification** — one line per metric choice driving the score.
   - **Comparable reports** — 2–4 `#<id> (severity) — title` analogues from corpus.
   - **Impact statement** — 2–3 sentences suitable to paste into a report.
   - **What would raise/lower it** — e.g. "if unauthenticated, PR:N pushes to High".

## Rules
- Be honest about pre-conditions; they usually drive the score most.
- Map severity to the corpus's observed ratings, not just textbook CVSS — note when
  a program tends to rate a class higher/lower than CVSS implies.
- Don't inflate. State the realistic attacker model.
