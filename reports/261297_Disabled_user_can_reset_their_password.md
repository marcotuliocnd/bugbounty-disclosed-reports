# Disabled user can reset their password  

## Report Details
- **Report ID**: 261297
- **URL**: https://hackerone.com/reports/261297
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-08-18T09:25:33.954Z
- **Disclosed**: 2020-03-01T15:01:45.393Z

## Reporter
- **Username**: egrep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information

Steps:
1) Create user and disable the account
2) Goto reset password and enter disabled user's email address. Password reset link sent and he can reset the password using that link.
 
The point is : Disabled user can still access their account via reset password page. This is a very minor issue

## Attachments
No attachments
