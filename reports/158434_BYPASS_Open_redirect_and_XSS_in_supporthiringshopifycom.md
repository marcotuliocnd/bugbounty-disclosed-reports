# (BYPASS) Open redirect and XSS in supporthiring.shopify.com

## Report Details
- **Report ID**: 158434
- **URL**: https://hackerone.com/reports/158434
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-11T11:28:42.427Z
- **Disclosed**: 2016-11-21T13:24:43.798Z

## Reporter
- **Username**: jamesclyde
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello,

The users can be redirected to some other site which is in control of the attacker from 

Vulnerable parameter: path=

You have a protection here at path= but it bypass the parameter if you add a double slash, like %2F%2F.

Let's say user is attacker asked victim to came to this page: :
http://supporthiring.shopify.com/apps/locksmith/resource/pages/gauntlet-challenge?&path=%2F%2Fevil.com

Victim will be see a 404 error page and after 2 seconds he will be redirected to: https://evil.com

These can be controlled by the attacker and used in other attacks

Works in all browsers!!




## Attachments
No attachments
