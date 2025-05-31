# Sensitive data exposure via /secure/███████ endpoint on ████████

## Report Details
- **Report ID**: 1278952
- **URL**: https://hackerone.com/reports/1278952
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-27T12:05:41.854Z
- **Disclosed**: 2024-12-18T19:49:30.332Z

## Reporter
- **Username**: njmulsqb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Hi,

While going through the testing of DoD assets, I have came across a subdomain that is vulnerable to CVE-2020-14179. Some of the internal fields that are exposed are Project, Status, Limits, Creator, Query, Created Date, Updated Date, Resolution Date, etc. 

## References
https://jira.atlassian.com/browse/JRASERVER-71536
https://www.cvedetails.com/cve/CVE-2020-14179

## Impact

It allows unauthenticated attackers like me to view custom field names and custom SLA names via an Information Disclosure vulnerability in the /secure/████████ endpoint.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers
CVE-2020-14179

## Steps to Reproduce
1. Open browser
2. Hit endpoint * /jira/secure/██████████* in the target
3. Observe the results.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
