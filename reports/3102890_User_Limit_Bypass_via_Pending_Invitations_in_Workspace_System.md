# User Limit Bypass via Pending Invitations in Workspace System

## Report Details
- **Report ID**: 3102890
- **URL**: https://hackerone.com/reports/3102890
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-04-21T18:28:14.369Z
- **Disclosed**: 2025-04-29T10:21:07.278Z

## Reporter
- **Username**: qatada
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: dust

## Vulnerability Information
The platform enforces a limit of 3 users per workspace for low tier accounts unless you have higher subscription. However, this limit can be bypassed by inviting additional users ahead of time. As long as a user has a pending invitation, they are able to join the workspace simply by signing up and verifying their email — even if the workspace has already reached its user limit. This effectively allows an unlimited number of users to join a restricted workspace, bypassing plan restrictions and potentially impacting the platform’s revenue model.
it can also lead to inviting 100 user and they all can join, the admin wont need to get enterprise plan at all

Steps to Reproduce:

Create a workspace under a normal tier account. (i used Free Security Researchers account)
invite 3 users or any number you want
now go sign up with one of the users you invited and now you're in
then go back to your account and try to invite more, the website will tell you that the workspace reached its limit, you have to upgrade your subscription, however this is broken

go sign up with another email you invited, you will see that you joined the workspace

now i can invite 100 users and they can join easily because the limitation is broken, and btw to have 100 users in your workspace you need enterprise plan, this is a huge loss to the company

expected behavior : 
Once a workspace reaches the 3-user limit, no additional users should be allowed to join — even if they were previously invited. unless the admin get a higher subscription like the website said


███

## Impact

Enables circumvention of low-tier restrictions.
Allows unauthorized overuse of the platform.
Potential revenue loss, as users avoid upgrading to higher tiers.
Could be abused at scale by sending mass invites and onboarding users beyond allowed limits.

## Attachments
No attachments
