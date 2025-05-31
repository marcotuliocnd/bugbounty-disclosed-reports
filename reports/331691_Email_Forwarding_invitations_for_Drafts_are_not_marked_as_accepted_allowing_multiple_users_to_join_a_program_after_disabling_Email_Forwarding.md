# Email Forwarding invitations for Drafts are not marked as accepted, allowing multiple users to join a program after disabling Email Forwarding

## Report Details
- **Report ID**: 331691
- **URL**: https://hackerone.com/reports/331691
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-03-31T23:35:36.633Z
- **Disclosed**: 2018-04-18T21:32:02.265Z

## Reporter
- **Username**: d4rk_g1rl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
###STEPS TO REPRODUCE:

1. I have found a sandboxed team in hackerone,named █████.
2. The manager of that team sends an invitation to: ██████████ ( which email was not exist on hackerone account)
3. Now the invitation link receive was ========> ████
4. I logged in from multiple researcher account and visited the link and accepted the request. 
5. Now the invitation link was still live.

So, a member  can pass this token to other people and they will be added to the team.I used this token multiple times and it's still live.

## Impact

The invitation token can be use in multiple times.

## Attachments
No attachments
