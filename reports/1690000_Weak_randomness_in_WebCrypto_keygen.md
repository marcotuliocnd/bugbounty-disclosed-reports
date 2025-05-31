# Weak randomness in WebCrypto keygen

## Report Details
- **Report ID**: 1690000
- **URL**: https://hackerone.com/reports/1690000
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-09-02T19:03:49.776Z
- **Disclosed**: 2022-10-26T08:18:10.825Z

## Reporter
- **Username**: bnoordhuis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
https://github.com/nodejs/node/pull/35093 introduced a call to `EntropySource()` in `SecretKeyGenTraits::DoKeyGen()` in `src/crypto/crypto_keygen.cc`. There are two problems with this:

1. It does not check the return value, it assumes `EntropySource()` always succeeds, but it can (and sometimes will) fail.

2. The random data returned by`EntropySource()` may not be cryptographically strong and therefore not suitable as keying material.

An example is a freshly booted system or a system without `/dev/random` or `getrandom(2)`.

## Impact

`EntropySource()` calls out to openssl's `RAND_poll()` and `RAND_bytes()` in a best-effort attempt to obtain random data.

OpenSSL has a built-in CSPRNG but that can fail to initialize, in which case it's possible either:

1. No random data gets written to the output buffer, i.e., the output is unmodified, or

2. Weak random data is written. It's theoretically possible for the output to be fully predictable because the CSPRNG starts from a predictable state.

The output buffer is allocated in `SecretKeyGenTraits::DoKeyGen()` using `OPENSSL_malloc()` (alias for `CRYPTO_malloc()`), which in turn calls `malloc()`.

`malloc()` does not zero the buffer but its contents may be predicted or manipulated by an external attacker, e.g. by manipulating an arraybuffer, then forcing the GC to reclaim it.

Users can override the CSPRNG (and do) so there are probably more failure modes. A buggy CSPRNG could write out only zeroes, for example, comparable to (2).

I have a (trivial!) patch available. H1 gives this a really high CVSS score but I suppose that's appropriate when the worst case failure mode is a complete breakdown of confidentiality and integrity.

## Attachments
No attachments
