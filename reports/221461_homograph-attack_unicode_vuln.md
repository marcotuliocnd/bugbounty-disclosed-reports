# homograph-attack (unicode vuln)

## Report Details
- **Report ID**: 221461
- **URL**: https://hackerone.com/reports/221461
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-04-16T20:32:35.590Z
- **Disclosed**: 2017-08-10T05:10:52.303Z

## Reporter
- **Username**: wala3at
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
Hi team
Summary:
Affacted product  appears identicaly different  websites domains
attacker  uses unicode to register domains that look identical to real domains ,These fake domains can be used  to fool users into signing into a fake website, thereby handing over their login credentials to an attacker...
example to demonstrate how an attacker can register their own domain that looks identical to another company’s domain in the browser, 
  ‘epic.com’(healthcare site)  by registering fake site  unicode domain: http://www.xn--e1awd7f.com/

and affected product show unicode domain looks like real domain 
{F176374}
{F176375}

Products affected:

    Brave 1.0.19 (Tested on android 6.0.1;nexus5)

Steps To Reproduce:
1.In browser open http://www.xn--e1awd7f.com/ unicode domain demo 
2. you can see brave browser show fake site like real site in address bar

 
The fix:
 make sure it's display the punycode ..and warning or proper handlings
References:
 http://www.crypto-it.net/eng/attacks/homograph-attack.html
  https://www.wordfence.com/blog/2017/04/chrome-firefox-unicode-phishing/



## Attachments
- 2017-04-16_2023-brave-android6.png
- 2017-04-16_2053-real-epic-site.png
