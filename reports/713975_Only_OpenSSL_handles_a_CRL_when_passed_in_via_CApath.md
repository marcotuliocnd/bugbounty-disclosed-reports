# Only OpenSSL handles a CRL when passed in via CApath 

## Report Details
- **Report ID**: 713975
- **URL**: https://hackerone.com/reports/713975
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-10-14T14:51:22.948Z
- **Disclosed**: 2021-01-08T09:09:22.411Z

## Reporter
- **Username**: salvet
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
Code in vtls/nss.c interprets CApath option differently than OpenSSL-using code,
user can be mislead to unsecure use of curl/libcurl easily. CApath directory
can contain CRL files in addition to CA certificate files and they are used
for certificate verification when curl calls OpenSSL. Code path using NSS blindly
loads all files residing in CApath as CA certificates instead, which has two effects:
first, the meaning of CRLs is ignored and revoked certificates can be accepted,
second, NSS may find duplicate SN in corrupt 'CA certificate' during TLS handshake and break
connection to legitimate server (NSS does not perform full validation in load
and search routines, ASN.1 templates used can mistakenly match both types of object).
Such use is not explicitly supported according to curl documentation strictly speaking
but I find current implementation very risky (I know security professionals who have fallen to this trap)
and recommend adding validation/type detection for each file loaded
from CApath (or using c_hash-style name extensions if any file with such extension
is present, if full validation is deemed too complicated or as a quick fix helping most users).

# Steps To Reproduce:
  1. revoke a certificate, install resulting CRL in CApath, try with NSS-based curl
  2. try connecting TLS server whose CA has self-signed certificate with SN=1 and CRL in CApath
     (success can depend on order of directory entries)

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

An attacker can impersonate TLS server using revoked (presumably leaked) certificate.

## Attachments
No attachments
