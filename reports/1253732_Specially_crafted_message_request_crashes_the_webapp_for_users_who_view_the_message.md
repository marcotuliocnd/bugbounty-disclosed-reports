# Specially crafted message request crashes the webapp for users who view the message

## Report Details
- **Report ID**: 1253732
- **URL**: https://hackerone.com/reports/1253732
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-07-07T16:59:31.466Z
- **Disclosed**: 2022-03-14T05:05:54.711Z

## Reporter
- **Username**: thesecuritydev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
## Summary:
If you post a message with a modified `deleted_at` JSON parameter, the webapp will crash for anyone currently viewing the channel, or for anyone viewing a different channel if they switch to that channel afterward.

## Steps To Reproduce:

1. Go to a team channel, with Burp Suite ready.
2. Send a message, intercepting the request with Burp. The JSON request contains keys like `message`, `channel_id`, and `pending_post_id`.
3. Add the following key to the JSON request: `deleted_at`, with a value that's greater than 0. For example: `"deleted_at": 10`.
4. Now if you send the request, the webapp will crash with a blank screen and you will have to refresh the page. _Note: If you want to send the request again, you may have to update the `pending_post_id` to some other unique value._

It affects all users viewing the channel, not just the sender. Also, you don't even have to be in the channel when the message is sent. If you are already on a different channel, and you switch to the affected channel after the message is sent, it still has the same effect.

## Impact

A user could prevent others from accessing a channel by continually making this request so that it's impossible to load the webapp, because a new message would come and crash it even after refreshing the page. And since after refreshing you will still be on the channel, it could prevent the users from having access to the entire webapp, as they may not be able to exit the channel quick enough to prevent the crash.

You could also send a DM to someone and when they click to view the message the webapp will crash.

## Attachments
No attachments
