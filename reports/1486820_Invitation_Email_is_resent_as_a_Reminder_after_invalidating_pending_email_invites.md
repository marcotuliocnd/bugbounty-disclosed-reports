# Invitation Email is resent as a Reminder after invalidating pending email invites

## Report Details
- **Report ID**: 1486820
- **URL**: https://hackerone.com/reports/1486820
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-02-21T03:36:02.577Z
- **Disclosed**: 2022-04-19T11:37:01.653Z

## Reporter
- **Username**: mr_anksec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
Hello Team , I have found an issue through which unwanted users can be added to victim's workspace inside *.cloud.mattermost.com  .

So I have created an workspace with my email id , let's say email1 and invited email2 to my workspace . Email2 is not having an account at mattermost , So email2 will be a fresh account. But I noticed that there is no option present to cancel the invite . This will lead to the issue . Let's see this in detail -

Real life case - Suppose a victim has invited someone to the workspace by putting email id but later on victim decided to withdraw the email id but there is no such option present due to which attacker can now join the workspace which leads to info disclosure . Also victim can mistype the email while inviting but victim now can't withdraw that email invite.

Mitigation - There should be an option present to cancel the invite sent to any email.

Steps to reproduce -
1) create account at mattermost and then create a workspace for yourself inside -  *.cloud.mattermost.com
2) now invite email2 (email2 is not having account at mattermost) by invite option
3) now you will notice that there is no way present to cancel the invite
4) now email2 can easily join the workspace

## Impact

Unwanted users can join the workspace leading to information disclosure.

## Attachments
No attachments
