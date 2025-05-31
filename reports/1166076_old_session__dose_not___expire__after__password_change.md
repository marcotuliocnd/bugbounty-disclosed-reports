# old session  dose not   expire  after  password change 

## Report Details
- **Report ID**: 1166076
- **URL**: https://hackerone.com/reports/1166076
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-04-15T22:47:37.583Z
- **Disclosed**: 2021-08-31T09:16:12.247Z

## Reporter
- **Username**: scorpion_0a0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
hello  all ::

I discovered that the application Failure to invalidate session after password changed . In this scenario changing the password doesn't destroys the other sessions which are logged in with old passwords.

url:: ==https://app.upchieve.org/==

STEPS TO REPRODUCE:

1- create account in  ==https://app.upchieve.org/== and login in two browser ==[firefox an Chrome]==
2- go to reset password and change it 
3- you will see that session not expire and accountThe account is still  loged in  with old password 


please follow me in  this vedio ::

{F1267183}


Mitigation

When some change in user password, each and every active sessions that belongs to that particular account must be destroyed!
I would like to recommend you to add a process that asks users whether user want to close all open sessions or not right after changing password.
So there is two way, either you let users to choose if they want to keep active sessions or just destroy every active sessions when an users change his/her password!
Please fix this Vulnerability and let me know. Looking forward to hear from you

## Impact

Due to this bug, there is no way for the victim to revoke access of attacker if account has been already compromised
and If attacker have user password and logged in different places, As other sessions is not destroyed, attacker will be still logged in your account even after changing password, cause his session is still active.. Malicious actor can complete access your account till that session expires! So, your account remains insecure even after the changing of password

## Attachments
- session-not-expire-after-change-password.mp4
