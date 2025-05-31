# [ecommerce.shopify.com] Invalidated redirection

## Report Details
- **Report ID**: 175168
- **URL**: https://hackerone.com/reports/175168
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-11T16:47:52.126Z
- **Disclosed**: 2016-12-04T15:57:02.684Z

## Reporter
- **Username**: shailesh4594
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello,

**Endpoint :** https://ecommerce.shopify.com/auth/shopify?shop=[victim_shop].myshopify.com&return_to=/////example.com

Suppose, victim has not linked his shop with ecommerce.shopify.com portal then an attacker can redirect him on an external website after linking or rejecting. 

**Steps to reproduce :**

1. Get logged in as admin in your shop and ecommerce.shopify.com
2. Open this link : https://ecommerce.shopify.com/auth/shopify?shop=[your-shop].myshopify.com&return_to=/////example.com
3. If you are logged in then **Link These Accounts** button and **No thanks** link will be shown.
4. Click on **Link Account** button or **No thanks** link.
5. You will be redirected on https://example.com instead of ecommerce.shopify.com
6. Done

Again, your shop should not be linked to ecommerce.shopify.com.

**Suggested Fix :** Use more stronger regular expression at this endpoint

Best regards,
Shailesh

## Attachments
No attachments
