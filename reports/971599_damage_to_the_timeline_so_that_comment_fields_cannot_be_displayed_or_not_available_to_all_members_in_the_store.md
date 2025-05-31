# damage to the timeline so that comment fields cannot be displayed or not available to all members in the store

## Report Details
- **Report ID**: 971599
- **URL**: https://hackerone.com/reports/971599
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-08-31T20:31:36.785Z
- **Disclosed**: 2020-09-09T16:45:15.103Z

## Reporter
- **Username**: jaka-tingkir
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
see https://a-alert-b-y000-b-finda.myshopify.com/admin/discounts/416981811222


I tried to make a discount code with a product name and a discount code like: ± <img src = x onerror = alert (1)> ±

when I havehtag (#) the product name on the timeline (comment) and I get a "server error" reply and it causes crashes to the timeline, so comments are automatically inactive or non-existent.

This can be done by members who want to destroy the shop, so that all members of the shop feel the impact.

## step for reproduction
1. create a product name and discount code using a payload like: ± <img src = x onerror = alert (1)> ±
2. Product name hashtags in the timeline
3. The comment field cannot be displayed

## Impact

The comment field cannot be displayed

## Attachments
- load.mp4
- impact
