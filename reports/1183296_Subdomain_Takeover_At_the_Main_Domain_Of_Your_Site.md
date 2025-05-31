# Subdomain Takeover At the Main Domain Of Your Site 

## Report Details
- **Report ID**: 1183296
- **URL**: https://hackerone.com/reports/1183296
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-03T20:55:53.266Z
- **Disclosed**: 2021-05-07T20:21:37.994Z

## Reporter
- **Username**: ahmedelmalky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Hello,

I Know that isn't in the Scope But this The Only Way I can Report With And This Issue Is Very High It Belongs to the Main Domain 
this is pretty serious security issue in some context, so please act as fast as possible.

##overview 
 the  Main Domain [sifchain.finance] is pointing to wix.com, which has unclaimed CNAME record. ANYONE is able to own http://sifchain.finance domain at the moment.
This vulnerability is called subdomain takeover. You can read more about it here:
https://blog.sweepatic.com/subdomain-takeover-principles/
https://hackerone.com/reports/32825
https://hackerone.com/reports/175070
https://hackerone.com/reports/172137

## Steps To Reproduce:
Visit >> https://sifchain.finance

when you open the above Link you will find wix.com subdomain error if you have an account in wix.com "premium" you can take over this subdomain
I don't try it manually because I haven't permission to test this issue and i haven't the Premuim Account . 

##Mitigation:
 Remove the CNAME record from  sifchain.finance  DNS zone completely.
Or renew the Subscription .  

Regards,

Ahmed Elmalky

## Impact

Very Critical It is In the Main Domain . 
Subdomain takeover is abused for several purposes:
    Authentication bypass
Malware distribution
Phishing / Spear phishing
XSS

## Attachments
No attachments
