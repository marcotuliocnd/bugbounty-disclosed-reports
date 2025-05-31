# Libuv: Improper Domain Lookup that potentially leads to SSRF attacks

## Report Details
- **Report ID**: 2429894
- **URL**: https://hackerone.com/reports/2429894
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-03-21T18:47:15.488Z
- **Disclosed**: 2024-03-29T22:54:22.421Z

## Reporter
- **Username**: hunt1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I recently encountered a challenge in a CTF competition that led me to discover a vulnerability within Node.js, present in all versions after v10. Upon further investigation and code debugging, it became apparent that the vulnerability originated from its direct dependency, `libuv`.

I submitted a report to the Node.js team via HackerOne, and they subsequently connected me with the libuv team. This collaboration resulted in the identification and resolution of the vulnerability, now recorded as CVE-2024-24806.

## Impact

This vulnerability could allow an attacker to craft payloads that results in **SSRF** attacks and **Internal API Access**. Full explanation of vulnerability, PoC and sample scenarios are provided within the original report:
https://github.com/libuv/libuv/security/advisories/GHSA-f74f-cvh7-c6q6

## Attachments
No attachments
