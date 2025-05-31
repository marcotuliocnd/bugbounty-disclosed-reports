# [CSRF] Install premium themes 

## Report Details
- **Report ID**: 103351
- **URL**: https://hackerone.com/reports/103351
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-12-04T01:13:24.382Z
- **Disclosed**: 2016-07-27T18:52:19.703Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi , I have found a CSRF issue in themes.shopify.com when installing premium themes.
#Details:
When going to a premium theme page for example: https://themes.shopify.com/themes/editions/styles/light/ there is a button saying `Preview in your store` , clicking that button sends a **POST** request to `https://themes.shopify.com/themes/editions/styles/light/demo` with an **authenticity token** to prevent CSRF , but going to the url `https://themes.shopify.com/themes/editions/styles/light/demo ` directly will get the theme installed without any validation for the authenticity token.
#Steps to reproduce:
1. Go to themes.myshopify.com then login with your store
2. Go to https://themes.shopify.com/themes/editions/styles/light/demo and the theme `editions` will be installed in your shop
3. To confirm go to `https://<your_store>.myshopify.com/admin/themes` and you'll see the theme installed there.

Thanks

## Attachments
No attachments
