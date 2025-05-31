# curl successfully matches IP address literal in URL against IP address literal in certificate Common Name

## Report Details
- **Report ID**: 715413
- **URL**: https://hackerone.com/reports/715413
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-10-16T11:24:19.420Z
- **Disclosed**: 2021-01-08T09:18:29.536Z

## Reporter
- **Username**: lersek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
A user may invoke the curl command line utility with an IP address literal in the URL, such as

    https://192.168.124.2/...

If the HTTPS server presents a certificate whose Common Name matches this IP address literal as a *string* (that is, Common Name is the ASCII string `192.168.124.2`), then curl accepts the certificate (assuming it is properly signed by a trusted CA).

This is wrong. Per [RFC-2818, section *3.1.  Server Identity*](https://tools.ietf.org/html/rfc2818#section-3.1):

    In some cases, the URI is specified as an IP address rather than a
    hostname. In this case, the iPAddress subjectAltName must be present
    in the certificate and must exactly match the IP in the URI.

That is, if the user-specified URL contains an IPv4 or IPv6 address literal, then the server certificate may only match the URL if the certificate contains the same *numeric* IP address in the *SAN*, as a `GEN_IP` entry.

Curl should first attempt `X509_VERIFY_PARAM_set_ip_asc()`, and call `X509_VERIFY_PARAM_set1_host()` only if the former fails.

## Steps To Reproduce:

  1. Generate a new certificate request, for example with the [`genkey` utility](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-web_servers#s3-apache-mod_ssl-genkey), specifying the server's IPv4 or IPv6 address on the command line / in the Common Name field. (My `genkey` is from `crypto-utils-2.4.1-42.el7.x86_64`.)
  1. Sign the certificate request with a local CA such that `curl` trust the local CA.
  1. Configure Apache's `mod_ssl` such that it listen on the IPv4 or IPv6 address in question.
  1. Fetch an URI with curl from the web server, using the `https` scheme, and the IP address.
  1. Curl accepts the certificate.

## Supporting Material/References:
This issue with curl popped up while discussing the edk2 patch series mitigating CVE-2019-14553:

https://bugzilla.tianocore.org/show_bug.cgi?id=960
http://mid.mail-archive.com/20190927034441.3096-1-Jiaxin.wu@intel.com

## Impact

I'm not sure this problem can be used for an *attack*. It's just that string representations of IP addresses are not unique. URL to Subject Name matching should use canonical representations only.

## Attachments
No attachments
