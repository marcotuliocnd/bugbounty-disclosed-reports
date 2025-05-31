# HTTP trace method is enabled on aspen.io

## Report Details
- **Report ID**: 203409
- **URL**: https://hackerone.com/reports/203409
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-02-04T14:31:46.604Z
- **Disclosed**: 2017-03-31T14:49:55.376Z

## Reporter
- **Username**: a0xnirudh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hello,

HTTP TRACE method is enabled on your server which should not be enabled. It can lead to cross site tracing ! I think this is not a critical issue but I thought I will still report because it is always better to fix it :)

Cross site tracing: https://www.owasp.org/index.php/Cross_Site_Tracing

```
$ curl -X TRACE http://aspen.io -vv                                                                                                        [19:57:58]
* Rebuilt URL to: http://aspen.io/
*   Trying 23.21.203.159...
* Connected to aspen.io (23.21.203.159) port 80 (#0)
> TRACE / HTTP/1.1
> Host: aspen.io
> User-Agent: curl/7.50.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: Cowboy
< Date: Sat, 04 Feb 2017 14:28:44 GMT
< Connection: close
< Content-Type: text/html; charset=UTF-8
< Via: 1.1 vegur
< 

```

## Mitigation:

Disable TRACE method support on your server.

## Attachments
No attachments
