# Stored XSS in Shopify Chat 

## Report Details
- **Report ID**: 756729
- **URL**: https://hackerone.com/reports/756729
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-12-12T07:01:36.511Z
- **Disclosed**: 2019-12-23T14:45:28.796Z

## Reporter
- **Username**: mosuan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
1.install app `Shopify Chat`
2.Click chat on the shop homepage or Shopify Ping to send poc `javascript:alert(1)//https://dqdqdqdqdq.myshopify.com`
3.Click url, alert
{F657395}

## Impact

1.Front end user Self-XSS
2.Administrator XSS foreground user

## Attachments
- 4234234234.png
