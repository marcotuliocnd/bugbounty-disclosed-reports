# User Impersonation through sendMessage options

## Report Details
- **Report ID**: 1031525
- **URL**: https://hackerone.com/reports/1031525
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-11T11:26:35.150Z
- **Disclosed**: 2024-08-10T21:58:02.682Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
## Summary

Clients can use the avatar and alias parameter of outgoing messages to impersonate other users in group chats.

## Description

The Meteor call `sendMessage` allows usage of custom avatar and alias, which in combination allows impersonation of other chat room members. Spoofed message senders can potentially be used in social engineering attacks.

```javascript
Meteor.call("sendMessage", {
  rid: "<ROOM ID>",
  msg: "@securityguard can you please walk the two technicians waiting at the entrance to the server room?",
  avatar: "/avatar/cto",
  alias: "Your CTO"
}, (...args) => console.log(...args));
```

Users could notice the attack when looking carefully at the user account `@gronke` in grey text next to the custom alias. Attackers on the other hand can change their account name to look similar to their targets ones.

## Releases Affected:

  * develop

## Steps To Reproduce (from initial installation to vulnerability):

1. Open Rocket.Chat
2. Find Room ID (found in the image path of the thumbnail)
3. Trigger `sendMessage` with Meteor.call() and malicious avatar and 

## Suggested mitigation

* Visually mark messages with alternative Alias or Avatar
* Prevent aliases that are claimed by another users profile

## Impact

Attackers with permission to post messages in a channel or direct message can impersonate other users.

## Attachments
- Rocket.Chat_Impersonation_Sing.Li.png
