# Pending member invitations are not revoked on program name change

## Report Details
- **Report ID**: 275293
- **URL**: https://hackerone.com/reports/275293
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-10-07T05:47:43.291Z
- **Disclosed**: 2017-11-18T00:53:39.057Z

## Reporter
- **Username**: ashish_r_padelkar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
When private program updates the handle of the hackerone program, former **team members** can see the new updated handles using old invitation link.

The invitation link looks like `https://hackerone.com/invitations/<UID>`

This may also be true for participants participating in private programs but i can not confirm this yet. 

**Description (Include Impact):**
Former team members should not see the updated handle. Lets consider the example of `█████` private program which may have invited few team members and later removed them for some reason. The program was later acquired by `█████████` and handle was changed accordingly. But the former team members can still see this updated name as `██████████` using old invitation links. I verified this by changing my demo team handle from test account using hackerone support.

This may be possible for researchers too. when private program invites them, they also get invitation links. if researcher themselves quits the program or program decides to remove them for some reason, they can still use old invitation link which redirects to new updated handle.

### Steps To Reproduce

1. Using a private program, invite any team members to join your team 
2. Team member receives the invitation and he joins the program
3. Remove team member from your program and update the program handle with new name 
4. Now, team member can browse to old invitation link, which will redirect him to new updated handle in url (he will get 404 but still can see the handle in url)

Regards,
Ashish

## Attachments
No attachments
