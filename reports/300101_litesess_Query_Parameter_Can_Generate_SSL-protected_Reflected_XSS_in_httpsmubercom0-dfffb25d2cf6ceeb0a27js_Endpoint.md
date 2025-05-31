# lite:sess Query Parameter Can Generate SSL-protected Reflected XSS in https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js Endpoint

## Report Details
- **Report ID**: 300101
- **URL**: https://hackerone.com/reports/300101
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-12-22T18:58:40.337Z
- **Disclosed**: 2017-12-26T11:04:49.924Z

## Reporter
- **Username**: gregoryvperry
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
## Summary
The lite:sess request parameter at the https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js mobile endpoint is copied into a javascript string encapsulated in double quotation marks, resulting in SSL-protected payloads being reflected unmodified in the application's response. The script-src whitelist at the endpoint includes a wildcard *.cloudfront.net host, which could be used by any attacker with an Amazon Web Services account to provision an arbitrary cloudfront.net host to serve trusted files from. The endpoint also has a missing base-uri, which allows the injection of base tags. They can be used to set the base URL for all relative (script) URLs to an attacker controlled domain. In addition to the reflected XSS issue, both the script-src and basi-uri issues are considered high severity findings under Content Security Policy 3.

## Security Impact
Using the lite:sess query variable, arbitrary SSL-protected XSS can be reflected unescaped from the https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js mobile endpoint, resulting in the ability for an attacker to generate arbitrary javascript and/or html content.

## Reproduction Steps
https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js?lite:sess=%22%7D}</script><div%20class%3D%27_b%20_c%20_d%20_e%20_f%20_g%20_h%20_i%20_a3%20_a4%20_a5%20_a6%20_a7%20_a8%20_a9%20_aa%20_ab%20_ac%20_ad%20_ae%20_af%20_ag%20_ah%20_ai%20_aj%20_ak%20_al%20_am%20_an%20_ao%20_ap%20_aq%20_ar%20_as%20_at%20_au%20_av%20_aw%27><a%20href%3D"http%3A%2F%2Fwww.lyft.com">Some%20arbitrary%20link%20text<%2Fa><%2Fdiv>%0A

## Impact

With a properly crafted javascript and/or html page, an attacker could harvest Uber login and password credentials, credit card payment information etc.

## Attachments
No attachments
