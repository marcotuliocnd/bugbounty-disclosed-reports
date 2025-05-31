# XSS vulnerable parameter in a location hash

## Report Details
- **Report ID**: 146336
- **URL**: https://hackerone.com/reports/146336
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-22T00:31:15.340Z
- **Disclosed**: 2019-10-16T09:47:48.170Z

## Reporter
- **Username**: virtualhunter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Hi!

There is a vulnerability on your pages, using convertro.

Vulnerable parameter from location hash (cvo_sid1), used in your live.js to call convertro code without sanitizing. On the convertro side it is sanitized, but with help of this parameter you could push another parameter (typ), that leads to generating malformed javascript answer with XSS injection ability. Like this : cvo_sid1=111\u0026;typ=[code injection] , where \u0026; is an ampersand symbol.
See screenshots below.
There is a restriction on a semicolon use, so i replaced it with %3b.

To reproduce vulnerability, you could try this safe example:
https://slack.com/is#?cvo_sid1=111\u0026;typ=55577]")%3balert(document.cookie)%3b//

This vulnerability provides a great opportunity for victim to lose not only cookies, but also control over the account after stealth forwarding to porposely generated link like this. I think, you know ;)

## Attachments
- slack1.jpg
- slack2.jpg
