# Sensitive data exposure via /secure/QueryComponent!Default.jspa endpoint on ████████

## Report Details
- **Report ID**: 1278977
- **URL**: https://hackerone.com/reports/1278977
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-27T12:14:31.201Z
- **Disclosed**: 2022-04-29T14:03:34.013Z

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

It allows unauthenticated attackers like me to view custom field names and custom SLA names via an Information Disclosure vulnerability in the /secure/QueryComponent!Default.jspa endpoint.

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers
CVE-2020-14179

## Steps to Reproduce
1.  Open browser
    2. Hit endpoint */jira/secure/QueryComponent!Default.jspa* in the target
    3. Observe the results.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
