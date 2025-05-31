# Password token validation in Weblate Bypass

## Report Details
- **Report ID**: 243842
- **URL**: https://hackerone.com/reports/243842
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-06-27T21:10:31.715Z
- **Disclosed**: 2017-08-21T17:39:12.452Z

## Reporter
- **Username**: footstep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi,

This is a bypass of the fix on #229987. I could confirm that old link still works. Though you would need to use 2 browsers to pull this off

##Reproduction Steps
1. In Browser1, request a password reset
- Load link sent to your email in the same browser 
- Request another password reset in Browser2
- Load link sent to your email in the same browser 
- Change the password on Browser2
- Successful :D
- Change the password on Browser1
- Success :D
- Now login in any of the password with the last password.

Shuaib.


## Attachments
No attachments
