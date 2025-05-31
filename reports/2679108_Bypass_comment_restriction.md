# Bypass comment restriction

## Report Details
- **Report ID**: 2679108
- **URL**: https://hackerone.com/reports/2679108
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-08-22T22:24:15.351Z
- **Disclosed**: 2024-09-19T10:28:39.472Z

## Reporter
- **Username**: retat4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hackerone disallows people with under 3000 reputation and 3 signal to comment on reports which have been closed as informative or N/A:
{F3542835}

However you can bypass this and leave an infinite amount of comments by "requesting disclosure" , then cancelling it (if you want to write more messages), then request again and so on. you can attach a comment on each request/cancellation , effectively bypassing this measure
{F3542836}

## Impact

broken access control (bypassing restriction)

## Attachments
- image.png
- image.png
- Screenshot_2024-08-22_at_18.23.14.png
