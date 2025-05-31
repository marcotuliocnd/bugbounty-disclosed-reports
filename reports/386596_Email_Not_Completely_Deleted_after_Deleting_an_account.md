# Email Not Completely Deleted after Deleting an account

## Report Details
- **Report ID**: 386596
- **URL**: https://hackerone.com/reports/386596
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-07-25T07:20:56.013Z
- **Disclosed**: 2019-03-25T13:45:19.354Z

## Reporter
- **Username**: 0xspade
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semmle

## Vulnerability Information
**Description:** 
If one of the user deletes their account it should be fully deleted in account while semmle doesnt delete it completely.

## Steps To Reproduce:
* Register email1
* After registering, confirm your account.
* once email1 is confirmed. add another email which we will name as email2
* Now Verify the email of email2.
* Delete account of email1 completely
* Now register email2
* after registering email2, confirm the account of email2
* after confirming with the link given in email2 it will automatically logged in and you will notice that email1 and email2 is in there and no need confirmation for email1.

**Fix/Remediation**
As per the rules, once you delete your data in an account it should be completely deleted. it should be another life for an account.

## Impact

User know that after deleting account to semmle, their data will be lost to semmle's database however, it still there which is a privacy violation.

## Attachments
No attachments
