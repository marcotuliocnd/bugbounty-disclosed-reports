# Constant-time comparison is not always implemented; critical areas are vulnerable to key-timing attacks

## Report Details
- **Report ID**: 363680
- **URL**: https://hackerone.com/reports/363680
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-06-09T08:51:57.047Z
- **Disclosed**: 2018-08-06T15:13:53.417Z

## Reporter
- **Username**: anonimal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
In my most superficial of reviews, constant-time comparison appears to not be globally implemented (at a glance, only implemented within the ref10 implementation).

With that said, the following areas either appear to be vulnerable, or are potentially vulnerable, to key-timing attacks:

1. Containers used for RingCT (in particular, the key struct) as deployed throughout RingCT
2. The definition and implementations of `CRYPTO_MAKE_COMPARABLE`
3. `equalKeys` in rctOps.cpp, whose comparison speed appears to be relative to its available hardware

For points 1 and 2, as a steadfast rule; do **NOT** use `memcmp` when comparing cryptographic secrets (or any cryptographic material for that matter). For point 3, be careful with conditional branches which can be optimized or subject to speculative execution. One possible fix for point 3 is to perform an XOR of all the bytes in both buffers, and then compare the result (see kovri below).

As the literature states, key timing vulnerabilities can range from somewhat-trivial to extremely-difficult to exploit. For this report, I cannot assess a difficulty. For an active attack, monero has a very simple yet friendly network layer which I *imagine* could make remote execution *somewhat* easier (depending on the context and application) but, I don't have PoC. Now, at the local level for, let's say, a malicious node that wants to forge X before sending to the next peer, the results could be easier to attain (again, no PoC).

This was only the most superficial of reviews - so please forgive any assumptions or inaccuracies on my part. If I had more time with this issue, I would love to look deeper in order to provide a more details and to assert a monero PoC. Unfortunately, I am too busy with kovri - but I hope that this report will at least raises awareness.

Mitigation:

- Use a function which provides constant-time comparison. For example, [kovri has a crypto++ solution](https://github.com/monero-project/kovri/issues/895) at its disposal.

## Impact

At first glance, a forged RingCT signature - but the extent of the problem could be possibly extended to other areas (to be determined).

## Attachments
No attachments
