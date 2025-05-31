# store internal email disclosed through shopify-data-exporter 

## Report Details
- **Report ID**: 1605962
- **URL**: https://hackerone.com/reports/1605962
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-06-18T15:12:34.540Z
- **Disclosed**: 2022-09-15T19:21:56.713Z

## Reporter
- **Username**: xenx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
Hey Shopify,

When a store install ```shopify-data-exporter``` app to export various data of the store a link is sent to the store internal email. This internal email is disclosed via the below request to anyone 
```json
GET /?shop=your_store.myshopify.com HTTP/2
Host: shopify-data-exporter.shopifycloud.com
```
{F1779393}

## Shops Used to Test:
[xentest11.myshopify.com]

## Relevant Request IDs:
[54bb78a050a2fddbc3ae360ff72d1d3e]

## Steps To Reproduce:

  1.  Install ```shopify-data-exporter``` in your store (```https://apps.shopify.com/data-exporter-tax-compliance```)
  2.  After installing the app just add your store link in ```shop``` parameter in the above shown request
  3. In the response check for  ```data-recipient``` attribute. It exposes the internal store email.

## Impact

Store internal email disclose to anyone in ```shopify-data-exporter.shopifycloud.com?shop=``` via ```data-recipient``` attribute

## Attachments
- Screenshot_(44).png
