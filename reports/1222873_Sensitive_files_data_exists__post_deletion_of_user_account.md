# Sensitive files/ data exists  post deletion of user account

## Report Details
- **Report ID**: 1222873
- **URL**: https://hackerone.com/reports/1222873
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-06-10T13:52:54.912Z
- **Disclosed**: 2022-05-20T09:25:31.330Z

## Reporter
- **Username**: geekysherlock
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
In the latest android app ,I created an account in the name of geekysherlock1@gmail.com. 
After few activities,deleted  the account . 
Files containing user emails and tokens still exist.Relevant files not deleted upon deletion of account.

Content of files post deletion of account:
generic_x86:/data/data/com.nextcloud.client/shared_prefs # ls
FirebaseAppHeartBeat.xml WebViewChromiumPrefs.xml com.google.android.gms.appid.xml com.nextcloud.client_preferences.xml migrations.xml variant-emoji-manager.xml

generic_x86:/data/data/com.nextcloud.client/shared_prefs # cat com.nextcloud.client_preferences.xml
<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <boolean name="keysMigration" value="true" />
    <string name="select_oc_account">geekysherlock1@gmail.com@us.cloudamo.com</string>
    <boolean name="autoUploadPathUpdate" value="true" />
    <boolean name="autoUploadInit" value="true" />
    <int name="prefs_uploader_behaviour" value="1" />
    <boolean name="storagePathFix" value="true" />
    <boolean name="autoUploadEntriesSplitOut" value="true" />
    <boolean name="keysReinit" value="true" />
    <string name="pushToken">euwTiu9CT3CvQNHqNVZPIk:APA91bHqkGjFhx-BiCEH_NcRnaEvrp21tbxvjOKhHrQ1mUTCW3Dp46X90YinSDcjfVXytTcT9CLQBcrOv5J_EfSGM7GbZrZAyeKC1xOtgNBLkFeo4_EqX7LqVW-ezuG_rou1y2Ux8ah5</string>
    <float name="grid_columns" value="3.0" />
    <string name="storage_path">/storage/emulated/0/Android/media/com.nextcloud.client</string>
    <boolean name="legacyClean" value="true" />
    <string name="upload_from_local_last_path">/storage/emulated/0/Pictures</string>
    <int name="lastSeenVersionCode" value="30160190" />
</map>

Images folder
generic_x86:/data/data/com.nextcloud.client/shared_prefs # cd /storage/emulated/0/Pictures
generic_x86:/storage/emulated/0/Pictures # ls
2131099731.jpg 2131099732.jpg 2131099733.jpg

## Impact

This information could be misused as  sensitive token related ,images,user related  details exist inspite of user account being deleted.

## Attachments
- com.nextcloud.client_preferences-xml.txt
