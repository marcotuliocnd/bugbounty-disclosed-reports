---
name: recon-playbook
description: Build a hunting checklist / methodology for a vulnerability class or target tech stack, distilled from the local disclosed-report corpus. Use when the user asks "how do I hunt for X", "give me a methodology / checklist for X", "what should I test on a <tech> target", or wants a recon plan grounded in real disclosed bugs (e.g. SSRF, IDOR, rate-limit, cache deception, subdomain takeover, OAuth).
---

# recon-playbook

Turn the disclosed-report corpus into an actionable hunting playbook for a given
vuln class or target type.

## Workflow

1. **Gather precedent.** Use the shared search helper to pull the relevant reports:
   ```bash
   python3 .claude/skills/_lib/search_reports.py "<vuln class or tech>" --full --limit 30
   ```
   Run a few variations (synonyms, related techniques). Read the highest-signal
   reports in full when their Steps To Reproduce look detailed.

2. **Extract patterns** across the reports:
   - Where the bug lived (endpoint shapes, parameters, headers, features).
   - The exact trigger / payload / bypass that worked.
   - Pre-conditions and the variations attackers tried before one worked.
   - How impact was escalated.

3. **Produce a playbook** with these sections:
   - **Where to look** — concrete endpoints, params, headers, features to probe.
   - **Test cases / payloads** — ordered from quickest to most involved, with the
     actual payloads/requests seen in reports.
   - **Bypass tricks** — encodings, parser quirks, allowlist evasions that worked.
   - **Escalation** — how to turn a weak signal into demonstrable impact.
   - **Tooling** — what to use (Burp, ffuf, nuclei, custom scripts) per step.
   - **Precedent** — bullet list of `#<id> — <title>` the playbook draws from, each
     with its `reports/<file>` path so the user can read the original.

## Rules
- Ground every checklist item in at least one real report; cite the ID.
- Order the checklist by effort-to-payoff (cheap, high-signal checks first).
- Keep payloads copy-pasteable. Note pre-conditions explicitly.
- If the corpus has thin coverage for the class, say so and supplement with general
  knowledge clearly labeled as not-from-corpus.
