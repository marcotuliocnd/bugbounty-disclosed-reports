# Homo graphs attack 

## Report Details
- **Report ID**: 268679
- **URL**: https://hackerone.com/reports/268679
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-09-15T16:16:55.915Z
- **Disclosed**: 2017-09-20T19:37:53.259Z

## Reporter
- **Username**: hackaccinocraft
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
Hi there, 

Greeting for the day, hope you are doing good, 

In Federa localhost i found homograph attack, 

Here i made homograph for the ```ebay.com```, when see this link its look like normal simple text link but no its not, however, when you click on this particular link you might be think that you are going to redirect on ```eBay.com``` but the fact that the link which add is malicious link and made from homograph encoding so when you click on this link you will redirect on some malicious website.

> The IDN (Malicious link which i add in website) :   https://ebаy.com  
> What behind of IDN link :  https://xn--eby-7cd.com/

How to check this link just click on IDN malicious link ```hackerone``` show you what behind of this link.

POC video 
-----------
>https://drive.google.com/file/d/0B0ZLJj-vVEG9RThidEVmbGdfS0U/view?usp=sharing


Exploit
-------
Normal user dose not know about any homograph attack or something and when user click on this particular link user will redirect on some malicious website instead of actual written website. 

Mitigation
----------
When user enter URL at that moment website should to check does entered URL is normal link or encoded malicious link but here in federa i did not found any protection for homograph attack.

Reference 
----------

https://hackerone.com/reports/29491
https://hackerone.com/reports/175286

Cheers,
Ninja

 

## Attachments
No attachments
