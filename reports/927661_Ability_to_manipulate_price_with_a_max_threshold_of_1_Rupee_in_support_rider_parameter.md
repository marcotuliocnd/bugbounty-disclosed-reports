# Ability to manipulate price with a max threshold of `<1 Rupee` in support rider parameter

## Report Details
- **Report ID**: 927661
- **URL**: https://hackerone.com/reports/927661
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-07-20T08:28:26.210Z
- **Disclosed**: 2020-08-08T07:36:50.195Z

## Reporter
- **Username**: 0xdekster
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hi Team

I have found an issue in support rider amount calculation at the time of checkout where the amount is tamperable by negative fraction of rupees which makes the total amount decreased by maximum of 1rs.

POC - 

1-Goto - zomato.com
2 - Add anything to your cart
3- At the checkout page , Add some money to Support Riders , click on any 25,50,100
4- Intercept the request of adding support rider money.
5- Change the price of Support Rider to " -0.99" in both fields of donation money.
6- Forward the request , the Cart value will change.
7- Pay by any platform, order will get placed.


Thanks

## Impact

Price Manipulation in Support Rider

## Attachments
No attachments
