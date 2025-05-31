# User automatically logged in as Sys Admin user on https://███/Administration/Administration.aspx

## Report Details
- **Report ID**: 2190808
- **URL**: https://hackerone.com/reports/2190808
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-10-03T12:06:17.557Z
- **Disclosed**: 2023-11-03T17:15:45.291Z

## Reporter
- **Username**: mrr0b0t2324
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Any user can access the Administration section of the following URL: https://███
When the user goes to the following domain they are automatically logged in as "████████" which is a sys admin user on the application, this allows any user to upload files, add users, change permissions for users and delete users.

## References

## Impact

A malicious actor can modify other user's privileges on the application, add users, upload files, delete users. They can also add false information to the application which will jeopardize the integrity of the application. With administrator privileges they have no restrictions on the application.

## System Host(s)
https://█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Step 1) Go to the following URL: https://███ 
There you will se that you are logged in as a Sys Admin user

## Suggested Mitigation/Remediation Actions
The application should prompt a user to authenticate first before being able to do any other actions on the system.



## Attachments
No attachments
