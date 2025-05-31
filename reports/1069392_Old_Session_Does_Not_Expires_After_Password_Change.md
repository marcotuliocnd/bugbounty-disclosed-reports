# Old Session Does Not Expires After Password Change

## Report Details
- **Report ID**: 1069392
- **URL**: https://hackerone.com/reports/1069392
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-31T18:51:17.737Z
- **Disclosed**: 2021-01-25T19:58:42.331Z

## Reporter
- **Username**: hemantsolo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Hello Team,
I am Hemant Patidar working as a security researcher and I found a bug in your site.
Report of bug is as follows:-

##Description:
While conducting my research I discovered that the application Failure to invalidate the session after the password change. In this scenario changing the password doesn't destroy the other sessions which are logged in with old passwords.

##Steps to reproduce:
1. Login with the same account in Chrome and Firefox Simultaneously using the URL: https://█████
2. Change the pass in Chrome Browser using the URL: https://██████
3. Go to firefox and Update any information, the information will be updated 

##POC:
███████

##Mitigation
When some change in user password, each and every active session that belongs to that particular account must be destroyed!
I would like to recommend you to add a process that asks users whether user want to close all open sessions or not right after changing password.
So there is two way, either you let users choose if they want to keep active sessions or just destroy every active session when users change his/her password!

## Impact

* If the attacker has a user password and logged in different places, As other sessions are not destroyed, the attacker will be still logged in to your account even after changing the password, cause his session is still active. A malicious actor can complete access your account till that session expires! So, your account remains insecure even after the changing of password

Please fix this Vulnerability and let me know. Looking forward to hearing from you.

Best Regards
Hemant Patidar

## Attachments
No attachments
