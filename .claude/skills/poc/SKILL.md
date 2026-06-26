---
name: poc
description: Build a proof-of-concept / reproduction steps for a candidate finding — HTTP requests (curl/Burp), payloads, or a small script — modeled on the "Steps To Reproduce" sections of the local disclosed-report corpus. Use when the user wants to confirm or demonstrate a bug, "build a PoC", "give me the curl/requests to reproduce", or "write a script to exploit this".
---

# poc

Produce a concrete, runnable proof of concept and clean reproduction steps for a
finding.

## Workflow

1. **Pin down the bug:** target endpoint/URL, method, required headers/auth/tokens,
   the parameter and payload, and the observable success signal (response field,
   status, side effect). Ask for what's missing rather than guessing.

2. **Borrow proven structure.** Look at how the same class was reproduced before:
   ```bash
   python3 .claude/skills/_lib/search_reports.py "<vuln class>" --full --limit 10
   ```
   Read a detailed example's Steps To Reproduce to mirror format and completeness.

3. **Build the PoC** in the most appropriate form:
   - **curl** — full command(s) with headers, ready to paste. Best default.
   - **Raw HTTP** — Burp-style request blocks when header order/raw bytes matter.
   - **Script** — Python (`requests`) or shell when the bug needs sequencing, a
     race, encoding tricks, or many iterations.
   - **HTML/JS** — a self-contained page for CSRF, clickjacking, postMessage,
     window.opener, DOM XSS, etc.

4. **Wrap with numbered reproduction steps:** pre-conditions (accounts/roles),
   each step, the exact expected result that proves the bug, and cleanup if needed.

## Rules
- Make it copy-paste runnable. Parameterize secrets/hosts as clearly named
  placeholders (`$TOKEN`, `victim.example.com`) — never bake in real credentials.
- Include the success indicator explicitly so a triager knows what "worked" means.
- Keep PoCs minimal and non-destructive; demonstrate impact without causing harm
  (no real data exf, no DoS volume, no changes to others' data beyond a marker).
- Only build PoCs for targets the user is authorized to test.
- Hand the finished PoC to `write-report` to assemble the full submission.
