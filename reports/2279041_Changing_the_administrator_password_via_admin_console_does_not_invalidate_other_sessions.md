# Changing the administrator password via admin console does not invalidate other sessions

## Report Details
- **Report ID**: 2279041
- **URL**: https://hackerone.com/reports/2279041
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-12-09T06:55:00.076Z
- **Disclosed**: 2024-05-20T07:57:41.730Z

## Reporter
- **Username**: osama-hamad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
- Login to your admin account from the browser. 
- Change the password of admin account via ``` ./resetAdministratorPassword``` as described in https://portswigger.net/burp/documentation/enterprise/managing-users-and-permissions/reset-admin-password

- Go back to your browser session and confirm the session still valid. 

Screen recording proof of concept attached : ████

## Impact

The impact is minimal but effective, assuming an attacker got in and changed the password and the owner realized that and tried to change the password of its account ( he have 1 option to change it via the admin console since he don't have access to its account via the dashboard ) . The admin will change the password of the account but the attacker will still have access to the administrator account as an administrator since its session didn't got invalidated.

## Attachments
No attachments
