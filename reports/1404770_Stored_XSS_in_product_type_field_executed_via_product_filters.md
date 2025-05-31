# Stored XSS in "product type" field executed via product filters

## Report Details
- **Report ID**: 1404770
- **URL**: https://hackerone.com/reports/1404770
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-18T23:47:51.475Z
- **Disclosed**: 2022-04-26T16:11:42.156Z

## Reporter
- **Username**: chupa-chups
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
HI @judgeme!
I found Stored XSS!)
I Install judge.me in Shopify E-Commerce. Step to reproduce:
1. Log in to our shopify dev store and install "judgeme" app.
2. Create random product in our Shopify store (make it active) and insert XSS playload  "><img src=x onerror=prompt(document.domain)> in "PRODUCT TYPE" field and SAVE


{F1518888}


3. Then go to our judgeme app https://xxx.myshopify.com/admin/apps/judgeme/products. There is a filter field TYPE . Click on it and select our playload from the list 
{F1518897}
4. And it works )))



{F1518898}

I attached video POC

## Impact

Session Hijacking, Cookie Stealing.

## Attachments
- 1.png
- 3.png
- 4.png
- jud1.mp4
