# Reset password more than once with a reset link #2

## Report Details
- **Report ID**: 245450
- **URL**: https://hackerone.com/reports/245450
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-07-03T05:57:24.610Z
- **Disclosed**: 2017-10-07T14:44:40.467Z

## Reporter
- **Username**: footstep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Sequel to the fix on #243594, this is still possible.

##Reproduction Steps
1. Request password reset
- Load the link in email and set a new password
- Navigate to https://demo.weblate.org/accounts/reset/
- Fill the email and captcha
- You'll be prompted to enter a new password

NOTE: I figured that if action is not performed after a few minutes, then this doesn't work. 

I suggest you make the link expire after use than setting a time frame.

Best!

## Attachments
No attachments
