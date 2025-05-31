# Stored - XSS

## Report Details
- **Report ID**: 532643
- **URL**: https://hackerone.com/reports/532643
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-09T13:53:42.265Z
- **Disclosed**: 2019-05-28T16:07:58.818Z

## Reporter
- **Username**: ashketchum
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Security Team,
I have Found Stored XSS Vulnerability 

POC : 
Step1: Go to https://app.oberlo.com/suppliers
Step2: Click on any product you will be redirected to URL as i have given for example https://app.oberlo.com/suppliers/8/products/488813?referralUrl=https%3A%2F%2Fapp.oberlo.com%2Fsuppliers%2F8%2Fproducts
Step3: You will get message icon in front of supplier name 
Step4: Click on that message 
Step5: Add Reason-->Subject-->and in message add my payload 
Payload: "><img src=x onerror=prompt(document.cookie)>
Step6: Click on send message 
Step7: Go to Inbox and you will see XSS is triggered and your payload was executed successfully

I have attached POC Video, Please go through it 

Thank you!
Ashish Dhone

## Impact

An attacker who exploits a cross-site scripting vulnerability is typically able to:

1) Impersonate or masquerade as the victim user.
2) Carry out any action that the user is able to perform.
3) Read any data that the user is able to access.
4) Capture the user's login credentials.
5) Perform virtual defacement of the web site.
6) Inject trojan functionality into the web site.

## Attachments
- XSSpoc.mkv
