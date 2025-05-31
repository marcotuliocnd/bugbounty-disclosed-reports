# Last pipeline status for MR leaked 

## Report Details
- **Report ID**: 582349
- **URL**: https://hackerone.com/reports/582349
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-05-16T12:09:57.979Z
- **Disclosed**: 2019-10-01T08:48:29.437Z

## Reporter
- **Username**: xanbanx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi GitLab security team,

### Summary

GitLab allows for public and internal projects to restrict the visibility of pipelines to project members only. Then, only project members should have access to the pipeline information. 

However, this can be bypassed. There is a internal endpoint (`:namespace/:project_name/merge_requests/:iid/pipeline_status`) on each merge request page allowing anyone with merge request access also view the last pipeline status for this merge request. 

### Steps to reproduce

1. Create a public project, disable public pipelines, and restrict the visibility of pipelines to project members only
2. Setup the repo such that there is a CI job, and create a merge request
3. As an unauthorized user, perform the following request in the browser: `https://example.gitlab.com/<namespace>/<project>/merge_requests/1/pipeline_status`. This will return a JSON response with a content similar to the one like this leaking the pipeline status:

```
{
    "icon": "status_running",
    "text": "running",
    "label": "running",
    "group": "running",
    "tooltip": "running",
    "has_details": false,
    "details_path": "/test-project/testproject/pipelines/37",
    "illustration": null,
    "favicon": "https://example.gitlab.com/assets/ci_favicons/favicon_status_running-9c635b2419a8e1ec991c993061b89cc5aefc0743bb238ecd0c381e7741a70e8c.png"
}
```

This information is only limited to project members only and thus is leaked to everyone with project and merge request access.

### Impact

Unauthorized users have access to the pipeline status of a merge request.

### What is the current *bug* behavior?

An unauthorized user can make this request and successfully can get information to attached pipelines.

### What is the expected *correct* behavior?

This request above should return 403 Forbidden, if the user does not have access to view pipelines.

### Output of checks

This happens on gitlab.com

Best regards,
Xanbanx

## Impact

Unauthorized users have access to the pipeline status of a merge request.

## Attachments
No attachments
