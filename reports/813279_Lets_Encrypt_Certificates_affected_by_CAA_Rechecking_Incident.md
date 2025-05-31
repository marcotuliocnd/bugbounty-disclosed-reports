# Lets Encrypt Certificates affected by CAA Rechecking Incident

## Report Details
- **Report ID**: 813279
- **URL**: https://hackerone.com/reports/813279
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-08T19:55:54.507Z
- **Disclosed**: 2020-04-01T12:38:47.167Z

## Reporter
- **Username**: pr3r00t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: endless_group

## Vulnerability Information
## Summary:
Lets encrypt released a statement regarding 3 million certificates being revoked due to a issue in the CA signing process, Looking at your subdomains it appears that you are affected by this incident. When the revoking occurs the certificates the certificates are no longer valid. This may affect automatic flows that use these sites and assume the certificates are valid and have no cert error checking. 

## Steps To Reproduce:

root@Bugslife:~/Desktop/endlesshosting# curl -XPOST -d 'fqdn=support.theendlessweb.com' https://checkhost.unboundtest.com/checkhost
The certificate currently available on support.theendlessweb.com needs renewal because it is affected by the Let's Encrypt CAA rechecking problem. Its serial number is 03a7c9ab7ac09b9e1f8772c181c584bff432. See your ACME client documentation for instructions on how to renew a certificate.

root@Bugslife:~/Desktop/endlesshosting# curl -XPOST -d 'fqdn=jira.theendlessweb.com' https://checkhost.unboundtest.com/checkhost
The certificate currently available on jira.theendlessweb.com needs renewal because it is affected by the Let's Encrypt CAA rechecking problem. Its serial number is 03a7c9ab7ac09b9e1f8772c181c584bff432. See your ACME client documentation for instructions on how to renew a certificate.

## Supporting Material/References:
https://letsencrypt.org/caaproblem/
https://threatpost.com/lets-encrypt-revoke-millions-tls-certs/153413/

## Impact

This may affect automatic flows that use these sites and assume the certificates are valid and have no cert error checking. 
As the certificates will no longer be valid this could aid in a successful phishing attack

## Attachments
- lets-encrypt-revoke-list.png
