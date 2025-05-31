# Notification implicit PendingIntent in com.nextcloud.client allows to access contacts

## Report Details
- **Report ID**: 1161401
- **URL**: https://hackerone.com/reports/1161401
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-12T12:20:37.002Z
- **Disclosed**: 2022-05-27T07:23:00.174Z

## Reporter
- **Username**: imnotyouaa_test
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
When the victim downloads files in nextcloud.A notification will be triggered. The content of the notification is "Downloaded".This notification is used to remind the user that the download is complete.The pendingintent in this notification is an implicit intent.

At this time a malicious app with "BINDNOTIFICATIONLISTENER_SERVICE" permission can get the pendintent of this notification, because it is an implicit pendintent. Therefore, the malicious app can set the "packageName" and "clipdata" of this pendintent. At this time, the malicious application will inherit the permissions of "com.nextcloud.client".Because nextcloud  has contacts permissions. Therefore, malicious applications can read the contacts without applying for the contacts permission.
{F1262742}
At the same time, because of the path configuration of fileprovider, the log file in the nextcloud app directory can also be read
{F1262743}

The code of this implicit pendingintent is in
"com.owncloud.android.files.services.FileDownloader.notifyDownloadResult(com.owncloud.android.operations.DownloadFileOperation, com.owncloud.android.lib.common.operations.RemoteOperationResult) : void"
{F1262747}

Steps To Reproduce:
packageName:com.nextcloud.client
versionName:3.15.1
phone:pixel3
AndroidVersion:10

1.install and run "poc.apk"
2.click the button to give the "BINDNOTIFICATIONLISTENER_SERVICE" permission to poc
3.install "com.nextcloud.client.apk" and give contacts permission to nextcloud.
4.Download a file as shown in the video.At this time, the victim's app will trigger a notification
5.run "adb logcat | grep sbn". now you can see the contact stolen by the attacker

Supporting Material/References:
1.read contacts poc video
{F1262750}

2.poc.apk
{F1262748}

3."com.nextcloud.client.apk"
{F1262746}

## Impact

Any application with notification permission can steal contacts without apply for the contacts permission
To fix this vulnerability, please set the flag of pengingintent to FLAG_IMMUTABLE

## Attachments
- contacts.png
- filepath.png
- com.nextcloud.client_3.15.1-30150190_minAPI21(arm64-v8a_armeabi-v7a_x86_x86_64)(nodpi)_apkmirror.com.apk
- pendingintent.png
- poc.apk
- nextcloud.mov
