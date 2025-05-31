# Node.js Certificate Verification Bypass via String Injection

## Report Details
- **Report ID**: 1429694
- **URL**: https://hackerone.com/reports/1429694
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-12-17T14:57:13.530Z
- **Disclosed**: 2022-02-10T01:26:57.782Z

## Reporter
- **Username**: bengl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
This is a report on behalf of Google, who did not want to report through H1.

---

**Summary**
Node’s APIs for reporting certificate fields are ambiguous and allow bypassing certificate verification in some circumstances.

**Details**
In light of CVE-2021-3712, I’ve been looking at code which misuses OpenSSL’s printing functions. Node’s use will cause it to misparse certificates, and, I believe, allows certificate verification bypasses in some circumstances, such as a name-constrained intermediate. It’s also just a generally unsafe pattern.

For background, the OpenSSL utility has options like openssl x509 -text which output some human-readable text representation of the certificate. This gives output like:

```
X509v3 Subject Alternative Name:  
  DNS:*.nodejs.org, DNS:nodejs.org
```

Certificates are not text. They use a structured binary encoding, called DER. Fields may contain commas, spaces, or any other byte. The text representation is just an ad-hoc diagnostic output by OpenSSL. It has no well-defined grammar and does not even escape characters, so the output is ambiguous. It should not be parsed.

OpenSSL has functions for the text format in the library itself. These are X509_print, i2v_GENERAL_NAME, X509V3_EXT_val_prn, X509V3_EXT_print, and others. But, these are still for diagnostics, not a well-defined serialization of the certificate.

Unfortunately, it looks like Node tries to parse this output to interpret the certificate itself:
https://github.com/nodejs/node/blob/95834d11a23b224f1abcc71a868d3cade4763717/src/crypto/crypto_x509.cc#L219
https://github.com/nodejs/node/blob/95834d11a23b224f1abcc71a868d3cade4763717/src/crypto/crypto_x509.cc#L229
https://github.com/nodejs/node/blob/95834d11a23b224f1abcc71a868d3cade4763717/src/crypto/crypto_common.h#L162
https://github.com/nodejs/node/blob/95834d11a23b224f1abcc71a868d3cade4763717/src/crypto/crypto_common.cc#L678
(Despite the name, SafeX509ExtPrint is not safe.)
https://github.com/nodejs/node/blob/95834d11a23b224f1abcc71a868d3cade4763717/lib/_tls_common.js#L133
https://github.com/nodejs/node/blob/95834d11a23b224f1abcc71a868d3cade4763717/lib/tls.js#L239

The last instance is especially concerning. If a certificate is issued for, say, "nodejs.org, DNS:blah.attacker.example", certificate issuance or verification may reason, “this has .attacker.example as a suffix, which you own, so this certificate is fine”. Meanwhile, Node sees a text output of "DNS:nodejs.org, DNS:blah.attacker.example" and misinterprets it as two names, one of which is nodejs.org. Concretely, this may happen if a CA issues a name-constrained intermediate certificate to attacker.example. OpenSSL performs the name constraint check against the correct parse, then Node misinterprets the certificate and bypasses the name constraint.

This is similar to the old null prefix attack from 11 years ago. Other SAN types may also be injection vectors.

Additionally, as this is not the intended use, OpenSSL’s print functions receive less attention than other parts of their X.509 stack. Indeed not mentioned in the CVE-2021-3712 advisory is that the print functions silently truncated their outputs on interior NUL bytes. That makes uses like Node’s vulnerable to exactly the old null prefix attack from 11 years ago. (The GEN_DNS special case in SafeX509ExtPrint avoids it for DNS SANs, but other SAN types are still truncated.)

Instead, Node should look at the GENERAL_NAME, etc., structure, which will give you the actual fields unambiguously, or call into the high-level OpenSSL functions that check hostnames.

**Recommendations**
This is part of Node’s public API, so the fix may be tricky. Here is a rough roadmap:

