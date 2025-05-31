# Add more seats by paying less via PUT /v2/seats request manipulation

## Report Details
- **Report ID**: 1446090
- **URL**: https://hackerone.com/reports/1446090
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-01-11T02:51:39.261Z
- **Disclosed**: 2022-06-20T15:41:33.357Z

## Reporter
- **Username**: life__001
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: krisp

## Vulnerability Information
## Summary:
I could not fully test this vulnerability because the test plan must be completed for the payment process, that is, 30 days. But the price value in api also changes and if payment is made according to this value, wrong billing will occur.

The annual pro option for Team plan billing is $60 per seat. However, if the user enters a decimal number instead of an integer while adding a seat, the number is rounded up, but the price is only multiplied by the integer part. For example it would be like this :

```javascript
seats = 5
amount = 300
bady.seats = 1.1

seats += Math.ceil(bady.seats)
// 5  +=             2
// seats : 7 

amount += Math.floor(bady.seats) * 60
// 300 +=                 1      * 60
// amount : 360 
```

## Steps To Reproduce:

* Register the app and finish the installation. [help document](https://help.krisp.ai/hc/en-us/articles/360017564739-Creating-a-Krisp-personal-account)
* Create a new team.
* Go to billing and listen to traffic with burp.
* Add seat and capture the request with burp.
* Replace the number of seats with 1.9 
* You will see that you have added 2 seats but the price has increased by $60.

We can reduce the price by adding and deleting seats.

Poc video -|

{F1574747}

## Impact

Attacker can manipulate membership price

## Attachments
- k.mp4
