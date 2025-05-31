# Host header Injection rubygems.org

## Report Details
- **Report ID**: 180196
- **URL**: https://hackerone.com/reports/180196
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-04T18:12:04.182Z
- **Disclosed**: 2018-02-08T23:10:47.550Z

## Reporter
- **Username**: bugs3ra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
Hi,

As you are interested in any bug in rubygems.org, I thought of reporting it.

The host header is not validated on rubygems.org. In many cases, developers are trusting the HTTP Host header value and using it to generate links, import scripts and even generate password resets links with its value. This is a very bad idea, because the HTTP Host header can be controlled by an attacker. This can be exploited using web-cache poisoning and by abusing alternative channels like password reset emails.

**POC**
```
GET / HTTP/1.1
Host: www.google.com
```
Response
```
HTTP/1.1 500 Domain Not Found
Server: Varnish
Retry-After: 0
content-type: text/html
Cache-Control: private, no-cache
connection: keep-alive
Content-Length: 207
Accept-Ranges: bytes
Date: Mon, 31 Oct 2016 07:49:14 GMT
Via: 1.1 varnish
Connection: close

<html>
<head>
<title>Fastly error: unknown domain www.google.com</title>
</head>
<body>
Fastly error: unknown domain: www.google.com. Please check that this domain has been added to a service.</body></html>
```
Now having my malicious page hosted on fastly(example taken is www.newrelic.com running on faslty), I can expolit the issue:
```
GET / HTTP/1.1
Host: www.newrelic.com
```
Response
```
HTTP/1.1 301 Moved Permanently
Server: nginx
Content-Type: application/x-msdownload
Status: 301 Moved Permanently
Location: http://newrelic.com/
```

## Attachments
- POC.JPG
