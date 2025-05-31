# Multiple OpenSSL error handling issues in nodejs crypto library

## Report Details
- **Report ID**: 1808596
- **URL**: https://hackerone.com/reports/1808596
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-16T21:14:34.589Z
- **Disclosed**: 2023-02-17T18:04:53.656Z

## Reporter
- **Username**: mjones-vsat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** NodeJS up to 19.2.0 does not clear the OpenSSL error stack after operations that may set it

**Description:** NodeJS up to 19.2.0 does not clear the OpenSSL error stack after operations that may set it. This may lead to false positive errors during subsequent cryptographic operations that happen to be on the same thread.

## Steps To Reproduce:

The following issues have reproduction cases:

https://github.com/nodejs/node/pull/45495
https://github.com/nodejs/node/pull/45377

Upon reviewing the code in crypto_x509.cc, at least one other function lacks use of ClearErrorOnReturn - X509Certificate::CheckPrivateKey.

https://github.com/nodejs/node/blob/main/src/crypto/crypto_x509.cc#L432

## Impact:

On our application, JWTs failed to sign after a certificate fails to verify on the same thread.

## Impact

If the server verifies certificates using Node's X509Certificate API, it may fail to sign other users' auth tokens: if a certificate fails to verify, the error from the previous failing call is applied to the next call that should succeed. It is worth auditing all OpenSSL entry points to see if they can cause errors to be raised.

## Attachments
No attachments
