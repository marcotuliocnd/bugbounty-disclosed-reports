# HTTP trace method is enabled on gip.rocks

## Report Details
- **Report ID**: 203384
- **URL**: https://hackerone.com/reports/203384
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-04T11:05:16.649Z
- **Disclosed**: 2017-04-08T11:06:44.196Z

## Reporter
- **Username**: a0xnirudh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hello,

HTTP TRACE method is enabled on your server which should not be enabled. It can lead to cross site tracing !

Cross site tracing: https://www.owasp.org/index.php/Cross_Site_Tracing

```
curl -X TRACE http://gip.rocks/ -vv
* Hostname was NOT found in DNS cache
*   Trying 184.73.218.93...
* Connected to gip.rocks (184.73.218.93) port 80 (#0)
> TRACE / HTTP/1.1
> User-Agent: curl/7.35.0
> Host: gip.rocks
> Accept: */*
> 
< HTTP/1.1 200 OK
< Connection: keep-alive
* Server gunicorn/18.0 is not blacklisted
< Server: gunicorn/18.0
< Date: Sat, 04 Feb 2017 10:59:49 GMT
< Transfer-Encoding: chunked
< Content-Type: text/html; charset=UTF-8
< Via: 1.1 vegur
< 
```

## Mitigation:

Disable TRACE method support on your server.

## Attachments
No attachments
