# Stored xss

## Report Details
- **Report ID**: 415484
- **URL**: https://hackerone.com/reports/415484
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-27T22:44:43.839Z
- **Disclosed**: 2018-11-07T19:09:57.697Z

## Reporter
- **Username**: dr_dragon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
# Description :
WAF cut html tages but when put <!--> before tages we can bypass it :) .

#Step to reproduce :
1-Open your store account
2-Navigate to https://xxx.myshopify.com/admin/settings/general
3-Put your street address xss payload (xss"><!--><svg/onload=alert(document.domain)>)
4-Go to https://xxx.myshopify.com/admin/dashboards/live
5-XSS alert message

## Impact

XSS attack

## Attachments
- xss2.PNG
- xss1.PNG
