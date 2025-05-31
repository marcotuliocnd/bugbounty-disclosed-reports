# XSS in my.shopify.com in  widget

## Report Details
- **Report ID**: 185826
- **URL**: https://hackerone.com/reports/185826
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-11-27T14:52:43.172Z
- **Disclosed**: 2017-07-21T15:20:57.540Z

## Reporter
- **Username**: xssa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi security team
I found XSS in the Buy Button in my.shopify.com


Step to reproduce 

1-Go to Product and create Product with these payload <img src="a" onerror="prompt(document.cookie)" />;
See (Step1)

2- Now Go to Embed on a website  and in the buy bouton page chose the third template and XSS will pop up 


Patch it 



## Attachments
- Step1.JPG
- xss222.JPG
