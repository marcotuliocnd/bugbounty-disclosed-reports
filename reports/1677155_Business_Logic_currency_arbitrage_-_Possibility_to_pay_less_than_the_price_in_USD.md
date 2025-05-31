# Business Logic, currency arbitrage - Possibility to pay less than the price in USD

## Report Details
- **Report ID**: 1677155
- **URL**: https://hackerone.com/reports/1677155
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-22T22:05:27.455Z
- **Disclosed**: 2022-10-26T06:57:05.992Z

## Reporter
- **Username**: xctzn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
Currency fluctuate all the time. Theses days EUR / USD key pair is around 1for1. It was even 1:0.99 when I was writing this report.
Portswigger doesn't change dynamically the price and exchange rate dynamically. 

Vulnerability at the following link: https://portswigger.net/buy/pro 

When you want to buy a product choose the currency, you can noticed they are fixed and with today difference it's quite a big difference.

## Impact

USD price is 399$USD, while EUR price is 349$. 
Therefore someone could just change the price to Euro and pay 347 $USD (349 Euro) instead of 399$(with current rate).

PS: It scale with the price, it could lead to thousands of dollars lost for your company.

## Attachments
No attachments
