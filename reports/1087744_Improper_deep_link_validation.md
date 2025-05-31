# Improper deep link validation 

## Report Details
- **Report ID**: 1087744
- **URL**: https://hackerone.com/reports/1087744
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-26T17:55:16.126Z
- **Disclosed**: 2022-07-11T19:51:08.923Z

## Reporter
- **Username**: fr4via
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
The application contains an activity which validates and handles the deep link requests, initiated from a VIEW intent action. The declared schemes include **http** and **https** request for the domain shopify.com as well as \*.myshopify.com. The path prefixes include mostly subdirectories of the /admin path , thus when a deep link request is created the application routes this request to the corresponding activity of the application. 
**It was identified that it is possible to bypass the path prefix restrictions by adding appending a "../" to the end of the URI.  This results on loading arbitrary urls in the application's Webview, leveraging its Javascript capabilities as well as the EASDK bridge in order to compromise the integrity of the application.**
For example in order to access the https://someone.myshopify.com instead of https://someone.myshopify.com/admin/collections in the application's webview, the following intent may be sent: 
```
am start -W -a android.intent.action.VIEW -d "https://ravel17.myshopify.com/admin/collections/../../
```
The above intent will yield the following result: 
{F1172971}

In order to load an external URL the following steps should be followed:
- Create a partner account and add a new app 
- Use as the app's URL the address of the 'malicious' server 

{F1173035}
- Navigate to the "Choose client store" in order to choose the target store

{F1173036}

- Finally, copy the link from the "Merchant install link"

{F1173040}

- Create the following intent:

```
am start -W -a android.intent.action.VIEW -d "https://TARGET-STORE.myshopify.com/admin/collections/.../oauth/install_custom_app?client_id=....
```
- The result will be the following:

{F1173046}

## Impact

As it is mentioned above besides the Javascript which is enabled for the specific webview, the application adds a javascript interface which is accessed via the instantiation of an EASDK object. Some potential risk (besides phishing attacks which may be considered trivial for the specific case) is showed bellow:

- Access to the application's sandbox via the EASDK.redirect:

EASDK.redirect("file:///data/data/com.shopify.mobile/shared_prefs/notification_ids.xml")
{F1173057}

- Javascript code execution:

{F1173073}

## Attachments
- load1.png
- Screenshot_2021-01-26_at_5.07.12_PM.png
- Screenshot_2021-01-26_at_5.09.40_PM.png
- Screenshot_2021-01-26_at_5.11.34_PM.png
- load2.png
- sand.png
- sand1.png
