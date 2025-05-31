# User can delete data in shared folders he's not autorized to access

## Report Details
- **Report ID**: 642515
- **URL**: https://hackerone.com/reports/642515
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-13T16:36:49.038Z
- **Disclosed**: 2020-04-10T16:13:47.638Z

## Reporter
- **Username**: jlord87
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
###Steps to reproduce

1. create a group folder named TEST and share with "admin group" and "test group", marking the advanced permission flag
2. create two folders inside the main share: visible and invisible
3. inside "invisible" folder create a test file (let's say something like "test.txt")
4. set the advanced folder permission to deny everything to "test group" for the "invisible" folder (deny read, deny write, deny share, deny create, deny delete...)
5. log in with test user (member of test group). The invisible folder is not shown, you can only see the visible one. That's great.
6. if you try to create a folder named "invisible" you get an error (that's good too) sync the new external share to your pc (in my case win7 with 2.5.2 client). Only the "visible" folder is synced.
7. create a folder named "temp" and create inside this new folder a new file (lets say "test2.txt"). This folder will be synced online
8. rename temp to invisible
9. the folder gets synced online overwriting the originale "invisible" folder

###Expected behaviour

The sync client should keep denying the syncronization of "invisible" folder to the unauthorized users

###Actual behaviour

The folder is synced, the original one and all its content (that should be inaccessible to test user) are overwritten and lost

## Impact

An "attacker" - that could simply be an user with low privileges - can delete sensitive data that were on purpose hidden to its group.

## Attachments
No attachments
