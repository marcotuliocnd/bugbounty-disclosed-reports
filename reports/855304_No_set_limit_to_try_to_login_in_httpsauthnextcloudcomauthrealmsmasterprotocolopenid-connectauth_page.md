# No set limit to try to login in "https://auth.nextcloud.com/auth/realms/master/protocol/openid-connect/auth" page.

## Report Details
- **Report ID**: 855304
- **URL**: https://hackerone.com/reports/855304
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-04-21T15:44:49.177Z
- **Disclosed**: 2021-04-20T13:50:20.712Z

## Reporter
- **Username**: syachineko
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi.
I checked the "https://nextcloud.com" page, and try to go to wp-admin page.
Then, I found the login page "https://auth.nextcloud.com/auth/realms/master/protocol/openid-connect/auth"
In this page, I tried to login more than 10 times!(manually)
I think that I can try to brute force to this login page, because it's no limit to try to login.
You should be better to set the limit to try to login.

## Impact

an attacker can try to brute force attack to login the page until he can success to login.

## Attachments
No attachments
