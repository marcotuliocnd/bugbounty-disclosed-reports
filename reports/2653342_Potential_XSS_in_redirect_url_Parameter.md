# Potential XSS in redirect_url Parameter

## Report Details
- **Report ID**: 2653342
- **URL**: https://hackerone.com/reports/2653342
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-08-12T21:27:35.362Z
- **Disclosed**: 2024-11-06T09:19:15.692Z

## Reporter
- **Username**: kindone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
An XSS vulnerability has been identified on https://learn.acronis.com/ in the redirect_url parameter. By manipulating the redirectUrl parameter, it is possible to inject arbitrary JavaScript code

## Steps To Reproduce
1) Log in to your https://learn.acronis.com/ account

2) Navigate to the following URL:
https://learn.acronis.com/portal/licensing-check?redirect_url=javascript:alert(document.domain)
 
3) Observe that an alert box displaying the current domain (document.domain) appears, indicating that the JavaScript code was executed.

{F3517115}

## Suggested Fix:
Validate and sanitize the redirectUrl parameter to ensure that it does not contain any malicious content. This can be done by:

  -  Restricting the parameter to only allow URLs that belong to the same origin.
  -  Encoding or escaping any user input before including it in the URL.

## Impact

An attacker can perform the following actions using this vulnerability:

   - Steal sensitive information, such as cookies, session tokens, or other sensitive data.
 -   Perform actions on behalf of the victim by exploiting their authenticated session.

## Attachments
- bug.png
