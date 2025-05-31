# [gratipay.com] Cross Site Tracing

## Report Details
- **Report ID**: 152834
- **URL**: https://hackerone.com/reports/152834
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-21T09:18:17.365Z
- **Disclosed**: 2017-08-21T13:32:01.664Z

## Reporter
- **Username**: ahsan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
**Hello team,**

I was checking if TRACE method is enabled on gratipay.com or not? I opened up my terminal (CLI) and executed this command: curl -v -X TRACE http://gratipay.com

The response may not actually shows it is vulnerable, but it is not as well a message for properly configured "no" to Cross Site Tracing attack.

And it showed up this response:
```
*   Trying 54.235.170.226...
* Connected to gratipay.com (54.235.170.226) port 80 (#0)
> TRACE / HTTP/1.1
> Host: gratipay.com
> User-Agent: curl/7.49.1
> Accept: */*
>
< HTTP/1.1 302 Found
< Server: gunicorn
< Date: Thu, 21 Jul 2016 09:15:54 GMT
< X-Frame-Options: SAMEORIGIN
< Cache-Control: no-cache
< X-Xss-Protection: 1; mode=block
< Location: https://gratipay.com/
< X-Content-Type-Options: nosniff
< X-Gratipay-Version: 1977
< Via: 1.1 vegur
< X-Cache: MISS from cache1
< X-Cache-Lookup: NONE from cache1:8080
< Transfer-Encoding: chunked
< Connection: keep-alive
<
* Connection #0 to host gratipay.com left intact
```

**While, it should show this error**
```
<html>
<head><title>405 Not Allowed</title></head>
<body bgcolor="white">
<center><h1>405 Not Allowed</h1></center>
<hr><center>nginx</center>
</body>
</html>
```

##PoC
We can inject headers in the response:

_Command:_ `curl -v -X TRACE -H "Header: value=Testing" http://gratipay.com/`

_Response:_
```
*   Trying 54.235.170.226...
* Connected to gratipay.com (54.235.170.226) port 80 (#0)
> TRACE / HTTP/1.1
> Host: gratipay.com 
> User-Agent: curl/7.49.1
> Accept: */*
> Header: value=Testing --> *** YOU CAN SEE HEADER INJECTED***
>
< HTTP/1.1 302 Found
< Server: gunicorn
< Date: Thu, 21 Jul 2016 09:17:01 GMT
< X-Frame-Options: SAMEORIGIN
< Cache-Control: no-cache
< X-Xss-Protection: 1; mode=block
< Location: https://gratipay.com/
< X-Content-Type-Options: nosniff
< X-Gratipay-Version: 1977
< Via: 1.1 vegur
< X-Cache: MISS from cache1
< X-Cache-Lookup: NONE from cache1:8080
< Transfer-Encoding: chunked
< Connection: keep-alive
<
* Connection #0 to host gratipay.com left intact
```

For more information: https://www.owasp.org/index.php/Cross_Site_Tracing

*Cheers,
Ahsan*

## Attachments
No attachments
