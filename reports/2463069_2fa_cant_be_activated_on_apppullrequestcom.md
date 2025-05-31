# 2fa can't be activated on app.pullrequest.com

## Report Details
- **Report ID**: 2463069
- **URL**: https://hackerone.com/reports/2463069
- **State**: Closed
- **Severity**: none
- **Submitted**: 2024-04-14T21:32:13.893Z
- **Disclosed**: 2024-07-11T15:20:45.237Z

## Reporter
- **Username**: iam_srpk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hello Team,
Since you are using deprecated google chart API service (which doesn't work now) for generating 2fa qr code image, users cannot setup 2fa for securing account.

### Steps To Reproduce

1. Log into https://app.pullrequest.com
2. Go to "User Settings" -> "Security" -> "Two-Factor Authentication"
3. You cannot when you try enabling it

## Impact

I understand it is kinda technical bug. But I decided to report as it literally affects all existing and new users by not allowing them to secure their account.

## Attachments
No attachments
