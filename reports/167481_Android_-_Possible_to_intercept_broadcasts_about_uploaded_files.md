# Android - Possible to intercept broadcasts about uploaded files

## Report Details
- **Report ID**: 167481
- **URL**: https://hackerone.com/reports/167481
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-11T00:49:12.872Z
- **Disclosed**: 2017-03-23T17:12:48.422Z

## Reporter
- **Username**: bagipro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi.
There are the moments of sending unprotected broadcasts
https://github.com/nextcloud/android/blob/master/src/com/owncloud/android/files/services/FileUploader.java#L1170
https://github.com/nextcloud/android/blob/master/src/com/owncloud/android/files/services/FileUploader.java#L1116
https://github.com/nextcloud/android/blob/master/src/com/owncloud/android/files/services/FileUploader.java#L1136
https://github.com/nextcloud/android/blob/600225c7c9684295bfdb43bcf7d078113b8b2f73/src/com/owncloud/android/services/SyncFolderHandler.java#L186
https://github.com/nextcloud/android/blob/600225c7c9684295bfdb43bcf7d078113b8b2f73/src/com/owncloud/android/services/SyncFolderHandler.java#L201
etc
A malware can simply create a receiver:
```xml
<receiver android:exported="true" android:enabled="true" android:name=".InterceptReceiver">
	<intent-filter android:priority="999">
		<action android:name="FileUploader.UPLOAD_START"/>
		<action android:name="FileUploader.UPLOAD_FINISH"/>
		<action android:name="FileUploader.UPLOADS_ADDED"/>
	</intent-filter>
</receiver>
```
(and other actions)
And receive the broadcasts **first** than your own receivers
More info about priority here
https://developer.android.com/guide/topics/manifest/intent-filter-element.html#priority

It will disclose info about account, file info, etc

The one thing you should do is to change all calls of ```Context.sendStickyBroadcast``` on ```LocalBroadcastManager.sendBroadcast``` and all calls of ```Context.registerReceiver``` on ```LocalBroadcastManager.registerReceiver```
https://developer.android.com/reference/android/support/v4/content/LocalBroadcastManager.html
instead on using ```removeStickyBroadcast(intent);```


## Attachments
No attachments
