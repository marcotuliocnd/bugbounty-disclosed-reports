# Improper access control for users with expired password, giving the user full access through API and Git

## Report Details
- **Report ID**: 1285226
- **URL**: https://hackerone.com/reports/1285226
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-30T23:05:58.300Z
- **Disclosed**: 2022-01-27T08:22:06.187Z

## Reporter
- **Username**: joaxcar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Users with an "expired password" can still access the full API with tokens. This includes the REST API, GraphQL API and Git HTTP access. The same issue was mitigated in [13.12.2](https://about.gitlab.com/releases/2021/06/01/security-release-gitlab-13-12-2-released/#insufficient-expired-password-validation) as "Insufficient Expired Password Validation". That patch blocked users with expired passwords from accessing the REST API. My report [1192460](https://hackerone.com/reports/1192460) led to a patch [14.0.2](https://about.gitlab.com/releases/2021/07/01/security-release-gitlab-14-0-2-released/#a-deactivated-user-can-access-data-through-graphql) that also blocked access through GraphQL.

It seems that these patches caused some problem for users accessing GitLab instances using LDAP. And a [merge request](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/63466) trying to address this problem got merged in one of the latests releases. Unfortenetly this new "fix for LDAP" also seems to have opened up access for regular user accounts with expired passwords again.

__Images showing access through REST, GraphQL and Git with a account with expired password:__

{F1394654}

{F1394656}

{F1394657}

### Steps to reproduce
(tested on 14.1.0 self-hosted)

1. Create a user user01, and log in
2. Create a new project at https://gitlab.domain.com/projects/new#blank_project make sure to put it as `private`. Take a note of the ID of the project
3. Go to https://gitlab.domain.com/-/profile/personal_access_tokens and create a personal access token
4. Log in as an administrator
5. Go to the admin page for editing the user https://gitlab.domain.com/admin/users/user01/edit and change the users password. This triggers `password expired at` to be set to the current time. Effectively putting the user01 in the state of "expired password""
6. Trying to log in as user01 with old password will now fail, using the new password will trigger "enter a new password" page. __Do not enter a new password here as this will put the user in a unexpired state again__

{F1394655}

7. Now instead try to use the user01 token from step 2 in a REST request such as
```
curl --request GET \
  --url https://gitlab.domain.com/api/v4/projects/:ID \
  --header 'Authorization: Bearer <TOKEN>' \
```
This should show the `private` project that should not be accessible.

### Impact

A user that should not have access to the instance as the password has expired can still access the API and Git with tokens.

### What is the current *bug* behavior?

Requests to the API and Git is not blocked for users with expired password

### What is the expected *correct* behavior?

Requests to the API and Git by users with expired password should be blocked and presented with a message like `403 Forbidden - Your password expired. Please access GitLab from a web browser to update your password.` as before.

## Impact

Users with expired passwords can still access the full API and Git using tokens

## Attachments
- git.png
- block.png
- graph.png
- rest.png
