# Multiple HTTP Smuggling reports

## Report Details
- **Report ID**: 648434
- **URL**: https://hackerone.com/reports/648434
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-07-17T22:47:10.824Z
- **Disclosed**: 2019-11-12T23:44:23.458Z

## Reporter
- **Username**: regilero
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Theses reports spreads other several years and are all about **HTTP Smuggling issues**
(HTTP Requests or Responses splitting, Cache Poisoning, Security filter bypass).
I've made reports on a wide range of open source projects, explaining
the (not always easy) problems to the various security maintainers and testing the fixs.

The starting point for this work was the 2005 work published by Amit Klein and some others:

 * 2004 - Amit Klein : "Divide and Conquer: HTTP Response Splitting, Web Cache Poisoning Attacks, and Related Topics" https://packetstormsecurity.com/papers/general/whitepaper_httpresponse.pdf
 * 2005 - Chaim Linhart, Amit Klein, Ronen Heled, Steve Orrin: "HTTP Request Smuggling" https://www.cgisecurity.com/lib/HTTP-Request-Smuggling.pdf
 * 2006 - Amit Klein: "HTTP Message Splitting, Smuggling and Other Animals" www.owasp.org/images/1/1a/OWASPAppSecEU2006_HTTPMessageSplittingSmugglingEtc.ppt 
 * 2005 - Amit Klein: "HTTP Request Smuggling - ERRATA (the IIS 48K buffer phenomenon)" 
 * 2006 - Amit Klein: “HTTP Response Smuggling” https://www.securityfocus.com/archive/1/425593
 * 2006 - Amit Klein : HTTP Response Smuggling http://lists.webappsec.org/pipermail/websecurity_lists.webappsec.org/2006-February/000836.html
 * RFC 7230 section 9 (splitting, parsing, smuggling, poisoning) https://tools.ietf.org/html/rfc7230#section-9

And also the works of James Kettle on HTTP Host headers "Practical HTTP Host header attacks (Absolute uri in host headers)"
https://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html
and, later, his work on ESI server or pingbacks and cache attacks or Pratical Web Cache Poisoning.

In 2015, Starting from these past studies, I studied **Apache**, **Nginx**, **Varnish** source code, I discovered
that a lot of smuggling problems were still present, found new ones based on overflows for the size
attributes (previous works were mostly based on doubling length information) and expanded my works on
**Golang**, **Nodejs**, **pound**, **HaProxy**, **Jetty**, **Tomcat**, **Apache Traffic Server**...

I sometime had to push for disclosure of fixed vulnerabilitie (Varnish 3) via bugtraq.
But in most of the case it's been a matter a patience -- the long time between reports and fixes
ha also something to deal with lazyness on my side as security is not the biggest part of my job --
as most of the fix implies updates on HTTP servers, which is not something as fast as updating a web
application framework. I did not get a security report or a CVE for each reported flaw, especially
on the first years. Smuggling is sometimes hard to explain (and public disclosure policies
are not always liked on HTTP servers dev teams).

The main problem of HTTP smuggling issues is that the final exploitation comes from **interactions between different http parsers**. If two actors badly interprets the HTTP message or disagree on the right
interpretation then bad things could happen. From the security maintainer point of view it's sometimes
easy to reject the problem as coming from the others.

It's also **very important** to understand that the attacker controls the HTTP message, **we do not use HTTP messages from browsers**, the attacker injects bad HTTP messages onto servers infrastructures, effects on the users comes later, when the real user HTTP messages reach the *infected* or  *shaken* servers. *Like when you do report a smuggling issue on hackerone reports, they prevent reporters that issues about header injection are not always security issues because we cannot control the user headers. That's a huge misunderstanding of smuggling payloads*.

I've made some blog posts explaining details (I still have one awaiting vendor authorization) for some
of the fixed problems.

And I also made a **Defcon 24** presentation on 2016. For someone knowing nothing on smuggling
it's a good starting point (links on next part below).

Note : my work is usually reported with the name 'regilero', and sometimes 'Régis Leroy'.

# Public ressources published

 * 2015 : Nginx Integer truncation : https://regilero.github.io/english/security/2015/03/25/nginx-integer_truncation/
 * 2015 : Checking HTTP Smuggling issues in 2015 – Part1 http://regilero.github.io/security/english/2015/10/04/http_smuggling_in_2015_part_one 
 * 2016 : Defcon 24 : Hiding Wookiees in HTTP: HTTP smuggling https://media.defcon.org/DEF%20CON%2024/DEF%20CON%2024%20presentations/DEF%20CON%2024%20-%20Regilero-Hiding-Wookiees-In-Http.pdf
    - Defcon presentation : https://www.youtube.com/watch?v=dVU9i5PsMPY
    - Defcon demos : https://www.youtube.com/watch?v=lY_Mf2Fv7kI  (which were not available on time due to Linux not supported by Defcon !!)
 * 2018 : HTTP Smuggling, Apsis Pound load balancer : https://regilero.github.io/english/security/2018/07/03/security_pound_http_smuggling/
 * 2019 : HTTP Smuggling, Jetty : https://regilero.github.io/english/security/2019/04/24/security_jetty_http_smuggling/
 
