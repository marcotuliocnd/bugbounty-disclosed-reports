# node.js process aborts when processing x509 certs with invalid public key information

## Report Details
- **Report ID**: 1884159
- **URL**: https://hackerone.com/reports/1884159
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-23T02:30:33.281Z
- **Disclosed**: 2023-07-20T20:58:47.044Z

## Reporter
- **Username**: m_r_beauchamp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** 
The code for the CreateAsymmetric method in src/crypto/crypto_keys.cc: assumes that the certificate includes a valid public key. 
However, malicious actors could construct x509 certificates that can break this assumption. 

**Description:** 

When we run the attached reproducer, the node process aborts with the following message: 

 /usr/local/bin/node loadcert_poc.js
v18.14.2
valid:Feb 21 23:59:59 2015 GMT
/usr/local/bin/node[392068]: ../src/crypto/crypto_keys.cc:869:static std::shared_ptr<node::crypto::KeyObjectData> node::crypto::KeyObjectData::CreateAsymmetric(node::crypto::KeyType, const node::crypto::ManagedEVPPKey&): Assertion `pkey' failed.
 1: 0xb7b3f0 node::Abort() [/usr/local/bin/node]
 2: 0xb7b46e  [/usr/local/bin/node]
 3: 0xd11002 node::crypto::KeyObjectData::CreateAsymmetric(node::crypto::KeyType, node::crypto::ManagedEVPPKey const&) [/usr/local/bin/node]
 4: 0xd29626 node::crypto::X509Certificate::PublicKey(v8::FunctionCallbackInfo<v8::Value> const&) [/usr/local/bin/node]
 5: 0xdc12a0  [/usr/local/bin/node]
 6: 0xdc27df v8::internal::Builtin_HandleApiCall(int, unsigned long*, v8::internal::Isolate*) [/usr/local/bin/node]
 7: 0x1700679  [/usr/local/bin/node]
Aborted

Same outcome with 19.7.0

The CHECK(pkey) in method CreateAsymmetric [1] could be made more aware of the invalid state of the provided x509 certificate to gracefully handle the situation. 

std::shared_ptr<KeyObjectData> KeyObjectData::CreateAsymmetric(
    KeyType key_type,
    const ManagedEVPPKey& pkey) {
  ===> CHECK(pkey);
  return std::shared_ptr<KeyObjectData>(new KeyObjectData(key_type, pkey));
}

## Steps To Reproduce:
/usr/local/bin/node loadcert_poc.js 
v19.7.0
[1]
valid:Feb 21 23:59:59 2015 GMT
/usr/local/bin/node[4119272]: ../src/crypto/crypto_keys.cc:869:static std::shared_ptr<node::crypto::KeyObjectData> node::crypto::KeyObjectData::CreateAsymmetric(node::crypto::KeyType, const node::crypto::ManagedEVPPKey&): Assertion `pkey' failed.
[..]
Aborted

## Impact: 

There are various use cases where an application may want to access the public key info of a client-provided certificate. Developer may assume that the crypto code is safe to feed with arbitrary x509 material. 

## Supporting Material/References:

[1] https://github.com/nodejs/node/blob/5fad0b93667ffc6e4def52996b9529ac99b26319/src/crypto/crypto_keys.cc#L881

## Impact

The attacker could force interruptions of application processing, as the process terminates when accessing public key info of provided certificates from user code.  The current context of the users will be gone, and that will cause a DoS scenario, downtime, reputation and potential revenue loss.

## Attachments
- loadcert_poc.js
