# Impersonation in Sequential Messages

## Report Details
- **Report ID**: 1379645
- **URL**: https://hackerone.com/reports/1379645
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-10-24T12:28:15.946Z
- **Disclosed**: 2024-08-10T21:57:15.442Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
## Summary

Sequential messages can be used to impersonate another user by hiding the leading message.

## Description

Sequential messages posted by the same user on the same date are rendered without repeating the author information and timestamp.

An adversary can use `customClass` or `className` message attributes to hide the initial message of a new author from the timeline, so that the second message appears to be written by a differnet author.

```javascript
const rid = "<Room ID>";
const msg = "This message was written by somebody else";
Meteor.call("sendMessage", {
  msg: "will be hidden",
  rid: rid,
  customClass: "rc-popover"
}, () =>  Meteor.call("sendMessage", { msg, rid }));
```

## Releases Affected:

  * 3.18.2
  * 4.0.3

## Steps To Reproduce (from initial installation to vulnerability):

  1. Login to Rocket.Chat
  2. Identify target Room 
  3. Send hidden message (`customClass: "rc-popover"`)
  4. Send target message
  5. UI will render the target message as written by the previous messages author

## Supporting Material/References

{F1491835}

## Suggested mitigation

  * Mitigate CSS Injection in messages
  * Indiate a messages author in the channel UI

## Impact

Adversaries can send messages that appear to be written by a different user.

## Attachments
- RC-sequential-message-impersonation.png
