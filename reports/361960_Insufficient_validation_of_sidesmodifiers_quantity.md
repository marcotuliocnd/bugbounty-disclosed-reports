# Insufficient validation of sides/modifiers quantity

## Report Details
- **Report ID**: 361960
- **URL**: https://hackerone.com/reports/361960
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-06-05T03:33:30.844Z
- **Disclosed**: 2019-06-06T22:41:21.679Z

## Reporter
- **Username**: liquid8
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upserve

## Vulnerability Information
**Summary:**
The Upserve Online Ordering (OLO) application does not properly verify on the server side the number of sides/modifiers that have been added

**Description:**
Certain items allow for selection of a limited number of sides/modifiers, and the application restricts the number of sides/modifies that can be selected on the client side through javascript, but does not validate the request on the server side for the number of sides/modifiers. By intercepting and modifying the traffic when the order request is sent, an attacker will be able to place an order with more than the allowed number of sides/modifiers.

**Steps To Reproduce:**
The issue can be demonstrated using the test store https://app.upserve.com/s/upserve-lounge-test-providence-2 and the menu item "Char Boil Trou". 

1) Select the "Char Boil Trou" option and add it to the cart. Note that only 1 side can be added (exceed-max-sides-1.png)
2) Checkout and submit the order
3) Intercept the request and add additional sides in the JSON request. In this example 3 sides are added instead of the maximum of 1 by changing the "sides" JSON parameter to (exceed-max-sides-3.png):
```"sides":[{"id":"aa79b4fe-d8be-40d8-8693-21fd5b94ef50","name":"Brussel Sprouts","price":0,"side_id":"1cbde3ee-0f16-4938-8139-3b5af5781c4c","price_cents":0,"tax_rate_id":"40eb334a-300c-4b02-8d70-54b199d1c197","tax_rate":{"id":"40eb334a-300c-4b02-8d70-54b199d1c197","name":"Sales Tax","percentage_rate":"0.1"}},{"id":"1074ac11-2c37-48d1-b4dd-13d8deaf183f","name":"Asparagus","price":0,"side_id":"573ff30a-1dd4-44be-9179-d4c81c088963","price_cents":0,"tax_rate_id":"40eb334a-300c-4b02-8d70-54b199d1c197","tax_rate":{"id":"40eb334a-300c-4b02-8d70-54b199d1c197","name":"Sales Tax","percentage_rate":"0.1"}},{"id":"d3f0aebe-e71b-4f6a-9f57-a449dd518422","name":"Mashed Potatoes","price":0,"side_id":"32b8f396-e779-4252-86cb-e0a8f41745dc","price_cents":0,"tax_rate_id":"40eb334a-300c-4b02-8d70-54b199d1c197","tax_rate":{"id":"40eb334a-300c-4b02-8d70-54b199d1c197","name":"Sales Tax","percentage_rate":"0.1"}}]```
4) The request is accepted by the application (exceed-max-sides-2.png)
5) Viewing the submitted order in the users profile shows that the order was made with 3 sides (exceed-max-sides-4.png)

## Impact

A malicious user will be able to add additional sides/modifiers beyond the maximum number allowed, which the restaurant might include if the discrepancy is not noticed, which would result in monetary loss to the restaurant.

## Attachments
- exceed-max-sides-1.png
- exceed-max-sides-2.png
- exceed-max-sides-3.png
- exceed-max-sides-4.png
