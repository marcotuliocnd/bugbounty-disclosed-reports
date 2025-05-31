# IDOR able to buy a plan with lesser fee

## Report Details
- **Report ID**: 1679276
- **URL**: https://hackerone.com/reports/1679276
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-24T16:12:00.120Z
- **Disclosed**: 2022-10-19T16:20:26.705Z

## Reporter
- **Username**: ug0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary
IDOR allows you to pay with the same amount but different currency. For example, paying 35000$ instead of 35000€

## Steps To Reproduce
1. Go to `https://account.mailpoet.com/` and select a plan
2. For example I have selected this plan; `https://account.mailpoet.com/orders/new?p=214`
3. Now, as you can see payment currency is euro (33600€)

{F1882065}

4. Add `cur` parameter as `usd` like `{F1882070}https://account.mailpoet.com/orders/new?p=214&cur=usd`
5. And now, we can buy it as 33600$ instead of 33600€

{F1882070}

##Suggested solutions
Add an Dollar/Euro converter to your payment system

Cheers,
@h1ugroon

## Impact

Any user can pay a fee with a different value but the same root number instead of euros. For example, for a €33600 transaction, the fee difference is about $107, but the reason for this is the recent increase in the dollar. The user's profit rate varies according to the value of the money. About 1 month ago, this profit rate is around 630 dollars. Although this is not a critical problem, it is a vulnerability that reduces the profit margin

## Attachments
- image.png
- image.png
