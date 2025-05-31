# Malicious apps can crash Nextcloud Android client by sending malformed intents 

## Report Details
- **Report ID**: 859136
- **URL**: https://hackerone.com/reports/859136
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-04-25T11:05:52.815Z
- **Disclosed**: 2021-06-17T10:50:12.335Z

## Reporter
- **Username**: bigbug
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Not sure if this can be tracked as a security issue, but this definitely calls for a code change. This can be classified into Denial of Service category attack and can seriously hamper user experience. 

Asset: Nexcloud Android Client (com.nextcloud.client)
Version: 3.11.1 (latest)

###_Details_ 

The Nextcloud android app registers a deeplink `nc://login` that is handled by the `com.owncloud.android.authentication.ModifiedAuthenticatorActivity` class as seen in AndroidManifest file.

The above mentioned class implements `AuthenticatorActivity` class in order to handle incoming deeplinks.

It is seen that the method `parseLoginDataUrl` does not handle exception correctly crashing the Nextcloud app.  

malicious apps can thus crash the nextcloud client by sending following data in intent : `nc://login`. 

ADB payload:

```
adb shell am start -a "android.intent.action.VIEW" -c "android.intent.category.DEFAULT" -n "com.nextcloud.client/com.owncloud.android.authentication.ModifiedAuthenticatorActivity" -d "nc://login"
```

Attaching video PoC
{F803256}

## Impact

1. Malicious apps can crash the nextcloud android client to cause a denial of service attack.

## Attachments
- nextcloud_intent_crash.mp4
