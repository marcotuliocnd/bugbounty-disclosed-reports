# LDAP anonymous access enabled at certrep.pki.state.gov:389

## Report Details
- **Report ID**: 1869184
- **URL**: https://hackerone.com/reports/1869184
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-09T22:50:24.714Z
- **Disclosed**: 2023-05-11T21:04:38.541Z

## Reporter
- **Username**: 0xjackal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: us-department-of-state

## Vulnerability Information
## Summary:
Hi us-department-of-state Security Team.

I have found that this subdomain certrep.pki.state.gov Is vulnerable LDAP Anonymous access enabled as you can see in the following screenshots:-

██████████

███████

████████

## Steps To Reproduce:
1. Run nmap -n -Pn --script "ldap* and not brute" certrep.pki.state.gov
2. You can use ldapadmin tool as showing above at screenshots.

## Supporting Material/References:
- https://book.hacktricks.xyz/network-services-pentesting/pentesting-ldap
- https://hackerone.com/reports/205908

Please let me know if need more info.
Best Regards.
@doosec101

## Impact

Improper access to LDAP with anonymous login.

## Attachments
No attachments
