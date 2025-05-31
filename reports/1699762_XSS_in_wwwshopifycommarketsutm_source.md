# XSS in www.shopify.com/markets?utm_source=

## Report Details
- **Report ID**: 1699762
- **URL**: https://hackerone.com/reports/1699762
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-09-14T08:30:04.165Z
- **Disclosed**: 2022-10-18T07:14:46.052Z

## Reporter
- **Username**: noblesix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello, hope you are having a good day :)

## Summary:
I found a reflected XSS in `www.shopify.com/markets` using the `utm_source` parameter

Reflected XSS vulnerabilities arise when the application accepts a malicious input script from a user and then it is executed in the victim's browser. Since the XSS is reflected, the attacker has to trick the victim into executing the payload, usually using another website or by sending a specially crafted link

##### URL: `https://www.shopify.com/markets`
##### INJECTION POINT: `utm_source` parameter
##### PAYLOAD: `injection%22%20style=%22animation-name:swoop-up%22%20onanimationstart=%22alert(document.domain)`

## Steps To Reproduce:
Visit this URL:  
```
https://www.shopify.com/markets?utm_source=INJECTION%22%20style=%22animation-name:swoop-up%22%20onanimationstart=%22alert(document.domain)
```

By visiting that link you'll get an alert on your screen, that demonstrates the existence of the vulnerability.

{F1925617}

The attack is unauthenticated

## Recommended Fix
Correctly escape special characters such as `<` `>` `"` `'` based on the context where the string gets reflected.

Thank you.

## Impact

An attacker could steal user cookies, create a trusted phishing page or bypass any CSRF protection mechanism.

## Attachments
- Schermata_2022-09-14_alle_10.27.11.png
