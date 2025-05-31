# Cookie steal through content Uri

## Report Details
- **Report ID**: 876192
- **URL**: https://hackerone.com/reports/876192
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-05-16T20:11:15.667Z
- **Disclosed**: 2021-04-22T18:05:12.454Z

## Reporter
- **Username**: kanytu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary

A misconfiguration in a content provider is allowing Brave for Android to download internal files to Downloads folder, making them accessible to other apps. A malicious app could order Brave to download the cookies database and retrieve it afterwards.

## Environment

- **Device:** HTC M8
- **OS version:** Android 9
- **Package name:** com.brave.browser
- **App version:** 1.8.93 (`versionCode` 410809320)



## Proof of concept

### Pre-conditions:

- Poc installed with `STORAGE` permissions
- Brave installed with some cookies saved
- Brave should have `STORAGE` permission as well

### Steps:

1. Tap "Start Exploit" in PoC app
2. Brave will start to download the cookies file
3. Open back PoC app

### Result

Cookies are shown in PoC app

### Expected result

Private files shouldn't be exported



## Detailed explanation

When `Start Exploit` is tapped, the app is sending an intent to Brave Browser to view a content URI:

```
content://com.brave.browser.FileProvider/root/data/data/com.brave.browser/app_chrome/Default/Cookies
```

This content URI will be resolved to `ChromeFileProvider`. This File Content Provider has the following path configuration:

```
<paths>
    <root-path name="root" path="." />
    <files-path name="images" path="images/" />
    <cache-path name="cache" path="net-export/" />
    <cache-path name="passwords" path="passwords/" />
    <cache-path name="traces" path="traces/" />
    <cache-path name="webapk" path="webapks/" />
    <cache-path name="offline-cache" path="Offline Pages/archives/" />
    <external-path name="downloads" path="Download/" />
    <external-path name="downloads" path="Android/data/com.brave.browser/files/Download/" />
</paths>
```

Because of the usage of `root-path` with path `.`, it is possible to use this provider to point to all files in the Android system.

By using the path segment `/root/` followed by the absolute path to the internal file, Brave will easily process this URI because it belongs to itself, hence, no need to grant permissions to this URI.

Brave will then proceed to download this file because of it's mime type (`application/octet-stream`). The file is saved in `/sdcard/Download/`. This is a public directory and all files with `STORAGE` permission can access them.

The PoC listens for changes in Downloads directory and when the Cookies file is created there, it will access this database and print all cookies in it.



## Remediation

Brave should not use `root-path` point to the root of the file system (`./`). If this needed for some edge case, Brave should implement path checks to make sure that no internal file is used in this URI.

## Attachments

- PoC.zip - source code of the PoC used in this exploit
- poc.apk - compiled binary to use in this exploit
- video.mp4 - a video showing the exploit in action

## Impact

This allows a malicious app with `STORAGE` permission to access all cookies in Brave which has a high confidentiality impact. This requires no user interaction other than a malicious app installed.

This works for all internal files but cookies allow the malicious app to potentially access private information from the user, impacting the availability and integrity of their logged in accounts.

## Attachments
- PoC.zip
- poc.apk
- video.mp4
