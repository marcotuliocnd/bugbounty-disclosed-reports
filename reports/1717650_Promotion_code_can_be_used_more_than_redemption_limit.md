# Promotion code can be used more than redemption limit.

## Report Details
- **Report ID**: 1717650
- **URL**: https://hackerone.com/reports/1717650
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-09-30T09:36:41.925Z
- **Disclosed**: 2023-02-13T22:04:14.701Z

## Reporter
- **Username**: d_sharad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripe

## Vulnerability Information
## Summary:
While creating a promotion code a user can specify number of times that code can be redeemed.(i.e. Redemption limit)
{F1962666}
Codes aren't supposed to be redeemed more than the redemption limit.
But there exists a race condition that allows use of promotion codes more than redemption limit.
{F1962665}

## Steps To Reproduce:
[In these steps i have used just a browser to show how easy this is to exploit and even a person with very limited knowledge on technology can exploit this. This can certainly be scaled using burp and other software .]

1. As a merchant create a promotion code with Redemption limit 1.
{F1962664}
2. As a user, Visit any two payment links of same merchant with the coupon.
3. In both payment links, Fill the form and apply coupon but don't hit Pay/ Subscribe.
4.Hit both link's pay/subscribe button as fast as you can.
5. Both payment will be successful using one coupon two times.

## Supporting Material/References:
I have added a video poc.
In this poc, I have used a promotion code with redemption limit 2.
I have also used laptops screentouch feature to click both link's pay/subscribe button as fast as I could.
{F1962525}

## Impact

Promotion code can be used more than redemption limit.

## Attachments
- stripecoupon.webm
- 2.jpg
- 12.jpg
- 1.jpg
