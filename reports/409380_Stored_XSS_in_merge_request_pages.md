# Stored XSS in merge request pages

## Report Details
- **Report ID**: 409380
- **URL**: https://hackerone.com/reports/409380
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-13T10:56:07.365Z
- **Disclosed**: 2018-12-03T22:15:49.225Z

## Reporter
- **Username**: 8ayac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:**
I found a Stored XSS in merge request pages. 

**Description:**
The exploit is via the parameter `merge_request[source_branch]` of the request to create a New Merge Request.

## Steps To Reproduce:
1. Sign ikn to GitLab.
2. Click the "[+]" icon.
3. Click "New Project".
4. Fill out "Project name" form with "test-project".
5. Check the radio button of "Public".
6. Check the "Initialize repository with a README".
7. Click "Create project" button.
8. Go to "http(s)://{GitLab host}/{user id}/test-project/branches/new".
9. Fill out each form as follows:
  - Branch name: test-branch
  - Create from: master
10. Click "Create branch" button.
11.  Go to "http://{GitLab host}/{user id}/test-project/merge_requests".
12. Click "Create merge request" button.
13. Click "Submit merge request" button.
14. Intercept the request.
15. Change the `merge_request[source_branch]` parameter's value to `<img/src=x onerror=alert(1)>`
16. Send the request.

Result: poc.png

Note: This behavior can be reproduced on all modern browsers.

## Impact

The security impact is the same as any typical Stored XSS.

Thank you.

## Attachments
- poc.png
