# *.shopify.com - Authentication bypass

## Report Details
- **Report ID**: 838231
- **URL**: https://hackerone.com/reports/838231
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-04-03T15:35:48.584Z
- **Disclosed**: 2020-08-24T16:18:08.375Z

## Reporter
- **Username**: nooblife
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I´ve found a flaw in the authentication process when accessing the website https://upcoming.shopify.com. There seems to be an HTTP Authentication in place to prevent access without authentication. Please follow below POC to get access to https://upcoming.shopify.com without login. The website is full with weird behavior and i´m able to register new accounts via https://upcoming.shopify.com. That could maybe lead to some internal issues.

***Normal request***
{F772305}

***POC**
1) Go to: https://upcoming.shopify.com/tools
2) From that point you can travel to any endpoint

{F772313}
{F772314}
{F772315}

## Impact

High

## Attachments
- httpbasic.png
- shopify1.png
- shopify2.png
- shopify3.png
