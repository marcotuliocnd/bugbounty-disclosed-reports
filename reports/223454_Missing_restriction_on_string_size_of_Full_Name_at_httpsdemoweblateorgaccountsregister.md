# Missing restriction on string size of Full Name at https://demo.weblate.org/accounts/register/

## Report Details
- **Report ID**: 223454
- **URL**: https://hackerone.com/reports/223454
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T14:01:33.917Z
- **Disclosed**: 2017-05-18T02:55:15.105Z

## Reporter
- **Username**: sumit7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi there

#Vulnerability Title:
>During my regular testing, I have found that there was no restriction on the amount of text that can be inserted into a user's Full name field.
 
#Security Impact:
>When the text size was large enough the service  resulting in a momentary outage in our non-production environment (not high-availability). An internal reproduction showed isolated disruption but no outage in our production environment.

#Mitigation:
>To mitigate, please restrict limit of user input field of Full name like you have already enforced on the fields E-mail and User name. 

If you need more info, be free to ask.


Happy to help.

Regards,
@smit

## Attachments
No attachments
