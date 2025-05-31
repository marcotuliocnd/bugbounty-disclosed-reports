# Information disclosure ( Google Sales Channel )

## Report Details
- **Report ID**: 1584718
- **URL**: https://hackerone.com/reports/1584718
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-05-29T14:41:03.086Z
- **Disclosed**: 2022-07-17T14:10:17.793Z

## Reporter
- **Username**: urfavenemy01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
In the review on apps.shopify.com the Google sales channel has a review of 5407 but the actual number of shopify stores that use the Google channel I believe is more than that number so I think this vulnerability can have an impact on many shopify stores and here I found a vulnerability where attackers can exploit every shopify store that has a Google Sales channel even though the store is in Password protection

1. Install google channel at your-store.myshopify.com
2. Enable password protection at your-store.myshopify.com
3. Add new product in shopify store
4. Now go to this link : google-shopping.shopifycloud.com/shopify/products?shop=your-store.myshopify.com&id=PRODUCT ID&locale=en
Change PRODUCT ID with your shopify product id
5. Now in the response you will see information disclosure in the form of data-channel-id and data-user-email

```
data-channel-id="70715703461"
data-user-email="VICTIMEMAIL@gmail.com"
```

Even though the shopify store which is in a password protected state is very private, but in this vulnerability the attacker can still find out sensitive information from the shopify store which is in a password protected state.
Stores that do not have a password protected are easier to exploit because attackers can get the product id of the victim's store

## Impact

Vulnerabilities that allow attackers to get sensitive information from victim stores

## Attachments
No attachments
