# Open redirect using checkout_url

## Report Details
- **Report ID**: 159522
- **URL**: https://hackerone.com/reports/159522
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-15T18:09:01.794Z
- **Disclosed**: 2016-09-01T16:55:02.115Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi , I would like to report an open redirect issue in `<account>.myshopify.com/account/logout` and `<account>.myshopify.com/account/login`
#Details:
Your application allow redirecting to `https://checkout.shopify.com/` through `https://<shop>.myshopify.com/account/logout?return_url=<url>` 
The page `https://checkout.shopify.com/<Store_id>` will display the 404 page of the store. 

Here is how this can be used for open redirection: 
1. Attacker creates a store then adds a new URL redirect with `/[Store_id]` in the **Old path** field and the malicious website(e.g:evil.com) in the **Redirect to** field.
{F112369}
2. Attacker sends the victim a link like this: 
`https://<victim>.myshopify.com/account/logout?return_url=https://checkout.shopify.com/[Attacker's_store_id] `
3. The victim will be redirected to the malicious website. 

#PoC:
`https://<account>.myshopify.com/account/logout?return_url=https://checkout.shopify.com/14372648`
This will redirect you to evil.com

`https://<account>.myshopify.com/account/login?checkout_url=https://checkout.shopify.com/14372648`
This will redirect you to evil.com after you login. 

Thanks!

## Attachments
- url_redirect.png
