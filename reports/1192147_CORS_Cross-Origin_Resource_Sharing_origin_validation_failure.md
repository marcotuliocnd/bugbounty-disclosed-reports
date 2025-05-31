# CORS (Cross-Origin Resource Sharing) origin validation failure

## Report Details
- **Report ID**: 1192147
- **URL**: https://hackerone.com/reports/1192147
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-11T14:00:17.204Z
- **Disclosed**: 2021-12-09T19:18:48.762Z

## Reporter
- **Username**: kapil18
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
***ATTACK  DETAILS***

Access-Control-Allow-Origin: https://sifchain.finance.evil.com
Access-Control-Allow-Credentials: true
Prefix origins are accepted (www.example.com trusts example.com.evil.com)


***Vulnerability Description***

CORS (Cross-Origin Resource Sharing) defines a mechanism to enable client-side cross-origin requests. This application is using CORS in an insecure way.

The web application fails to properly validate the Origin header (check Details section for more information) and returns the header Access-Control-Allow-Credentials: true.

In this configuration any website can issue requests made with user credentials and read the responses to these requests. Trusting arbitrary origins effectively disables the same-origin policy, allowing two-way interaction by third-party web sites

## Impact

***The impact of this vulnerability***

Any website can issue requests made with user credentials and read the responses to these requests.

## Attachments
No attachments
