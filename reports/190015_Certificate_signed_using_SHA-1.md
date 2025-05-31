# Certificate signed using SHA-1

## Report Details
- **Report ID**: 190015
- **URL**: https://hackerone.com/reports/190015
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-10T00:44:05.860Z
- **Disclosed**: 2016-12-29T21:17:35.070Z

## Reporter
- **Username**: lulliii
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hello,
I detected a certificate signed using SHA-1. SHA-1 is a hash algorithm used in digital signatures. It is currently considered deprecated due to the increasing feasibility in breaking it. 

Impact:
Certificates can be forged by capable adversaries. 
Forged certificates can be used in MITM attacks against connecting clients. 

Solution:
Renew certificates with SHA-256 signatures. 
This should be done before 2016. 



## Attachments
No attachments
