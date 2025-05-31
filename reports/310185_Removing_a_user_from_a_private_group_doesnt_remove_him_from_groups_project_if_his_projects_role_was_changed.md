# Removing a user from a private group doesn't remove him from group's project, if his project's role was changed

## Report Details
- **Report ID**: 310185
- **URL**: https://hackerone.com/reports/310185
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-29T16:09:39.604Z
- **Disclosed**: 2019-04-05T21:49:34.894Z

## Reporter
- **Username**: rpadovani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:**
(a) *rogue* user is added to a private group with dozen of projects
(b) The role in some projects is changed for the *rogue* user
(c) *rogue* is fired, and removed from the group: he still has access to projects where his role was changed

**Description:** 

the (b) can happen for a lot of different reasons:
- *rogue* is added as master - knowing this vulnerability, he decreases his privileges to stay in some projects (this is the only malicious one)
- *rogue* is added as developer, but for some projects he becomes responsible, and is promoted to master
- *rogue* is added as reporter, and then he is promoted for a project, and so on.

When an admin removes an user from a private group, there is no indication that the user still has access to private projects, if role was changed.

I suggest one of these solutions:
- add an alert, showing which project he will still have access
- he is removed from every project

## Steps To Reproduce:

  1. *admin* creates superSecretGroup
  2. *admin* creates bunch of projects 
  3. *admin* adds *myFirstCTO* as master in the group
  4. *myFirstCTO* is bad and he is fired
  5. *myFirstCTO* changes his role in every project
  6. *admin* removes *myFirstCTO* from group's member
  7. *myFirstCTO* has still access to everything. As long as *admin* doesn' t go to the single project members page, he will have no idea

Step 3-5 can happen for a lot of different reasons, also not malicious. I found out because I was removed from a group as "developer", but I was master of some projects and still had access to them

## Impact

A user can still see all resources of a project of a secret group after he has been removed from the group

## Attachments
No attachments
