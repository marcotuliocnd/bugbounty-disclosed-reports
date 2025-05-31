# Vulnerable exported broadcast receiver

## Report Details
- **Report ID**: 289000
- **URL**: https://hackerone.com/reports/289000
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-11-10T00:51:21.802Z
- **Disclosed**: 2017-11-10T05:24:14.592Z

## Reporter
- **Username**: b3nac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bitwarden

## Vulnerability Information
Good evening,

This is actually in your code base this time.  :)

Since the following broadcast receiver has export=true it can be exploited by 3rd parties.

#Vulnerability

com.x8bit.bitwarden.PackageReplacedReceiver has exported set to true making the receiver vulnerable to tampering.

{F238236}

#POC

I was able to send information to the receiver and get a response with Drozer. This gives me further information to craft the right payload.

{F238227}

#Fix
In the manifest changing exported to false or if the broadcast needs to be exported the following would be the correct fix.

At the top of the manifest with the other permissions.

```
<permission android: name="com.x8bit.bitwarden.PackageReplacedReceiverPermission" android:protectionLevel="signature" />
```

Modified receiver manifest entry.
```
<receiver android:name="com.x8bit.bitwarden.PackageReplacedReceiver" android:exported="true" android:permission="com.x8bit.bitwarden.PackageReplacedReceiverPermission">
            <intent-filter>
                <action android:name="android.intent.action.MY_PACKAGE_REPLACED" />
            </intent-filter>
        </receiver>
```

Adding the signature custom permission makes it so the broadcast can only be used with applications that were signed with the same key.

Please let me know if you have any questions. Great job on this app by the way. It's one of the most secure apps I've seen so far on H1.

#Resources
https://oldbam.github.io/android/security/android-vulnerabilities-insecurebank-broadcast-receivers


## Attachments
- TestingtheBroadcast.PNG
- Vuln_Receiver.PNG
