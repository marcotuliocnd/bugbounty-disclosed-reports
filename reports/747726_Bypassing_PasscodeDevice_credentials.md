# Bypassing Passcode/Device credentials

## Report Details
- **Report ID**: 747726
- **URL**: https://hackerone.com/reports/747726
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-11-27T19:31:13.966Z
- **Disclosed**: 2021-01-15T15:55:12.414Z

## Reporter
- **Username**: arvind-hacker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Assume user have set **"App passcode"** to **"Passcode/Device credentials"**. So whenever user opens the app, it will prompt to unlock before accessing the app. Unfortunately there is a issue, attacker can able to bypass the lock easily in **two ways**.

### Setup

1. Install NextCloud app and Log in.
2. Go to Settings and set "App passcode" to "Passcode/Device credentials".

## How to bypass?

- Bypassing the lock using ADB

**Reproduce steps**

1.Execute the below command in command Prompt.

```
adb shell am start com.nextcloud.client/com.owncloud.android.ui.activity.FileDisplayActivity
```

2.It will open the app and prompt to unlock, now don't close the app and execute the below command.

```
adb shell am start -a android.intent.action.SEARCH com.nextcloud.client/com.owncloud.android.ui.activity.FileDisplayActivity
```

Now it will open the app again, but this time **it will not prompt to unlock** (You can able to use the app without unlocking).

- Bypassing the lock by changing device time

By default the app lock timeout is 5 seconds, so when the user close and reopens the app within 5 seconds, it will not prompt to unlock. 

Source code - https://github.com/nextcloud/android/blob/master/src/main/java/com/owncloud/android/authentication/PassCodeManager.java

```java
   private boolean passCodeShouldBeRequested(Long timestamp) {
        return (System.currentTimeMillis() - timestamp) > PASS_CODE_TIMEOUT &&
            visibleActivitiesCounter <= 0 && isPassCodeEnabled();
    }
```

In the above code, it checks whether user opened the app within 5 seconds or not by comparing the `current timestamp` and `app closed timestamp`. So attacker (Who knows the app closed time) can bypass this lock easily by changing the device time to app closed time.

**Reproduce steps**

1. Open the app and unlock.
2. Close the app and note the app closed time (For instance, it is 10:00 AM).
3. After 5 seconds or later (For instance, at 11:00 AM), open the app, it will prompt to unlock.
4. Now change the device time to app closed time (For instance, 10:00 AM).
5. Now open the app, it will not prompt to unlock.

**Fix**

Don't Use `System.currentTimeMillis()`, use `SystemClock.elapsedRealTime()` (Now attacker can't able to bypass the lock even if the app closed time is known). Refer http://sangsoonam.github.io/2017/03/01/do-not-use-curenttimemillis-for-time-interval.html

**Tested envirnoment**

App version: 3.9.0
Android version(s): 6.0, 8.1

## Impact

An attacker can easily access the victim Nextcloud app without unlocking "Passcode/Device credentials" lock.

## Attachments
No attachments
