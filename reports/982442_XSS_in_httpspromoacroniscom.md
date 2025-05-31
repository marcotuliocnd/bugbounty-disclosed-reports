# XSS in https://promo.acronis.com/

## Report Details
- **Report ID**: 982442
- **URL**: https://hackerone.com/reports/982442
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-15T07:06:32.246Z
- **Disclosed**: 2024-08-26T15:34:06.480Z

## Reporter
- **Username**: yash_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hello, 

I found DOM XSS in https://promo.acronis.com/  
Open this URL https://promo.acronis.com/GL-Trial-MassTransit.html and view source.
Search for `document.write` and there will be 4 statements inside try/catch block.  
{F988381}

The last statement loads script from using `document.referrer`. So we can host a page that loads https://promo.acronis.com/GL-Trial-MassTransit.html in iframe. So it will load the script `/marketo/common.js` from our domain.

## Steps To Reproduce
  1. To create server I am using Node.js you can use static files also..  If you are using static files server make sure to create `/marketo/common.js` file.
  1. Create a director and copy this file F988371 in it.
  1. Run `npm init -y`
  1. and then `npm i express` to install exprss.
  1. Now run `node index.js` this will start server on 'localhost:5000'
  1. Open http://localhost:5000 and you will see alert.  
   {F988380}

## Impact

Anyone who opens this page, attacker can execute JavaScript code on their device or redirect victims to phishing websites.

## Attachments
- index.js
- 1.png
- 0.png
