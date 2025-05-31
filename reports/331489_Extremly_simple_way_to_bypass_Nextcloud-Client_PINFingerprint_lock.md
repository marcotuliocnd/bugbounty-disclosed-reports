# Extremly simple way to bypass Nextcloud-Client PIN/Fingerprint lock

## Report Details
- **Report ID**: 331489
- **URL**: https://hackerone.com/reports/331489
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-03-30T22:36:18.123Z
- **Disclosed**: 2019-07-26T07:24:06.851Z

## Reporter
- **Username**: volker_weissmann
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
(I'm sorry for my bad English, I'm German)
How to reproduce this security bug.

Step 1: Take a normal Android smartphone (maybe it also works on iOS, but I have not tested it yet).
Step 2: Install the official nextcloud-client.
Step 3: Set up nextcloud: Open the nextcloud app, tap on "Skip", enter the server-address, tap on "Grant access", enter username and password, tick the "Stay logged in" checkbox and tap on "Log in". If the OS asks you "Allow Nextcloud to access photos, media and files on your device?", tap on "ALLOW".
Step 4: Open a directory within the nextcloud app with important, secret files.
Step 5: Open the nextcloud app, tap on the hamburger button, enter the settings an switch either the "Passcode lock" or the "Fingerpring lock" option on. Close the nextcloud app

Now, nobody without this passcode or without this fingerprint can access the nextcloud-files, even if they have physical access to the device without screen lock. But I found a way to bypass this Passcode/Fingerprint lock:
Step 6: Open nextcloud, but do not enter the passcode/do not put your finger on the fingerprint-scanner
Step 7: Press the home button. (Nextcloud now runs in the background)
Step 8: Open the default  Android file manager (com.android.documentsui)
Step 9: Tap on the hamburger menu, then tap on the nextcloud logo.
Now you should see your nextcloud-files (Note: You can only see/read/modify a file, if you opened the directory with this file within the nextcloud-app at least once). This is a security bug, you shouldn't be able to access these files without the Passcode/Fingerprint lock. This makes the Passcode/Fingerprint lock a useless feature.

Note: If you once opened the secret file before, you can also access ist by opening /storage/emulated/0/Android/media/com.nextcloud.client/nextcloud/...

## Impact

If an attacker has physical access to an Android smartphone without a screen lock, but with nextcloud installed and set up, he can easily access the nextcloud-files even if the nextcloud app is locked with a fingerprint or pin. This shouldn't be possible.

## Attachments
No attachments
