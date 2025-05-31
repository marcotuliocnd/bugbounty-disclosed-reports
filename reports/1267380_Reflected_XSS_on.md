# Reflected XSS on [█████████]

## Report Details
- **Report ID**: 1267380
- **URL**: https://hackerone.com/reports/1267380
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-18T12:41:02.173Z
- **Disclosed**: 2022-04-07T20:09:29.406Z

## Reporter
- **Username**: saajanbhujel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary:
Hi security team members,

I found a reflected XSS on the URL

## Impact

1. An attacker can steal the victim's cookies.
2. An attacker can execute JS code.

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Navigate to this link:- https://██████████/██████=%3C/script%3E%3Cscript%3Ealert(document.domain)%3C/script%3E
2. Then, it will execute.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
