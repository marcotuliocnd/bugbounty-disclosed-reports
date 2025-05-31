# Invalidate session after password reset

## Report Details
- **Report ID**: 678050
- **URL**: https://hackerone.com/reports/678050
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-21T04:31:06.982Z
- **Disclosed**: 2019-11-05T08:37:11.687Z

## Reporter
- **Username**: nikhil786
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Website doesn't invalidate session after the password is reset which can enable attacker to continue using the compromised session.

Steps:
1) Open same accounts in two different browsers
2) Change password in one browser and you will see that another browser still validate the session after password change (even after refresh the page ).

Recommendation:

As per OWASP, it is recommended to terminate all the active sessions when a password is changed and force the user to re-login.

## Impact

Logging in with the new password doesn't invalidate the older session either: I could browse Liberapay using two sessions (in two different browsers) which were initiated using two different passwords.

## Attachments
- Screencast_Wednesday_21_August_2019_09_54_51__IST.webm
