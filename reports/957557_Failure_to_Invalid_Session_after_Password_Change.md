# Failure to Invalid Session after Password Change

## Report Details
- **Report ID**: 957557
- **URL**: https://hackerone.com/reports/957557
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-08-13T11:57:28.847Z
- **Disclosed**: 2021-11-09T21:14:24.945Z

## Reporter
- **Username**: shad0123
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rockset

## Vulnerability Information
## Summary:
While conducting my researching I discovered that the application Failure to invalidate session after password. In this scenario changing the password doesn't destroys the other sessions which are logged in with old passwords.

## Steps To Reproduce:


  1. Login with the same account in Chrome and Firefox Simultaneously
  2. Change the pass in Chrome Browser
  3. Go to firefox and Update any information (example:if you are a admin you can delete user from users), information will be update *If attacker login with firefox and user know his password stolen so even user change their password, his account remain insecure and attacker have full access of victim account.



Mitigation

When some change in user password, each and every active sessions that belongs to that particular account must be destroyed!
I would like to recommend you to add a process that asks users whether user want to close all open sessions or not right after changing password.

So there is two way, either you let users to choose if they want to keep active sessions or just destroy every active sessions when an users change his/her password!

Please fix this Vulnerability and let me know. Looking forward to hear from you.

Best Regards

## Impact

If attacker have user password and logged in different places, As other sessions is not destroyed, attacker will be still logged in your account even after changing password, cause his session is still active.. Malicious actor can complete access your account till that session expires! So, your account remains insecure even after the changing of password

## Attachments
No attachments
