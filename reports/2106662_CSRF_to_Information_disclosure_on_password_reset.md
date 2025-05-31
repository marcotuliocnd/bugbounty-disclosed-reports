# CSRF to Information disclosure on password reset

## Report Details
- **Report ID**: 2106662
- **URL**: https://hackerone.com/reports/2106662
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-08-11T15:51:35.245Z
- **Disclosed**: 2023-11-27T10:18:02.535Z

## Reporter
- **Username**: hackeriron1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
Hi Team,

It's low hanging security risk but it's significant for users. where attacker able to get victim IP, Address and Browser details. 
This is disclosing users information. one click information disclosed. 

CSRF vulnerability on password reser link.
Attacker can ask for a password reset link on his own email by sending a link to the Victim, which will contain the Victim's IP address and browser details.


## Steps To Reproduce:
1. Go to ███████ and change email to your own email.
2. send to victim and victim will open in browser.
3. Automatically Password reset link send 

## Supporting Material/References:
POC Video you can see. 
███

## Impact

Attacker can ask for a password reset link on his own email by sending a link to the Victim, which will contain the Victim's IP address and browser details.

## Attachments
No attachments
