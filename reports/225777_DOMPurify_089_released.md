# DOMPurify 0.8.9 released

## Report Details
- **Report ID**: 225777
- **URL**: https://hackerone.com/reports/225777
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-03T08:12:33.951Z
- **Disclosed**: 2020-03-01T14:05:56.195Z

## Reporter
- **Username**: lukasreschke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Got the following via the [DOMPurify-Security mailing list](https://lists.ruhr-uni-bochum.de/mailman/listinfo/dompurify-security):

```
*Intro*

A new version of DOMPurify was released today: DOMPurify 0.8.9

*Background*

DOMPurify showed weaknesses when handling both the recent Safari
DOMParser XSS and a Firefox mXSS when working with document.write().

Caused by a broken logical check, not all browser bugs were being worked
around correctly.

*Fix*

DOMPurify now performs better checks to mitigate both the Safari
DOMParser XSS and a Firefox mXSS when using document.write().

*Packages*

Updated packages are available here:
https://github.com/cure53/DOMPurify/releases/tag/0.8.9

EOF
```

## Attachments
No attachments
