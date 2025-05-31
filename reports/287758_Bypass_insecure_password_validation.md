# Bypass insecure password validation

## Report Details
- **Report ID**: 287758
- **URL**: https://hackerone.com/reports/287758
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-11-06T16:00:11.463Z
- **Disclosed**: 2017-11-16T08:08:29.922Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Hi Team,

## Summary:

Registration is checking the password creation __if the password is insecure__ , but the password reset page was not doing the same validation, so when i input an insecure password using the password reset, the validation on the password creation can be bypass because the password reset was not doing the same validation.

## Steps to reproduce:

  1. Try to create/signup an account here: https://infogram.com/signup with password `1234567890` and the error message will appear: `Insecure password`.
  2. Now lets bypass it, assuming i already created an account, now go to forgot password: https://infogram.com/forgot and enter you email.
  3. The password reset link will send, click the link and it will redirect to password reset page.
  4. On password reset, enter `1234567890` as your new password.
  5. Password accepted! , insecure password validation has been bypassed.

Let me know if you need more information.

Regards
Japz

## Attachments
No attachments
