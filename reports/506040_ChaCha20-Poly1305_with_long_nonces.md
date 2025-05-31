# ChaCha20-Poly1305 with long nonces

## Report Details
- **Report ID**: 506040
- **URL**: https://hackerone.com/reports/506040
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-07T09:21:12.416Z
- **Disclosed**: 2019-09-30T12:46:17.462Z

## Reporter
- **Username**: jorandirkgreef
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This report relates to CVE-2019-1543, https://www.openssl.org/news/secadv/20190306.txt, which I reported to the OpenSSL maintainers a few days ago.

OpenSSL accepts nonces for the AEAD cipher ChaCha20-Poly1305 of up to 16-bytes. This support is advertised in the OpenSSL documentation and via the CHACHA_CTR_SIZE (16) constant.

However, the specification for ChaCha20-Poly1305 supports only up to 12-bytes.

If a user passes a 16-byte nonce to OpenSSL, OpenSSL will discard the first 4-bytes of the nonce.

## Impact

The maintainers classified the severity of this as LOW since it only affects user applications of OpenSSL, while at the same time recognizing the severity of this for these user applications as MEDIUM (or "serious" and "catastrophic" in the words of two maintainers).

This breaks the guarantees provided by OpenSSL to user applications in two ways:

1. These first 4-bytes are not authenticated, breaking the integrity guarantees of the AEAD cipher, and allowing an attacker to tamper with 4-bytes of the AEAD message. This in itself is serious for applications which rely on AEAD ciphers to detect message tampering and/or message corruption.

2. This introduces the likelihood of nonce-reuse, since the most significant 4-bytes of nonce entropy are discarded by OpenSSL, for example, where a user provides a 32-bit nonce counter in a statically allocated 16-byte buffer to OpenSSL. Nonce-reuse is catastrophic for an AEAD cipher such as ChaCha20-Poly1305, as it would allow an attacker to completely decrypt all sensitive information.

## Attachments
No attachments