First, change the private C++/JavaScript interface for subjectaltname and infoAccess from OpenSSL print functions to structured JavaScript objects. Walk the actual structs, rather than using the print functions. I can help review this, as may not be obvious what fields you need, or what checks OpenSSL has (or, usually, hasn’t) done on the expected character encoding.

You’ll need to decide how to represent IPv6 addresses. Node seems to typically use uv_inet_ntop, but I think the old OpenSSL format was slightly different. I don’t know what you expect from your public API.

With that done, delete GetInfoString andSafeX509ExtPrint. To prevent future copy-and-paste mishaps, there should be _no_ references to the print functions remaining.

Next, decide what to do with the public API. I assume you cannot remove these:
https://nodejs.org/api/crypto.html#crypto_x509_subjectaltname
https://nodejs.org/api/crypto.html#crypto_x509_infoaccess
https://nodejs.org/api/tls.html#tls_certificate_object
(Odd that infoAccess is in a different format between the two modules.)

Instead, document an actual format for these, based on the ad-hoc OpenSSL output you were picking up. To avoid injection attacks in downstream code, have the internal JavaScript logic strip out entries with characters like commas or spaces. Update the documentation to describe how callers can safely parse these strings.

Optionally, you all may wish to define a more structured API and deprecate the old ones.

**Additional instances**
There are some more instances of the printing APIs, that also need to be fixed.

GetCertificateAltNames and GetCertificateCN, seem unused and should just be deleted. GetCertificateAltNames is not suitable as reference for future code and should be removed.
https://github.com/nodejs/node/blob/95834d11a23b224f1abcc71a868d3cade4763717/src/crypto/crypto_common.cc#L136

Next the issuer and subject names are reported via X509_NAME_print_ex and parsed back out:
https://github.com/nodejs/node/blob/95834d11a23b224f1abcc71a868d3cade4763717/src/crypto/crypto_common.cc#L718
https://github.com/nodejs/node/blob/95834d11a23b224f1abcc71a868d3cade4763717/lib/_tls_common.js#L133
https://github.com/nodejs/node/blob/95834d11a23b224f1abcc71a868d3cade4763717/lib/internal/tls/parse-cert-string.js#L15

Unlike the other print functions, there is a defined text form of X.509 names in RFC 2253. However, I have not carefully analyzed OpenSSL’s RFC 2253 implementation to see if it always produces unambiguous output. Moreover, Node is not correctly parsing RFC 2253. There are quoting and escaping mechanisms. The newline separator is also not the usual one. There is probably a similar injection bug lurking here. For instance, in the CA/B Forum BRs, the OU field is not quite yet sunset. The OU field is largely unverified beyond not containing trademarks/company names, so it may be an injection vector in even a trusted CA. This also needs to be switched to something structured, or at least well-defined.

That said, extracting DNS names from the subject common name, as opposed to the SAN list, is outdated anyway. Browsers do not do it anymore, and the IETF is updating the specifications to match. Consider removing it from checkServerIdentity.
https://github.com/nodejs/node/blob/95834d11a23b224f1abcc71a868d3cade4763717/lib/tls.js#L281

Disclosure Timeline: We are privately disclosing this vulnerability to you so that you can develop a fix and manage its rollout. We do not require you to keep any information of this report secret, but if you make it public then please let us know that you did. This advisory will be kept private by Google for 30 days after a fix is publicly available or after 90 days if no fix is made. After this deadline we plan to disclose this advisory in full at: https://github.com/google/security-research/. Please read more details about this policy here: https://g.co/appsecurity

---

In putting that together, I found another bug, also in the repro: Node accepts URI SANs as a substitute for DNS name verification. Accepting random SAN types is not actually safe. Name constraints in X.509 are defined weirdly and do not actually constrain unrelated SAN types. That means, unless your PKI is specifically defined to use a particular SAN type, it is not safe to consume it, or you'll bypass name-constrained intermediates. (Arguably name constraints shouldn't have worked this way. Alas, they are what they are, which means the Node behavior is wrong.)

## Impact

See above.

## Attachments
No attachments
