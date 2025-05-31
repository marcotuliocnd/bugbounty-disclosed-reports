# Weak HSTS age

## Report Details
- **Report ID**: 147260
- **URL**: https://hackerone.com/reports/147260
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-25T17:54:16.638Z
- **Disclosed**: 2016-07-14T18:51:09.750Z

## Reporter
- **Username**: ketankumar_godhani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fantasytote

## Vulnerability Information
Send this request:

https://www.fantasytote.com/login

GET /login HTTP/1.1
Host: www.fantasytote.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Cookie: __cfduid=d8a2061ca9ed456b3696715a5f068a5731466869224; _session_id=838eb8d660cd138f1b7fab029187cc9a; _ga=GA1.2.321412493.1466869396; _gu=732e6098-8746-4c7d-be39-fd7fb86290d3; _gw=2.69166(sc~7,s~o9c97z)u[~0,~0,~0,~0,~0]v[~ek05j,~5,~1]a(); _gs=2.s(src=https://www.fantasytote.com/login); _gat=1
Connection: keep-alive

HTTP/1.1 200 OK
Date: Sat, 25 Jun 2016 17:50:24 GMT
Content-Type: text/html; charset=utf-8
Connection: close
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Cache-Control: no-cache, no-store, private, must-revalidate, max-age=0, max-stale=0, post-check=0, pre-check=0
surrogate-control: max-age: 0
Pragma: no-cache
Expires: 0
Vary: *
Set-Cookie: _session_id=8b128154bdaf0790aa1120cc4f5d8b4e; path=/; expires=Mon, 27 Jun 2016 17:50:24 -0000; secure; HttpOnly
x-request-id: 72a13e25-b3fb-4a60-9260-c2e9c9ef373b
x-runtime: 0.045696
Strict-Transport-Security: max-age=0; includeSubDomains; preload
x-ua-compatible: IE=Edge,chrome=1
Server: cloudflare-nginx
cf-ray: 2b8a42f9e2122dcd-BOM
Content-Length: 27864







==>>Strict-Transport-Security: max-age=0
==>> Directs the browser to delete the entire HSTS policy.

https://blog.qualys.com/securitylabs/2016/03/28/the-importance-of-a-proper-http-strict-transport-security-implementation-on-your-web-server

## Attachments
No attachments
