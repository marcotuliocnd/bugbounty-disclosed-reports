# Missing Certificate Authority Authorization rule

## Report Details
- **Report ID**: 260928
- **URL**: https://hackerone.com/reports/260928
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-17T04:53:13.805Z
- **Disclosed**: 2017-09-09T17:23:54.834Z

## Reporter
- **Username**: gujjuboy10x00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hi Team,

# Summary

Certificate Authority Authorization (supported by LetsEncrypt and other CAs) allows a domain owner to specify which Certificate Authorities should be allowed to issue certificates for the domain. All CAA-compliant certificate authorities should refuse to issue a certificate unless they are the CA of record for the target site. This helps reduce the threat of a bad guy tricking a Certificate Authority into issuing a phony certificate for your site.

The CAA rule is stored as a DNS resource record of type 257. You can view a domain’s CAA rule using a DNS lookup service:

https://caatest.co.uk/gratipay.com

gratipay should set a CAA record to help prevent misissuance of a certificate for its domains.

https://hackerone.com/reports/129992

Thanks,
Vishal

## Attachments
No attachments
