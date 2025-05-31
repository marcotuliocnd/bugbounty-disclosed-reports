# Unauthorized user is able to access schedule pipeline variables and values

## Report Details
- **Report ID**: 962462
- **URL**: https://hackerone.com/reports/962462
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-08-19T16:08:55.229Z
- **Disclosed**: 2020-11-30T23:17:21.193Z

## Reporter
- **Username**: vaib25vicky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

The feature allows to add or overwrite variables that are passed to jobs  in order to modify the behavior just for that specific instance.
 
As per this https://gitlab.com/gitlab-org/gitlab-foss/-/issues/32568#note_32531510 , the current security model is
>If you are owner of schedule (as developer) or master => you can read, modify and delete,
If you are developer => you can just list, not read,

>This allows only owners and masters to read variables assigned to the schedule. It prevents other developers from hijacking schedules, but allows master to fully control them. Master already has access to Secret Variables.

But api endpoints are cleary showing this values to everyone even if the user is not part of the project. https://docs.gitlab.com/ee/api/pipeline_schedules.html#get-a-single-pipeline-schedule


### PoC

This is my test project https://gitlab.com/thevicc/trigg with schedule pipeline which custom variables you can't read.

Now, run this to read the variable and its value

`curl  --header "Private-Token: <your_access_token>"  https://gitlab.com/api/v4/projects/20618145/pipeline_schedules/69918`

Response
{F955402}

### Steps to reproduce

* Create a project and add a schedule pipeline with custom variables
*  Only you or owner can read variables
* As second account, use the api `https://docs.gitlab.com/ee/api/pipeline_schedules.html#get-a-single-pipeline-schedule`

## Impact

This bug allows unauthorized users to read scheduled pipeline custom variables and values. As per security model, this allows other devs to hijack schedules.

## Attachments
- poc_var.png
