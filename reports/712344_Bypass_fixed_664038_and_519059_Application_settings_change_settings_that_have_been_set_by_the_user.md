# [Bypass fixed #664038 and #519059] Application settings change settings that have been set by the user

## Report Details
- **Report ID**: 712344
- **URL**: https://hackerone.com/reports/712344
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-11T17:44:24.917Z
- **Disclosed**: 2021-07-13T17:47:10.090Z

## Reporter
- **Username**: jaka-tingkir
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
I have reported this bug in report #681361 so that you make a FULL fix, but you refused (considered duplicate) and I have to wait for report #664038 to be resolved, now I come again to report the bug.

The settings for "protected tweets" that have been set from another application accidentally change after the user changes the settings on the twitter application.

## Step To Reproduction
1. Set "protected tweets" from the Twitter Web or Twitter Lite application
2. Confirm and make sure that "tweet is protected" from the web or lite
3. then open the twitter application and change the hashtag (#) setting from OFF to ON

This method will trigger problems in the settings between the web and Twitter applications so that what has been set from outside the Twitter application can change.


##the bug in this report has the same impact as report #664038 and #519059 but this bugs can still be triggered even though one of these bugs in reports has been fixed.


I say that because the bug in report #664038 and #519059 has been fixed and I can trigger the bug again in new versi app twitter 8.16.0 release 00


## my conclusion this bug is ==Bypassing significant controls== because after this bug is fixed it can be triggered again

## Impact

accidentally the "protected tweet" setting OFF and user tweets seen publicly

## Attachments
No attachments
