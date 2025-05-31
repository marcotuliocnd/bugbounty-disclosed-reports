# limit HTTP methods on other domains

## Report Details
- **Report ID**: 117142
- **URL**: https://hackerone.com/reports/117142
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-02-18T12:31:43.167Z
- **Disclosed**: 2016-07-19T20:08:50.321Z

## Reporter
- **Username**: jackds
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hi there! I've found out that also one of your subdomains still has HTTP TRACE enabled. This is similar to the issue described in #109054, except that it is for http://inside.gratipay.com.

```
curl -v -X TRACE http://inside.gratipay.com
* Rebuilt URL to: http://inside.gratipay.com/
* Hostname was NOT found in DNS cache
*   Trying 107.21.92.176...
* Connected to inside.gratipay.com (107.21.92.176) port 80 (#0)
> TRACE / HTTP/1.1
> User-Agent: curl/7.35.0
> Host: inside.gratipay.com
> Accept: */*
> 
< HTTP/1.1 200 OK
< Connection: close
< Date: Thu, 18 Feb 2016 12:26:17 GMT
* Server WSGIServer/0.1 Python/2.7.6 is not blacklisted
< Server: WSGIServer/0.1 Python/2.7.6
< Content-Type: text/html; charset=UTF-8
< Via: 1.1 vegur
<  data...
```

## Attachments
No attachments
