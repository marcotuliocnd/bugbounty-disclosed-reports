# Reflected XSS in <any>.myshopify.com through theme preview

## Report Details
- **Report ID**: 226428
- **URL**: https://hackerone.com/reports/226428
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-05T21:22:15.520Z
- **Disclosed**: 2017-05-29T16:06:44.441Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,
I have found a reflected cross site scripting vulnerability in `<any>.myshopify.com` through `theme_hanlde` parameter due to not single quotes.

#Steps to reproduce: 
1. Navigate to `<account>.myshopify.com` 
2. view the source of the page and copy the value of `Shopify.theme` Id.
3. Navigate to `https://echo.myshopify.com/?theme_handle=xx%27-alert(document.cookie)-%27&style_id=1&style_handle=1&preview_theme_id=<theme_ID>` 
> *replace `<theme_ID>` with the ID you just copied*.
4. XSS will trigger in all of the online shop pages unless you click `Cancel theme preview` .

**PoC:** 
`https://test.myshopify.com/?theme_handle=xx%27-alert(document.cookie)-%27&style_id=1&style_handle=1&preview_theme_id=3572` 

{F182252}
Thanks!

## Attachments
- xss-triggered.png
