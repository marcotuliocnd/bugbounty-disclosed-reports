# Attacker is able to access commit title and team member comments which are supposed to be private

## Report Details
- **Report ID**: 502593
- **URL**: https://hackerone.com/reports/502593
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-02-27T08:48:36.089Z
- **Disclosed**: 2019-07-03T17:05:17.620Z

## Reporter
- **Username**: yashrs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:** [add summary of the vulnerability]

**Description:** [add more details about this vulnerability]

## Steps To Reproduce:

To reproduce this vulnerability, we need two accounts, lets say those accounts are:
-> victim@gmail.com
-> attacker@gmail.com

- Create a project from account victim@gmail.com with the following permissions:
{F432203}
Note that the project visibility should be `internal`.

- Go to profile of `victim@gmail.com` from `attacker@gmail.com`  and subscribe to all events, like this:
{F432204}

- From victim account, comment on any commit, and you should receive it's notification on attacker@gmail.com, like this:
{F432207}

As you can see, the message of the commit, team members who commented, what the comment was, everything is visible from the email received. This shouldn't be sent via email because the settings selected for repository is 'Only Team Members' whereas attacker@gmail.com is not a team member.

I have tried my best to have perfect steps to reproduce this, still do tell me if you need more info :)

Thanks,
Yash :)

## Impact

An attacker will be able to view any commit titles, and all comments which shouldn't be visible to him using this vulnerability

## Attachments
- settings.PNG
- subscribe.PNG
- leaked.PNG
