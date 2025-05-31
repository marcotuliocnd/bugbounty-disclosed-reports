# Leakage badges on disabled user

## Report Details
- **Report ID**: 325594
- **URL**: https://hackerone.com/reports/325594
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-03-13T17:22:10.328Z
- **Disclosed**: 2018-03-15T09:29:12.291Z

## Reporter
- **Username**: e333jsjs7se
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
﻿**********************************************
                                  Indonesia Here ;)
**********************************************

*Hi HackerOne Team,*

**Description:**
This attack occurs when an attacker uses this graphql code:


and this builds the path of the attacker getting disclosure information about how many programs already in the close Resolved from the Public or Disable user.

okay now I do not say if the Public User just open the username profile page target will also look hacktivity that has been already Resolved or already sent bounty (bounty awarded).

but what if you open a username that is disabled? (disabled) you can not see the user page profile, and this bug can see badges username disabled.

This means that anyone who gets 10 badges means that you have submitted a report to 10 Program Handles. (This applies also to Public users)

##POC:
*  for the first I will enum and check username disable or not through UserID. POST /graphql

```
{
  "query": "query Profile_settings_MeRelayQL($id_0:ID!,$size_1:ProfilePictureSizes!) {\n  node(id:$id_0) {\n    id,\n    __typename,\n    ...F0\n  }\n}\nfragment F0 on User {\n  id,\n  username,\n  disabled,\n  bio,\n  location,\n  website,\n  _profile_picture:profile_picture(size:$size_1),\n  website,\n  next_update_username_date\n}",
  "variables": {
    "id_0": "Z2lkOi8vaGFja2Vyb25lL1VzZXIvMzA5",
    "size_1": "xtralarge"
  }
}
```
**for example 
I use @alex-rice UserID 15  or @janpaul123 UserID 309
gid://hackerone/User/309
gid://hackerone/User/15**

Body Response:

```
{
  "data": {
    "node": {
      "id": "Z2lkOi8vaGFja2Vyb25lL1VzZXIvMzA5",
      "__typename": "User",
      "username": "janpaul123",
      "disabled": true,
......
......
......
}
  }
}
```
well user ```janpaul123``` disabled. 

* then if you open the user profile page will not appear. https://hackerone.com/janpaul123

**let's get to the point:**
POST /graphql


```{"query":"query User_badges($first_0:Int!) {\n query {\n id,\n ...F0\n }\n}\nfragment F0 on Query {\n _user:user(username:\"janpaul123\") {\n username,\n _badges:badges(first:$first_0) {\n edges {\n node {\n id,\n created_at,\n badge {\n name,\n description,\n image_path,\n id\n }\n },\n cursor\n },\n pageInfo {\n hasNextPage,\n hasPreviousPage\n }\n },\n id\n },\n id\n}","variables":{"first_0":100}}```

And Response Body: ( I made it short. )
```
"created_at": "2016-06-15T10:03:25.319Z",
                "badge": {
                  "name": "Publish or Perish",
                  "description": "Publicly disclosed a report",

"created_at": "2013-11-07T22:54:43.947Z",
                "badge": {
                  "name": "Hacking Hackers",
                  "description": "Hacked HackerOne",

"created_at": "2013-11-07T22:54:43.947Z",
                "badge": {
                  "name": "Insecticide",
                  "description": "First report closed as resolved",

"created_at": "2013-11-29T22:31:21.260Z",
                "badge": {
                  "name": "Bounty Hunter",
                  "description": "First bounty received",
```
**this means that there are only 4 handle programs that have been completed by** ```janpaul123```

**Maybe you will ask me can you see the handle completed there (resolved)?
I will reply: Of course I can not see the handle that has been resolved.**

**and if according to your discussion there is nothing about security, then why I can see a badge of user profile page that can not be seen publicly.**

*sorry if there is my writing is wrong, please understand my english bad, I use google translate hahaha*

*Best Regards,*
@terlupakan

## Impact

Depending on the context in which it is used, an attacker can see the badges and the description.
but this user is disabled, but the attacker can still see it.

## Attachments
No attachments
