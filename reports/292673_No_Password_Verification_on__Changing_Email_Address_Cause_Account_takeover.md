# No Password Verification on  Changing Email Address Cause Account takeover   

## Report Details
- **Report ID**: 292673
- **URL**: https://hackerone.com/reports/292673
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-23T19:15:27.613Z
- **Disclosed**: 2018-05-19T12:42:08.859Z

## Reporter
- **Username**: nohack
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coursera

## Vulnerability Information
In coursera.org website, there is no password verification on changing email id. 

Generally when user try to change the password , they were asked to verify the request by entering old password. For the same reason a verification should be there on changing email.

But the worst part is, when user change email address then coursera.org website send verification mail on new mail id without asking current password or inform to old email id.

## Impact

if some one left his account open on public computer(say office or cafe), then attacker can change the email ,verify it himself. Then abuse forgot password field to take over whole account.

Suggested mitigation: 
a password field can be applied (just like Facebook do) or verification mail should be send on old email id registered.


If you required any POC then Let me know. 

Thanks

## Attachments
No attachments
