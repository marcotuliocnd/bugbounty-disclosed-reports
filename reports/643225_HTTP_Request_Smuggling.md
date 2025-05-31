# HTTP Request Smuggling

## Report Details
- **Report ID**: 643225
- **URL**: https://hackerone.com/reports/643225
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-15T04:41:11.494Z
- **Disclosed**: 2020-03-09T00:26:50.803Z

## Reporter
- **Username**: mah3sec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: jamieweb

## Vulnerability Information
is vulnerable to host header injection because the host header can be changed to something outside the target domain.

Attack vectors are somewhat limited but depends on how the host header is used by the back-end application code. If code references the hostname used in the URL such as password reset pages, an attacker could spoof the host header of the request in order to trick the application to forwarding the password reset email to the attackers domain instead, etc. Other attack vectors may also be possible through manipulation of hyperlinks or other misc. code that relies on the host/domain of the request.


## Steps To Reproduce:
request:--
GET /contact/ HTTP/1.1
Host: www.google.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.jamieweb.net/
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0

Response:---

HTTP/1.1 421 Misdirected Request
Date: Mon, 15 Jul 2019 04:24:41 GMT
Server: Apache
Content-Security-Policy: default-src 'none'; base-uri 'none'; font-src 'self'; form-action 'none'; frame-ancestors 'none'; img-src 'self'; style-src 'self'; block-all-mixed-content
Feature-Policy: accelerometer 'none'; ambient-light-sensor 'none'; autoplay 'none'; camera 'none'; document-write 'none'; fullscreen 'none'; geolocation 'none'; gyroscope 'none'; magnetometer 'none'; microphone 'none'; midi 'none'; payment 'none'; speaker 'none'; sync-script 'none'; sync-xhr 'none'; usb 'none'; vr 'none'
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-DNS-Prefetch-Control: off
Referrer-Policy: no-referrer-when-downgrade
Content-Length: 322
Connection: close
Content-Type: text/html; charset=iso-8859-1


## Supporting Material/References (if applicable): https://hackerone.com/reports/170333
                                                                          https://hackerone.com/reports/182670
https://hackerone.com/reports/264405
https://hackerone.com/reports/158482


POC attach below.

## Impact

password reset poisoning
cache poisoning
access to other internal host/application
XSS, etc.

## Attachments
- check2.PNG
- check1.PNG
