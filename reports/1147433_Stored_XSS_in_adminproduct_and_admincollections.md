# Stored XSS in /admin/product and /admin/collections

## Report Details
- **Report ID**: 1147433
- **URL**: https://hackerone.com/reports/1147433
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-03T09:41:30.138Z
- **Disclosed**: 2022-12-01T22:44:01.766Z

## Reporter
- **Username**: ashketchum
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
### Hello Security Team,

I was going through previous reports of XSS and I have found this,
https://hackerone.com/reports/978125

As stated by team on this page even on https://hackerone.com/shopify?type=team under Known issues
 that we can now report XSS under Rich Text Editor on Product description and Collection description. 
I have found XSS on this endpoints /admin/product and /admin/collections

{F1252456}

### Steps to Reproduce:
#### /admin/product

Step1: Go to https://your-store.myshopify.com/admin/products?selectedView=all
Step2: Click on Add product 
Step3: Add anything in Title
Step4: Right side corner in description click on Show HTML
Step5: Add below Payloads and Click on Save

#### Payload: 
">\]<img src=x onerror=alert(document.domain)>  ">\]<img src=x onerror=alert(document.cookie)>
      
XSS will get triggered.

{F1252457}

#### /admin/collections

Step1: Go to https://your-store.myshopify.com/admin/collections
Step2: Click on Create collection
Step3: Add anything in Title
Step4: Right side corner in description click on Show HTML
Step5: Add below Payloads and Click on Save

#### Payload: 
">\]<img src=x onerror=alert(document.domain)>  ">\]<img src=x onerror=alert(document.cookie)>
      
XSS will get triggered.

{F1252455}

I have attached POC Video, Please take a look.

{F1252458}

#### Thank You
Ashish Dhone

## Impact

A malicious user can steal cookies and use them to gain further access even an attacker can use XSS to send requests that appear to be from the victim to the web server.

## Attachments
- collection_XSS.PNG
- policy.PNG
- products_xss.PNG
- XSS_POC.mp4
