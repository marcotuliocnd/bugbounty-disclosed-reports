# Know undisclosed Bounty Amount when Bounty Statistics are enabled.

## Report Details
- **Report ID**: 148050
- **URL**: https://hackerone.com/reports/148050
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-28T18:53:18.061Z
- **Disclosed**: 2016-09-02T18:06:44.723Z

## Reporter
- **Username**: vijay_kumar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi,
When a program does not disclose How much bounty is paid to particular report , but if bounty statics is enabled then undisclosed Bounty Amount can be enumerated.

For example Uber does not disclose bounty awarded to particular researcher but show bounty statics so we can write a script that check in every 5 or 10 sec bounty statics and if new Total bounty paid amount is found then it save it in text file . So we can get bounty awarded to a particular report by -
 "New Total bounty paid Amount - Old Total Bounty Paid Amount" .

By using this i can comment about recently bounty paid by uber-
fin1te = 3000$
ishwar_prasad_bhat = 500$
tahamah = 500$
aabuagla = 2000$
safedog = 5000$
brakhane = 10000$
benhayak = 3000$
nismo = 250$
jouko  = 5100$
ganapa = 500$

I also write a php script which check in every 10 sec , and if new record is bound then save it in txt file. Further by comparing i can comment Who got how much Bounty.

Possible Fix : Update bounty statics after 24 hrs OR after 5 bounties are paid.

Thanks

## Attachments
- poc.rar
