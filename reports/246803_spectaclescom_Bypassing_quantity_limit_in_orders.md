# [spectacles.com] Bypassing quantity limit in orders

## Report Details
- **Report ID**: 246803
- **URL**: https://hackerone.com/reports/246803
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-07T07:37:34.463Z
- **Disclosed**: 2017-08-12T00:52:37.236Z

## Reporter
- **Username**: hiorws
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
Hi Snapchat team,
In the https://www.spectacles.com the quantity of orders has limited (for spectacles is 6 and for accessories is 10 according to help support page). But it can easily be manipulated by editing the URL.

Problem originates from limiting the quantity of the items is with just the UI elements just before adding to cart. After adding to cart step there is no checking step. (The last payment step is included!)

Let me show you PoC to reproduce this issue;

- First add a single spectacle to cart,
- i.e. Make the quantity of spectacles 6 and add both two accessories with quantity 10.
- You will see the "+" buttons will be inactive.
- Then copy the link address of "CHECKOUT" button
- Paste it to a new tab of browser and you will see something like that;
`https://orders.spectacles.com/cart/24637376965:6,24637373189:10,24637375493:10?attributes[delivery-min-days]=7&attributes[delivery-max-days]=14&attributes[locale]=en-US&checkout[shipping_address][country]=US&access_token=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&_fd=0&_ga=X.XXXXXXXXX.XXXXXXXXXX.XXXXXXXXXX-XXXXXXXXX.XXXXXXXXXX`
- To make an example change these values `24637376965:6,24637373189:10,24637375493:10` with these `24637376965:6,24637373189:2500,24637375493:25000` then enter
- You will see the accessories quantity will be 25000 and the price will be updated according to that.
- And you can pass to the last payment step with writing shipping information.

In the screenshots it will be clear and it is easy to reproduce the issue you can easily check this out.

To prevent this issue, a checking operation can be implemented to shopping web app.

Lots of thanks.

hiorws






## Attachments
- ss3.png
- ss2.png
- ss1.png
