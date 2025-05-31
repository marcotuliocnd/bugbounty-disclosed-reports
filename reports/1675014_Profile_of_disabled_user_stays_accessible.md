# Profile of disabled user stays accessible

## Report Details
- **Report ID**: 1675014
- **URL**: https://hackerone.com/reports/1675014
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-08-19T19:36:52.602Z
- **Disclosed**: 2022-11-26T06:53:30.529Z

## Reporter
- **Username**: mikaelgundersen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Userprofiles of disabled users keep staying accessible. on DOMAIN/u/USERID
This is quite undesirable as this user has no way to clear or modify this data in case they do not want it exposed anymore.
I'd assume profiles of disabled users would not be visible to ensure they can always be in control of their own data.

## Impact

exposure of user info that they can't control anymore.

## Attachments
No attachments
