#  Bypass password confirmation via Context-dependent access control (CDCA)

## Report Details
- **Report ID**: 2120667
- **URL**: https://hackerone.com/reports/2120667
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-22T21:46:19.322Z
- **Disclosed**: 2024-01-17T08:26:39.469Z

## Reporter
- **Username**: st0nzyy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Hi Team,
After some testing in nextcloud server, i found  Context-dependent access control when i delete workflow at ``` /nextcloud/index.php/settings/user/workflow ``` the server ask for password confirmation but it can be bypassed if i directly request the delete endpoint.

CDCA is a security mechanism that restricts access to resources based on the context of the request. If CDCA is broken, an attacker can exploit this flaw to gain unauthorized access to resources. This can have serious consequences, such as data breaches, theft of credentials, and denial of service attacks.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

- go to /nextcloud/index.php/settings/user/workflow and create workflow.

{F2626834}

- now click on Delete button, the Password require for confirmation

{F2626842}

- A Broken Context-dependent access control happen when user can bypass password confirmation by send the folowing request 

``` DELETE /nextcloud/ocs/v2.php/apps/workflowengine/api/v1/workflows/user/3?format=json```

{F2626845}

- as you can see, user bypass password confirmation and the workflow succssufilly deleted.

{F2626858}

## Supporting Material/References:

https://www.geeksforgeeks.org/how-to-prevent-broken-access-control

## Impact

bypass password confirmation

delete workflow without password confirmation

## Attachments
- create-workflow.JPG
- require-password.JPG
- delete-endpoint.JPG
- workflow-deleted.JPG
