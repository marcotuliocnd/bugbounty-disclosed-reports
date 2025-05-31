# Rounding errors on rewarding a bounty leads to bypassing the 20% H1 commission fee

## Report Details
- **Report ID**: 808975
- **URL**: https://hackerone.com/reports/808975
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-02T22:33:11.767Z
- **Disclosed**: 2020-05-15T17:23:12.521Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
The team discovered a rounding error issue when rewarding hackers with a bounty. Through a series of micro-payments, a malicious program manager is able to pay a full amount to the hacker while evading the 20% H1 commission fee. 

**Description:**
H1 has a system for awarding and paying hackers a monetary amount for a report. On each payment, HackerOne charges a 20% commission fee. As an example, if a program awards the hacker with 100$, HackerOne charges 20$. The total amount the program will have to pay is 100$ + 20$ = 120$.

While testing, we noticed that we can enter a `float` value when issuing a reward, for example - 0.0004 . This resulted in an error and the request did not go through. Next, we noticed that the `bounty_award` and `bounty_fee` fields have a `float` type as well. During testing, we noticed that it has a limit of two numbers after the dot - `0.00`.
Finally, we observed that the system has rounding values.

The `bounty_fee` is calculated as such:
`bounty_fee` = `bounty_award/100*20`

## Testing done:
`bounty_award` = 1$ , `bounty_fee` = 0.2$
`bounty_award` = 0.1$ , `bounty_fee` = 0.02$
`bounty_award` = 0.01$ , `bounty_fee` = 0.002$ , but `bounty_fee` rounds two only two decimals. After rounding, the system will result in value - `bounty_fee`=`0.00`$

### Optimal values
`bounty_award` = 0.02$ , `bounty_fee` = 0.004$ - system rounding and will `bounty_fee` = 0.00$
`bounty_award` = 0.03$,  `bounty_fee` = 0.006$ - system rounding and will `bounty_fee` = 0.01$ - not ideal

If the value is between 0.000 - 0.004, system rounding and will be `0.00` - good.
If the value is between 0.005 - 0.009, system rounding and will be `0.01` - bad.

This lead us to conclude that the optimal value to set a reward is 0.02$.

Thus, by sending multiple set award requests with a value of 0.01$ or 0.02$, we will effectively avoid the 20% commission fee.

In the report we show the result of working with the value 0.01$

### Steps To Reproduce

1) Select a report that should be rewarded
2) In our testing we used report #808343
3) Set award amount - 0.01$
4) Intercept the request

https://hackerone.com/reports/bulk
```
POST
X-CSRF-Token: you_token_:)

message=&substate=bounty-award&bounty_amount=0.01&reference=&add_reporter_to_original=false&reply_action=set-bounty&mark_ineligible_for_bounty=false&reports_count=1&report_ids%5B%5D=808343&bounty_currency=USD
```

5) Repeat this request multiple times - this can do using an intruder style attack with null payloads, e.g. 100 requests.
6) Check the billing dashboard under https://hackerone.com/hackerone_h1p_bbp3/billing.json?month=3&year=2020

```
`{"activity_date":"2020-03-02T10:56:29.265Z","activity_description":"Bounty for report #808343","report_id":808343,"team_handle":"hackerone_h1p_bbp3","report_url":"https://hackerone.com/reports/808343","reporter":"ggttss1","bounty_award":0.01,"bounty_fee":0.0,"debit_or_credit_amount":-0.01,"paid_to_hacker_date":null}`
```

E.g:
"bounty_award":0.01,"bounty_fee":0.0,"debit_or_credit_amount":-0.01`

The 20% fee was not paid.

9) After all the testing and using the best values we have:
`https://hackerone.com/hackerone_h1p_bbp3/billing.json?month=3&year=2020`

###{"balance":99.88,"fee_percentage":20.0,"team_active":true,"billing_2_0":true,"has_credit_card":false,"billing_start_date":"2020-02-11T00:01:22.214+00:00","total_bounty_award":1.28,"total_fees":0.05,"invoice_total":1.33,"ending_balance":98.55

Rewarded: 1.28$
Fee: 0.05$ 
Invoice total: 1.33$

Where in reality, it should have been:
Rewarded: 1.28$
Fee: (1.28/(100*20))  ~ 0.26$
Invoice total: 1.33$

We’ve effectively saved 0.21$. Obviously, this will have a big impact long term, especially when dealing with substantial amounts.

Thanks , @haxta4ok00 !

## Impact

Bypassing the 20% commission charged by HackerOne, resulting in substantial financial loss for the platform.

## Attachments
No attachments
