# Privilege Escalation in BuddyPress core allows Moderate to Administrator 

## Report Details
- **Report ID**: 837018
- **URL**: https://hackerone.com/reports/837018
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-02T10:44:14.895Z
- **Disclosed**: 2020-05-22T00:31:34.282Z

## Reporter
- **Username**: hoangkien1020
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Description:

BuddyPress core allows Moderate to Administrator in Manage Group Members module

## Steps To Reproduce:

Step 1 : Create two account with two groups
Step 2 : In account A, create group abc with this two users.
Step 3 : Administrator in group abc promote account B to Moderator
Step 4 : In account B, create own group(without account A), only account B.
Step 5: In account B, access quick link here:
domain/groups/[group_name]/admin/manage-members/ 
Change your B's group.
There are  Edit | Ban | Remove for you to select. Focusing to admin(When you are admin, all thing belongs you).
Therefore, I select Edit. Change to Moderate(To capture this request)
Change such as here:
In POST method: 
POST /wp-json/buddypress/v1/groups/[group_A_id]/members/[id_user] HTTP/1.1
In body/data:
action=promote&role=admin
Note: change [group_A_id] to group you are moderator and [id_user]- your id
Step 6: Done, you are admin's group A. You can do anything.

Poc with video

## Recommendations
Valid user with their roles

## Impact

User will takeover group, do anything such as, edit roles,remove, ban, delelte group,..... (Perform as administrator)

## Attachments
- Privilege_Escalation_in_BuddyPress_core.mp4
