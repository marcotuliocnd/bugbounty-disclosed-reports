# Gaining access to private topics using quoting feature

## Report Details
- **Report ID**: 312647
- **URL**: https://hackerone.com/reports/312647
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-05T21:45:55.181Z
- **Disclosed**: 2018-03-17T18:27:00.122Z

## Reporter
- **Username**: mishre
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: discourse

## Vulnerability Information
## Description
Some topics have limited access to certain groups and users, and while there exists a validation for access on this topic, it can be bypassed by abusing a vulnerability in the "onebox" quoting feature. 
When pasting a link in a reply, if this link happens to be a link to another topic on Discourse a small preview is shown which includes the topic content or the post content where the link is pointing to. Also there are some protections in place to make sure that the user can view the linked content, the said protections can be bypassed by adding a query string parameter to the link containing the value 
```
?source_topic_id={victim-topic-id}
```

## Steps to reproduce
1. Login as an administrator to Discourse and create a topic which can only be viewed by the staff.
2. Copy the topic's id from the topic's page. the topic id can be found by browsing the topic and then copying the number in the end of the url (`http://localhost:4000/t/{topic-name}/{topic-id}`)
3. Login with a non-admin user.
4. Go to any topic you have access to, and type in the following reply:
```
http://localhost:80/t/blablabla/?source_topic_id=29
```
please note that the port should 80 or 443 even if the url of your local installation is a different (probably some software bug)
5. Wait for the preview to load and see that you can see topic's content.

## Root cause
The following piece of code determines if the logged-in user is capable of viewing the post/topic :

```
        def can_see_post?(post, source_topic)
          return false if post.nil? || post.hidden || post.trashed? || post.topic.nil?
          Guardian.new.can_see_post?(post) || same_category?(post.topic.category, source_topic)
        end

        def can_see_topic?(topic, source_topic)
          return false if topic.nil? || topic.trashed? || topic.private_message?
          Guardian.new.can_see_topic?(topic) || same_category?(topic.category, source_topic)
        end
```
as can be seen here: https://github.com/discourse/discourse/blob/master/lib/onebox/engine/discourse_local_onebox.rb#L113

However, the source_topic parameter is controlled directly by user input:
```
source_topic_id = @url[/[&?]source_topic_id=(\d+)/, 1].to_i
```
as can be seen here: 
https://github.com/discourse/discourse/blob/master/lib/onebox/engine/discourse_local_onebox.rb#L47
So if we pass in the same topic id as the one we are trying to view, basically the function same_category will always return true, effectively bypassing any protection in place.

## Impact

An attacker will be able to access all private topics and posts on Discourse.

## Attachments
No attachments
