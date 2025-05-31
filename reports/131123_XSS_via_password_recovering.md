# XSS via password recovering

## Report Details
- **Report ID**: 131123
- **URL**: https://hackerone.com/reports/131123
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-15T15:27:55.012Z
- **Disclosed**: 2016-07-26T00:34:42.868Z

## Reporter
- **Username**: codequick
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
I found that xss can be executed if we provide xss payload as a password in Uber during password recovery.

Steps to follow:

1) Goto https://login.uber.com/forgot-password
2) Enter email and submit
3) Open the recover link you got
4) Enter Set password: <script>alert(document.domain);</script> and submit it
5) Click Show password

 XSS Executed.

Video and screenshot added

## Attachments
- Screencast_Saturday_16_April_2016_02_16_57__IST.webm
- Screenshot_from_2016-04-16_02-27-16.png
