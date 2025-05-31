# Subdomain Takeover of Brave.com

## Report Details
- **Report ID**: 175397
- **URL**: https://hackerone.com/reports/175397
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-10-12T14:49:13.371Z
- **Disclosed**: 2016-10-14T17:33:23.573Z

## Reporter
- **Username**: sahiltikoo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

Hey!

I want to inform you about sub domain takeover issue i.e. when I did your DNS enumeration i came across :-

Ip Address        Target Name
----------        -----------
151.101.9.7       www.brave.com
151.101.9.7       prod.p.ssl.global.fastly.net
151.101.9.7       prod.p.ssl.global.fastlylb.net

Except the first domain name , the rest two CName point to an unclaimed domain on fastly.com(CDN) that when opened show :-

Fastly error: unknown domain: prod.p.ssl.global.fastly.net. Please check that this domain has been added to a service

the above error indicates that the above address is not in use and can be claimed by an attacker by making an account on fastly.com . 



## Products affected: 

 *  Brave's sub domain 

## Steps To Reproduce:

 * Steps:- Open the above CName ( prod.p.ssl.global.fastly.net.) , as the error is thrown , it indicates the above address can be claimed by creating an account on fastly and giving this as the Cname for your own domain.

## Supporting Material/References:

  * I have added POC image for the DNS enumeration i did. just have a look .


## Attachments
- poc(brave).png
