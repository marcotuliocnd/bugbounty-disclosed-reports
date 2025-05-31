# Improper ACL in Message Starring

## Report Details
- **Report ID**: 1060837
- **URL**: https://hackerone.com/reports/1060837
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-17T11:54:24.769Z
- **Disclosed**: 2024-08-10T21:58:18.786Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:** Improper access checks when starring messages allow write operations of the starred attribute of arbitrary messages.

**Description:** Room access validation is performed on user provided data. In absence of a check whether a Message is in a certain room, attackers can provide an unrelated Room ID where they have access to (e.g. general) to then star an arbitrary message.

## Releases Affected:

  * develop Branch (`19685c04c32e8c9ae95371acd2301769f0b734a9`)

## Steps To Reproduce (from initial installation to vulnerability):

(Add details for how we can reproduce the issue)

  1. Login to Rocket.Chat
  2. Open Web Inspector
  3. Call `starMessage` Meteor method:

```javascript
Meteor.call("starMessage", {
  rid: "<ANY_ROOM_ID_WITH_ACCESS>",
  _id: "<TARGET_MESSAGE_ID>",
  starred: true
}, (...args) => console.log(...args));
```

## Suggested mitigation

  * Validate match of the Message rid before writing changes

## Impact

Attackers can manipulate manipulate the starred attribute of arbitrary messages.

## Attachments
No attachments
