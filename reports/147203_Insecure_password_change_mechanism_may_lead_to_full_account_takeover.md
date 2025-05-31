# Insecure password change mechanism may lead to full account takeover

## Report Details
- **Report ID**: 147203
- **URL**: https://hackerone.com/reports/147203
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-25T14:55:51.458Z
- **Disclosed**: 2016-07-23T17:34:41.085Z

## Reporter
- **Username**: shawarkhan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fantasytote

## Vulnerability Information
###Description:
The password change mechanism which is located at https://www.fantasytote.com/users/edit is insecure as there is no old password field deployed in it. Any unauthorized user can access the account and can change the password directly without knowing the old password. The current password or old password field is necessary because it prevents any unauthorized user from changing the password.

Facebook, Google and many other companies have deployed this fix.

###Steps to Reproduce:

* Goto https://www.fantasytote.com
* Sign in 
* Goto https://www.fantasytote.com/users/edit
* You will see password change area
* Change the password and it will be changed without prompting the old password

###Fix / Patch:
Deploy a mechanism that asks the user for the old password in order to change his password. If the user knows his old password, the password should be changed otherwise not.

Waiting for positive response,
Thanks.

## Attachments
No attachments
