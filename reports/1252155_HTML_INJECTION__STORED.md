# HTML INJECTION  (STORED)

## Report Details
- **Report ID**: 1252155
- **URL**: https://hackerone.com/reports/1252155
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-07-06T03:16:24.810Z
- **Disclosed**: 2023-02-01T03:35:18.184Z

## Reporter
- **Username**: criptex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
Hi team!

I found a way to inject arbitrary html which is also persistent or stored.
Unfortunately I could not execute javascript code, however I think that being stored html it is important to take a look, attackers could use this vulnerability for phishing attacks for example.

###PoC

https://judge.me/profile/y5YJe35X

You can see in the product description how I can add various html elements.

###To reproduce this:

In your profile judge.me go to "my public profile" then my recommendations, now add some html tags in description and then press "add recommendation"


{F1366217}

## Impact

Attackers can use this vulnerability to carry out phishing attacks. It is important to mention again that the stored html code has more impact, the victim does not need user interaction as in the case of the reflected xss.
Also, an attacker could generate good ratings and fake reviews by using html about your product to build trust.

## Attachments
- htmlinjection.png
