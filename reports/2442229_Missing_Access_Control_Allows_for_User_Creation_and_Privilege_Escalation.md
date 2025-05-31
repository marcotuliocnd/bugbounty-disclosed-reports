# Missing Access Control Allows for User Creation and Privilege Escalation 

## Report Details
- **Report ID**: 2442229
- **URL**: https://hackerone.com/reports/2442229
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-03-31T02:54:51.546Z
- **Disclosed**: 2024-07-19T14:37:34.538Z

## Reporter
- **Username**: bulldawg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello,

The RSI Test Environment application at https://███████████████/ords/f?p=842:1 does not enforce access controls on the user management endpoint. This allows any unauthenticated person to both create new users as well as give them the administrator role. This then provides access to https://███████████████/ords/f?p=303 as an administrator.

The user management endpoint can be accessed at https://████████████/ords/f?p=842:9:::::: 

I have attached screenshots which show this misconfiguration.

If there are any questions or concerns please let me know as I am more than happy to provide additional information!

## Impact

This is a critical security issue which poses risk to the confidentiality and integrity of data within the ███████████████ application. An attacker would be able to view, modify, and/or delete the restricted information and documents within the application as well as manage other user accounts. This provides unauthorized access that is otherwise restricted to USG-authorized individuals per the disclaimer.

## System Host(s)
█████████████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Visit https://█████████████████/ords/f?p=842:9, which is the user management endpoint for the environment.
2. Under "Add New User", enter an email address, first name, last name, and select an Agency.
3. Under "Assign User Roles", select the newly created user and apply the administrator role.
4. Retrieve the credentials for the new account that were sent to the email address entered.
5. Go to https://███████████/ords/f?p=303 and login using the credentials.
6. Change to a new password on prompt.
7. View the logged in username in the top right with the Administrator role.

## Suggested Mitigation/Remediation Actions
Enforce access controls on page 9 of the application with an ID of 842.



## Attachments
No attachments
