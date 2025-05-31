# Self-XSS on partners.uber.com

## Report Details
- **Report ID**: 138622
- **URL**: https://hackerone.com/reports/138622
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-13T13:12:00.206Z
- **Disclosed**: 2016-07-26T00:35:43.594Z

## Reporter
- **Username**: cyber__sec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Hi,

I found a reflected XSS vulnerability in password reset page https://partners.uber.com/reset-password. 
I have tested this vulnerability in the latest Chrome and Firefox browsers.

Reproduction Steps:
1- Go to https://login.uber.com/forgot-password and reset password. Then, Click password reset link on your mailbox.
2- Paste  "><img src=x onerror=prompt(document.domain)>   as your new password and submit.
3- Wait and see XSS payload fired.

Also I added screenshots.

Thanks,

## Attachments
- 1.png
- 2.png
