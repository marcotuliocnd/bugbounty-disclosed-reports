# User can upload files even after closing his account

## Report Details
- **Report ID**: 1020371
- **URL**: https://hackerone.com/reports/1020371
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-10-27T23:22:11.217Z
- **Disclosed**: 2021-03-29T19:13:30.482Z

## Reporter
- **Username**: h4x0r_dz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
Summary:
===========================

Hello @basecamp This is my first report on your program and I hope to end well :) .

I was testing https://app.hey.com/ and I my account has been closed, so I back to the requests history, and I tried to send these requests even my account closed.

and I found that the user can still upload files even his account closed.

 Steps To Reproduce:
================ 
I have already a closed account. to Reproduce this bug you can create a new account and closed.


1.run burp suite and go to https://app.hey.com and create a new account 
2. upload any file  and send the `POST app.hey.com/rails/active_storage/direct_uploads` request to the repeater  
3. close the account 

4.  login to the closed account on https://app.hey.com/ and you will find this page :

{F1054506}


5. intercept the page and find `csrf-token` and put it on `X-CSRF-Token:` header in `POST app.hey.com/rails/active_storage/direct_uploads` request.
and change the Cookie for the new one.

6. back to burp history , you will find ths PUT request (send it to repater )`https://haystack-production-storage-us-east-1.s3.amazonaws.com/<key>?x-amz-storage-class=<>&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=<>&X-Amz-Date=<>&X-Amz-Expires=300&X-Amz-SignedHeaders=content-length%3Bcontent-md5%3Bcontent-type%3Bhost&X-Amz-Signature=<>`

it contains the file content that you uploaded .

7. send this request :

```
POST /rails/active_storage/direct_uploads HTTP/1.1
Host: app.hey.com
Connection: close
Content-Length: 116
Accept: application/json
X-CSRF-Token:<your_CSRF-Token>
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 Chrome/83.0.4103.61 Safari/537.36
Content-Type: application/json
Origin: https://app.hey.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://app.hey.com/messages/support/new
Accept-Encoding: gzip, deflate
Accept-Language: ar,en-US;q=0.9,en;q=0.8
Cookie: <your_Cookie>

{"blob":{"filename":"<filename>","content_type":"<content_type>","byte_size":338,"checksum":"<checksum>"}}`
```

in the response you will find something like THis :

```
HTTP/1.1 200 OK
Date: Tue, 27 Oct 2020 22:40:16 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Server: openresty
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
Vary: Accept
Set-Cookie: force-primary-dc=1; path=/; max-age=3; secure
Set-Cookie: authenticity_token=ie9Iq%2By2%2B8dqEzgfYEgCWcFvD0jJ3DGH999TM8ObvceSNnk%2Beb79Myae2rImhpXVn%2F%2BD1nz3onYUawGbYZVicA%3D%3D; path=/; expires=Sat, 27 Oct 2040 22:40:16 GMT; SameSite=Lax; secure
Set-Cookie: _haystack_session=ErWRGp2IIXTWN2OcrubqWOK9GYsf1M4J%2BEQEboc%2BsTyF3Crrc8fOxS5QFq6DnhptMAqsHuToydbTzRnobqBtiR2sLiYetn4rNSit80siXqea7l0OE6fadEjpE4pA8wpHYN71HCSiJPtC%2FX0Ft9svU8xN0ybaczRDjWJi5I%2F3Qz4rPyuAdFSwHpoPrSOOC%2BYXIqeE55OBpI0VBH6IhAggK4dFiRb1Cs8jiaXVXqD%2Bi7A81ZFIw%2BLwZng0187SHY4SEaU5raCFkXuRJ6BDoq0wK8Sr5haLjTvUxFzdYdYLmsnDcslKzGb5QVNV62d9NbcmAJ6O7ZQh0vK8LxrEFA%3D%3D--pKSAzE6vGEr77yCg--R9MNGFlyj98MLnbKaX5h0Q%3D%3D; path=/; secure; HttpOnly
ETag: W/"9101e50c2c6269212bb817279c93a1e6"
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: 42cb6125062852dd41f9ae7d
X-Runtime: 0.021788
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Region: us-east-1
Content-Length: 1283

{"id":165504432,"key":"fyeem62eqa2ipopoty6c5j0aye3t","filename":"xss.svg","content_type":"image/svg+xml","metadata":{},"byte_size":338,"checksum":"QvuRT8WQtAGYrfSb+pmYdQ==","created_at":"2020-10-27T22:40:16.000000Z","service_name":"production","signed_id":"eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCTEJsM1FrPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--4c4a7ab7c81958dee84da90fd0e5d2f759d5330f","attachable_sgid":"BAh7CEkiCGdpZAY6BkVUSSI8Z2lkOi8vaGF5c3RhY2svQWN0aXZlU3RvcmFnZTo6QmxvYi8xNjU1MDQ0MzI_ZXhwaXJlc19pbgY7AFRJIgxwdXJwb3NlBjsAVEkiD2F0dGFjaGFibGUGOwBUSSIPZXhwaXJlc19hdAY7AFQw--ee2d9e3be264f7c2628062c9d0bfd3260dbd1377","direct_upload":{"url":"https://haystack-production-storage-us-east-1.s3.amazonaws.com/fyeem62eqa2ipopoty6c5j0aye3t?x-amz-storage-class=INTELLIGENT_TIERING\u0026X-Amz-Algorithm=AWS4-HMAC-SHA256\u0026X-Amz-Credential=AKIAQ742G4ISOGL5I25G%2F20201027%2Fus-east-1%2Fs3%2Faws4_request\u0026X-Amz-Date=20201027T224016Z\u0026X-Amz-Expires=300\u0026X-Amz-SignedHeaders=content-length%3Bcontent-md5%3Bcontent-type%3Bhost\u0026X-Amz-Signature=4c158a4ecc84191abb75e4a5670dff3979cfd1e5e06cf3006c8492260b5a4f96","headers":{"Content-Type":"image/svg+xml","Content-MD5":"QvuRT8WQtAGYrfSb+pmYdQ==","Content-Disposition":"inline; filename=\"xss.svg\"; filename*=UTF-8''xss.svg"}}}
```

back to PUT request in haystack-production-storage-us-east-1.s3.amazonaws.com and change the AWS keys with the new one that you got in the Response. and in the body, you can put anything.

send the PUT request, and back to the previous response and copy `signed_id` value and put it here with the filename.

`https://app.hey.com/rails/active_storage/blobs/redirect/<signed_id>/<filename>`

and you can see you able to upload files even your account is closed.



 ### POC

## Impact

Unauthenticated users at https://app.hey.com/ can upload files after close his account.

## Attachments
- Screenshot_from_2020-10-27_23-26-47.png
