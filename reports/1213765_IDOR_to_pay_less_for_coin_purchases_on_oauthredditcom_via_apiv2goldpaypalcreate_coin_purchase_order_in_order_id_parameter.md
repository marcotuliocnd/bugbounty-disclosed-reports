# IDOR to pay less for coin purchases on oauth.reddit.com via /api/v2/gold/paypal/create_coin_purchase_order in `order_id` parameter 

## Report Details
- **Report ID**: 1213765
- **URL**: https://hackerone.com/reports/1213765
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-01T00:08:29.625Z
- **Disclosed**: 2021-10-21T19:50:33.525Z

## Reporter
- **Username**: yanouhd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
This vulnerability consist of modifying the PayPal transaction ID to buy a big coin pack but paying the small price for it.

## Impact:
The only impact here could be that you don't earn the money you deserve, and users can offer a lot of presents to other users, breaking the magic of the reddit community.

## Steps To Reproduce:
Here are the steps to reproduce : 

  1. Click on the PayPal button to buy the smallest package (1.99$ for 500 coins at the time of writing).

  2. By intercepting requests,  you should see a POST to https://oauth.reddit.com/api/v2/gold/paypal/create_coin_purchase_order, with this body : 
`coins=500&pennies=199&correlation_id=b0fc62e4-e759-4b9e-be52-da4c926560ce`

  3. The response to this request is an order_id, keep it aside. This is the order_id corresponding to a PayPal transaction with an amount of 1.99$.
{"order_id": "1CR56170K7852611T"}

  4. Cancel the order, then make a new one with a bigger package (I took the 3.99$ for 1100 coins for my tests.)

  5. Keep intercepting requests until you make it to the POST /api/v2/gold/paypal/create_coin_purchase_order one.

  6. Now instead of forwarding the real response, change the `order_id` of this order to the one you kept from the 1.99$ transaction.
{"order_id": "~~1CR56170K7852611T~~ **1F444042JJ523625W**"}
  7. You will be redirected to the PayPal transaction page with an amount of 1.99$ to pay.

  8. Pay, and boom ! You paid 1.99$, but when you complete the order you will be given the amount of coins you "purchased" for the "fake price".

## Supporting Material/References:

If you want to check my purchase history, here is the account I used for this exploit : u/YanvegHD (This is my personal account, I think I made a mistake and I should've used a test account, my apologise...)

{F1321925}
{F1321926}

## Impact

Breaks the reddit magic about rewarding people / and people kinda stealing your money.

## Attachments
- reddit1.png
- reddit2.png
