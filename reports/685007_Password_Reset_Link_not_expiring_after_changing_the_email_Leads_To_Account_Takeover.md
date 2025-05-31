# Password Reset Link not expiring after changing the email Leads To Account Takeover

## Report Details
- **Report ID**: 685007
- **URL**: https://hackerone.com/reports/685007
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-30T10:37:07.483Z
- **Disclosed**: 2019-12-03T15:30:01.609Z

## Reporter
- **Username**: alishah
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
###Vulnerability:
Password Reset Link not expiring after changing the email

###Proof Of Concept:

1.Send the password reset link to your email.
2.Don`t open the password link just copy it and paste into any editor.
3.Open your account.
4.Go to your account settings.
5.Under account, you will see Account Overview.
6.Go to the Email and password Option and change the email and verify it.
7.After changing the email go to your password reset link which you copied.
8.Change your password.


BooM password Changed.

#####Thanks

## Impact

The attacker can still change the password if victim thinks his/her account is compromised and decided to change his/her email.

## Attachments
- Imgur.avi
