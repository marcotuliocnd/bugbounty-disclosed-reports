# Issue with VDP Program's Transition to Private Status and Missing Warning Labels on ORG Invitation

## Report Details
- **Report ID**: 2719622
- **URL**: https://hackerone.com/reports/2719622
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-09-16T10:07:29.721Z
- **Disclosed**: 2024-09-19T11:50:40.783Z

## Reporter
- **Username**: harshdranjan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hey Team,

Around 30 minutes ago, HackerOne made changes to how Vulnerability Disclosure Programs (VDPs) are handled. Previously, VDPs were treated as public programs, but they have now been converted into private programs without anything being revealed to the public. This means you can no longer directly visit HackerOne to check if a VDP program exists, which presents several issues.

Thus this report should be treated as a Valid issue now as when the old report was submitted the Program was public while it's private now, making it different from #2713956

HackerOne has recently introduced a feature allowing anyone to create a VDP (Vulnerability Disclosure Program) via: https://hackerone.com/vdp-sign-up
Since anyone can create a program, it will be quite similar to sandbox programs because HackerOne has not yet verified these programs and now they are treated as a private program 

Typically, invitations from unverified private programs will have the label:

==Warning: This team has not yet been verified by HackerOne. Please exercise caution when providing any sensitive information.==

However, for the user program, anyone can invite anyone into the program, but the recipient's email does not have the warning label, even though this is an unverified program by HackerOne.


### Steps To Reproduce

1. Create an account at: https://hackerone.com/vdp-sign-up
2. After creating the account, log in and go to: https://hackerone.com/organizations/team:handle/settings/users/invite
3. Invite any email address, and the recipient will receive an email without the warning label.

{F3605204}

### Optional: Supporting Material/References (Screenshots)

Warning labeled Private Program looks like :
{F3605203}

## Impact

Lack of warning label when receiving a letter

## Attachments
- Screenshot_(34).png
- Screenshot_(35).png
