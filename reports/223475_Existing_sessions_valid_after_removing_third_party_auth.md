# Existing sessions valid after removing third party auth

## Report Details
- **Report ID**: 223475
- **URL**: https://hackerone.com/reports/223475
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T15:11:10.094Z
- **Disclosed**: 2017-06-16T14:16:34.266Z

## Reporter
- **Username**: brdoors3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi team,

I noticed an authentication break when logging in with 3rd party credentials in https://hosted.weblate.org/

POC

1 access https://hosted.weblate.org/accounts/profile/#auth> link to a Google account (for example)
2 on other device access the same account using Google credentials
3 return to the device of step 1> remove the Google account at https://hosted.weblate.org/accounts/profile/#auth> disconnect

The session remains active on the device in step 2. So I continue with a valid session from credentials not linked to any account at https://hosted.weblate.org

Please check it.

## Attachments
No attachments
