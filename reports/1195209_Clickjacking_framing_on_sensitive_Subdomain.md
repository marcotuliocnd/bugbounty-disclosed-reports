# Clickjacking /framing on sensitive Subdomain 

## Report Details
- **Report ID**: 1195209
- **URL**: https://hackerone.com/reports/1195209
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-13T00:20:33.818Z
- **Disclosed**: 2021-12-09T17:51:55.225Z

## Reporter
- **Username**: ilxax1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Vulnerability Name  :  Clickjacking /framing 
Vulnerability Description  :  Clickjacking is an interface-based attack in which user is tricked into clicking on actionable content on a hidden website by 
                                                               clicking on some other content in a decoy website .

Vulnerable Url  : https://cryptoeconomics.sifchain.finance/ 

. Steps to reproduce :
 1 -  copy the url  :  https://cryptoeconomics.sifchain.finance/#sif10jatqfd88m8s2uhtdtdl3txtayjtzsve2klyhh&type=lm
 2 - Go to test the vulnerability by using : https://www.lookout.net/test/clickjack.html
 

 $ POC :
. Screenshots .

## Impact

The user assumes that they're entering their information into a usual form but they're actually entering it in fields the hacker has overlaid on the UI. Hackers will target passwords, credit card numbers and any other valuable data they can exploit .

## Attachments
- 1.png
- 2.png
- 3.png
