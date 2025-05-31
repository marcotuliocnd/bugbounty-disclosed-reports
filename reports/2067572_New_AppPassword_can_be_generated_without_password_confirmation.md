# New AppPassword can be generated without password confirmation

## Report Details
- **Report ID**: 2067572
- **URL**: https://hackerone.com/reports/2067572
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-07-12T19:28:03.088Z
- **Disclosed**: 2023-08-10T07:20:18.566Z

## Reporter
- **Username**: mikaelgundersen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
There is protection on https://github.com/nextcloud/server/blob/master/apps/settings/lib/Controller/AuthSettingsController.php#L122 that you must have recently entered your password to be able to generate a new AppPassword. However if an attacker would obtain access to your system (say you forgot to lock it when taking a quick bathroom break).

They can abuse a route to just obtain this. ```https://SERVER/ocs/v2.php/core/getapppassword```
Probably without you ever noticing.

## Impact

The password confirmation to generate an app password is effectively useless as it is trivial to bypass.

## Attachments
No attachments
