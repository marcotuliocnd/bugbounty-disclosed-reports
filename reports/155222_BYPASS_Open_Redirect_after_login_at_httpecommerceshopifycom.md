# (BYPASS) Open Redirect after login at http://ecommerce.shopify.com

## Report Details
- **Report ID**: 155222
- **URL**: https://hackerone.com/reports/155222
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-30T00:49:24.264Z
- **Disclosed**: 2016-09-01T16:00:50.952Z

## Reporter
- **Username**: jamesclyde
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

The users can be redirected to some other site which is in control of the attacker from http://ecommerce.shopify.com/accounts

Let's say user is attacker asked victim to login from the here :
https://ecommerce.shopify.com/accounts?return_to=%40evil.com/

When victim enters the password he is redirected to https://evil.com

These can be controlled by the attacker and used in other attacks

Works in all browsers!!






## Attachments
No attachments
