# ACME TLS-SNI-01/02 challenge vulnerable when combined with shared hosting providers

## Report Details
- **Report ID**: 304378
- **URL**: https://hackerone.com/reports/304378
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-01-12T21:42:47.027Z
- **Disclosed**: 2018-05-19T19:22:01.149Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The [ACME TLS-SNI-01](https://tools.ietf.org/html/draft-ietf-acme-acme-01#section-7.3) (and [TLS-SNI-02](https://tools.ietf.org/html/draft-ietf-acme-acme-09#section-8.4)) specification assumed wrong in terms of how current major cloud providers routed and validated domains. This was reported earlier this week to Let's Encrypt, and they decided to disable the method. Today Let's Encrypt decided to sunset both TLS-SNI-01 and TLS-SNI-02 due to the vulnerability I found. 

A full writeup of the finding and my side of the timeline can be found here:

* [How I exploited ACME TLS-SNI-01 issuing Let's Encrypt SSL-certs for any domain using shared hosting](https://labs.detectify.com/2018/01/12/how-i-exploited-acme-tls-sni-01-issuing-lets-encrypt-ssl-certs-for-any-domain-using-shared-hosting/)

Here is Let's Encrypt first and second announcement about the reported issue:

* [2018.01.09 Issue with TLS-SNI-01 and Shared Hosting Infrastructure](https://community.letsencrypt.org/t/2018-01-09-issue-with-tls-sni-01-and-shared-hosting-infrastructure/49996)
* [2018.01.11 Update Regarding ACME TLS-SNI and Shared Hosting Infrastructure](https://community.letsencrypt.org/t/2018-01-11-update-regarding-acme-tls-sni-and-shared-hosting-infrastructure/50188)

Regards,
Frans

## Impact

The ability to issue SSL-certificates for domains not under the attacker's control but served using the same shared hosting provider.

## Attachments
No attachments
