# Failure to Invalid Session after Password Change

## Report Details
- **Report ID**: 1118402
- **URL**: https://hackerone.com/reports/1118402
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-05T18:13:47.335Z
- **Disclosed**: 2021-03-12T11:10:52.691Z

## Reporter
- **Username**: sudipraj
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
##Summary
While conducting my researching I discovered that the application Failure to invalidate session after password. In this scenario changing the password doesn't destroys the other sessions which are logged in with old passwords.

##Reproduction Steps
->Login with the same account in Chrome and Firefox Simultaneously
->Change the pass in Chrome Browser
->Go to firefox and Update any information, information will be update *If attacker login with firefox and user know his password stolen so even user change their password, his account remain insecure and attacker have full access of victim account.

## Impact

If attacker have user password and logged in different places, As other sessions is not destroyed, attacker will be still logged in your account even after changing password, cause his session is still active.. Malicious actor can complete access your account till that session expires! So, your account remains insecure even after the changing of password

## Attachments
No attachments
