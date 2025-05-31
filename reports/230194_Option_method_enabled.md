# Option method enabled

## Report Details
- **Report ID**: 230194
- **URL**: https://hackerone.com/reports/230194
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-05-20T10:59:44.461Z
- **Disclosed**: 2017-05-21T17:13:44.164Z

## Reporter
- **Username**: hurthearts
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
__Description__
HTTP OPTIONS method is enabled. 

__Affected URL__ :
https://demo.weblate.org/
https://weblate.org/en/
https://hosted.weblate.org

__PoC__
`curl -X OPTIONS https://hosted.weblate.org -vv`

__Output__

```
aku@galau:~$ curl -X OPTIONS https://hosted.weblate.org -vv
* Rebuilt URL to: https://hosted.weblate.org/
*   Trying 77.78.107.252...
*   Trying 2001:1528:136:dead:beef:4242:0:30...
* Immediate connect fail for 2001:1528:136:dead:beef:4242:0:30: Network is unreachable
* Connected to hosted.weblate.org (77.78.107.252) port 443 (#0)
* found 173 certificates in /etc/ssl/certs/ca-certificates.crt
* found 704 certificates in /etc/ssl/certs
* ALPN, offering http/1.1
* SSL connection using TLS1.2 / ECDHE_RSA_AES_128_GCM_SHA256
* 	 server certificate verification OK
* 	 server certificate status verification SKIPPED
* 	 common name: hosted.weblate.org (matched)
* 	 server certificate expiration date OK
* 	 server certificate activation date OK
* 	 certificate public key: RSA
* 	 certificate version: #3
* 	 subject: CN=hosted.weblate.org
* 	 start date: Tue, 21 Mar 2017 22:13:00 GMT
* 	 expire date: Mon, 19 Jun 2017 22:13:00 GMT
* 	 issuer: C=US,O=Let's Encrypt,CN=Let's Encrypt Authority X3
* 	 compression: NULL
* ALPN, server accepted to use http/1.1
> OPTIONS / HTTP/1.1
> Host: hosted.weblate.org
> User-Agent: curl/7.43.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: nginx
< Date: Sat, 20 May 2017 10:57:28 GMT
< Content-Type: text/html; charset=utf-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< Vary: Accept-Encoding
< Vary: Accept-Encoding
< X-XSS-Protection: 1; mode=block
< Content-Security-Policy: default-src 'self'; style-src 'unsafe-inline' 'self'; img-src stats.cihar.com 'self'; script-src 'unsafe-inline' stats.cihar.com 'self'; connect-src 'self'; object-src 'none'; child-src 'none'; frame-ancestors 'none';
< Content-Language: en
< Vary: Cookie, Accept-Language
< ETag: "2e34db48979ddcc32e17218e269fa41f"
< X-Frame-Options: SAMEORIGIN
< Set-Cookie: csrftoken=HFmatIka7TfftqL640ZC0JKQsRTMCjYejpfLZixD5fXDqCK956ylu34JchMKF7VT; expires=Sat, 19-May-2018 10:57:28 GMT; httponly; Max-Age=31449600; Path=/; secure
< Strict-Transport-Security: max-age=31536000; includeSubdomains;
< X-Content-Type-Options: nosniff
< 
```

__Reference__ 

https://hackerone.com/reports/8184
https://hackerone.com/reports/182265

Thanks

## Attachments
No attachments
