# Remote client memory corruption in ssl_add_clienthello_tlsext()

## Report Details
- **Report ID**: 175766
- **URL**: https://hackerone.com/reports/175766
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-10-14T14:15:56.506Z
- **Disclosed**: 2016-12-30T13:16:26.253Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://guidovranken.wordpress.com/2016/10/13/openssl-1-1-0-remote-client-memory-corruption-in-ssl_add_clienthello_tlsext/

OpenSSL is not treating this as a security vulnerability because 1) session tickets need to be enabled 2) request certificate status from server 3) an unrealistically large ALPN list set.

Reporting this for reputation points.

## Attachments
No attachments
