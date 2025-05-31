# Stored XSS in partners dashboard

## Report Details
- **Report ID**: 271765
- **URL**: https://hackerone.com/reports/271765
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-09-25T20:35:48.248Z
- **Disclosed**: 2018-04-18T17:15:46.340Z

## Reporter
- **Username**: bastianwelfrid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello


Stored XSS and UI redressing on https://partners.shopify.com/[partnerID]/confirm.

PoC:

1.Change your First Name and Last Name with XSS payload on https://accounts.shopify.com/account
2.Create an account on https://partners.shopify.com/ or if you have an account on https://partners.shopify.com/,go to https://partners.shopify.com/[partnerID]/complete

You'll see the stored XSS


1. https://partners.shopify.com/[partnerID]/confirm
2. https://partners.shopify.com/[partnerID]/complete
are missing with X-Frame-Options header.

Maybe an attacker can attack user with clickjacking.


## Attachments
- XSS.png
