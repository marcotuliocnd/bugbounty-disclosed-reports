# Order lookup features of Shopify Chat Application leads to customer orders enumeration due to lack of user input validation

## Report Details
- **Report ID**: 1017576
- **URL**: https://hackerone.com/reports/1017576
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-10-24T04:07:57.631Z
- **Disclosed**: 2020-11-19T22:28:12.139Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
It came to my attention that the Shopify Chat application allows a customer to retrieve its order status by only providing the order email and number. 

Noticing that it results in being provided the order status page link, I started playing a bit with both parameters and I found out that it is possible to:
1. Access any customer first order without having to provide any actual order number
1. Provide multiple order number within the same payload resulting in orders "enumeration"

As it stands, I'm not sure if it has to do with _SQL injection_. I'll keep digging.

## Steps to reproduce
1. Having a shop with Shopify Chat application installed (with OrderLookup feature), open up `https://{shop}.myshopify.com/?chat`
1. Within the Shopify Chat Widget, click on **I need an update on my order**
1. Click on **Enter order information** and fill in the form by entering any customer email and order number
1. Using Burp Client and/or any other way to intercept the request that is being made to `https://shopify-chat.shopifycloud.com/api/storefront/conversations/{id}/order_lookup` and copy its content so it can be replayed

The intercepted payload should looks like this:
```
{
	"order_lookup":
	{
		"email": "francisbeaudoin@wearehackerone.com",
		"order_number":"1000"
	}
}
```

As mentioned earlier, there's two different exploit.

### First one: Access any customer's first order details
From the above payload:
  1. Update `email` value to the targeted customer email address
  1. Update `order_number` value to `1 OR 2`

If the targeted customer email address have made any order, you'll be given the link to access his first order details.

### Second one: Enumerate orders by providing multiple order numbers at once
From the above payload:
1. Update `email` value to the targeted customer email address
1. Update `order_number` value to `1000 OR 1001 OR 1002 OR 1003 OR 1004 OR 1005`. 

Given that the customer does have any order having a number between 1000 and 1005, you'll be given the link to access the **first matching one**. If any, all you have to do to get the next one is to remove that specific order number from the payload and resend the request once again.

While testing, I used a payload with around 50 different numbers and it did work. My assumption there is that we can input a big payload but didn't go much deeper just in case it ends up being evaluated in SQL.

On a site note, I think that order lookup should have some kind of rate-limiting to prevent any abuse. 

## Demo
██████████

## Impact

Retrieve customers orders informations

## Attachments
No attachments
