# Able to bypass "Device credentials" Lock

## Report Details
- **Report ID**: 507172
- **URL**: https://hackerone.com/reports/507172
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-09T16:46:38.527Z
- **Disclosed**: 2019-07-26T07:47:28.854Z

## Reporter
- **Username**: blackdex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Prepare
1. Enable "Device credentials" lock via the settings. (I'm using fingerprint in my case)
2. Test if this works by closing the app and open it again.
3.  If this works close the app again, do a force close to make sure the application is closed.

## The next steps need to be done quickly right after each other.
1. Make sure you are able to quickly start the Nextcloud app, i put mine on the homescreen.
2. Now quickly open the app and press backspace and open the app and press backspace, do this a few times right after each other until you see a flash of the folder list.
3. After you have seen this folder tree flash, you can start the application without any credentials.

Note: This only happens when doing this fast, else this won't work.
I added a adb logcat output of the nextcloud process i started during my test.

## Impact

The impact is that someone without the correct credentials but an unlocked phone is still able to login to the Nextcloud app and see all the files of the user.

## Attachments
- nextcloud-bug-adb
