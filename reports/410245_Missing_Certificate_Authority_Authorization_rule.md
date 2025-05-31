# Missing Certificate Authority Authorization rule

## Report Details
- **Report ID**: 410245
- **URL**: https://hackerone.com/reports/410245
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-09-16T06:34:51.908Z
- **Disclosed**: 2019-04-11T18:29:36.372Z

## Reporter
- **Username**: shiv_shakti
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Certificate Authority Authorization (supported by LetsEncrypt and other CAs) allows a domain owner to specify which Certificate Authorities should be allowed to issue certificates for the domain. All CAA-compliant certificate authorities should refuse to issue a certificate unless they are the CA of record for the target site. This helps reduce the threat of a bad guy tricking a Certificate Authority into issuing a phony certificate for your site.

The CAA rule is stored as a DNS resource record of type 257. You can view a domain’s CAA rule using a DNS lookup service:

https://dns.google.com/query?name=hacker101.com&type=257&dnssec=true

https://dns.google.com/query?name=ctf.hacker101.com&type=257&dnssec=true

hacker101 should set a CAA record to help prevent misissuance of a certificate for its domains.

Reference Report :  https://hackerone.com/reports/129992

## Impact

Misissuance of a certificate

## Attachments
No attachments
