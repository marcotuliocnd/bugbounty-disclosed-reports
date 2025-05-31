# One Click XSS in [www.shopify.com]

## Report Details
- **Report ID**: 1563334
- **URL**: https://hackerone.com/reports/1563334
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-05-09T10:15:55.369Z
- **Disclosed**: 2022-07-13T06:13:14.473Z

## Reporter
- **Username**: comwrg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Steps To Reproduce:

  1. You need a web server, put {F1722320} to www
  2. visit it: http://<host>:<port>/poc.html?x=${alert(1)}
3. click it
4. you will see the alert

## Supporting Material:

{F1722333}

## Impact

Cookie Stealing - A malicious user can steal cookies and use them to gain access to the application.
Arbitrary requests - An attacker can use XSS to send requests that appear to be from the victim to the web server.
Malware download - XSS can prompt the user to download malware. Since the prompt looks like a legitimate request from the
site, the user may be more likely to trust the request and actually install the malware.
Defacement - attacker can deface the website usig javascript code.

## Attachments
- poc.html
- poc.mp4
