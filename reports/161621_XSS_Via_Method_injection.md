# XSS Via Method injection

## Report Details
- **Report ID**: 161621
- **URL**: https://hackerone.com/reports/161621
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-08-20T14:02:47.376Z
- **Disclosed**: 2016-09-01T11:43:56.356Z

## Reporter
- **Username**: exception
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hi guys

i found a low risk vuln , when you request a page on gratipay.com with uncommon Method , the server responds with error message .

Invalid Method 'Invalid HTTP method:TTEGETTT
with out escaping chars 

so when you inject an html element with method you can trigger an XSS .


Steps to reproduce  
- make an http request with a method  like this 
<img|src='3'|onerror=alert(3)/>



Fix :
you should validate the method value before printing it back in responses 


## Attachments
- Screen_Shot_2016-08-20_at_3.48.33_PM.png
- Screen_Shot_2016-08-20_at_3.49.56_PM.png
