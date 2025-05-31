# Authorization Bypass in Delivery Chat Logs

## Report Details
- **Report ID**: 144000
- **URL**: https://hackerone.com/reports/144000
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-10T06:49:22.462Z
- **Disclosed**: 2016-11-03T23:02:35.514Z

## Reporter
- **Username**: michiel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
An authorization issue in the mobile app API allows any Instacart user to gain access to other users' order delivery chat logs. The `/api/v2/order_deliveries/:order_delivery_id/order_change_logs` endpoint does not sufficiently check if the user has permissions to access that particular order's chat logs. 

# Steps to Reproduce
I used Burp Suite to intercept the traffic between my iPhone and the Instacart API. When I found the "View 
Chat Logs" button on one of my past orders, I noticed it triggered the following API request:

```
GET /api/v2/order_deliveries/261932226/order_change_logs HTTP/1.1
Host: www.instacart.com
Accept: */*
[...]
```

This request is answered by the API with a JSON blob that contains chat messages that were exchanged between the buyer and the shopper. As well as a few other details like when the order was placed and if any changes were made to the order due to out of stock items. 

However, if you change the ID in the URL to something else, you will notice the API actually responds with the chat log and order data, regardless of who made the order. I tried with `261972220` and you can confirm this delivery does not belong to the user with account ███, but for instance `261972226` does.

# Risk
This vulnerability leaks private messages exchanged between shopper, driver, and customer. It may also include product names that were on the order if something had to be changed about the order. 

Here is an example:
{F98768}

This could lead to greater compromise, since the API returns the Firebase tokens for a few objects as well. So far I have not been able to do anything interesting with the Firebase tokens, but I'm not a Firebase expert. 

Here is an example (id: 261972220):

```
michiel@msp ~ $ curl https://instacart.firebaseio.com/order_deliveries/xy8TcFsDZiKm1JwnqqFp.json
{"46671792":"","46671794":"","46671795":"","46671802":"","46671804":"","46872067":"","46872104":"","46872195":"","46872357":""}%
```

# Mitigation
Implement an authorization check that makes sure only a users' own orders can be accessed.

## Attachments
- IMG_0008.PNG
