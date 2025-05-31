# User deletion is not handled properly everywhere

## Report Details
- **Report ID**: 1200700
- **URL**: https://hackerone.com/reports/1200700
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-18T09:00:54.327Z
- **Disclosed**: 2021-07-15T19:12:16.497Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
So I came across this when going over https://nextcloud.com/compare/

And noticed the section: "BUILT IN DATA-REQUEST/ACCOUNT DELETION"

However looking at this it seems this is not handled properly everywhere in Nextcloud. I understand that the GDPR etc do consider shared data differently. For example a conversation two people have is shared data often and does not always have to be deleted.

In anycase let me describe what I found.

1. userA has an account on server
2. userB has an account on server
3. userA and userB do a lot of chatting via talk
4. At some point userB leaves the server and their account is deleted
5. Now a new user comes along that gets assigned the id userB (or registers it or whatever)
6. If the new userB now opens the chat to userA they will see all the messages exchanged between userA and the old userB

## Impact

New users might get access to data of other users that left the system. This should not happen.

I would suggest (to make your own life easier) to keep a blocklist of ids for users. So that these things can't happen.
You still have to make sure all required data is removed. But of you miss something at least it won't possibly get leaked to new users.

## Attachments
No attachments
