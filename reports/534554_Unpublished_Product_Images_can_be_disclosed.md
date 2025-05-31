# Unpublished Product Images can be disclosed

## Report Details
- **Report ID**: 534554
- **URL**: https://hackerone.com/reports/534554
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-04-10T15:50:37.700Z
- **Disclosed**: 2019-06-12T13:54:05.608Z

## Reporter
- **Username**: h13-
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

This looks like a minor issue but felt like it was something worth reporting. Ideally, a product can be published or remain unpublished on any sales channel. If a product remains unpublished, then no information regarding it must be visible to public including product pictures.

But I found an endpoint which when queried with the `Product_ID` value of the unpublished product will returns its product image.

__STEPS__

1.Create product in Shopify Admin and upload a product image to it.
2.Make sure the product is not published in any sales channels/Apps.
{F466173}

3.Navigate to Online store front and check if any product is being shown/listed.
{F466174}

As you can see from above, no products or its images are visible.

4.Now navigate to the below endpoint

```
https://{shop_name}.myshopify.com/services/img?product={Product_ID}
```

Ex - https://bir1.myshopify.com/services/img?product=1767141736514

{F466175}

The product image of an unpublished item can be seen in the above screen shot

## Impact

Through the above vulnerable endpoint, it was possible for an unauthenticated user to query product images of unpublished products in Shopify store by specifying their `Product_ID`.

Thanks,
@h13-

## Attachments
- p1.JPG
- p2.JPG
- p3.JPG
