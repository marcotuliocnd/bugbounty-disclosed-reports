# Read-only user can delete higher privileged members using open DELETE /api/memberships/<membershipID> endpoint

## Report Details
- **Report ID**: 810320
- **URL**: https://hackerone.com/reports/810320
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-04T04:37:08.980Z
- **Disclosed**: 2020-06-29T21:25:08.722Z

## Reporter
- **Username**: chipped
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: helium

## Vulnerability Information
##Summary
The `/api/memberships/membershipID` endpoint on console.helium.com is open to anyone, including read-only users in an organization. This means that a read-only member can kick a manager, administrator, or even the owner out of an organization using this vulnerability. 

##Steps to Reproduce:
1. Create two accounts, user 1 (admin), user 2 (read-only member) with any organization name
2. You should already have the orgs set up, so for user 1, head over to the `Users` tab on the left
3. Click `Add User` on the right
4. Enter user 2's email (make sure their permission is read-only) and submit
5. Log in to user 2
6. Click **Switch** next to user 1's organization (should be at the home page)
7. Turn on burp or any proxy and start intercepting
8. Click on users on the left
9. Look for the GraphQL request with the operation name of **PaginatedMembershipsQuery**, this will list all memberships in that organization (including the ID, which is what we're looking for) {F736503}
10. Look for user 1's email and store the membership ID (`id`)
11. Now go to user 2 and switch back to **their** organization and add user 1 to that org (perms don't matter)
12. This will instantly add them to the user list without an invite
13. Start intercepting and delete them from the user list
14. Send the `DELETE /api/memberships/id` to repeater
15. Now put the membership ID you stored earlier and replace it with the current ID, this should then delete the membership {F736504}
16. Refresh the page for user 1, it will actually log them out as well with a 401 of `You don't have access to this organization`

This will remove any user from the organization. This is particularly dangerous if you want to take over an organization, except the only thing you can do is kick users out, the rest is still read-only. This is also possible for managers, they can remove administrators, which is more impactful since managers actually have permission within the org. So as a result, administrators wouldn't be able to supervise the hacker and he would have complete control over the organization.

## Impact

You can kick any user you want from an organization as long as you are a member.

## Attachments
- POC1.png
- POC2.png
