# Certificate authentication re-use on redirect

## Report Details
- **Report ID**: 1563061
- **URL**: https://hackerone.com/reports/1563061
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-05-08T19:54:44.664Z
- **Disclosed**: 2022-05-11T06:48:43.113Z

## Reporter
- **Username**: nyymi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
Curl will reuse existing certificate for further TLS requests when following redirects. This is similar to `CVE 2022-27774` but with narrower impact, as the secret (private key) is not leaked.

## Steps To Reproduce:
  1. Configure a site (`targetsite.tld`) to require client certificates for authentication
  2. Have `client.crt` and `client.key` that can be used to access this site
  3.  Create an attacker controller site `https://evilsite.tld/something` that redirects to `https://targetsite.tld/secretfile`
  4. `curl -L --cert client.crt --key client.key https://evilsite.tld/something`
  5.  The redirect is followed and the secretfile content fetched

In effect the attacker can choose which content is accessed with the client certificate. This proof of concept is of course rather silly as one-liner curl command, but it still demonstrates the  inability of libcurl to restrict where key/cert are used. This scenario of course requires that the application in question can be passed attacker controlled URLs and that redirects are followed. If the attacker also wishes to obtain the secretfile response the application in question should be returning the file contents to the request to the attacker (lets assume attacker can pass URLs the app and gets the fetched content back as result).

Configuring client key/cert for arbitrary requests is unwise. However, since the common understanding is that the client certificate public key is "useless" to the attacker without the corresponding private key, it might happen that this (arguably silly) use pattern might exists. It is "harmless" after all...

 I believe that the key/cert should not used when following a redirect to a different protocol/host/port. This wouldn't prevent the minor leak of the `client.crt` to the attacker, but at least the attacker wouldn't get to choose which resources to access.

This is CWE-522: Insufficiently Protected Credentials

## Impact

The attacker can control which resource is accessed with the key/cert, and potentially gain unauthorised access to confidential information.

## Attachments
No attachments
