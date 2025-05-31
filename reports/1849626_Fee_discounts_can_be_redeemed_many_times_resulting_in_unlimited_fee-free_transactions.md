# Fee discounts can be redeemed many times, resulting in unlimited fee-free transactions

## Report Details
- **Report ID**: 1849626
- **URL**: https://hackerone.com/reports/1849626
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-28T03:16:41.299Z
- **Disclosed**: 2023-02-25T01:27:24.869Z

## Reporter
- **Username**: ian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripe

## Vulnerability Information
## Summary:
Hi there, first off, I am an actual Stripe customer using Stripe for my real business, so I used my actual Stripe account to test this (as there is no other way). I realize this is not ideal but hope you understand given the unique scenario!

I was recently offered a fee discount of $20,000 on Stripe transactions. Stripe Support applied the offer to my account, and I was shown a prompt to accept the fee discount in my dashboard. 

I decided I should try and look for a race condition in this acceptance. So, I used Burp Turbo Intruder to race the request that accepts the fee discount, `/ajax/accept_fee_discount_offer` (forgot to take screenshot as I did not think it would work!). 

It seems a race was not even needed though, as I called it 30 times and 30 fee discounts were immediately applied to my account! As a result, I now have $600,000 of fee-free processing applied to my account. Obviously, this is not ideal for Stripe as you only intended to offer me $20,000! I believe you could keep calling this endpoint if you wanted to, you just need a valid `fdo_` ID.

████

## Impact

Unlimited fee-free discounts. This will cost Stripe about 3% of each discount, so $600 each time a $20k discount is abused.

## Attachments
No attachments
