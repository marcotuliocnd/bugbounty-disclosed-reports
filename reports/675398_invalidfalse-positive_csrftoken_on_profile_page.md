# [invalid][false-positive] csrftoken on profile page

## Report Details
- **Report ID**: 675398
- **URL**: https://hackerone.com/reports/675398
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-08-17T04:04:01.824Z
- **Disclosed**: 2019-08-20T07:32:21.557Z

## Reporter
- **Username**: tkd8
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
step of reproduce-
1. Go to https://wakatime.com and create account.
2. login account after that go public profile.
3. after that change the full name and intercept brup suite and delete csrftoken.
4. After forward then you see name was changed.

## Impact

Violation of Secure Design Principles

## Attachments
- 1sta.png
- 2ndb.png
