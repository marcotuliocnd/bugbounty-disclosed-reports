# user_oidc app is missing bruteforce protection

## Report Details
- **Report ID**: 1954711
- **URL**: https://hackerone.com/reports/1954711
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-04-19T14:53:04.396Z
- **Disclosed**: 2023-06-23T09:44:42.159Z

## Reporter
- **Username**: nickvergessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Various controllers of the user_oidc app are not bruteforce protected, allowing attackers to iterate over data until they find valid one.

* Id4meController::login
* Id4meController::code
* LoginController::login
* LoginController::code
* LoginController::csingleLogoutService
* LoginController::cbackChannelLogout

## Impact

Authentication can be broken/bypassed

## Attachments
No attachments
