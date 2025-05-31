# Android content provider exposes password-protected share password hashes

## Report Details
- **Report ID**: 242727
- **URL**: https://hackerone.com/reports/242727
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-23T20:00:05.583Z
- **Disclosed**: 2020-01-31T16:18:03.107Z

## Reporter
- **Username**: netranger
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary
Nextcloud Android client v1.4.3 has a globally available content provider which exposes the bcrypt password hashes for password protected shared files and folders. 

## Description
Android apps can use a content provider to handle storage and retrieval of data. Content providers that are exported allow any app on the same device to access their content. The Nextcloud Android app has an exported content provider called com.owncloud.android.providers.FileContentProvider (authority content://org.nextcloud) which holds sensitive information, including the share identifiers (aka tokens) and bcrypt password hashes for the user's password protected shares. An attacker can, through a malicious app on the device, query the provider and extract the share password hashes for offline cracking. This effectively bypasses any brute force share password protections implemented by the Nextcloud server and speeds up the cracking process, increasing the chances of share password recovery. Combined with the share identifier/token, if an attacker successfully cracks a password, he/she has enough information to access the protected share.

## Reproduction

Install the Nextcloud Android app on a device and sign in. Ensure some files are shared via password-protected links so you'll have some data to view. :)

From here there are 2 ways to reproduce the issue:

Method 1:
Connect an Android device with USB debugging enabled to a computer with the Android Studio or development tools installed. Run the following commands on a command prompt (Windows) or terminal (Linux):
- adb devices //start adb if not already running
- adb shell //get a shell on the target device
- content query --uri content://org.nextcloud/shares //use Android's 'content' program to query the vulnerable provider

The provider returns data including 1) the password hashes of shares protected with a password (the value of the 'shate_with' field) and 2) the token identifier used to access the share on the Nextcloud server (value of the 'token' field). 

Method 2:
The following app (among others), Content Provider Helper, allows you to query content providers on the device: https://play.google.com/store/apps/details?id=com.jensdriller.contentproviderhelper

Install and open it, tap the settings button in the upper right, tap 'Add Content Provider', add 'org.nextcloud/shares' (content:// is already prefilled), then tap 'Add'. Tap 'Query' and view the returned data. Since this 3rd party app can view the provider's data, it helps illustrate the fact that any app on the device can also access the provider and it's data.
 
Other queries return additional information, including file and folder names:
content://org.nextcloud/file
content://org.nextcloud/dir/[dir ID]

## Screenshots

- 1_settings - navigate to add provider in the Content Provider Helper app
- 2_add_provider - adding the vulnerable provider in the helper app
- 3_ready_to_query - provider added, tap Query here
- 4_results - results from the provider. The start of the hashes are visible in the far right column. Only shares that have been password-protected have a hash entry.
- 5_token - view showing the share identifier/token
- 6_cli - retrieving the same information via an adb shell with the 'content' command
- 7_files - results from querying content://org.nextcloud/file. Filenames are leaked which may or may not be considered sensitive information.

## Impact/Notes
This vulnerability allows a malicious app to extract the password protect hashes and send them to an attacker, who can attempt to crack them offline instead of brute-forcing the Nextcloud server. This speeds up the cracking process and increases the chance of password recovery, though password recovery is not guaranteed.

The vulnerability also allows a malicious app to retrieve the names of the user's Nextcloud files synced with the app. File names may or may not be considered sensitive information, not sure if this is noteworthy or not.

The Nextcloud threat model (https://nextcloud.com/security/threat-model/) mentions attacks involving other Android apps as 'minimal risk'. I understand if this vulnerability is considered an acceptable risk but thought it best to let you decide that.

Testing was primarily done on a Motorola Moto G running Android 6.0.1, Nextcloud Android app v1.4.3.

## Possible Mitigation
I do not see a valid reason to export the vulnerable content provider and make it accessible to any app on the device. One mitigation solution, therefore, is to mark the content provider as not exported by removing 'exported=true' from the com.owncloud.android.providers.FileContentProvider <provider> declaration in the AndroidManifest.xml file. This would prevent other apps from accessing the provider.

If there is a valid reason to export the provider, do share hashes need to be kept on the device? The Nextcloud server seems to be the one comparing the provided share password with the hash if someone attempts to access it. Not storing the hash in the content provider is another possible fix.

If this vulnerability is considered an acceptable risk, then no action is needed. :)

## Attachments
- 1_settings.png
- 2_add_provider.png
- 3_ready_to_query.png
- 4_results.png
- 5_token.png
- 6_cli.JPG
- 7_files.png
