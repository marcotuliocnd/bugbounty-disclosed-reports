# Silent omission of certificate hostname verification in LibreSSL and BoringSSL

## Report Details
- **Report ID**: 329645
- **URL**: https://hackerone.com/reports/329645
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-03-25T12:36:24.157Z
- **Disclosed**: 2019-09-26T20:38:28.174Z

## Reporter
- **Username**: tiran
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Abstract

LibreSSL and BoringSSL implemented ``X509_VERIFY_PARAM_set1_host`` differently than OpenSSL. All applications that use the preferred and documented way to configure a TLS connection for hostname validation, silently neglect to perform hostname validation at all. As a consequence, they are vulnerable to MitM attacks.

## Description

OpenSSL 1.0.2 introduced the function [X509_VERIFY_PARAM_set1_host](https://www.openssl.org/docs/man1.0.2/crypto/X509_VERIFY_PARAM_set1_host.html). It sets the expected DNS hostname for a TLS connection. During the handshake, OpenSSL verifies, that the hostname matches one of the DNS names in the subject alternative name extension of the server's X.509 certificate. It's a critical step to authenticate the identity of a TLS server. A client **must** properly validate the server's DNS name.

The ``X509_VERIFY_PARAM_set1_host`` function takes three parameters. The second parameter is the expected host name, the third parameter is the length of the host name. OpenSSL allows the caller to pass in ``0`` as namelen. It indicates that the server name is a NULL terminated C string. It's documented in the man page for the function and used as example on OpenSSL's [wiki page](https://wiki.openssl.org/index.php/Hostname_validation) about hostname validation. The wiki page is the top hit for a Google search for "openssl hostname validation".

LibreSSL and BoringSSL implement the same function. LibreSSL release 2.7.0 added ``X509_VERIFY_PARAM_set1_host`` just a few days ago. However both libraries behave differently in very subtle but critical way. Their implementation of ``X509_VERIFY_PARAM_set1_host(param, "hostname", 0)`` does **not** configure the TLS/SSL connection to validate the hostname. Instead the call only clears any previously configured hostname and returns success. As a consequence, LibreSSL and BoringSSL do **not** perform any hostname validation and except just any arbitrary certificate for any hostname as long as the certificate is generally trusted. Since the function call returns success, the application never sees an error, too.

The man page for LibreSSL 2.7.0 even documented to support the calling convention. The release took the divergent implementation from BoringSSL but the documentation from OpenSSL.

## Demo

The attached files and https://github.com/tiran/CVE-2018-8970 are a demo for the bug. WIth OpenSSL the command fails as expected with a hostname mismatch error:

```
$ make
...
Error connecting to server
140678245971584:error:1416F086:SSL routines:tls_process_server_certificate:certificate verify failed:ssl/statem/statem_clnt.c:1230:
X509 verify error: Hostname mismatch
```

With LibreSSL 2.7.0 the command does not fail

```
$ make SSL_BASEDIR=/path/to/libressl/2.7.0
...
./cve2018_8970_demo
HTTP/1.1 200 OK
Server: nginx
Content-Type: text/plain
X-Frame-Options: SAMEORIGIN
x-xss-protection: 1; mode=block
X-Clacks-Overhead: GNU Terry Pratchett
Via: 1.1 varnish
Content-Length: 539
Accept-Ranges: bytes
Date: Sun, 25 Mar 2018 12:30:49 GMT
...
CVE2018-8970: Expected a hostname mismatch error
```

## Resources

* LibreSSL CVE https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8970
* LibreSSL 2.7.1 fix https://github.com/libressl-portable/openbsd/commit/0654414afcce51a16d35d05060190a3ec4618d42
* BoringSSL ticket https://bugs.chromium.org/p/chromium/issues/detail?id=824799
* BoringSSL fix https://boringssl.googlesource.com/boringssl/+/e759a9cd84198613199259dbed401f4951747cff

## Impact

The silent omission of hostname verification completely breaks confidence of TLS/SSL protocol.  It consequently allows man-in-the-middle attackers to spoof servers and obtain sensitive information via any  certificate. An attacker can use any trusted certificate from any CA and pretend to be any website. For example a malicious Wifi provider could use a Lets Encrypt cert to spoof a user to be Apple, Google, or Facebook.

## CPython
CPython's [ssl module](https://github.com/python/cpython/blob/4ca0739c9d97ac7cd45499e0d31be68dc659d0e1/Modules/_ssl.c#L855) was directly affected by the bug. Since Python 3.7 the module uses ``X509_VERIFY_PARAM_set1_host(param, server_hostname, 0)`` to match the server's hostname against the certificate.

## Mongo DB
Mongo DB's [C driver](https://github.com/mongodb/mongo-c-driver/blob/9163c64753f9f2d358a7203ce95741f87061f6b4/src/mongoc/mongoc-stream-tls-openssl.c#L687) also uses ``X509_VERIFY_PARAM_set1_host`` with namelen=0. The code segment is currently disabled for LibreSSL because it hasn't been ported to LibreSSL 2.7 yet. With high probability they would have been vulnerable, too.

## More
I suspect that more application are vulnerable to the bug. OpenSSL's wiki page https://wiki.openssl.org/index.php/Hostname_validation recommends ``X509_VERIFY_PARAM_set1_host(param, servername, 0);`` as preferred way to enable hostname verification. The namelen=0 is also explicitly mentioned in the documentation and man page for [X509_VERIFY_PARAM_set1_host](https://www.openssl.org/docs/man1.0.2/crypto/X509_VERIFY_PARAM_set1_host.html) since OpenSSL 1.0.2 and LibreSSL 2.7.0.

## Attachments
- Makefile
- cve2018_8970_demo.c
