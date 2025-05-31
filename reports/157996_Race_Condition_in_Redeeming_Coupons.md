# Race Condition in Redeeming Coupons

## Report Details
- **Report ID**: 157996
- **URL**: https://hackerone.com/reports/157996
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-09T22:12:20.760Z
- **Disclosed**: 2016-09-12T08:40:37.759Z

## Reporter
- **Username**: cablej
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Hello,

There exists a race condition in redeeming coupons, allowing a user to redeem the same coupon multiple times, and stacking savings added. This allows for a user to get virtually any discount.

POC:

1. Visit your account and select 'Promo Codes'.
2. Select redeem promo code, and add any promo code. For example, I found the code 'dallas20'.
3. Intercept the request using a proxy, and make the request multiple times, asynchronously.
4. The code will be redeemed multiple times.

For an example, see the screenshot attached.

## Attachments
- screenshot.png
