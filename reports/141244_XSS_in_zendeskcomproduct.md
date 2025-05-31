# XSS in zendesk.com/product/

## Report Details
- **Report ID**: 141244
- **URL**: https://hackerone.com/reports/141244
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-26T17:21:14.256Z
- **Disclosed**: 2016-12-15T00:56:43.041Z

## Reporter
- **Username**: virtualhunter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zendesk

## Vulnerability Information
Vulnerable urls:
https://www.zendesk.com/product/tour/
https://www.zendesk.com/product/pricing/
or just https://www.zendesk.com/product/

Vulnerable parameter is a **cvo_sid1**, used in **live.js**  to call convertro code (without sanitizing). This leads to generating malformed javascript answer with XSS injection ability. (See screenshots below).
There is a restriction on a semicolon use, so i replaced it with %3b.

To reproduce vulnerability, you could try this safe example:
`https://www.zendesk.com/product/tour/#?cvo_sid1=1")%3balert(document.cookie%2b"`

This vulnerability provides a great opportunity for victim to lose not only cookies, but also control over the account after stealth forwarding to porposely generated link like this :))





## Attachments
- zendesk1a.jpg
- zendesk1b.jpg
