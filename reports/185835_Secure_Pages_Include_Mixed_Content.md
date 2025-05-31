# Secure Pages Include Mixed Content

## Report Details
- **Report ID**: 185835
- **URL**: https://hackerone.com/reports/185835
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-27T16:31:18.708Z
- **Disclosed**: 2016-12-29T21:17:57.596Z

## Reporter
- **Username**: lulliii
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hello,
The page includes mixed content, that is content accessed via HTTP instead of HTTPS.
tag=img src=http://www.gravatar.com/avatar/abbcd6344e160597fb2694f25c46149f.jpg?s=256&d=http%3A%2F%2Fwww.openstreetmap.org%2Fassets%2Fusers%2Fimages%2Flarge-8d2e51c2ddd01eb899f4bfb0bca3cf5e.png
Evidence:  http://www.gravatar.com/avatar/abbcd6344e160597fb2694f25c46149f.jpg?s=256&d=http%3A%2F%2Fwww.openstreetmap.org%2Fassets%2Fusers%2Fimages%2Flarge-8d2e51c2ddd01eb899f4bfb0bca3cf5e.png


HTTP/1.1 200 OK
Connection: keep-alive
Server: gunicorn
Date: Sun, 27 Nov 2016 16:21:49 GMT
Content-Type: text/html; charset=UTF-8
X-Gratipay-Version: 2014
Set-Cookie: csrf_token=SyU4gwZJ221GAFZDCb3wpG62UU8n58vY; expires=Sun, 04 Dec 2016 16:21:49 GMT; Path=/; secure
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-Xss-Protection: 1; mode=block
Cache-Control: no-cache
Via: 1.1 vegur

Solution:
A page that is available over SSL/TLS must be comprised completely of content which is transmitted over SSL/TLS.
The page must not contain any content that is transmitted over unencrypted HTTP.
 This includes content from third party sites.

## Attachments
No attachments
