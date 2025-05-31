# Payment method token being sent to 3rd party analytics service

## Report Details
- **Report ID**: 637267
- **URL**: https://hackerone.com/reports/637267
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-07-07T20:06:38.956Z
- **Disclosed**: 2021-09-03T15:06:32.787Z

## Reporter
- **Username**: ctulhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upserve

## Vulnerability Information
Vulnerability Details:

Payment Tokens can be re-used to link the Credit Card to Another Users Account.

When Linking a Credit Card, a url with Payment_method_token will be generated and then the user will be redirected to the generated url

{F523794}

Then, a Request will be Made to ```orders.upserve.com``` to Finally Link the Credit Card using the payment_method_token


{F523795}


##Reproduction Steps

1.) Create 2 Accounts on https://app.upserve.com/s/upserve-lounge-test-providence-2
 * juandelacruz@gmail.com
 * juandoe@gmail.com

2.) Add a Credit Card
 * 4834422077410033|01|2023|730  - for juandelacruz@gmail.com
 * 4834422073330870|06|2024|582 - juandoe@gmail.com

3.) While Adding the Credit Cards, Make sure to Capture all Request.

4.) Remove the Credit Card linked to the account of juandoe@gmail.com

5.) Using the payment_method_token of juandelacruz@gmail.com we will link his credit card to the account of juandoe@gmail.com

6.) Your Credit Card Will be linked to the account of juandoe@gmail.com.


I am Confused:
* The ```last_four":"3579"``` is confusing me here, it doesnt really validate the last 4 digit it just accepts what ever is on the request, you can change it to any 4 digit numbers.
*  If you Added a MasterCard Credit Card, if the card_type is set to visa, it will show as a Visa Card.


Could you Please Verify on your Endpoint? 

* "payment_method_token":"a0543b88d2ddae5d2bd5f8fe"
* ctulhu@wearehackerone.com

also

Important Details Such as Payment Method Tokens are shared thru 3rd Party Analytics. 

{F523791}

##Proof of Concept:

{F523813}

## Impact

If any attacker can access the 3rd party analytics account, they can get the payment method token of upserve users and use the tokens to link any credit cards to their account and cause a monetary impact to Upserve, a merchant, or a customer  ( creating a payment method they dont own)

* Large Scale Fraud

## Attachments
- 58.png
- 60.png
- 61.png
- 1.mp4
