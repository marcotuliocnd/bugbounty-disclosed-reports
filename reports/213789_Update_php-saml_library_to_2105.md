# Update php-saml library to 2.10.5

## Report Details
- **Report ID**: 213789
- **URL**: https://hackerone.com/reports/213789
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-15T21:18:16.108Z
- **Disclosed**: 2017-04-27T22:48:04.894Z

## Reporter
- **Username**: lukasreschke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The php-saml library as used by our SSO implementation had a minor security patch in 2.10.4 as per https://github.com/onelogin/php-saml/commit/949359f5cad5e1d085c4e5447d9aa8f49a6e82a1.  So we should update this in our next minor releases.

> Security update for signature validation on LogoutRequest/LogoutResponse.
>
> In order to verify Signatures on Logoutrequests and LogoutResponses we use
> the verifySignature of the class XMLSecurityKey from the xmlseclibs library.
> That method end up calling openssl_verify() depending on the signature algorithm used.
> 
> The openssl_verify() function returns 1 when the signature was successfully verified,
> 0 if it failed to verify with the given key, and -1 in case an error occurs.
> PHP allows translating numerical values to boolean implicitly, with the following correspondences:
> - 0 equals false.
> - Non-zero equals true.
> 
> This means that an implicit conversion to boolean of the values returned by openssl_verify()
> will convert an error state, signaled by the value -1, to a successful verification of the
> signature (represented by the boolean true).
> 
> The LogoutRequest/LogoutResponse signature validator was performing an implicit conversion > to boolean
> of the values returned by the verify() method, which subsequently will return the same output
> as openssl_verify() under most circumstances.
> This means an error during signature verification is treated as a successful verification by the  method.
>
> Since the signature validation of SAMLResponses were not affected, the impact of this security
vulnerability is lower, but an update of the php-saml toolkit is recommended.

## Attachments
No attachments
