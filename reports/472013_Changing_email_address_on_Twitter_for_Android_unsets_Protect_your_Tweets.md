# Changing email address on Twitter for Android unsets "Protect your Tweets"

## Report Details
- **Report ID**: 472013
- **URL**: https://hackerone.com/reports/472013
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-12-26T01:46:22.366Z
- **Disclosed**: 2019-01-18T16:49:29.340Z

## Reporter
- **Username**: alexiaya
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** Verifying email address on Twitter for Android unsets "Protect your Tweets"

**Description:** Verifying a new email address on a Twitter account in the Android app causes the "Protect your Tweets" option to be unset, resulting in the user's tweets being made publicly visible.

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Log in to a Twitter account on the Android app.
  2. Make sure the app is set to handle twitter.com links.
  3. Change the email address on the account.
  4. Verify the new email address by clicking the link in the email from the same Android device.

## Impact: This can lead to a user's private tweets being exposed to the public until they realize this happened. An attacker does not need to be involved as they would need to have access to the user's account to change the email, but a user could be tricked into changing their email if an attacker sent them a phishing email telling them to do so.
## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

This can lead to a user's private tweets being exposed to the public until they realize this happened. An attacker does not need to be involved as they would need to have access to the user's account to change the email, but a user could be tricked into changing their email if an attacker sent them a phishing email telling them to do so.

## Attachments
No attachments
