# Vine - overwrite account associated with email via android application

## Report Details
- **Report ID**: 187714
- **URL**: https://hackerone.com/reports/187714
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-02T14:08:03.500Z
- **Disclosed**: 2017-06-14T23:35:01.220Z

## Reporter
- **Username**: mishre
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,

It's possible to deny any user from logging in to his account by overwriting the password associated with his email. This is not an account takeover because while we do override the password associated with that specific mail we just login to a "new" account and not the user's original one.

Steps to reproduce:
===
1) Create first account via Vine for android with the mail firstaccountmail@gmail.com with the password Bla123
2) You can now see that you can login to the account created above.
3) Go and create another account - this time with a different password and with the mail Firstaccountmail@gmail.com - notice the CAPS (you can put the caps everywhere on the mail).
4) Finish the creation process - and see that it succeeds
5) Now go back and try to login with firstaccountmail@gmail.com and the password Bla123 and see that you can't. However, it's possible to login with firstaccountmail@gmail.com and the second password you have created - but you"ll login to the second created account.

## Attachments
No attachments
