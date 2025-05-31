# UI spoofing by showing sms:/tel: dialog on another website

## Report Details
- **Report ID**: 1819652
- **URL**: https://hackerone.com/reports/1819652
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-01-01T08:27:16.328Z
- **Disclosed**: 2023-06-22T05:50:39.559Z

## Reporter
- **Username**: nishimunea
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
The dialog asking if you want to open the sms:/tel: link doesn't show the caller origin.
Also, unlike the JavaScript alert dialog, etc., it appears on the top screen even when another tab is active.
This can be used for UI spoofing attack to make it looks as if another site is displaying the dialog.

## Products affected: 

 * Brave for iOS (Version 1.45.2)

## Steps To Reproduce:

 * Visit https://csrf.jp/brave/sms.php
 * Tap "Click Me" button
 * google.com is opened in the new tab
 * Confirmation dialog for sms: link is shown on google.com

## Supporting Material/References:

  * See the demonstration movie I attached

## Impact

This can be used for UI spoofing attack to make it looks as if another site is displaying the dialog.

## Attachments
- sms_tel_dialog_on_other_origin.mov
