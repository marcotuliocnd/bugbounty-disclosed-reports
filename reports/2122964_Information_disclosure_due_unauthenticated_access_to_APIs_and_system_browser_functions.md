# [███████] Information disclosure due unauthenticated access to APIs and system browser functions

## Report Details
- **Report ID**: 2122964
- **URL**: https://hackerone.com/reports/2122964
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-24T22:14:14.678Z
- **Disclosed**: 2023-11-03T17:18:54.176Z

## Reporter
- **Username**: h0w
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Multiple information exposure vulnerabilites were identified in a Jira Server instance (unauthenticated access to APIs and system browser functions). This report describes a combination of two separate vulnerabilities in two separate services This chain of vulnerabilities allows unauthenticated attacker to run arbitrary code on a server inside the company's internal network. the vulnerable registered as references JRASERVER-73060


## References
https://jira.atlassian.com/browse/JRASERVER-73060
https://nvd.nist.gov/vuln/detail/CVE-2020-14179

## Impact

Unauthorised access and the data should not be visible.
Project categories, resolutions, and usernames are listed even if the API is not authenticated

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers
CVE-2020-14179

## Steps to Reproduce
1. Navigate visit the target scope is https://█████████/secure/JiraCreditsPage!default.jspa
 1. And now we found a directory is jira sensitive
 1. Lets send a curl request to the `?maxResults=1000` endpoint, as shown below. In the request, point the post request to the server address you want to send the request to:

Here's the HTTP Parameter request that the issue:
```
GET /rest/menu/latest/admin HTTP/1.1
Host: ███
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
sec-ch-ua-platform: "Mac OS"
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
```
 * https://██████/secure/JiraCreditsPage!default.jspa
 * https://███████/rest/menu/latest/admin?maxResults=1000

## Suggested Mitigation/Remediation Actions
## Workaround
Anonymous access to endpoints listed below is restricted starting Jira 9.0. On future Jira 8.x releases and all LTS releases it is possible to restrict anonymous access with feature flags. On Jira 8.x to restrict anonymous access to the endpoint you need to disable feature flag aka provide `<feature.flag>`.disabled On Jira 9.0 you need to enable the same feature flag aka provide `<feature.flag>`.enabled


**You can use given feature flags: **
`/rest/api/2/projectCategory` - (Anonymous access disabled completely) 
`/rest/api/2/resolution` - (Anonymous access blocked only when there is no projects available for anonymous users) 
`/rest/menu/latest/admin` - There is currently no feature flag to disable anonymous access, please check linked ticket in "duplicates by" to track this problem.

**Refferences**
https://hackerone.com/reports/994612 
[JRASERVER-73060](https://jira.atlassian.com/browse/JRASERVER-73060)



## Attachments
No attachments
