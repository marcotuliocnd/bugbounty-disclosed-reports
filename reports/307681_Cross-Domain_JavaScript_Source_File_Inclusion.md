# Cross-Domain JavaScript Source File Inclusion 

## Report Details
- **Report ID**: 307681
- **URL**: https://hackerone.com/reports/307681
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-01-21T17:17:34.880Z
- **Disclosed**: 2018-12-10T17:34:25.429Z

## Reporter
- **Username**: mrunal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
The page includes one or more script files from a third-party domain.

XSSI is a fancy way of saying: you are including in your program, someone elses code; You don't have any control over what is in that code, and you don't have any control over the security of the server on which it is hosted.
 
parameter : //secure.gaug.es/track.js
evidence: <script type="text/javascript" async defer id="gauges-tracker" data-site-id="4eab0ac8613f5d1583000005" src="//secure.gaug.es/track.js"></script>

solution : Ensure JavaScript source files are loaded from only trusted sources, and the sources can't be controlled by end users of the application.


    <script type="text/javascript" async defer id="gauges-tracker" data-site-id="4eab0ac8613f5d1583000005" src="//secure.gaug.es/track.js"></script>
  </body>


HTTP request :

HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'; script-src 'self' https://secure.gaug.es; style-src 'self' https://fonts.googleapis.com; img-src 'self' https://secure.gaug.es https://gravatar.com https://secure.gravatar.com; font-src 'self' https://fonts.gstatic.com; connect-src https://s3-us-west-2.amazonaws.com/rubygems-dumps/; frame-src https://ghbtns.com
Cache-Control: max-age=0, private, must-revalidate
Set-Cookie: _rubygems_session=R2ovd2tLZG9lUGtmY1pQczgvSFBjdC9IdjE5QnVJQ0Ywby9xbmNUSlRQU3JaOVNoNnF5WE1KZW14eGFlTTdZbHJPZFp6Vk5Udlp3QTRMSElkTmJnWlFlRjMyVWJJa2k5NU1LTm9XTVozWVBYaHdWLzg1dW1UaDd6TitZR1FYZ041M0oyZk94T2tVMG1vbU54Rm02SThnPT0tLTdZK1pRK0QxTW1GcS9GWVlPZlFoVUE9PQ%3D%3D--102c1918815967faefb0604b28daa2d3900df474; path=/; secure; HttpOnly
X-Request-Id: 282c9423-26fd-4517-8bfc-1359900c553e
X-Runtime: 0.013107
Strict-Transport-Security: max-age=0
X-UA-Compatible: IE=Edge,chrome=1
X-Backend: F_Rails 54.186.104.15:443
Accept-Ranges: bytes
Date: Sun, 21 Jan 2018 17:00:41 GMT
Via: 1.1 varnish
Age: 0
Connection: keep-alive
X-Served-By: cache-sin18034-SIN
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1516554041.101894,VS0,VE220
Vary: Accept-Encoding,Fastly-SSL
ETag: "a2988a0215687cad2553179ed0d2d3ef"
Server: RubyGems.org

## Impact

Browsers prevent pages of one domain from reading pages in other domains. But they do not prevent pages of a domain from referencing resources in other domains. In particular, they allow images to be rendered from other domains and scripts to be executed from other domains. An included script doesn't have its own security context. It runs in the security context of the page that included it. For example, if www.evil.example.com includes a script hosted on www.google.com then that script runs in the evil context not in the google context. So any user data in that script will "leak

## Attachments
- jerms.html
