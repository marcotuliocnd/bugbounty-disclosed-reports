# Old password can be new password

## Report Details
- **Report ID**: 229577
- **URL**: https://hackerone.com/reports/229577
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-18T09:58:45.364Z
- **Disclosed**: 2017-06-03T05:07:16.115Z

## Reporter
- **Username**: proabiral
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
### Affected Domain:
https://demo.weblate.org/ 

### Issue: 
The sites like Facebook and Google keeps tracks of old password and does not allow user to set password similar to their old passwords.
However in case of demo.weblate.org. It is possible for a user to set new password which is exactly similar to old passwords. 

### Impact:
Thought the impact of the issue is not high, it is always best practice to now allow so. 

### Solution:
The password history of the user should be tracked and user should not be allowed to set password which are similar to his old passwords.

## Attachments
No attachments
