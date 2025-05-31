# Enable 2FA without verifying the email

## Report Details
- **Report ID**: 3016540
- **URL**: https://hackerone.com/reports/3016540
- **State**: Closed
- **Severity**: low
- **Submitted**: 2025-02-27T10:56:50.806Z
- **Disclosed**: 2025-05-09T06:37:34.778Z

## Reporter
- **Username**: samtime
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: xvideos

## Vulnerability Information
A vulnerability in xvideos.com allows an attacker to register using victim email addresses which are unverified. This can be further exploited to enable two-factor authentication (2FA), permanently locking the victim out of their own email account. This results in a denial-of-service attack against the legitimate email owner.

Steps to Reproduce:
Go to: https://www.xvideos.com/
Then, navigate to join for free and create an account using victim email address
After that, Navigate to: https://www.xvideos.com/account/security
Select "Two-step verification" and enable it using the Google Authenticator app.

 Reference

https://hackerone.com/reports/1618021

## Impact

The victim can't register an account with their email. If the victim reset the password, the password will change, but the victim can't login because of 2FA which was enabled by attacker leading to denial-of-service against the legitimate email owner.

## Attachments
- poc1.png
- poc2.png
- poc3.png
- poc4.png
- poc5.png
- poc6.png
- poc7.png
