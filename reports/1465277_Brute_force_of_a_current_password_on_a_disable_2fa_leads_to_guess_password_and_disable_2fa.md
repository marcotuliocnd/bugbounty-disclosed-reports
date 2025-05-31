# Brute force of a current password on a disable 2fa leads to guess password and disable 2fa.

## Report Details
- **Report ID**: 1465277
- **URL**: https://hackerone.com/reports/1465277
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-01-31T06:28:15.346Z
- **Disclosed**: 2022-07-07T16:35:19.537Z

## Reporter
- **Username**: sachinrajput
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
Summary:
This Attack happen when victim login in other device and forget to logout ,Then attacker can enable 2-factor authentication by brute fore the password of victim endpoints.

## Steps To Reproduce:
(1)Login in https://dashboard.omise.co/signin
(2) Click on your username
(3)Navigate to Two-factor authentication --> Disable 2FA
(4)add random password in Please confirm your identity to register a new Two-Factor Authenticator
(5)Capture the request and send it for fuzz


POC
In screenshot you can see change in length of content when request encounter right password.

## Impact

Attacker can disable 2fa and brute force currrent password.

## Attachments
- omise1.png
