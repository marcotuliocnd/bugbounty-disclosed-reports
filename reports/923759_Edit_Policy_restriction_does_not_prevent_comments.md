# Edit Policy restriction does not prevent comments.

## Report Details
- **Report ID**: 923759
- **URL**: https://hackerone.com/reports/923759
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-14T17:58:43.758Z
- **Disclosed**: 2020-07-17T17:14:06.076Z

## Reporter
- **Username**: rhinosf1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
- Change the edit policy of a Maniphest Task
- Attempt to comment on the the task with a user who doesn't have access

## Impact

Given a few users I spoke to believe restricting the edit policy blocks comments, This allows an underpriveleged user to gain access to carry out a restrcited action.

(Mongoose)

## Attachments
No attachments
