# HTTP Parameter Pollution using semicolons in iframe element at hackerone.com/careers allows loading external Greenhouse forms

## Report Details
- **Report ID**: 298265
- **URL**: https://hackerone.com/reports/298265
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-12-15T14:29:49.649Z
- **Disclosed**: 2018-03-13T20:14:44.096Z

## Reporter
- **Username**: kapytein
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
I noticed that HackerOne career pages loads it's application forms from Greenhouse.io via an iframe. The **gh_jid** parameter value is taken into the iframe element for the token parameter in the iframe URL (boards.greenhouse.io). Any html characters are escaped in order to avoid XSS (and possibly also to avoid any additional parameters to be included to avoid that parameters are overridden). However, I have discovered that I could load any form on the page.

**Description (Include Impact):**
Basically, you can load any form of Greenhouse.io via a GET request. I am not entirely sure how Greenhouse works (I also can not discover how it actually works since you only have paid subscriptions at Greenhouse), but you might also be able to craft pages instead of forms only (which would be more effective for a phishing attack, than only a form).

This happens because due to the fact that you can include a semicolon in the iframe element. As stated on https://en.wikipedia.org/wiki/Query_string, a semicolon can be used besides the ampersand in URLs embedded in HTML. 

### Steps To Reproduce

1. Go to https://www.hackerone.com/careers?gh_jid=795069;for=airbnb for example.
2. You will notice an AIrbnb application form being loaded on the page.

(I sadly could not test my own forms, hence why I have used Airbnb forms to load on the page, as stated above).

A fix would be to either escape the semicolon, or to adjust the position of the for parameter in the iframe URL to avoid the URL being overridden. 

Example for changing the order of the URLs:

* https://boards.greenhouse.io/embed/job_app?for=hackerone&token=795069;for=airbnb&b=https%3A%2F%2Fwww.hackerone.com%2Fcareers (this would load the form as the parameter is overridden).

with

* https://boards.greenhouse.io/embed/job_app?token=795069;for=airbnb&b=https%3A%2F%2Fwww.hackerone.com%2Fcareers&for=hackerone (this would not load the form as the parameter is not overridden).


PS: After my pretty much failed report (#289999) (which was valid, but the way I described the vulnerability made it invalid), I appreciate any feedback on the quality of my report! Thanks in advance.

## Impact

An attacker can load any other forms on the page, and possibly craft pages as well, but that depends on how Greenhouse.io actually works with it's forms. Therefore, a phishing attack would be possible.

## Attachments
No attachments
