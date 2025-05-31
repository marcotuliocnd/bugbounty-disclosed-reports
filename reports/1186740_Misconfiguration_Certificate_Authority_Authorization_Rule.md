# Misconfiguration Certificate Authority Authorization Rule

## Report Details
- **Report ID**: 1186740
- **URL**: https://hackerone.com/reports/1186740
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-06T16:08:09.672Z
- **Disclosed**: 2021-12-09T19:49:18.159Z

## Reporter
- **Username**: d4rk_r0s3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Hello,Sifchain Security Team,
I found a bug called Missing CAA. Certificate Authority Authorization (supported by LetsEncrypt and other CAs) allows a domain owner to specify which Certificate Authorities should be allowed to issue certificates for the domain. All CAA-compliant certificate authorities should refuse to issue a certificate unless they are the CA of record for the target site. This helps reduce the threat of a bad guy tricking a Certificate Authority into issuing a phony certificate for your site. The CAA rule is stored as a DNS resource record of type 257. You can view a domain’s CAA rule using a DNS lookup service:
https://caatest.co.uk/sifchain.finance
Sifchain should set a CAA record to help prevent misissuance of a certificate for its domains.

## Impact

Impact:-
Domain Authority Can Be Takeover. If you need further information let me know

## Attachments
- 20210506_213332.jpg
