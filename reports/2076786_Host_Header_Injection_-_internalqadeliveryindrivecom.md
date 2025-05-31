# Host Header Injection - internal.qa.delivery.indrive.com

## Report Details
- **Report ID**: 2076786
- **URL**: https://hackerone.com/reports/2076786
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-07-20T06:49:15.880Z
- **Disclosed**: 2024-02-12T10:42:44.308Z

## Reporter
- **Username**: sid_x95
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
HTTP Host header attacks exploit vulnerable websites that handle the value of the Host header in an unsafe way. If the server implicitly trusts the Host header, and fails to validate or escape it properly, an attacker may be able to use this input to inject harmful payloads that manipulate server-side behavior.

Found the host header injection of given URLs:
https://internal.qa.delivery.indrive.com/
https://internal.sandbox.delivery.indrive.com/

## Steps To Reproduce:
1. Intercept the request in burp
3. Change the host name to bing.com

Request:
GET / HTTP/1.1
Host: bing.com
Upgrade-Insecure-Requests: 1
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en-US,en-GB;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36
Connection: close
Cache-Control: max-age=0


Response:
HTTP/1.1 301 Moved Permanently
location: https://bing.com/
date: Thu, 20 Jul 2023 06:24:26 GMT
server: istio-envoy
connection: close
content-length: 0

## Impact

An attacker can redirect users to malicious websites, which can lead to phishing attacks.

An attacker can create a valid webpage with malicious recommendations and the user believes the recommendation as it was from the valid website.

## Attachments
- bandicam_2023-07-20_11-54-12-264.mp4
- internal.qa.delivery.indrive.com_host-header-redirect.png
- POC2.png
