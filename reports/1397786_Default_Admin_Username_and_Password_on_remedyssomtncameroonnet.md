# Default Admin Username and Password on remedysso.mtncameroon.net

## Report Details
- **Report ID**: 1397786
- **URL**: https://hackerone.com/reports/1397786
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-11-10T19:00:17.419Z
- **Disclosed**: 2022-09-01T20:50:32.925Z

## Reporter
- **Username**: dh0pe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
A Remedy Single Sign-On (Remedy SSO) Server is running at https://remedysso.mtncameroon.net/rsso/admin/#/.  
It is possible to access the application is using the default Administrator credentials.

## Steps To Reproduce:
Go to https://remedysso.mtncameroon.net/rsso/admin/#/ and login with credentials:
- Username: Admin
- Password: RSSO#Admin#

## Remediation
Change the password of the Admin user or disable the account.

## References
https://cwe.mitre.org/data/definitions/521.html

## Impact

A MNT Group Single Sign-On application was misconfigured in a manner that may have allowed a malicious user to login with the administrator user. The user is capable to perform any kind of configuration of the SSO system and retrieve sensitive information about organization users and infrastructure.

## Attachments
No attachments
