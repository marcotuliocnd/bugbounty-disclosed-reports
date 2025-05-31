# Sensitive Information Disclosure Through Config File

## Report Details
- **Report ID**: 1397788
- **URL**: https://hackerone.com/reports/1397788
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-11-10T19:03:13.636Z
- **Disclosed**: 2022-09-01T20:50:48.872Z

## Reporter
- **Username**: dh0pe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
An attacker could gain access to sensitive information about usernames, encrypted passwords, internal IP addresses and configuration data of internal services.

## Steps To Reproduce:
- Go to https://zik.mtncameroon.net/common/queryconfig.action

## Remediation
Configure the application to not reveal sensitive information to client.

## References
https://cwe.mitre.org/data/definitions/200.html

## Impact

A malicious user is able to gain sensitive information usernames, encrypted passwords, internal IP addresses and configuration data of internal services.

## Attachments
No attachments
