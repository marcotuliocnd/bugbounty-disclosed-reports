# Security headers missed on https://acme-validation.jamieweb.net/

## Report Details
- **Report ID**: 500588
- **URL**: https://hackerone.com/reports/500588
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-24T21:33:45.456Z
- **Disclosed**: 2019-03-28T00:51:43.017Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: jamieweb

## Vulnerability Information
## Summary:
Hi JamieWeb team,
the `https://acme-validation.jamieweb.net/` domain doesn't present some important security headers.
The `X-DNS-Prefetch-Control` header isn't specified with value `off`, so is enabled b default on modern web browsers, and can lead to `information disclosure` ((https://security.stackexchange.com/questions/121796/what-security-implications-does-dns-prefetching-have). 
Additionally, the `X-Download-Options` isn't present, while a good security implication would be `noopen` (here is explained why is important in certain circumstances: https://github.com/Fyrd/caniuse/issues/3388). 
Finally, the `Public-Key-Pins header` isn't present. It is very helpful because tells to the web browser to associate a public key with a certain web server to prevent `MITM attacks` using `rogue and forged X.509 certificates`. This protects users in case a certificate authority is compromised. Is useful also for the validation of the `SSL` certificate.

## Steps To Reproduce:
  1. Add a `X-DNS-Prefetch-Control: off` header
  1. Add a `X-Download-Options: noopen` header
  1. Add a `Public-Key-Pins` header (for calculate its value follow the https://scotthelme.co.uk/hpkp-http-public-key-pinning/ article)

If you don't consider this a valid issue, let me know it and I'l autoclose by myself as N/A :)

## Impact

Some security headers missed can lead to prevention of certain attacks that can be exploited using reflected attacks in the local network either in remote contexts.

## Attachments
No attachments
