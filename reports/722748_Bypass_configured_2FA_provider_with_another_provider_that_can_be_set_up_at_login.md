# Bypass configured 2FA provider with another provider that can be set up at login

## Report Details
- **Report ID**: 722748
- **URL**: https://hackerone.com/reports/722748
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-25T12:14:03.111Z
- **Disclosed**: 2020-03-01T12:41:32.802Z

## Reporter
- **Username**: christophwurst
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
In Nextcloud 17 there is the possibility to set up 2FA providers at login. A missing check allows the following steps

1) Enforce 2FA for all users
2) As a user, configure a 2FA provider (via settings or at login)
3) Log out
4) Log in again (password only)
5) When prompted with the earlier set up provider, go to /login/setupchallenge
6) Set up another provider that hasn't been set up before
7) You're logged in

## Impact

Bypass a user's second-factor authentication protection.

## Attachments
No attachments
