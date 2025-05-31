# Unsanitized Location Name in POS Channel can lead to XSS in Orders Timeline

## Report Details
- **Report ID**: 166887
- **URL**: https://hackerone.com/reports/166887
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-08T16:41:23.254Z
- **Disclosed**: 2016-09-19T16:02:04.941Z

## Reporter
- **Username**: nismo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi!

I would like to report XSS at Shopify Admin Interface in Orders TImeline, in line Usename processes this order at NAME

NAME is not sanitized and if this is set to <img src=x onerror=prompt(1)> XSS will happen

***POC***
Visit
https://whitehat-3.myshopify.com/admin/orders/2253786753
or
https://whitehat-3.myshopify.com/admin/orders/2253753665

XSS will trigger!

Thanks!


## Attachments
No attachments
