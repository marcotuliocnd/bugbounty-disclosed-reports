# Wordpress Users Disclosure

## Report Details
- **Report ID**: 625199
- **URL**: https://hackerone.com/reports/625199
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-06-22T00:04:42.696Z
- **Disclosed**: 2019-07-01T09:32:11.233Z

## Reporter
- **Username**: abay
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
**Information**
Using REST API, we can see all the WordPress users/author with some of their information.

**Step to Reproduce**
You can get user info by entering below url in your browser: 
https://nextcloud.com/wp-json/wp/v2/users

Reference: [#356047](https://hackerone.com/reports/356047)

## Impact

Authors : LTR , LTREditor can be created scenario of doing bruteforce attacks to this users.

## Attachments
No attachments
