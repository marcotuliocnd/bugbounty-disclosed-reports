# Broken Authentication – Session Token bug

## Report Details
- **Report ID**: 400826
- **URL**: https://hackerone.com/reports/400826
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-08-27T07:37:28.159Z
- **Disclosed**: 2018-09-26T09:22:13.897Z

## Reporter
- **Username**: code_monkey
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
I found a broken authentitication vuln

POC:

1- Create a https://demo.weblate.org/accounts/profile/ account
2- Confirm your email
3- Now request a password reset for your account.
4- Don’t use the password reset link that was sent to your email.
5- Login to your account, remember don’t use first the reset password link you requested in 3 step
6- Change your password in the Account Settings( url: https://demo.weblate.org/accounts/profile/
Step 5. After you changed your password inside your account, Check now the reset password link you requested in Step 3 in your email.
Step 6. Change your password using the reset password link you requested.


See this link: https://www.owasp.org/index.php/Broken_Authentication_and_Session_Management

## Impact

tokken should expire 


If the site has a token issue, The result is the reset password token in the Step 3 is still usable and did not expire yet. Not invalidating the session token for the reset password is not a good practice for a company.

## Attachments
No attachments
