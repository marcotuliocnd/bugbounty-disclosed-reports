# Reflected XSS on help.shopify.com

## Report Details
- **Report ID**: 1940245
- **URL**: https://hackerone.com/reports/1940245
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-04-09T23:51:15.057Z
- **Disclosed**: 2024-01-25T15:01:57.497Z

## Reporter
- **Username**: becfe31193676118ae5073d
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
Reflected Cross Site Scripting  (XSS) on https://help.shopify.com/en/support/confirm-account-details?returnTo=

## Platform(s) affected:
All platforms in other languages, exp:
* https://help.shopify.com/es/

## Steps To Reproduce:

  1. Open the URL https://help.shopify.com/en/support/confirm-account-details?returnTo=javascript:alert(document.cookie)
  2. Make login
  3. Back again to https://help.shopify.com/en/support/confirm-account-details?returnTo=javascript:alert(document.cookie)
  4. Click on button "Continue"
  5. The JS will execute.

Notes: 
* If the user already logged, just access the url and click on the button that the js will be executed.
* Also possible make a "Open redirect" when the user click on the button.
   EXP:  
https://help.shopify.com/en/support/confirm-account-details?returnTo=https://evil.com

## Supporting Material:

## Impact

The attacker can execute javascript code and redirect targets for others pages.

## Attachments
- poc_shopify.png
