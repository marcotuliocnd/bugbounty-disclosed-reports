# Potential to abuse pricing errors in saved carts

## Report Details
- **Report ID**: 336131
- **URL**: https://hackerone.com/reports/336131
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-11T20:59:56.472Z
- **Disclosed**: 2018-05-02T13:51:05.050Z

## Reporter
- **Username**: richardf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
If someone abandons a shopping cart and the price changes between that time and when the abandoned cart recovery email is sent, the saved cart will always show the old price. 

If saved carts do not expire, this can create a situation where bad actors can fill and save shopping carts with sale priced items for purchase at any time in the future simply by bookmarking the cart or saving the abandoned cart recovery email. 

One could for example, save 50% off sale prices in a cart in June and complete the transaction in December. Automated stores or stores in jurisdictions where pricing errors must be honored, may fulfill these purchases at incorrect prices.  

Any Shopify store not using automated abandoned cart emails are probably susceptible to this. 

To replicate this bug simply add any product to a cart with valid purchaser information and then abandon the cart. Then go to the shopify dashboard for that store and change the price for the product in the cart. Then click the abandoned cart link in the corresponding abandoned checkout or send an abandoned cart recovery email and click on the link in that email. The cart will show the old price and will never update.

## Impact

If commonly known, this could dramatically undermine the integrity of the Shopify platform by allowing unethical consumers attempt to take advantage of vendors by saving and using invalid prices. Any Shopify store not using automated abandoned cart emails are probably susceptible to this.

## Attachments
No attachments
