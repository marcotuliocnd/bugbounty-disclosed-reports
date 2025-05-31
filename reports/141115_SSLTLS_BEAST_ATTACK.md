# SSL/TLS BEAST ATTACK

## Report Details
- **Report ID**: 141115
- **URL**: https://hackerone.com/reports/141115
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-26T05:34:55.665Z
- **Disclosed**: 2018-04-09T20:41:04.937Z

## Reporter
- **Username**: d0rkerdevil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drchrono

## Vulnerability Information
Supported versions:
 TLSv1.0 TLSv1.1 TLSv1.2
Deflate compression: no
Supported cipher suites (ORDER IS NOT SIGNIFICANT):
  TLSv1.0
     RSA_WITH_3DES_EDE_CBC_SHA
     RSA_WITH_AES_128_CBC_SHA
     RSA_WITH_AES_256_CBC_SHA
     TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA
     TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
     TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
  (TLSv1.1: idem)
  TLSv1.2
     RSA_WITH_3DES_EDE_CBC_SHA
     RSA_WITH_AES_128_CBC_SHA
     RSA_WITH_AES_256_CBC_SHA
     RSA_WITH_AES_128_CBC_SHA256
     RSA_WITH_AES_256_CBC_SHA256
     TLS_RSA_WITH_AES_128_GCM_SHA256
     TLS_RSA_WITH_AES_256_GCM_SHA384
     TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA
     TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
     TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
     TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
     TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
     TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
     TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
----------------------
Server certificate(s):
  4784741821c06e5af52b053fd6362db38c222df3: CN=*.drchrono.com, O=Drchrono Inc., L=Mountain View, S=California, C=US
----------------------
Minimal encryption strength:     strong encryption (96-bit or more)
Achievable encryption strength:  strong encryption (96-bit or more)
BEAST status: vulnerable <<<<<<<<<<<<<<<<<<<< patch it
CRIME status: protected


## Attachments
No attachments
