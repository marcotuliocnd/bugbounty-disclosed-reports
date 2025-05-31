# Bypass email verification when register new account

## Report Details
- **Report ID**: 265749
- **URL**: https://hackerone.com/reports/265749
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-09-04T09:35:10.047Z
- **Disclosed**: 2017-09-04T21:40:40.107Z

## Reporter
- **Username**: superman85
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi Legalrobot,

I have found a way to ignore Activate your account in my mailbox.
Here is my new acc: masterdzung@gmail.com and the activate link:
https://app.legalrobot-uat.com/email-verify?v=1Y5wiWwcvGcxznjlUsO-TuyEZgFpVbxMmQdfpEKrVTp

I never click on that link and i can still log in at app.legalrobot-uat.com

Here are steps to do:
1 - Register new account, you will get email to verify your email address
2 - Go to https://app.legalrobot-uat.com/sign-in, using Forgot password function
3 - Check your mailbox and you will get the link https://app.legalrobot-uat.com/password-reset/token?v=cFJ4kQuAfBFLqVmtyxuxxbNeudzpm4hZHwTDPcUNZd0
4 - After you changed new password. You can able to login your account without verified your email first


## Attachments
No attachments
