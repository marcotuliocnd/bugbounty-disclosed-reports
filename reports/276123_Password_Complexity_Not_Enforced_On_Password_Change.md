# Password Complexity Not Enforced On Password Change

## Report Details
- **Report ID**: 276123
- **URL**: https://hackerone.com/reports/276123
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-10T14:38:29.036Z
- **Disclosed**: 2018-03-03T13:55:25.389Z

## Reporter
- **Username**: cosmopolitan_fi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
Hi!

Owncloud does not enforce password complexity on password change, so it's possible to use passwords of any size or form. 

In example I can set my password to be "a" or "qwerty".

__________________________________________________________________
How to reproduce:
Change your password to something that does not match your required complexity.
__________________________________________________________________

__________________________________________________________________
Proof Of Concept:
Login with my dummy account
account --> "testingdisp2@gmail.com"
password --> "q"
__________________________________________________________________

Thanks!
WdeM

## Attachments
No attachments
