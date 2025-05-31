# H1514 Wholesale customer without checkout permission can complete purchases

## Report Details
- **Report ID**: 423546
- **URL**: https://hackerone.com/reports/423546
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-13T22:40:37.218Z
- **Disclosed**: 2019-04-10T20:24:25.101Z

## Reporter
- **Username**: cablej
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
**Summary:**

By default, Shopify Wholesale customers are prevented from immediately checking out:

{F360280}

Instead, a store admin must approve each order before the customer can pay.

This restriction can be bypassed, allowing a customer to check out orders without prior approval. This also bypasses any maximum checkout amount that a store can set.

## Steps To Reproduce:

  1. As a Wholesale owner, ensure that a customer is disallowed from immediately checking out at https://your-store.myshopify.com/admin/apps/wholesale/admin/shops/x/accounts.
  1. As the customer, visit the Wholesale shop and fill your cart with products.
  1. Observe that the UI forces the user to submit a purchase order:

    {F360285}

  1. To bypass this restriction, intercept the request to `PUT /purchase_orders/submit` to submit the purchase order and change the url to `/purchase_orders/update_checkout`.
  1. Observe that executing the request will allow the customer to proceed through the checkout flow and place the order:

{F360296}

## Impact

This allows a customer to bypass manual approval restrictions for a Wholesale store and immediately check out.

## Attachments
No attachments
