# Users with member privilege are able to see emails and membership information of other users

## Report Details
- **Report ID**: 244781
- **URL**: https://hackerone.com/reports/244781
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-30T16:08:40.549Z
- **Disclosed**: 2017-09-25T22:14:41.272Z

## Reporter
- **Username**: hackedbrain
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
**Description:** According to the rules of Leaderboard Teams only Owners and admins have access to other team members' personal information like email address, roles etc.

Users whose role set as "Member" can't see other users' details.

But through API it is possible for a user with member role to reveal personal information of all team members.

**Vulnerable URL: `https://wakatime.com/api/v1/users/current/leaderboards/<team_id>/members`**

**Steps to reproduce:**

1. Join a Leaderboard team as a member.
2. Copy the team id.
3. Visit the vulnerable url.

You'll find that emails of all members being disclosed.

## Attachments
No attachments
