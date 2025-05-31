# Stored XSS in Discounts section

## Report Details
- **Report ID**: 618031
- **URL**: https://hackerone.com/reports/618031
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-18T09:14:02.574Z
- **Disclosed**: 2019-06-27T15:00:15.658Z

## Reporter
- **Username**: mosuan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
self-xss

## Impact

1.add `Products`, shop name is '"'><img src=x onerror=alert(domain.domain)>'
2.click `Discounts->code`, https://mosuan-img-src-x.myshopify.com/admin/discounts/367541518396
3.add comments, Choose the goods just now.
4.alert

## Attachments
- 1560849217964.jpg
