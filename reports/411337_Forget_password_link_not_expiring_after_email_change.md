# Forget password link not expiring after email change.

## Report Details
- **Report ID**: 411337
- **URL**: https://hackerone.com/reports/411337
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-19T05:13:33.396Z
- **Disclosed**: 2018-09-20T06:42:43.088Z

## Reporter
- **Username**: imran_nisar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
I found a token miss configuration flaw in chaturbate.com, When we reset password for a user a link is sent to the registered email address but incase it remain unused and email is updated by user from setting panel then too that old token [reset link] sent at old email address remains valid.

#A better explanation

1- User use reset feature to get reset link [Email : etc@x.com]
2- User came to know about his old password so remain the link unused and the token not expires 
3- Now User changes his email from control panel [New email : etc11@z.com]
4- But the old reset still remains valid after email change

In-case an attacker able to get access to user's old email account he can hack his chaturbate account too via that link, so expiring the token at email change will be a better practice

## Impact

The attacker can still change the password if victim thinks his/her account is compromised and decided to chnage his email

## Attachments
No attachments
