# Customer's full name disclosure via Shopify Chat (by email lookup)

## Report Details
- **Report ID**: 1018336
- **URL**: https://hackerone.com/reports/1018336
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-10-25T14:15:32.110Z
- **Disclosed**: 2020-11-19T20:06:41.792Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
By making use of the Shopify Chat Application, it is possible to retrieve a customer  **First Name** and **Last Name** by providing its email.

## Steps to reproduce
1. Having a shop with Shopify Chat installed, open up `https://{shop}.myshopify.com/?chat` in Incognito mode
1. Click on **I need an update on my order**
1. Click on **Enter order information**
1. Enter targeted customer email and enter any order number and click on **Send**
1. By using Burp Client and/or any other tool to intercept and alter the request, intercept the request being made to `https://shopify-chat.shopifycloud.com/api/storefront/conversations/{id}/messages`  
```
{
   "message":{
      "dedupe_key":"05cdde10-05f4-452a-9688-136a89f3f5ed",
      "content":{
         "text":"My order number is #1.\nMy email is customer@fbsolutions.ca."
      },
      "automated":true,
      "group":"customer"
   },
   "skip_customer_creation":true
}
```

1. From that intercepted payload, update the `skip_customer_creation` to `false` and send the request
1. From your browser Network tab, look at API response of the call being made to `https://shopify-chat.shopifycloud.com/api/storefront/conversations/{id}/messages?after={date}&message_id={id}`. The `conversations.name` contains the targeted customer full name.

### Demo
███████

## Impact

Retrieve any customer's full name by providing his email.

## Attachments
No attachments
