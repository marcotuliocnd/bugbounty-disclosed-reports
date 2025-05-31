# Revoked User can still view  the Merge Request  created by him via API

## Report Details
- **Report ID**: 962604
- **URL**: https://hackerone.com/reports/962604
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-19T17:56:38.867Z
- **Disclosed**: 2021-03-15T21:37:30.946Z

## Reporter
- **Username**: muthu_prakash
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

In Gitlab when a user is demoted to Guest role, the Guest user will not be able to view and edit the Merge requests in a project even if the merge request is created by him. But this check is not implemented in API so the Guest user will be able to the following actions for the Merge request which he don't have a permission.

Allowed Actions in API 

- Able to view the title and Description of the Merge Request via   /projects/:id/merge_requests/:merge_request_iid endpoint
- Get a list of merge request participants via /projects/:id/merge_requests/:merge_request_iid/participants
- Get a list of merge request commits via /projects/:id/merge_requests/:merge_request_iid/commits 
- Get  information about the merge request including its files and changes via /projects/:id/merge_requests/:merge_request_iid/changes
- Get a list of merge request pipelines via /projects/:id/merge_requests/:merge_request_iid/pipelines
- Create a TODO for that Merge Request via POST /projects/:id/merge_requests/:merge_request_iid/todo
- Get a list of merge request diff versions via /projects/:id/merge_requests/:merge_request_iid/versions
- Get Merge Request approvals status via /projects/:id/merge_requests/:merge_request_iid/approvals

### Steps to reproduce

1. Add a user a to a project with developer role.
2. From the Added user account create a Merge Request 
3. From Admin account demote to the user to Guest Role
4. From the Guest user account try to access the Merge request created by that user. (Merge Request tab will not be available for that user)
5. Now Create an access token from the Guest user account and try to access the Merge Request created by the user  by the above mentioned any one of the endpoints  (Notice you will be able to view  the Merge Request)

### Impact

Guest Role users have access to Merge Request data that he's not authorised to view and Edit

### What is the current *bug* behavior?

Guest Roles users have access to Merge Request data that he's not authorised to view and Edit via API

### What is the expected *correct* behavior?

Guest Roles users should be restricted  access to Merge Request  to view and Edit via API

### Output of checks

 This bug happens on GitLab.com

## Impact

Guest Role users have access to Merge Request data that he's not authorised to view and Edit

## Attachments
No attachments
