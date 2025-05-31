# Proxy-Authorization header carried to a new host on a redirect

## Report Details
- **Report ID**: 1086259
- **URL**: https://hackerone.com/reports/1086259
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-25T02:37:39.879Z
- **Disclosed**: 2021-03-08T08:25:39.680Z

## Reporter
- **Username**: dftrace
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
hi cURL team

I am not entirely sure this is an issue, please feel free to close of it isn't.

I noticed that when making an HTTP GET request with Proxy-Authorization header, together with the "-L" flag to follow redirects

 curl -H "Authorization-Proxy: Basic xxx==" http://host:8000 -L

If the remote web server redirects to an alternate host/port, cURL  will carry over the Proxy-Authorization header to the redirected new host along with the secret.

If Authorization header is used (vs Proxy-Authentication) then the header gets stripped as it should.

Client  sends GET request with Proxy-Authorization header to Server 1:8080
Server1 Redirects cURL to Server2:8081
Server2:8081 Receives the Proxy-Authorization header
This was reproducible in the following version:

curl 7.64.1 (x86_64-apple-darwin20.0) libcurl/7.64.1 (SecureTransport) LibreSSL/2.8.3 zlib/1.2.11 nghttp2/1.41.0
Release-Date: 2019-03-27

I believe the expected behaviour is that Proxy-Authorization header should be stripped upon a server redirection, since its not within the same domain origin.

I also noticed a similar issue was opened 3 years ago regarding Authorization header: https://curl.se/docs/CVE-2018-1000007.html

## Impact

If the password is sent via HTTPS, the server may redirect it to over unencrypted protocols if sent to an HTTP web server, making the Interception of the password possible.

## Attachments
No attachments
