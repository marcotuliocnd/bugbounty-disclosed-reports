# XSS in Email Input [intensedebate.com]

## Report Details
- **Report ID**: 1037714
- **URL**: https://hackerone.com/reports/1037714
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-18T17:09:13.205Z
- **Disclosed**: 2020-12-26T10:58:15.527Z

## Reporter
- **Username**: ahmd_halabi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
I found an XSS in Email input. This input is not sanitized like other inputs allowing user to execute xss payloads.

## Platform(s) Affected:
https://www.intensedebate.com/edit-user-account

## Steps To Reproduce:
1. Navigate to your account.
2. In email address, add the below payload next to your email.
`"><img src=x onerror=alert(document.cookie);>`

## Supporting Material/References:
██████

## Impact

Reflected XSS, An attacker can execute malicious javascript codes on the target application (email input specifically). It is highly recommended to fix this one because it is found in sensitive input (email).

Kind Regards.

## Attachments
No attachments
