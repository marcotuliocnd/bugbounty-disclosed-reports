# Persistent XSS - Selecting users as allowed merge request approvers

## Report Details
- **Report ID**: 346217
- **URL**: https://hackerone.com/reports/346217
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-01T19:54:11.493Z
- **Disclosed**: 2018-07-16T17:19:23.297Z

## Reporter
- **Username**: phillycheeze
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:**
When using the dropdown that selects the users that are allowed to approve a merge request, it is possible to trigger a XSS with a malicious user name string.

**Description:**
This vulnerability is similar to the recently announced CVE-2018-10379 (and another vulnerability I recently reported here in hackerone).

The steps to reproduce are fairly simple but there are some restrictions:

  *  Only members of a project with Master access are able to become victims of the XSS
  *  Only groups/members with a subscription level of Starter or higher are able to perform the XSS. This is a premium feature only allowed at Starter or higher. (https://gitlab.com/help/user/project/merge_requests/merge_request_approvals)

## Steps To Reproduce:

  1. Set your own username as "<img src=x onerror=alert(document.domain)> foo / bar"
  1. Make yourself have at least Master access to a project
  1. Under Project Settings -> General -> Merge Request Settings,click the "Merge request approvals" checkbox
  1. Select the user dropdown input for selecting eligible users to approve merge requests
  1. Notice that the onerror attribute from the username renders.

## Supporting Material/References:

More information can be provided upon request.

## Suggested Remediation

Like the previous report I submitted, it is due to improper sanitization in a JS file.  I believe this is the offending line: https://gitlab.com/gitlab-org/gitlab-ee/blob/master/ee/app/assets/javascripts/approvers_select.js#L134

## Impact

The security impact is the same as any typical persistent xss.

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://gitlab.com/group/project/edit

**Verified**
Yes



## Attachments
No attachments
