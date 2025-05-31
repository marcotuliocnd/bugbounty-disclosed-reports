# [U.S. Air Force] Information disclosure due unauthenticated access to APIs and system browser functions

## Report Details
- **Report ID**: 1822160
- **URL**: https://hackerone.com/reports/1822160
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-04T15:20:22.626Z
- **Disclosed**: 2023-01-27T18:40:37.316Z

## Reporter
- **Username**: hackeronanywhere
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Multiple information exposure vulnerabilites were identified in a Jira Server instance (unauthenticated access to APIs and system browser functions). This report describes a combination of two separate vulnerabilities in two separate services This chain of vulnerabilities allows unauthenticated attacker to run arbitrary code on a server inside the company's internal network. the vulnerable registered as references [JRASERVER-73060](https://jira.atlassian.com/browse/JRASERVER-73060)

## References
https://jira.atlassian.com/browse/JRASERVER-73060
https://nvd.nist.gov/vuln/detail/CVE-2020-14179

## Impact

Unauthorised access and the data should not be visible.
Project categories, resolutions, and usernames are listed even if the API is not authenticated

## System Host(s)
███

## Affected Product(s) and Version(s)
https://██████/rest/menu/latest/admin

## CVE Numbers
CVE-2020-14179

## Steps to Reproduce
1. Navigate visit the target scope is https://████//rest/menu/latest/admin
 1. And now we found a directory is jira sensitive
 1. You can used recon-tool for finding sensitive directory
 1. Lets send a curl request to the **`?maxResults=1000`** endpoint, as shown below. In the request, point the post request to the server address you want to send the request to:

Here's the HTTP Parameter request that the issue:
```
GET /rest/api/2/projectCategory?maxResults=1000 HTTP/1.1
Host: ████████
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"
Accept: application/json, text/plain, */*
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
sec-ch-ua-platform: "Mac OS"
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Language: en-US,en;q=0.9,fi;q=0.8
```
```js
{
      "self":"https://█████/rest/api/2/projectCategory/10000",
      "id":"10000",
      "description":"Used by the broader DoD/IC for collaborative development.",
      "name":"Community Collaboration"
   }
][
   {
      "key":"admin",
      "link":"https://█████████/secure/project/BrowseProjects.jspa?s=view_projects",
      "label":"Jira administration",
      "tooltip":"",
      "local":true,
      "self":true,
      "applicationType":"jira"
   },
   {
      "key":"admin",
      "link":"https://████████/admin/console.action",
      "label":"Confluence administration",
      "tooltip":"",
      "local":false,
      "self":false,
      "applicationType":"confluence"
   }
```
 * https://█████/rest/menu/latest/admin?maxResults=1000
 * https://██████/rest/api/2/projectCategory?maxResults=1000
 * https://███/rest/api/2/resolution?maxResults=1000

## Suggested Mitigation/Remediation Actions
Anonymous access to endpoints listed below is restricted starting Jira 9.0. On future Jira 8.x releases and all LTS releases it is possible to restrict anonymous access with feature flags. On Jira 8.x to restrict anonymous access to the endpoint you need to disable feature flag aka provide `<feature.flag>`.disabled On Jira 9.0 you need to enable the same feature flag aka provide `<feature.flag>`.enabled

>
You can use given feature flags: 
`/rest/api/2/projectCategory` - (Anonymous access disabled completely) 
`/rest/api/2/resolution` - (Anonymous access blocked only when there is no projects available for anonymous users) 
`/rest/menu/latest/admin` - There is currently no feature flag to disable anonymous access, please check linked ticket in "duplicates by" to track this problem.



## Attachments
No attachments
