# Bypassing one-time checkout router page (revealing payment information)

## Report Details
- **Report ID**: 271176
- **URL**: https://hackerone.com/reports/271176
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-09-23T14:41:40.255Z
- **Disclosed**: 2018-05-10T01:04:39.702Z

## Reporter
- **Username**: tolo7010
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lyst

## Vulnerability Information
Description:
========
When user submits for a checkout, the checkout router page /checkout-router/[ID]/ is accessible only once, which can be bypassed by crafting the checkout [ID] in cookie basket_key send to the page /new/checkout/order/. combining with brute-force attack, if the ID is valid a result page shown from any user that made the payment. this disclosure contains items ordered, prices, customer name, billing address, email address, phone number... This attack require no authentications, and no rate-limit in brute-forcing checkout [ID]

Step to reproduce:
============
1. Go to https://www.lyst.com/cart/
2. Assuming your shopping bag is not empty, click "checkout securely" or https://www.lyst.com/cart/verify/set-password/
3. Confirming account by entering email & password.
4. Upon click "checkout", use burp to intercept the request.

You will get a redirection link to the checkout router, the form of the url is:
https://checkout.lyst.com/checkout-router/[ID]/

where [ID] is the 19 digit number identification - the link redirects again to https://checkout.lyst.com/new/checkout/order/ which you will provide billing information.

Now the point is the link https://checkout.lyst.com/checkout-router/[ID]/ is accessible only once, you will get "This page doesn't exist" message if you try to request the link. To bypass this, we can craft cookie value key basket_key=[ID] in request to the endpoint /new/checkout/order/.

In this report I use base key 7092456849791607456 which I created from my own check out (filled with billing address).

I use chrome extension EditThisCookie in the attached image, here are the same result from burp (also image attached):

GET /new/checkout/order/ HTTP/1.1
Host: checkout.lyst.com
User-Agent: 
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Cookie: basket_key=7092456849791607456
Connection: close
Upgrade-Insecure-Requests: 1

Images Attached:
===========
1.jpg: access the regular endpoint second time resulting in error
2.jpg: bypassing via cookie injection in another endpoint
3.jpg: tested in burp suite




## Attachments
- 1.jpg
- 2.jpg
- 3.jpg
