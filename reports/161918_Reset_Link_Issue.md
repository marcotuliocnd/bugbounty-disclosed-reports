# Reset Link Issue

## Report Details
- **Report ID**: 161918
- **URL**: https://hackerone.com/reports/161918
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-08-21T12:20:56.525Z
- **Disclosed**: 2016-08-30T00:03:49.508Z

## Reporter
- **Username**: i1ackerone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hello,
i found out about an issue in your password reset links and their expiration
Steps to reproduce:
Request a password reset link to an account
Login to the account afterwards
Logout and use the link to reset the password
The link would not be expired

Now i know that the links need to expire after a certain time, but thinking logically there is no point of keeping the link alive once the user has logged in, It indicates the possibility that the user's original email has been compromised and the attacker has requested the link, This way the user's account can be compromised.

Attack Scenario:
Attacker requests the password reset link, User logs in, Link does not expire even after that. The attacker can use the link easily. Infact requesting a link when the account is logged in from a location should be prohibited to prevent compromise

I think this should be fixed, 
Thanks

## Attachments
No attachments
