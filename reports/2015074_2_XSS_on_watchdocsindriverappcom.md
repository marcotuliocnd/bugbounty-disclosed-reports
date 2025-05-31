# #2 XSS on watchdocs.indriverapp.com

## Report Details
- **Report ID**: 2015074
- **URL**: https://hackerone.com/reports/2015074
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2023-06-06T20:12:30.611Z
- **Disclosed**: 2024-04-11T08:33:21.051Z

## Reporter
- **Username**: maxdha
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
## Summary:
I've found an XSS on https://watchdocs.indriverapp.com/

## Steps To Reproduce:


  1. Visit https://watchdocs.indriverapp.com/webview/v1?phone=████████&token=██████████&service=cargo&locale=en&jwt=%22%3E%3Cimg%20src=raw%20onerror=alert(%22hackerone%22)%3E#/
  1. You'll get an XSS alert



## Supporting Material/References:
███

## Impact

Execute javascript on user browser

## Attachments
No attachments
