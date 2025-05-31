# Moderators can send messages to users from banned subreddits via `oauth.reddit.com/api/mod/conversations`

## Report Details
- **Report ID**: 1543770
- **URL**: https://hackerone.com/reports/1543770
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-04-18T19:29:03.094Z
- **Disclosed**: 2022-07-04T12:59:33.089Z

## Reporter
- **Username**: ba-reynolds
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:

It is possible for moderators to send messages to users from a banned subreddit.

I assume this is not intended considering that when trying to send a message as a banned subreddit via [reddit.com/message/compose](https://www.reddit.com/message/compose) (`from` field) you get a `200` response but the message is never delivered to the recipient.

## Steps To Reproduce:

1. While in [mod.reddit.com/mail/create](https://mod.reddit.com/mail/create), select a banned subreddit from the dropdown menu.
2. Fill in all other fields and send the message.

## Impact

Moderators can "officially" communicate with users even after the subreddit gets banned. This can be used to organize a new subreddit to migrate to in order to circumvent the ban.

## Attachments
No attachments
