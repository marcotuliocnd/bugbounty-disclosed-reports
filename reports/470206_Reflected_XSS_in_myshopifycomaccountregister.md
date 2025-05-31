# Reflected XSS in *.myshopify.com/account/register

## Report Details
- **Report ID**: 470206
- **URL**: https://hackerone.com/reports/470206
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-20T09:55:07.127Z
- **Disclosed**: 2019-03-12T16:21:08.480Z

## Reporter
- **Username**: ishahriyar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Shopify allows shop admin to enable customer registration. When a customer registers with a short password and HTML content as the first name and last name then customer redirects to *.myshopify.com/account/register with error messages and the provided data. As there is no Cross-site Scripting validation and CSRF protection anyone can force the customers to execute  XSS on that page.

{F394911}

## Impact

By exploiting this Vulnerability
An attacker can force the customer to execute XSS and 
1. Steal user's cookie.
2. Launch advanced phishing attacks by rendering arbitrary HTML forms.
3. Force users to download malware/viruses.
4. Execute browser-based attacks etc.

## Attachments
- poc.html
- Screencast_12-20-18_15_33_02.webm
