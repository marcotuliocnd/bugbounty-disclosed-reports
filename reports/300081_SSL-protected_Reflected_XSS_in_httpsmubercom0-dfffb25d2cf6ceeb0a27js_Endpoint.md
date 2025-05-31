# SSL-protected Reflected XSS in https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js Endpoint

## Report Details
- **Report ID**: 300081
- **URL**: https://hackerone.com/reports/300081
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-12-22T18:00:25.129Z
- **Disclosed**: 2017-12-26T11:03:53.114Z

## Reporter
- **Username**: gregoryvperry
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
## Summary
The _ga request parameter at the https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js mobile endpoint is copied into a javascript string encapsulated in double quotation marks, resulting in SSL-protected payloads being reflected unmodified in the application's response. The script-src whitelist at the endpoint includes a wildcard *.cloudfront.net host, which could be used by any attacker with an Amazon Web Services account to provision an arbitrary cloudfront.net host to serve trusted files from. The endpoint also has a missing base-uri, which allows the injection of base tags. They can be used to set the base URL for all relative (script) URLs to an attacker controlled domain. In addition to the reflected XSS issue, both the script-src and basi-uri issues are considered high severity findings under Content Security Policy 3.

## Security Impact
Arbitrary SSL-protected XSS can be reflected unescaped from the https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js mobile endpoint, resulting in the ability for an attacker to generate arbitrary javascript and/or html content.

## Reproduction Steps
https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js?_ga=asdf"}}</script><script>alert(1)</script>

## Specifics
The following unescaped code is rendered:

```
{"enabled":true,"sid":"bbc661585c424072","url":"www.cdn-net.com","cf":1022963},"queryParams":{"_ga":"asdf\"}}</script><script>alert(1)</script>"},"useragent":{"ua":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36","browser":
```

## Impact

With properly crafted javascript and/or html, an attacker could harvest Uber login and password credentials, credit card payment information etc.

## Attachments
No attachments
