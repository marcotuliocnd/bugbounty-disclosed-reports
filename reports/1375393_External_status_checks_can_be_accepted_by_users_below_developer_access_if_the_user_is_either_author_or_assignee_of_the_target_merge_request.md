# "External status checks" can be accepted by users below developer access if the user is either author or assignee of the target merge request

## Report Details
- **Report ID**: 1375393
- **URL**: https://hackerone.com/reports/1375393
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-10-20T07:03:56.531Z
- **Disclosed**: 2022-06-08T14:04:26.012Z

## Reporter
- **Username**: joaxcar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Any user who is either author or assignee of a merge request can approve that merge request's `external status checks`. This includes users with `Guest` access that creates MR's either through email or through a fork of the project. It also includes users with `Guest` or `Reporter` access getting assigned to an MR, which is not uncommon in public projects.

There exists a tiny overlap with my report [1375376](https://hackerone.com/reports/1375376) which is yet not triaged. I describe this overlap in the end of this summary. The reports look similar, but the vulnerabilities are not related. A fix in 1375376 would not fix this report, only the overlap.

The `external status check` documentation does not offer too much information about how the feature is supposed to function. But the developer discussions and the unit tests suggests that approving an `external status check` should be restricted for users with at least `Developer` access in the project. Here is the issue tracking the development https://gitlab.com/gitlab-org/gitlab/-/issues/267519

In this [thread](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/59137#note_567776066) the possibility of users abusing the fact that a status check is not tied to any special token. Rather they use regular PAT's, these discussion mentions

> find_merge_request_with_access will at least mean that only those with developer+ access to the project in question would be able to exploit the feature in this way.

The [unit tests](https://gitlab.com/gitlab-org/gitlab/-/blob/master/ee/spec/requests/api/status_checks_spec.rb#L29) for this feature checks this assumption with these lines

```
describe 'permissions' do
    before do
      stub_licensed_features(external_status_checks: true)
    end

    it { expect { subject }.to be_allowed_for(:maintainer).of(project) }
    it { expect { subject }.to be_allowed_for(:developer).of(project) }
    it { expect { subject }.to be_denied_for(:reporter).of(project) }
  end
```

Validating if the user making the request is developer+.

So to enforce this they have put an authentication block checking if the user have permission to respond to `external status checks` using the function called `find_merge_request_with_access` in this way
```
merge_request = find_merge_request_with_access(params[:merge_request_iid], :approve_merge_request)
```
Checking the permission `:approve_merge_request` which is enabled for developers. But as it turns out, this permission is also enabled for users with the permission `:update_merge_request`. In https://gitlab.com/gitlab-org/gitlab/-/blob/master/app/policies/merge_request_policy.rb there is this rule

```
 rule { can?(:update_merge_request) }.policy do
    enable :approve_merge_request
  end
```
That enables the permission for anyone that are allowed to update the MR. And in https://gitlab.com/gitlab-org/gitlab/-/blob/master/app/policies/issuable_policy.rb there exists this rule

```
rule { can?(:guest_access) & assignee_or_author }.policy do
    enable :read_issue
    enable :update_issue
    enable :reopen_issue
    enable :read_merge_request
    enable :update_merge_request
    enable :reopen_merge_request
  end
```
enabling `:update_merge_request` for anyone that have `:guest_access` and is either assignee or author.

This is probably the root of the problem. And as far as I could make out this is not the intended behavior. A user with `Guest` access can create an MR by forking and directly send approval for all `external status checks` to lure the developers that the MR have been checked. It leads to at least two problems:

* A user with no membership can create a MR in a public project and then "approve" the `external status check's without any membership
* A user who is demoted to `Reporter` in a private project can still "approve" `external status check's in MR's where the user is either author or assignee

and at the moment thanks to the vulnerability that I have reported in [1375376](https://hackerone.com/reports/1375376) at present it is also possible to:
* A user who is demoted to `Guest` in a private project can still "approve" `external status check's in MR's where the user is either author or assignee while not being able to actually view the MR

### Steps to reproduce

External status checks is an `Ultimate` feature, so make sure the project is created in such an environment

1. Create two users `owner01` and `guest01`
2. Log in as `owner01` and create a public project `project01` by visiting https://gitlab.com/projects/new#blank_project and take a note of the project ID
3. Go to the project settings page and expand the tab `merge requests` and scroll down to `external status checks`, settings page https://gitlab.com/owner01/project01/edit
4. Create a status check with any name and endpoint, and leave the 
5. Log out and log in as `guest01`
6. Go to the project page https://gitlab.com/owner01/project01 and create a fork with the `fork` button, call it `fork01`.
7. When the fork is created, create a new branch in the fork https://gitlab.com/guest01/fork01/-/branches/new called `new_branch`
8. When the fork is created directly click on the option "create a merge request", in the "New merge request" page click `Change branches` and select the target branch as any branch on the original `project01`
9. Click "Create" and a new MR should be created in `project01` (this is a guest contribution and a normal open-source flow, but note that the `guest01` user is NOT a member of `project01`)
10. Go to https://gitlab.com/-/profile/personal_access_tokens and create an access token for the API for `guest01`
11. Open a terminal and make this request to get the ID of the status check (user `project01` ID and MR IID which is probably 1 and `guest01` token), take a note of the returned ID of the status check
```
curl "https://gitlab.███/api/v4/projects/<PROJECT_ID>/merge_requests/<MR_IID>/status_checks" -H "Authorization: Bearer <TOKEN>"
```
12. Send this request to check for the SHA, the request will fail with a message telling you which SHA to use, in this request we use a dummy SHA=a (make sure to also replace CHECK_ID to the found ID from step 12)
```
curl --request POST \
  --url 'https://gitlab.com/api/v4/projects/<PROJECT_ID>/merge_requests/<MR_IID>/status_check_responses?sha=a&external_status_check_id=<CHECK_ID>' \
  --header 'Authorization: Bearer <TOKEN>'
```
13. Now use the returned SHA in this request to finally "approve" the status check for the MR
```
curl --request POST \
  --url 'https://gitlab.domain.com/api/v4/projects/<PROJECT_ID>/merge_requests/<MR_IID>/status_check_responses?sha=<SHA>&external_status_check_id=<CHECK_ID>' \
  --header 'Authorization: Bearer <TOKEN>'
```
14. Go to the MR page and verify that the status check is now green and checked, https://gitlab.com/owner01/project01/-/merge_requests/1

### Impact

A `Guest` user can send acknowledge messages to "approve" `external status checks` on MR's where the user is either author or assignee. This makes it possible for a malicious user to "spoof" acceptance of MR's in projects where the user should not be able to do this. In public projects this mean that any guest contribution from non-members can have its `external status checks` checked by the author itself even if not a member of the project.

### What is the current *bug* behavior?

Users with access level below `Developer` can accept `external status checks` if they are either author or assignee of the MR

### What is the expected *correct* behavior?

Only `Developer`+ users that are members of the project should be able to user their PAT to "approve" the `external status check`

### Output of checks

This bug happens on GitLab.com

## Impact

A `Guest` (or `Reporter`) user can send acknowledge messages to "approve" `external status checks` on MR's where the user is either author or assignee. This makes it possible for a malicious user to "spoof" acceptance of MR's in projects where the user should not be able to do this. In public projects this mean that any guest contribution from non-members can have its `external status checks` checked by the author itself even if not a member of the project.

## Attachments
No attachments
