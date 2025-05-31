# CSRF on https://apps.topcoder.com/wiki/users/editmyprofilepicture.action

## Report Details
- **Report ID**: 868572
- **URL**: https://hackerone.com/reports/868572
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-07T22:57:10.893Z
- **Disclosed**: 2020-12-14T16:00:02.165Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
Hi :) There is a CSRF on uploading user profile photo and saving it.

## Steps To Reproduce:
There is no CSRF token or anything like that on https://apps.topcoder.com/wiki/users/editmyprofilepicture.action . I added the poc html files below. Attacker can upload a new profile photo and update victim's profil photo.

Note: This only works to signed-in users. Because unauthorized users cannot upload attachments. There is a mistake on https://apps.topcoder.com/wiki/login.action now. If you encounter an error, you can login on main site (https://accounts.topcoder.com/member) then try.

## Impact

An attacker can force other users to change their profile pictures without their knowledge.

## Attachments
- csrf_upload.html
- csrf_save.html
