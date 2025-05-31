# Sub domain take over in gratipay.com

## Report Details
- **Report ID**: 257331
- **URL**: https://hackerone.com/reports/257331
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-08-07T08:18:08.540Z
- **Disclosed**: 2017-08-08T16:04:50.362Z

## Reporter
- **Username**: anshad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
# Summary

Sub domain take over in gratipay.com

# Description

I scanned gratipay.com using knockpy to find the sub domains. I found one subdomain
'www.gratipay.com.herokudns.com'. But this sub domain is not registered in heroku. An attacker can buy this sub domain from heroku. 

# Browsers Verified In

  * Firefox
  * Chrome

# Steps To Reproduce

  1. use the 'knockpy gratipay.com' command in  knockpy to find sub domains
       .
       You will get one domain like 'www.gratipay.com.herokudns.com'.
  1. Test this domain in browser. Then you will get error message from heroku. Please refer attached screen shot for more clarity.
  

## Attachments
No attachments
