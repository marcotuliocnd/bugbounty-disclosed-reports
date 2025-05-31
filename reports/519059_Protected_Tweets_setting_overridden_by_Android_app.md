# Protected Tweets setting overridden by Android app

## Report Details
- **Report ID**: 519059
- **URL**: https://hackerone.com/reports/519059
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-30T13:55:11.669Z
- **Disclosed**: 2019-05-17T18:08:02.377Z

## Reporter
- **Username**: alexiaya
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** Protected Tweets setting overridden by Android app

**Description:** The Android app overrides the "Protect your Tweets" setting set from outside the app in some cases when changing other settings.

## Steps To Reproduce:

  1. Log in to an account with unprotected tweets on the Android app.
  1. Log in to the same account on mobile.twitter.com and turn on protected tweets.
  1. Confirm that the account's tweets are protected.
  1. In the Android app, go to the Direct Messages tab, click the gear icon and change a setting such as "Receive message requests" or "Show read receipts."
  1. The account's tweets are now unprotected.

If this does not work, you may have to first explicitly unset the protected tweets setting in the Android app before setting it elsewhere.

## Impact:

This can cause a user's tweets to unknowingly become public. It is possible this could be exploited by an attacker asking the user to change their settings but that is less likely to succeed than with the previous bug where only changing the email address was required.

## Impact

See above.

## Attachments
No attachments
