# potential denial of service attack via the locale parameter

## Report Details
- **Report ID**: 1746098
- **URL**: https://hackerone.com/reports/1746098
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-10-21T21:33:21.760Z
- **Disclosed**: 2022-11-28T18:31:27.075Z

## Reporter
- **Username**: benjaoming_realone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
In Django 3.2 before 3.2.16, 4.0 before 4.0.8, and 4.1 before 4.1.2, internationalized URLs were subject to a denial of service attack via the locale parameter, which is treated as a regular expression.

## Impact

By crafting a Python regex, a vulnerable site could suffer a DOS attack. The attack was most likely to happen on sites that processes locale IDs from URL parameters.

## Attachments
No attachments
