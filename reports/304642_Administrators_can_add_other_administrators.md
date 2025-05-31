# Administrators can add other administrators

## Report Details
- **Report ID**: 304642
- **URL**: https://hackerone.com/reports/304642
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-01-14T00:09:14.760Z
- **Disclosed**: 2020-05-11T18:32:29.634Z

## Reporter
- **Username**: gamliel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
Because I know you like crayons here's a token of my appreciation... **:D** {F253771}

Concrete5 version: **8.3.1**
Release date: **12/20/17**
Where: **Core CMS**

###Vulnerability: Privilege Escalation **(OTG-AUTHZ-003)**
Privilege escalation occurs when a user gets to access more resources than is normally allowed when it should have been protected from the application.

**Vertical escalation:** Occurs when the attacker get access to accounts with high level privileges.
**Horizontal escalation:** Occurs when the attacker get access to other accounts with same privileges level.

Vertical escalation is not possible, let's say that Admin user is safe. With the Admin user created other users and some of them were added to Administrators group. I opened other window browser in private mode and logged as **admin2** user (This user was added to administrators group).
As **admin2** user went to `Dashboard -> Members -> Search Users` and clicked on a link corresponding to other user (user **admin3**) with administrator privileges and I'm able to do actions that can lead to takeover other administrator accounts.

## Impact

**High**. A disgruntled user with Administration privileges can change password, email, username, deactivate account or delete other users in the Administrators group. It happens because an user in the Administrators group can create users and add them to his same level group.

Recommendations
============
Only **Admin** must be able to add or make changes to users in the **Administrators** group.

Kind regards,
**Gamliel Hernadez.**

## Attachments
- crayons.jpg
