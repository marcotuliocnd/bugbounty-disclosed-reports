# Bypassing Two-Factor Authentication via Account Deactivation and Password Reset

## Report Details
- **Report ID**: 2543342
- **URL**: https://hackerone.com/reports/2543342
- **State**: Closed
- **Severity**: none
- **Submitted**: 2024-06-10T01:37:42.516Z
- **Disclosed**: 2024-07-11T14:35:44.162Z

## Reporter
- **Username**: 011alsanosi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

The vulnerability arises from a logical flaw in the account recovery and 2FA enforcement processes. Specifically, after deactivating an account, users can reset their password and log in without being prompted for 2FA. The 2FA mechanism, which is designed to provide an additional layer of security, is effectively bypassed.

### Steps To Reproduce

1. Go to settings enable 2fa and click on Deactivation
2. After Deactivation your account go to reset password and reset your password 
3. After change your password you can notice access account without 2fa

*poc*
███
### Recommendations

Disable Password Resets for Deactivated Accounts: Ensure that deactivated accounts cannot reset their passwords without reactivating.
	•	Enforce 2FA During Password Reset: Require 2FA verification as part of the password reset process.

## Impact

Attackers with access to a user’s email can deactivate the account and reset the password, gaining full access without passing 2FA.

## Attachments
No attachments
