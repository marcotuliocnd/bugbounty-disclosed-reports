# Server version/OS type disclosure via HTTP Response Header

## Report Details
- **Report ID**: 215372
- **URL**: https://hackerone.com/reports/215372
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-22T15:14:11.777Z
- **Disclosed**: 2017-03-23T16:54:33.036Z

## Reporter
- **Username**: ryudox
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
1) Issued request below:
GET / HTTP/1.1
Host: demo.nextcloud.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/css,*/*;q=0.1
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://demo.nextcloud.com/hohoho/
Cookie: PHPSESSID=s5qqervpnmuc8o8mrifveikvhn
Connection: close
If-Modified-Since: Thu, 23 Feb 2017 14:44:27 GMT
If-None-Match: "984-54933a66d83a6"
Cache-Control: max-age=0

2) Responded back the following headers:
HTTP/1.1 200 OK
Date: Wed, 22 Mar 2017 15:07:29 GMT
Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.1e-fips
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Strict-Transport-Security: max-age=15768000
Connection: close
Content-Type: text/html; charset=UTF-8
Content-Length: 9154

Note that Apache version, OS type and OpenSSL version were disclosed. For other pages in the same domain, it was only shown as Server: Apache, probably some mis-configuration.

## Attachments
No attachments
