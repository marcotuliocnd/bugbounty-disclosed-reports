# Open redirect allows changing iframe content in *.myshopify.com/admin/themes/<id>/editor

## Report Details
- **Report ID**: 165046
- **URL**: https://hackerone.com/reports/165046
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-01T16:55:40.671Z
- **Disclosed**: 2016-09-22T17:04:13.832Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi ,

I managed to bypass the fix you deployed to the issue I reported in #159522.
Apparently this is what the fix does:

- Redirecting to `https://checkout.shopify.com/<exact_store_id> /` only is allowed.
- For example: `victim.myshopify.com/account/logout?return_url=https://checkout.shopify.com/<victim_store_id>/` will work 

- but `victim.myshopify.com/account/logout?return_url=https://checkout.shopify.com/<attacker_store_id>/` won't work 
- `https://checkout.shopify.com/<store_id>` no longer follows the 302 redirect rules added in the admin dashboard.

##Redirect bypass: 

`<victim>.myshopify.com/account/logout?return_url=https://checkout.shopify.com/<victim_store_id>/../14467660` 

Note that `14467660` is the attacker's store id.

The 302 redirect no longer works , but the attacker can still inject any HTML/JavaScript code in his store's 404 page that will redirect to any domain he wants.

##Change theme editor iframe content:

Here is the PoC:
`https://<your_store>.myshopify.com/admin/themes/<theme_id>/editor#/account/logout?return_url=https://checkout.shopify.com/<your_store_id>/../14467660`

Thanks!

## Attachments
No attachments
