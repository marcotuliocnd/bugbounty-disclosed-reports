# Missing Certificate Authority Authorization rule

## Report Details
- **Report ID**: 261706
- **URL**: https://hackerone.com/reports/261706
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-20T11:06:01.195Z
- **Disclosed**: 2017-09-09T17:23:46.490Z

## Reporter
- **Username**: shiv_shakti
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Certificate Authority Authorization (supported by LetsEncrypt and other CAs) allows a domain owner to specify which Certificate Authorities should be allowed to issue certificates for the domain. All CAA-compliant certificate authorities should refuse to issue a certificate unless they are the CA of record for the target site. This helps reduce the threat of a bad guy tricking a Certificate Authority into issuing a phony certificate for your site.

The CAA rule is stored as a DNS resource record of type 257. You can view a domain’s CAA rule using a DNS lookup service:

https://dns.google.com/query?name=gratipay.com&type=257&dnssec=true

Gratipay should set a CAA record to help prevent misissuance of a certificate for its domains.

## Attachments
No attachments
