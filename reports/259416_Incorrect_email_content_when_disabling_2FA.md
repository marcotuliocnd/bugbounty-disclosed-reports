# Incorrect email content when disabling 2FA

## Report Details
- **Report ID**: 259416
- **URL**: https://hackerone.com/reports/259416
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-13T12:57:15.922Z
- **Disclosed**: 2017-08-15T05:18:37.554Z

## Reporter
- **Username**: goodhackonly
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hello @team,

I found that there is false statement in the 2FA disabled mails sent by the legalrobot.

what is the issue?
When user is disabling the 2fa authenticator app Registration.He will get a notification regarding the Disabling of the 2FA .the mail structure is like this:
**
2FA disabled

The 2FA Authenticator App registration was just removed from your Legal Robot (TEST) account. 2-Factor Authentication is still enabled since you registered a security key.

**


but the user haven't registered any security key.

steps to reproduce:
1.Create a new account.
2.login to your account and enable the 2FA authentication.
3.dont make any changed to the FIDO U2F Security Key .
4.disable the 2FA Authenticator App registration.
5.now you will receive mail from legalrobot updating about the 2FA disabled.
6.but still you can find the statement " 2-Factor Authentication is still enabled since you registered a security key."

This will create confusion among the users and the trust will break.

Kindly find the attached video poc for better understanding.

Thanks!



## Attachments
- legalrobot_poc.mkv
