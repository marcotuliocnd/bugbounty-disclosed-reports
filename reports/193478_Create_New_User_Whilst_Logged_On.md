# Create New User Whilst Logged On

## Report Details
- **Report ID**: 193478
- **URL**: https://hackerone.com/reports/193478
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-12-22T20:02:29.563Z
- **Disclosed**: 2017-01-13T00:28:37.384Z

## Reporter
- **Username**: id-is-vulnerable
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
The website www.teavana.com allows users already logged on to create new account with a very simple url redirect. When an account is created a page is displayed with your account information and what you want to update. By simply refreshing the page allows you to create a new account whilst still logged on. If you try to recreate the same account with the same email but different password, there will be no error message displayed though when you try to login, the password will be incorrect.

## Attachments
- Screen_Shot_2016-12-22_at_19.38.54.png
- Screen_Shot_2016-12-22_at_19.38.08.png
- Screen_Shot_2016-12-22_at_19.38.19.png
