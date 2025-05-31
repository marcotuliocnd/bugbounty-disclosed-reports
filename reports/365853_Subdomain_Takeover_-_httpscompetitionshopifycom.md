# Subdomain Takeover - https://competition.shopify.com/

## Report Details
- **Report ID**: 365853
- **URL**: https://hackerone.com/reports/365853
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-06-14T04:26:21.517Z
- **Disclosed**: 2018-06-19T03:35:19.055Z

## Reporter
- **Username**: llt4l
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Dear Shopify Security Team,

The Shopify.com subdomain competition.shopify.com was vulnerable to a subdomain takeover as it was pointing to an unclaimed Heroku service through the CNAME competition.shopify.com.herokudns.com, while the custom domain 'competition.shopify.com' was unclaimed in Heroku.

To prevent an attacker from claiming the domain and using it for malicious purposes, and also as a proof of concept, I have claimed the domain in Heroku and uploaded a proof of concept, which you can view here: https://competition.shopify.com/329a01fddb5a552265170b02c579c85f.html (I've also redirected visitors of the index page to https://shopify.com)

To fix the issue, there are two possible solutions. If you would like to re-start using Heroku with this domain, I can remove the custom domain from my Heroku app. Otherwise you may choose to delete the entry from your DNS servers, which will also fix the problem.

## Impact

I don't think I need to go into the security implications of a malicious attacker hijacking the domain, but here are a few possible attacks that could be performed if a malicious attacker were to hijack the domain:
* The ability for an attacker to execute JavaScript to steal user cookies and/or using the site as an endpoint for browser exploitation.
* Using the subdomain as a fool-proof phishing site (stealing Shopify customer/employee credentials). SSL has also been enabled, giving end users more trust of the site.
* Defacement of the website, or deployment of a fake site, such as a fake Shopify competition that harvests customer credit card details.
* Spreading of malware, or use of the domain as a C2 server.

I look forward to hearing back from your team.

Regards,
t4

## Attachments
- competition.shopify.com.png
