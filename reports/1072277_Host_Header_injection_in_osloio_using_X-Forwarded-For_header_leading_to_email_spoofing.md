# Host Header injection in oslo.io (using X-Forwarded-For header) leading to email spoofing

## Report Details
- **Report ID**: 1072277
- **URL**: https://hackerone.com/reports/1072277
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-01-05T21:03:32.486Z
- **Disclosed**: 2021-01-07T21:18:41.842Z

## Reporter
- **Username**: hammodmt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: logitech

## Vulnerability Information
#Hello team
##I hope it will be a happy year for you and for me 😇 
## Summary:

I found Host Header injection in oslo.io  
I tried to use it to show the security effect on users And I found this

## Steps To Reproduce:

 1. Well, first of all, enter your project 
2.Make an invitation by email 
3.Now through the burpsuite 
If we try to change the host, 403 will appear
  {F1145857}

So we will use  ```X-Forwarded-Host:  example.com```
 
PoC : 
{F1145858}

## Impact

Many things can be done, including deceiving the user and referring to something else or a login page and stealing their account
>>There is a lot of information about it here : 

 https://portswigger.net/web-security/host-header

## Attachments
- osla1.png
- POC.webm
