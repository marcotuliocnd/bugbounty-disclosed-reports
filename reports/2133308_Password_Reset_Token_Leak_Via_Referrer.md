# Password Reset Token Leak Via Referrer

## Report Details
- **Report ID**: 2133308
- **URL**: https://hackerone.com/reports/2133308
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-09-03T19:58:51.347Z
- **Disclosed**: 2023-11-23T16:01:39.082Z

## Reporter
- **Username**: 0xthem7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
# Exploitation
Request password reset to your email address
Click on the password reset link
Dont change password
Click on about us
Intercept the request in burpsuite proxy
Check if the referer header is leaking password reset token.

# Impact
It allows the person who has control of particular site to change the user’s password (CSRF attack), because this person knows reset password token of the user.

# Reference:
https://hackerone.com/reports/342693
https://hackerone.com/reports/272379
https://hackerone.com/reports/737042
https://medium.com/@rubiojhayz1234/toyotas-password-reset-token-and-email-address-leak-via-referer-header-b0ede6507c6a
https://medium.com/@shahjerry33/password-reset-token-leak-via-referrer-2e622500c2c1

## Impact

It allows the person who has control of particular site to change the user’s password (CSRF attack), because this person knows reset password token of the user.

## Attachments
No attachments
