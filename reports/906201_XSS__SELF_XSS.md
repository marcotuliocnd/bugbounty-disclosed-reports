# XSS / SELF XSS

## Report Details
- **Report ID**: 906201
- **URL**: https://hackerone.com/reports/906201
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-06-23T15:23:04.621Z
- **Disclosed**: 2020-09-14T19:25:10.699Z

## Reporter
- **Username**: ferdihermawan1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
I found xss but i think its self xss

POC

1. Go to yourstore.myshopify.com
2. Go to settings > import 
3. Upload wrong file csv with file name payload xss "><img src=xx onerror=alert(document.domain)>

## Impact

xss attack

## Attachments
- xss.png
