# www.hackerone.com website CSP "script-src" includes "unsafe-inline"

## Report Details
- **Report ID**: 225833
- **URL**: https://hackerone.com/reports/225833
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-05-03T13:58:52.776Z
- **Disclosed**: 2017-05-23T06:24:45.388Z

## Reporter
- **Username**: rootkid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:** 

The HTTP header of the hackerone.com website includes an unsafe CSP parameter for "script-src". 

**Description:** 
The hackerone.com website (https://www.hackerone.com) has a  Content-Security-Policy configured, as pointed out on the Bug Bounty page of their program:

>We utilize a strict Content Security Policy and a safe-by-default templating language to effectively neutralize Cross-Site Scripting (XSS).

However, the "script-src" parameter is set to "unsafe-inline", which allows injection of user passed values, which in result can be misused for Cross-Site Scripting attacks. As a best practice, this value should not be included as a "script-src" parameter, if possible.


### Steps To Reproduce

The header can be read using a simple curl query:
```
$ curl -I https://www.hackerone.com
HTTP/1.1 200 OK
Date: Wed, 03 May 2017 13:43:29 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Set-Cookie: __cfduid=d80b77473f21b44450916a32b6f4e56d11493819008; expires=Thu, 03-May-18 13:43:28 GMT; path=/; Domain=www.hackerone.com; HttpOnly
Cache-Control: max-age=300, public
X-Drupal-Dynamic-Cache: HIT
X-UA-Compatible: IE=edge
Content-language: en
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Expires: Sun, 19 Nov 1978 05:00:00 GMT
Last-Modified: Mon, 01 May 2017 21:41:56 GMT
ETag: W/"1493674916"
Vary: Cookie,Accept-Encoding
X-Generator: Drupal 8 (https://www.drupal.org)
Content-Security-Policy: default-src 'none'; base-uri 'self'; block-all-mixed-content; child-src www.youtube-nocookie.com app-sj17.marketo.com; connect-src 'self' hackerone.com *.mktoresp.com checkout.stripe.com; font-src 'self'; form-action 'self' syndication.twitter.com platform.twitter.com; frame-ancestors 'self'; frame-src www.youtube.com www.youtube-nocookie.com app-sj17.marketo.com boards.greenhouse.io platform.twitter.com syndication.twitter.com checkout.stripe.com; img-src 'self' data: www.google-analytics.com syndication.twitter.com platform.twitter.com *.twimg.com q.stripe.com; media-src 'self'; script-src 'self' 'unsafe-inline' www.google-analytics.com app-sj17.marketo.com munchkin.marketo.net boards.greenhouse.io platform.twitter.com cdn.syndication.twimg.com checkout.stripe.com; style-src 'self' 'unsafe-inline' app-sj17.marketo.com boards.greenhouse.io boards-use1-cdn.greenhouse.io platform.twitter.com checkout.stripe.com; report-uri https://errors.hackerone.net/api/30/csp-report/?sentry_key=61c1e2f50d21487c97a071737701f598
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Xss-Protection: 1; mode=block
X-Drupal-Cache: HIT
X-Request-ID: v-50f3aef2-3006-11e7-9597-02c51b741cbd
X-AH-Environment: prod
X-Varnish: 549998133 549985183
Age: 75
Via: 1.1 varnish
X-Cache: HIT
X-Cache-Hits: 43
Server: cloudflare-nginx
CF-RAY: 3593a644588915ad-FRA
```

As can be seen, "unsafe-inline" is included in in the list of "script-src" parameters. 
This does not result in an immediate threat, but should be excluded, if possible, as a best practice. For further information, see https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src

## Attachments
No attachments
