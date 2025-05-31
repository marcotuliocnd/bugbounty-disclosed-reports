# Online Status of arbitrary users can be changed

## Report Details
- **Report ID**: 501077
- **URL**: https://hackerone.com/reports/501077
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-25T14:22:47.849Z
- **Disclosed**: 2024-08-10T21:59:34.719Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
# Summary

A third-party Meteor module [Konecty/meteor-user-presence](https://github.com/Konecty/meteor-user-presence) was found to improperly authenticate user Status changes, so that it is possible to change other users online status by sending HTTP requests or data via WebSocket connection.

# Description

With the following payloads, an users online status can be changed without proper authentication:

```
["{\"msg\":\"method\",\"method\":\"UserPresence:away\",\"params\":[\"$USER_ID\"],\"id\":\"23\"}"]
["{\"msg\":\"method\",\"method\":\"UserPresence:online\",\"params\":[\"$USER_ID\"],\"id\":\"23\"}"]
```

Expected result is an error, when attempting to change other users status.

It was not possible to reproduce this finding with every user - more investigation required to figure out what sometimes makes it unreliable.

## Releases Affected:

  * [develop@5f0180d]( https://github.com/RocketChat/Rocket.Chat/commit/5f0180dc1500b4e37b8320b39869babadb5d01cd)

## Steps To Reproduce (from initial installation to vulnerability):

  1. Figure out another users `_id` from client network requests
  1. Send the crafted payload via WebSockets
  1. Observe status-change in other chat sessions

## Suggested mitigation

  * Authenticate `UserPresence:*` methods in https://github.com/Konecty/meteor-user-presence/blob/04ca1a0c3fe3cd52857012bbad0a02e3e838ff9e/server/server.js#L249-L281

## Impact

The online status of arbitrary users can be changed by others.

## Attachments
No attachments