Tools: HTTPWookiee : https://github.com/regilero/HTTPWookiee : this contains a small subset of the real tests I perform on HTTP servers.

# List of CVEs

## Apache Traffic Server

 * **CVE-2018-8004** : space before colon + force connection close on error 400 + duplicate Content-Lenght issues + bad parsing of request size on cache hit

## Jetty

 * **CVE-2017-7656** : HTTP/0.9 Request Smuggling
  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-7656 (score 6.5)

 * **CVE-2017-7657**: Transfer-Encoding Request Smuggling
  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-7657 (score 6.5)

 * **CVE-2017-7658**: Too Tolerant Parser, Double Content-Length + Transfer-Encoding + Whitespace 
  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-7658 (score 6.5)


# Apache httpd

 * https://bz.apache.org/bugzilla/show_bug.cgi?id=57832 : Apache issues on 'socket poisoning', where we could store HTTP responses on
  the reverse proxy by sending extra responses, and mix these response with other users later. Not fixed via a CVE because this behavior
  was not considered as a real security issue (it's a consequence of a successful splitting attack on the backend, or of a compromised backend).
  If you ask my opinion this is one of the most problematic issue I found on these 5 years. Fixs were included in 2016 on version 2.4.24.

 * **CVE-2016-8743** : httpd: Apache HTTP Request Parsing Whitespace Defects : problems with CR, FF, VTAB and others strange characeters in parsing HTTP messages
 especially the space before colon problem. They were also some HTTP 0.9 downgrades.
 This work contributed to the internal dev debates around the HttpProtocolOptions Strict|LenientMethods|Allow0.9 option added on 2.4

 * **CVE-2015-3183** : chunk header attribute truncation (low)

# Facebook Proxygen

Proxygen is a C++ Open Source library which is the core library for Facebook HTTP related projects

In 2016 I reported several smuggling issues (about doubled headers or bad end of line, for example), via the facebook bounty program `#1710044992591113`

# Apsis Pound

Pound is an open Source SSL terminator, but the project has not published major changes for a long time, and I experienced difficulties having my reports fixed and delivered to final users.
After reports on 09-2016 a Version 2.8a fixing the flaws was published on 10-2016 but marked as experimental.
Details of the flaws were published in 07-2018. CVE was reserved by myslef on 2018-01. A version 2.8 was published on 2018-05.

 * **CVE-2016-10711** : Apsis Pound before 2.8a allows request smuggling via crafted headers

Details of issues (double Content Length, chunk prioriy, headers concatenation vuia NULL character, etc.) are published on my blog post https://regilero.github.io/english/security/2018/07/03/security_pound_http_smuggling/

# Nodejs

 * **CVE-2016-2086** (but not CVE-2016-2216 from the same release) : support of bad end of lines (especially \r followed by anything) + double Content Length, + mixed chunked and Content Length + space before colon

# Tomcat

 * **CVE-2016-6816** : Tomcat 6,7 & 8: HTTP/0.9 downgrade and various bad characters support

# Varnish

 * Varnish3 :  **CVE-2015-8852** : received after public disclosure : https://seclists.org/oss-sec/2016/q2/95
 * Varnish4 : 2016 : space before colon fix without CVE : https://github.com/varnishcache/varnish-cache/commit/0577f3fba200e45c05099427eec01610ee061436
 cache poisoning of Varnish4 with a golang traefik server as backend was demonstrated to the project maintainer, but the project 'does not like CVE'.
 * Varnish 4 : 2016 messsage splitting on bad characters fixed without CVE : https://github.com/varnishcache/varnish-cache/commit/d1eb31109f614976f06dd506a63e0fa21185a89b

HTTP/0.9 support was also removed after my reports in 2015, but without public disclosure of potential abuse.

# golang (go language)

 * **CVE-2015-5739** : "Content Length" magically fixed to "Content-Length."
 * **CVE-2015-5740** : support of double Content-Length
 * 01-2016 : integer overflow on chunk size : https://go-review.googlesource.com/c/go/+/18871
 * 06-2016 : downgrade HTTP/0.9 : https://github.com/golang/go/issues/16197, no CVE, as described in the commit comment
 "@regilero also mentioned there might be some cache poisoning or request smuggling possibilities here, but I don't see how. It seems to only affect the person making the bogus request." (sic)
 * 06-2016 : Splitting on space + colon

# Nginx

Not the project where I had the most success, I do not think any smuggling issue would be considered a security issue.

 * Integer overflow on Content Length : fixed without CVE : http://hg.nginx.org/nginx/rev/15a15f6ae3a2 after a report and a proposed patch (not as good as the final one)
  the security team 'don't consider this to be something serious from security point of view and have no plans for CVE and/or security advisories'.
 I made examples of exploitation at https://regilero.github.io/english/security/2015/03/25/nginx-integer_truncation/
 * https://trac.nginx.org/nginx/ticket/762 : 0.9 downgrade: protocol version overflow; HTTP/65536.8 or HTTP/65536.9 treated as a 0.9 request
 rejected as a security issue, classified as minor issue, fixed 1 year and 6 month after public report (11-2016). This was in my mind quite huge.
 * https://trac.nginx.org/nginx/ticket/1014 : wontfix : I'd like an error 400 instead of silently ignoring a bad header, no success

# OpenBSD

In 2015 the OpenBSD Http server was very new, crashing on 0.9 requests, I reported some smuggling issues (bad end of line, double Content-Length) which were fixed later.

# HaProxy

HaProxy was transmitting some of the very bad request I use to perform splitting attacks on backends (something which is not a security issue, but which allows security issues).
I had various discussions with Willy Tarreau which leaded to some improvments in HaProxy, blocking bad requests before any less robust HTTP parser could read it.

For example:

 * commit 987aa383c85525b163267110a4bcff4dff3849b8 : BUG/MEDIUM: http: remove content-length from chunked messages
 * commit e1ce063c12bf22b99e6caa6a55484f1b9a27e113 : MEDIUM: http: disable support for HTTP/0.9 by default
 * commit b053c03d6f05c8ddf264de78fe321d8455358690 : MEDIUM: http: restrict the HTTP version token to 1 digit as per RFC7230

# Summary

I think this work allows for more robusts HTTP servers. Some of the very old issues already reported in the 2005 era reports, like double Content Length,
were still widely supported in 2015 and are now harder to find on most open source http servers. I think I contributed greatly to enforce the RFC 7230
anti-smuggling policies (chunk priority, no double content-length) and for the removal of old-rfc dangerous features (like the continuation of headers
with the space prefix, or the HTTP/0.9 support). For this I just had to read the 2005 studies and the RFC, tests the servers, and try to explain
exploitations.

A big part of my added work and reports was studying effects of control characters (\r, \n, NULL, vtab, htab, bell, backspace & formfeed) on various parts of the messages.
With some real good success on vartious project for NULL or for bad enf of lines.
Another big thing was studying the HTTP/0.9 downgrade exploitations (like extracting a valid HTTP message stored in an image from a partial 0.9 response) and
finding new 0.9 downgrade vectors.
Finally another part of this work was finding new attack vectors (truncation of size, overflows, concatenation of strings, effects of cache hit on header parsing, etc).

The last big part of my work was spending a long time explaining the potential attacks to maintainers. If you need hints from people understanding the smuggling attacks
and the implications of the fixed flaws, usually better than the project maintainers, I could give you some names. If you need samples of reports or detailled lab exploitations I could also deliver.

HTTP/2 or TLS are not preventing bad effects of HTTP/1.1 bad parsers (they embed HTTP/1.1 parsers in another layer), nor they could prevent effects of an HTTP/0.9 downgrades.
Every HTTP actors which enforces a more robust protocol parsing prevents chaining effects of smuggling attacks.
So I hope the work I made on the subject had real effects on the ecosystem.

Some of these CVE were already elected for bounties:
- Verizon: undisclosed (#433076): 2 700 USD
- Apache httpd CVE-2016-8743 : https://hackerone.com/reports/244459 : 1500 USD
- FaceBook Proxygen: (bugcrowd) 1000 USD
- Golang CVE-2015-5739 &CVE-2015-5740 : Google Security Bounty program : 1337 USD

## Impact

For the final user the consequences may be huge:
- Cache poisoning : so effects starts at Deny of Service, but may go to code injection (like replacing
 the code of a well known js library)
- Credentials hijacking : one of the smuggling exploitation is storing unterminated requests and waiting
 for other users requests to terminate the pending requests, mixing the users credentials on something
 they did not requested (hijacking users credentials). But this cannot work on applications using csrf protections.
- a lot of Deny of Service attacks, one of the attacks allows mixing requests and responses of
 different users, so you have documents requested by others, and they have yours.
- security filter bypass: here the public effect is less important, the attacker use smuggling to
 remove some of the security layers

A massive scale smuggling attack on a big actor (a cloud provider for example) could make a huge DOS.
A more realist usage with a public consequence is a targeted cache poisoning, to inject an XSS.
An advanced usage is the filter bypass usage, where the smuggled requests is usually not even logged. A prefect way of sending requests without notices, so a nice tool for SSRF exploits.

## Attachments
No attachments
