# Password reset link not expired at Stocky App

## Report Details
- **Report ID**: 898841
- **URL**: https://hackerone.com/reports/898841
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-06-15T18:09:41.270Z
- **Disclosed**: 2020-08-18T22:53:55.541Z

## Reporter
- **Username**: ayyoub
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
You can use password reset link to reset password multiple times.

Steps:

1. Go to `https://stocky.shopifyapps.com/users/forgotten_password` and Send the password reset link to your email.
(if this page doesn't  appear you should add login details via this `https://stocky.shopifyapps.com/preferences/users` )
{F869115}
2. Go to your email inbox you see reset token like this `https://stocky.shopifyapps.com/users/new_password?reset_token=your-reset-token`and click the link to change password. you can use this link many times to reset password

## Impact

Password Reset Link not expiring after changing password

## Attachments
- Capture_(2).PNG
