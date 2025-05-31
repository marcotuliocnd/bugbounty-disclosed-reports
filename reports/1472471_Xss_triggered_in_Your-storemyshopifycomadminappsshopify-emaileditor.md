# Xss triggered in Your-store.myshopify.com/admin/apps/shopify-email/editor/****

## Report Details
- **Report ID**: 1472471
- **URL**: https://hackerone.com/reports/1472471
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-02-06T09:48:54.694Z
- **Disclosed**: 2022-04-25T11:01:01.398Z

## Reporter
- **Username**: danishalkatiri
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi team,
I have found `Store` Xss in shopify-email

#Reproduction Instructions /
1.Configure `shopify-email` for Shopify stores at https://apps.shopify.com/shopify-email
2.Goto `Your-store.myshopify.com/admin/apps/shopify-email/template-branding` 
3.Change F1607675 with "><img src=xx onerror=alert(document.domain)> click `Save`.
4.Now Select any F1607682.
#██████████

#Proof of Concept
███
████

## Impact

Stored XSS triggered.

## Attachments
- Store_name.PNG
- pre-built_template.PNG
