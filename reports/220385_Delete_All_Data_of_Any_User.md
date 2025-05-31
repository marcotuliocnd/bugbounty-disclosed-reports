# Delete All Data of Any User

## Report Details
- **Report ID**: 220385
- **URL**: https://hackerone.com/reports/220385
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-12T04:11:31.638Z
- **Disclosed**: 2020-03-01T14:10:36.716Z

## Reporter
- **Username**: dalt4sec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
If you are user have permission manage user(admin group), you can delete all data off website.
step:
1. Create new user with username is '.'.
2. Delete user, who just have been created.

Cause:
when you create new use, nextcloud app will make a new folder same name with username, which have been created. in folder (sourceweb/data)
Unfortunately, if username is '.', nextcloud app will make a new folder has name is '.'.
And when you delete user, nextcloud app will remote all folder 'data'.

## Attachments
- Screen_Shot_2017-04-12_at_10.58.30_AM.png
- Screen_Shot_2017-04-12_at_10.58.13_AM.png
