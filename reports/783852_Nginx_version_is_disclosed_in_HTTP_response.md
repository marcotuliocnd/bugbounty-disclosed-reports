# Nginx version is disclosed in HTTP response

## Report Details
- **Report ID**: 783852
- **URL**: https://hackerone.com/reports/783852
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-01-26T21:54:31.337Z
- **Disclosed**: 2020-02-06T20:07:24.886Z

## Reporter
- **Username**: hckit_02
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: localizejs

## Vulnerability Information
## Summary:
I found a version disclosure (Nginx) in your web server's HTTP response.

***Extracted Version:*** 1.16.1

This information might help an attacker gain a greater understanding of the systems in use and potentially develop further attacks targeted at the specific version of Nginx.

## Steps To Reproduce:

***Checkout the URL:** https://localizestaging.com/

Checkout the header response:

HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Connection: close
Date: Sun, 26 Jan 2020 21:37:55 GMT
Server: nginx/1.16.1
Vary: Accept-Encoding
X-DNS-Prefetch-Control: off
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Security-Policy: object-src 'none'; base-uri https://localizestaging.com; frame-ancestors https://localize.live
ETag: W/"883d-dUYoyQDdg3V8h1QICXD3rs4"
X-Cache: Miss from cloudfront
Via: 1.1 5157dedfe33ef5a309f236599901abe3.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: SIN52-C3
X-Amz-Cf-Id: 
Content-Length: 34877

PoC : F696981: Server Disclosure .jpg 

## Supporting Material/References:
***Number of vulnerabilities:*** 3
***CVE IDs:*** 	
1. CVE-2019-9511
2. CVE-2019-9513
3. CVE-2019-9516

##1) Resource exhaustion
Severity: Medium
CVE-ID: CVE-2019-9511
CWE-ID: CWE-400 - Uncontrolled Resource Consumption ('Resource Exhaustion')
***Description***
The vulnerability allows a remote attacker to perform a denial of service (DoS) attack.
The vulnerability exists due to improper input validation when processing HTTP/2 requests. A remote attacker can send a specially crafted HTTP/2 request the affected server, consume all available CPU resources and perform a denial of service (DoS) attack.
Successful exploitation of the vulnerability requires that support for HTTP/2 is enabled.
***Mitigation***
Install updates from vendor's website.

##2) Resource exhaustion
Severity: Medium
CVE-ID: CVE-2019-9513
CWE-ID: CWE-400 - Uncontrolled Resource Consumption ('Resource Exhaustion')
***Description***
The vulnerability allows a remote attacker to perform a denial of service (DoS) attack.

The vulnerability exists due to improper input validation when processing HTTP/2 requests. A remote attacker can send a specially crafted HTTP/2 request the affected server, consume all available CPU resources and perform a denial of service (DoS) attack.
Successful exploitation of the vulnerability requires that support for HTTP/2 is enabled.
***Mitigation***
Install updates from vendor's website.

##3) Resource exhaustion
Severity: Medium
CVE-ID: CVE-2019-9516

CWE-ID: CWE-400 - Uncontrolled Resource Consumption ('Resource Exhaustion')
***Description***
The vulnerability allows a remote attacker to perform a denial of service (DoS) attack.

The vulnerability exists due to improper input validation when processing HTTP/2 requests within the ngx_http_v2_module module. A remote attacker can send a specially crafted HTTP/2 request the affected server, consume all available CPU resources and perform a denial of service (DoS) attack.
Successful exploitation of the vulnerability requires that support for HTTP/2 is enabled.
***Mitigation***
Install updates from vendor's website.

***More details:*** https://www.cybersecurity-help.cz/vdb/SB2019081323

## Impact

An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified.

Add the following line to your nginx.conf file to prevent information leakage from the SERVER header of its HTTP response:

```server_tokens off```

## Attachments
- Server_Disclosure_.jpg
