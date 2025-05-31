# Self xss in product reviews

## Report Details
- **Report ID**: 1029668
- **URL**: https://hackerone.com/reports/1029668
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-09T00:54:42.306Z
- **Disclosed**: 2020-11-19T23:29:16.179Z

## Reporter
- **Username**: tomorrow_future
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
1、install app `Product Reviews`
{F1070556} 

2、Open a product and write a review

3、Press F12 on the keyboard，Change the type of email to text.

4、Write in email`"><img src=a onerror=alert(1)>123@sdf.com`.
{F1070565}

5、Write other required fields，then submit.
{F1070566}

## Impact

Self xss

## Attachments
- Product_Reviews_.png
- write_email.png
- alert.png
- self_xss.mp4
