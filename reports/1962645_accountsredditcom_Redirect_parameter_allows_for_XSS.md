# [accounts.reddit.com] Redirect parameter allows for XSS

## Report Details
- **Report ID**: 1962645
- **URL**: https://hackerone.com/reports/1962645
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-04-26T16:43:39.352Z
- **Disclosed**: 2023-05-18T13:46:49.459Z

## Reporter
- **Username**: dvorakxl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
Hello team! I was tampering with the dest parameter in accounts.reddit.com and found out it is vulnerable to Cross Site Scripting once the victim performs the log in.

## Steps To Reproduce:
  1. Enter to the following link: ```https://accounts.reddit.com/?dest=javascript:alert(document.domain)```
  - If not signed in, the user will be promped to log in and after doing so XSS will excecute

{F2315850}
  - If user is logged into his account, following the link will also make the XSS pop up

{F2315847}

## Impact

An attacker could trick users into executing XSS, executing code and stealing their cookies only by them logging in.

## Attachments
- XSSsignedin.jpg
- XSSnotsignedin.jpg
