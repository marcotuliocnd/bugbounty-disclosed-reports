# Account members can re-add themselve after has been deleted by administrator

## Report Details
- **Report ID**: 300881
- **URL**: https://hackerone.com/reports/300881
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-28T01:04:01.627Z
- **Disclosed**: 2018-05-03T18:36:50.342Z

## Reporter
- **Username**: tolo7010
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mavenlink

## Vulnerability Information
Reproduction:
=========

- As an administrator, invite an account members e.g: user1@email.com via https://app.mavenlink.com/settings/account/members 
- An invitation link sent to user1@email.com, as user1, open email inbox and click on the link, notice the link redirects to page url:
https://app.mavenlink.com/account_invitations/[token]/acceptances/new
- Note the above link.
- As user1, Click "Accept", the user has been added as an active member.
- As administrator, remove user1 from active member list.
- As user1, go to the noted link: https://app.mavenlink.com/account_invitations/[token]/acceptances/new,
and click "Accept", the user has been added to the group again.

## Impact

Any user can add himself after has been deleted from an administrator.

## Attachments
No attachments
