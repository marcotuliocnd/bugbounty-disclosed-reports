# Reflected XSS when renaming a file with a vulnerable name which results in an error

## Report Details
- **Report ID**: 896522
- **URL**: https://hackerone.com/reports/896522
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-12T08:17:47.751Z
- **Disclosed**: 2021-03-01T11:02:05.545Z

## Reporter
- **Username**: yzy9951
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi,

It looks like Nextcloud team will accept the XSS protected by the CSP. (Report #896511)
Here is another XSS.
1. Rename an existing filename to <img src=x onerror=prompt(1)>.jpg.
2. Anyone tries to rename this <img src=x onerror=prompt(1)>.jpg with an invalid filename, like add a "\" in it, will trigger the XSS attack.
3. Need bypass the CSP.

Thanks

## Impact

Cross-Site Scripting

## Attachments
- XSS.png
- Add_PoC.png
