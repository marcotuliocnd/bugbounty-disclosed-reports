# Stored XSS in *.myshopify.com

## Report Details
- **Report ID**: 241008
- **URL**: https://hackerone.com/reports/241008
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-17T13:20:45.777Z
- **Disclosed**: 2017-06-27T13:33:49.917Z

## Reporter
- **Username**: jamesclyde
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello,

First of all in noticed that this is out of scope "Any issue related to the storefront area being displayed in a <iframe> element in the admin area, for example in the Theme Editor." 

This is not in the store front and this will be set in an XSS payload.

1. Go to https://(YOUR SHOP).myshopify.com/admin/themes/THEME id)/editor
2. Select header and scroll down to "annoucement text".
3. Fill there as payload: "&gt;<img src="x" onerror="alert(document.cookie)">
4. Click save and the XSS will be popped up.

I have checked it twice and it is not gonna reflect on the store front. This XSS is in the myshopify/admin section.

POC screen:
https://snag.gy/FImTKd.jpg

## Attachments
No attachments
