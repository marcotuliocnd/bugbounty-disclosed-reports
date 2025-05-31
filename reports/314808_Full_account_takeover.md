# Full account takeover

## Report Details
- **Report ID**: 314808
- **URL**: https://hackerone.com/reports/314808
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-10T18:54:54.830Z
- **Disclosed**: 2020-03-19T15:26:51.759Z

## Reporter
- **Username**: sandeep_hodkasia
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reverb

## Vulnerability Information
Hello Team,

I got a security issue in reverb ios application which allows an attacker hack all users account.
Since iOS application is not in the scope but still I am reporting this, because this vulnerability may compromise all users account.
Please resolve this quickly. 

Desription:
Reverb ios application is not validating facebook `access_token` on the server side in login api, which allows an  attacker to hack all account using his own app access token.

Vulnerable request:
```
POST /api/auth/facebook HTTP/1.1
Host: reverb.com

{"fb_token":"EAAJ8Of8DF2IBAL5wChKjuRHSV2VEWpm7eCz2IMqqJy1lJJq8ooyQuKHcOXn6aZCZAIrCtClbrZBdUGhC3FbvncNYk1E0k7AOktEhDjUPwHPOh3x29JURSGIGPBlZCj5WlBHhHzI5KYAPbuXKiZBGTkKZABZATh9JjTqEDhRubYSEiTmhjeytx5moFH9naZB6XjZBRUMkmcbucFD9Vf8IoFZAD1LGngi6j5pXFGcTFPfBEudAZDZD"}
```
Here in vulnerable i used lyst app access token to login.

Steps to reproduce:
1. Replay vulnerable request in vulnerable request in burp suite
2. Use any other app access token .

Fix recommendation:
https://developers.facebook.com/docs/facebook-login/security

**(Bug in oauth flow)

## Impact

Attacker Can hack all users account using his own app access token

## Attachments
No attachments
