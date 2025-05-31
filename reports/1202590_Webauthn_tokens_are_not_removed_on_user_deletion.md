# Webauthn tokens are not removed on user deletion

## Report Details
- **Report ID**: 1202590
- **URL**: https://hackerone.com/reports/1202590
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-19T12:07:33.427Z
- **Disclosed**: 2021-08-07T14:28:53.107Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
1. userA has an account on serverA
2. userA enables passwordless login (webauthn) and registers a key/device
3. userA is removed from the system
4. a new user comes along and gets assigned userA as id
5. the old userA tries to login with their key
6. the old userA can see all data of the new userA

## Impact

This can lead to an unauthorized actor gaining full access to the data of another user.
As suggested in https://hackerone.com/reports/1200700 a blocklist of old userids would help here. However the data should all be cleaned up as well of course!

## Attachments
No attachments
