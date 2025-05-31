# Remote Code Execution on █████████

## Report Details
- **Report ID**: 962013
- **URL**: https://hackerone.com/reports/962013
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-08-19T04:07:49.260Z
- **Disclosed**: 2020-09-03T17:25:54.912Z

## Reporter
- **Username**: xy_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An unauth solr lead to RCE on ██████████

**Description:**
Hello, I found a solr unauth at https://██████/solr/

This version is 5.5.1, vulnerable with CVE-2019-0192 and CVE-2019-0193, i have try CVE-2019-0193 and successful RCE.

## Impact
Attacker can get shell on server.

## Step-by-step Reproduction Instructions

1. First go to Core Admin and copy path.
██████
2. Update the config.
███████
3. Execute code.
██████████

## Product, Version, and Configuration (If applicable)
Apache Sole 5.5.1
## Suggested Mitigation/Remediation Actions
Update to the latest version and set auth.

## Impact

Attacker can get shell on server.

## Attachments
No attachments
