# [h1-2102] Stored XSS in product description via `productUpdate` GraphQL query leads to XSS at handshake-web-internal.shopifycloud.com/products/[ID]

## Report Details
- **Report ID**: 1085546
- **URL**: https://hackerone.com/reports/1085546
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-23T23:22:39.251Z
- **Disclosed**: 2022-07-11T21:33:50.391Z

## Reporter
- **Username**: intidc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
This is most likely going to be a duplicate, so I'll keep it short.

A stored cross site scripting vulnerability exists at `handshake-web-internal.shopifycloud.com` through the `product description` field.

## Recruirements

A shop with the Handshake plugin enabled and set-up

## Reproduction steps

1. Add a product in your store with the following description (make sure to click the < > button first so you can enter HTML):

> <img src=x onerror=prompt(document.domain)>

then set it to `Active`:

{F1169545}

2. Go to your Handshake portal, pick a price and a category to publish the item:

{F1169544}

3. Check your item in the on the handshake website, XSS will pop up after +/- 3 seconds:

{F1169546}

(I removed the PoC for obvious reasons, please do the same when triaging or everyone will submit)

## Impact

Arbitrary javascript execution (stored) on a shared domain

## Attachments
- Screenshot_2021-01-24_at_00.17.16.png
- Screenshot_2021-01-24_at_00.20.02.png
- Screenshot_2021-01-24_at_00.17.57.png
