# Common response suggestion is sent to Google Analytics when user accepts duplicate comment Genius suggestion

## Report Details
- **Report ID**: 297181
- **URL**: https://hackerone.com/reports/297181
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-12T06:40:35.325Z
- **Disclosed**: 2018-01-22T00:20:53.640Z

## Reporter
- **Username**: bigbug
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary**

It was found that although the `referrer-policy` header for https://hackerone.com/hacktivity was set to `strict-origin-when-cross-origin
`, a request to https://www.hackerone.com/blog contains full url path of the the hackivity page as the `referer` header eg. `https://hackerone.com/hacktivity?sort_type=popular&filter=type%3Aall&page=1&range=forever`. The `www.hackerone.com` being hosted on a third party, this can lead to private url information being passed to third party.    

**Description**

A `referrer policy` header is set on all pages including **/hacktivity** to `strict-origin-when-cross-origin` wherein the full path of the url will be set as the `referer` only if the request is `same-origin`. But it was seen that although this header being set at /hacktivity page, it still sends a full url to an different origin ie `www.hackerone.com`. www.hackerone.com being hosted on a third party and also even after setting the referrer-policy header the hacktivity page sends full url in the referer header. This is something serious here. 


**Steps to reproduce**

+ Sign-in to hackerone.
+ Start a web debugging proxy like burp to capture the request.
+ Click on hacktivity tab -  https://hackerone.com/hacktivity. The url will contain filter parameters that are set default eg `https://hackerone.com/hacktivity?sort_type=popular&filter=type%3Aall&page=1&range=forever`. This is the `popular` hackivity page with default filters. capture the request and response. The response looks like this.


```:status:                           200
date:                              Tue, 12 Dec 2017 05:42:21 GMT
content-type:                      text/html; charset=utf-8
cache-control:                     private, no-cache, no-store, must-revalidate
content-disposition:               inline; filename="response.html"
x-request-id:                      d7905553-8780-4731-93b8-021b4761817a
set-cookie:                        __Host-session=<Redacted value>; path=/; secure; HttpOnly
strict-transport-security:         max-age=31536000; includeSubDomains; preload
expect-ct:                         enforce, max-age=86400
content-security-policy:           <Redacted as long for clarity>
referrer-policy:                   strict-origin-when-cross-origin
x-content-type-options:            nosniff
x-download-options:                noopen
x-frame-options:                   DENY
x-permitted-cross-domain-policies: none
x-xss-protection:                  1; mode=block
server:                            cloudflare-nginx
cf-ray:                            3cbe5c199a952db5-BOM
content-encoding:                  gzip```

**Note** - If we look at the `referrer-policy:` header it is set to `strict-origin-when-cross-origin`.

+ Click on `blog` link at the bottom of the page and capture the request. The request looks like this. 

```:method:         GET
:path:           /blog
:authority:      www.hackerone.com
:scheme:         https
user-agent:      Mozilla/5.0 (Windows NT 6.3; rv:46.0) Gecko/20100101 Firefox/46.0
accept:          text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
accept-language: en-US,en;q=0.5
accept-encoding: gzip, deflate, br
referer:         https://hackerone.com/hacktivity?sort_type=popular&filter=type%3Aall&page=1&range=forever
cookie:          <Redacted cookie values>
if-none-match:   "1513035467"```

**Note** - The `referer:` header contains the full url path inspite of referrer-policy header being set to strict-origin-when-cross-origin. This is a security violation as www.hackerone.com is not a `same-origin` and also hosted on a third party.

## Impact

The hackivity url does not contain any private or hidden paths. But even after a strict header being set, this behaviour is a threat as it violates the policy. If a header is set, the policy must be followed and enforced. This is to be ensured for better security.

## Attachments
No attachments
