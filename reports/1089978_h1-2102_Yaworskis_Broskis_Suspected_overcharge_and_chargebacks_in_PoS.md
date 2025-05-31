# [h1-2102] [Yaworski's Broskis] Suspected overcharge and chargebacks in PoS

## Report Details
- **Report ID**: 1089978
- **URL**: https://hackerone.com/reports/1089978
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-29T01:30:03.315Z
- **Disclosed**: 2021-12-03T14:51:37.311Z

## Reporter
- **Username**: xiridium
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:

NOTE: This one need verification from the side of Shopify as we can't set up a real payment GW or check the logs of the test one

When checking out in PoS and paying with credit card, it is possible to manipulate numbers in the end request to overcharge a client (charge more than the item price) and to send money to the client from the store

```json 
{
    "payment": {
        "session_id": "9",
        "amount_in": 1.09,       <<<<<
        "amount_rounding": 0,    <<<<<<<
        "amount": 1.09,   <<<<<<<
        "device_id": 2131722262,
        "unique_token": "xxx",
        "amount_tip": 0,
        "card_source": "manual",
        "auto_finalize": false,
        "user_id": 64582418454,
        "amount_out": 0,     <<<<<
        "location_id": 52512587798,
        "charge": true
    }
}
```

There are four  values which interest us here: `amount`, `amount_in`, `amount_rounding` and `amount_out`. Those control how much the client is charged. They should follow the formula `amount = amount_in - amount_rounding - amount_out`. `amount`  should always remain the price of the cart.
 `amount_in` is how much is charged from the client. `amount_out` is how much is taken from the shop. Looks like `amount_rounding` is a number which is not taken from anyone and is in fact some in-fact-rounding-value.

Some of these values allow negative values which broadens our possibilities. Let's see how it works. 

## Steps To Reproduce:
You would need PoS in your show installed and installed on your phone (I used iphone with jailbreak to proxy data into Burp). https://apps.shopify.com/shopify-pos.

> NOTE: I have used the test store to work with the payments. In real case this might work differently, but since I couldn't find a way to approve that, I decided to submit it nonetheless.

Create a new order with an item. I will be using a $1.09 dummy item from my shop. Now start the checkout process and select credit card as a payment source.

{F1176221}

{F1176222}

Enter card details and be ready to intercept this request.
{F1176223}

We are looking for the similar `payments.json` request:
  
{F1176220}

```http
POST /admin/api/unstable/checkouts/5788adb325c4824f193d08daf474f21a/payments.json HTTP/1.1
Host: c0rv4x2.myshopify.com
...

{"payment":{"amount":1.09,"user_id":64582418454,"amount_rounding":0,"charge":true,"card_source":"manual","amount_out":0,"location_id":52512587798,"session_id":"east-fbc4aa9a711b9a5f13a0a76e9bd7c879","amount_tip":0,"amount_in":1.09,"auto_finalize":false,"device_id":2131722262,"unique_token":"4DA811C1-4824-4451-B576-290137624B1A"}}
```

Change `amount_in` to `2.09` (1 USD more than the current price) `amount_rounding` to `-1.0` (retracting that one dollar to make our equation from the begging of this report true).

```http
POST /admin/api/unstable/checkouts/5788adb325c4824f193d08daf474f21a/payments.json HTTP/1.1
Host: c0rv4x2.myshopify.com
...

{"payment":{"amount":1.09,"user_id":64582418454,"amount_rounding":-1.0,"charge":true,"card_source":"manual","amount_out":0,"location_id":52512587798,"session_id":"east-fbc4aa9a711b9a5f13a0a76e9bd7c879","amount_tip":0,"amount_in":2.09,"auto_finalize":false,"device_id":2131722262,"unique_token":"4DA811C1-4824-4451-B576-290137624B1A"}}
```

{F1176224}

## Similar behaviour

Similar behaviour is possible if we set `amount_out` to a non negative value (which would mean the shop is losing money).

## Impact

Potentially manipulate customers and shops money without their conscent

## Attachments
- 2021-01-29_04-20.png
- photo_2021-01-29_04-28-29.jpg
- photo_2021-01-29_04-28-28.jpg
- photo_2021-01-29_04-28-26.jpg
- photo_2021-01-29_04-28-24.jpg
