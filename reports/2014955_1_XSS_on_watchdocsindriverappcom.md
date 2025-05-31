# #1 XSS on watchdocs.indriverapp.com

## Report Details
- **Report ID**: 2014955
- **URL**: https://hackerone.com/reports/2014955
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-06-06T17:18:15.473Z
- **Disclosed**: 2024-04-11T09:01:27.222Z

## Reporter
- **Username**: maxdha
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
## Summary:
XSS on watchdocs.indriverapp.com

## Steps To Reproduce:

  1. Go to https://watchdocs.indriverapp.com/webview/v1/refresh-jwt?redirect=%22%3E%3Cimg%20src=faw%20onerror=alert(1)%3E
  2. An alert window will popup
  




{F2401964}

## Impact

Allow executing js code on users browsers

## Attachments
- image.png
