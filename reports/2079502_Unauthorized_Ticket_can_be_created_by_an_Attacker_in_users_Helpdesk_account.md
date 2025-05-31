# Unauthorized Ticket can be created by an Attacker in user's Helpdesk account

## Report Details
- **Report ID**: 2079502
- **URL**: https://hackerone.com/reports/2079502
- **State**: Closed
- **Severity**: none
- **Submitted**: 2023-07-21T23:57:21.271Z
- **Disclosed**: 2023-09-08T09:29:52.808Z

## Reporter
- **Username**: fanimalikhack
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hey Team! 

I was able to create a ticket in any user's Support.hackerone.com account without authorization, and can write whatever I wanted in that ticket. Normally, in order to get help, users are required to log in and create a ticket. However, due to this flaw, I could create tickets on behalf of any user without their permission or knowledge. 


### Steps To Reproduce

1. Go to https://emkei.cz/ and enter victim's email as the sender, and support@hackerone.com as the receiver. Fill out other necessary details.

2. Solve the captcha and send the email.

3. Check your helpdesk account at support.hackerone.com and you will see new ticket.


### Optional: Supporting Material/References (Screenshots)

https://medium.com/@khaled.hassan/hacking-thousands-of-companies-through-their-helpdesk-8f180a8595ef

POC :
████

## Impact

Unauthorized user can create  tickets in any user's help desk account!

## Attachments
No attachments
