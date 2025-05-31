# Items bought for free due to lacks of quantity controls

## Report Details
- **Report ID**: 357929
- **URL**: https://hackerone.com/reports/357929
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-05-26T17:13:59.486Z
- **Disclosed**: 2018-08-31T12:43:21.141Z

## Reporter
- **Username**: nadino
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reverb

## Vulnerability Information
Hi,

The server fails to check the quantity of the items that are going to be sell. Values <= 0 are accepted as 1.

PoC:

Go here
https://sandbox.reverb.com/fr/item/139897-fender-2-strap-leather-test-2018-leather

Intercept the response after clicking "Add to cart" and put "quantity: 0"

{F302179}

Proceed to checkout

{F302180}

Place order

{F302181}

{F302182}

I used one of the fake credit cards you provide us.

## Impact

Items are sold gratis

## Attachments
- reverb_quantity_0.png
- reverb_0_euros.png
- reverb_final.png
- reverb_gratis.png
