# Exposure of shopify employee summit page allows anonymous user to place orders for free books

## Report Details
- **Report ID**: 2552027
- **URL**: https://hackerone.com/reports/2552027
- **State**: Closed
- **Severity**: none
- **Submitted**: 2024-06-14T02:10:39.923Z
- **Disclosed**: 2024-07-29T14:55:21.263Z

## Reporter
- **Username**: g0lden1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
The online shop at https://book-bar.shopify.io/ appears to be for a shopify employee summit. On this site, with no promo code, any user can checkout books for free. I only did one in the PoC (Feel free to cancel that or tell me how to). It appeared that I was able to put as many books as was available in my cart to checkout. So an anonymous user could claim all the product.

## Steps To Reproduce:
  1. Browse to https://book-bar.shopify.io/
  2. Select a book that is not sold out, and add it to your cart
  3. Fill out shipping information, no payment info is needed, and confirm the checkout
  4. You will see a "Thank you for your purchase" screen confirming your FREE selection. 

## Supporting Material:
Please see the attached video of me being able to add "Sapiens" to my cart, and checkout for free. (Also, feel free to cancel the transaction!)

 ## Video PoC
██████

## Impact

## Summary:
An anonymous user can claim all the books and free merchandise, and essentially empty out the entire shop and ship it for free.

## Attachments
No attachments
