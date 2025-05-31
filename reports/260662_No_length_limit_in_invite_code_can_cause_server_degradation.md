# No length limit in invite_code can cause server degradation

## Report Details
- **Report ID**: 260662
- **URL**: https://hackerone.com/reports/260662
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-16T09:45:54.392Z
- **Disclosed**: 2017-08-31T04:57:44.411Z

## Reporter
- **Username**: gujjuboy10x00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi Team,

I get to know that in every field is secured by restricted limit by length,
but, i can see that one place where you forget to add that security feature , which can cause server degradation.

https://app.legalrobot-uat.com/dmca-safe-harbor

Here, i can see feature to add invite-code , but i can see there is no length limit in that filed.

i can recommend to restrict limit to 10-12 character (as per business requirement ).

Thanks,
Vishal. 

## Attachments
- invite_code.JPG
