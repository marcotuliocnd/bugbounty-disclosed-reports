# [h1-2102] HTML injection in packing slips can lead to physical theft

## Report Details
- **Report ID**: 1087122
- **URL**: https://hackerone.com/reports/1087122
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-25T23:51:32.561Z
- **Disclosed**: 2022-07-11T21:35:25.241Z

## Reporter
- **Username**: intidc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
A HTML injection vulnerability exists in the packing slip generator, allowing customers to alter the logistical process of their and other's orders for shops that choose to display the user's e-mail address on the packing slip. The success rate depends on the shops setup and can result in financial losses for the affected stores.

###Background - how stores use the packing slip
Once an order comes in, the packing slips and shipping labels get printed to be processed. From my understanding, when preparing orders, logistical teams don't go back and forth between the Shopify orders, but print the packing slips in bulk (hence the new ability to print in bulk), fill the boxes in the warehouse with whatever is on the packing slip, put on a shipping label on the box and send it off.
Should the customer be able to alter these packing slips upon printing, it could be possible to alter what (and how many) items will be in their box. It is observed that this is possible using some CSS tweaks and a HTML injection in the e-mail field.

## Prerequisites

- You'll need a store with a product that you can order. You can either work with a bogus payment gateway, or set the price of the product to 0 and mark it as a non-physical good so there's no shipping costs involved.

## Steps To Reproduce:
-  Go to admin > delivery and set a packing slip template that displays the user's e-mail address in the billing / checkout info. **You can use the one in the attachment** (packingslip.txt). The example should look like this:

{F1171862}

- As a customer, go to the store and check out the item. **Buy only one**, we'll alter the amount through this bug as a PoC.

{F1171898}

- Enter the following e-mail (yes, this is a valid e-mail address, see  [RFC3696](https://tools.ietf.org/html/rfc3696)):

> "<style>.flex-line-item-quantity>p{font-size:0}.flex-line-item-quantity:after{content:'1337\0000a0of\0000a01337';margin-left:420px;}</style>"@gmail.com

{F1171899}

- Complete your order:

{F1171900}

- You're done! Now wait and profit!

**From the shop employee's perspective, go to orders. You have a new order, yay!**

Free product has been ordered one time. Great! Let's print the packing slip (in big stores this would be printed in bulk, so people wouldn't really notice anything):

{F1171902}

Notice that the packing slip looks like this:

{F1171903}

Seems like the logistics team will be shipping *1337* items in instead of 1. We only paid for 1.
We could also alter other stuff, like the actual item, or when printed in bulk, we could alter _other_ people's packing slip. The sky is the limit! This won't work for all shops, but when it does, the impact will be very effective.

## Impact

- Literally steal goods
- Alter other people's stuff as well if they use the bulk printer (e.g. add a special note, put your return address on the slip instead of the shop's, etc...)

## Attachments
- packingslip.txt
- Screenshot_2021-01-25_at_23.46.30.png
- Screenshot_2021-01-26_at_00.30.51.png
- Screenshot_2021-01-26_at_00.31.16.png
- Screenshot_2021-01-26_at_00.31.27.png
- Screenshot_2021-01-26_at_00.45.53.png
- Screenshot_2021-01-26_at_00.46.37.png
