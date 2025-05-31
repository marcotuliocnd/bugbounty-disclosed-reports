# Stored XSS in Question edit for product name (bypass #1416672)

## Report Details
- **Report ID**: 1428207
- **URL**: https://hackerone.com/reports/1428207
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-12-15T21:24:16.677Z
- **Disclosed**: 2022-03-31T14:01:04.420Z

## Reporter
- **Username**: chupa-chups
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
Hi @judgeme!
Step to reproduce:
1. Log in to your shopify account and create product with name `&#34;&#62;&#60;&#34;&#62;&#60;img src=x onerror=prompt(document.domain)&#62; img src=x onerror=prompt(document.domain)&#62;`
2. Go to our store and write question to our product with name `&#34;&#62;&#60;&#34;&#62;&#60;img src=x onerror=prompt(document.domain)&#62; img src=x onerror=prompt(document.domain)&#62;`
3. Then delete our product from store (The product status must be (out of store) in questions.
4. Then go to Shopify admin/Judge.me Product Reviews/Questions and edit question. XSS triage


{F1547145}


POC video

{F1547181}

## Impact

session stealer

## Attachments
- POC1.png
- bypass_POC.mp4
