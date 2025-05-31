# XSS in "explore-keywords-dropdown" results.

## Report Details
- **Report ID**: 347567
- **URL**: https://hackerone.com/reports/347567
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-05-04T17:16:05.673Z
- **Disclosed**: 2018-05-09T18:06:18.659Z

## Reporter
- **Username**: gcurtiss_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
It seems that people have exploited this vulnerability before on this website, however, it remains unpatched, so here I am reporting the vulnerability.

A XSS vulnerability exists when a restaurant or dish is created with a malicious name. The title of the dish or restaurant is not properly filtered by the web application. Any code in the dish or restaurant name is executed on the client.

DEMO: https://www.zomato.com/kingman-ks/restaurants, search for: single quote, double quote, GT angle bracket. '">

## Impact

An attacker could achieve XSS and inject hooks into the web browser (e.g. BeEF)

## Attachments
No attachments
