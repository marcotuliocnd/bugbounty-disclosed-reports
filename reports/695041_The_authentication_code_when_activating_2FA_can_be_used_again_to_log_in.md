# The authentication code when activating 2FA can be used again to log in

## Report Details
- **Report ID**: 695041
- **URL**: https://hackerone.com/reports/695041
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-09-15T03:02:44.866Z
- **Disclosed**: 2021-02-11T19:06:02.695Z

## Reporter
- **Username**: shadow-m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi team,
Summary:
======================
I noticed that when activating 2FA by sms, you can also use that 2FA activation code, to use as an authentication code when logging in.
Steps:
=========================
1, Go to: https://accounts.shopify.com/accounts/36430415/security and log in
2, Activate 2FA by sms for the account and save the code sent in your phone
3, Log out and perform login again
4, After entering the password and being asked to enter the verification code, you only need to replay the code used to activate the previous 2FA.
5, Logged in successfully.

## Impact

Assuming the hacker knows the authentication code when activating the victim's 2FA, he can reuse the victim's code to replay and log in successfully without the victim knowing.

Recommend:
============
Each authentication code should only be used once.

Best regards,
john

## Attachments
No attachments
