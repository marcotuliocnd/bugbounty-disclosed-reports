# Cross-site scripting in "Contact customer" form

## Report Details
- **Report ID**: 294505
- **URL**: https://hackerone.com/reports/294505
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-02T16:03:21.082Z
- **Disclosed**: 2017-12-19T09:57:02.421Z

## Reporter
- **Username**: protector47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,
I found HTML Injection Vulnerability while admin contact with customer.
In this vulnerability admin is attacker whereas customer is victim.

#Steps to Reproduce:

1. Go to **Customers** and Click on **Customer Email Address**.
2. New Pop-Up window will become open, In **Customer Message** field type this html code

><h1>HTML INJECTION</h1>

3 . Click on **Review Email** Button.

HTML will become execute.

Checkout the POC Video.
  
Thanks,

## Impact

Admin of store can redirect any user to any malicious website, and can perform all possible attacks through this vulnerability.

## Attachments
- html_injection_shopify.webm
