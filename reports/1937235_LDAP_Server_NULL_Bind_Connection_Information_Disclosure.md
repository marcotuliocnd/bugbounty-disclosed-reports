# LDAP Server NULL Bind Connection Information Disclosure

## Report Details
- **Report ID**: 1937235
- **URL**: https://hackerone.com/reports/1937235
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-04-06T18:14:09.423Z
- **Disclosed**: 2023-05-15T15:07:05.908Z

## Reporter
- **Username**: 0xmaruf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
The remote LDAP server allows anonymous access

## References
  - https://www.tenable.com/plugins/nessus/10723
  - https://ldap.com/ldapv3-wire-protocol-reference-bind

## Impact

information  disclosure

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. run $ `nmap -n -sV --script "ldap* and not brute" -p 389 ██████████`

check the response
## POC
██████

## Suggested Mitigation/Remediation Actions
Configure the service to disallow NULL BINDs.



## Attachments
No attachments
