# Unread Messages can leak Message IDs

## Report Details
- **Report ID**: 1063114
- **URL**: https://hackerone.com/reports/1063114
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-20T22:01:01.605Z
- **Disclosed**: 2024-08-10T21:59:12.079Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:** The Meteor Method `unreadMessages`, called with a regular expression, can leak existing Message IDs to unauthorized clients.

**Description:**
The MongoDB `_id` of a Rocket.Chat Message is private, because unauthorized clients could use it to affect or leak chat messages. With a regular expression as target `firstUnreadMessage`, the following Meteor.call prints true when a matching message exists:

```javascript
Meteor.call("unreadMessages", {
  _id: { $regex: /(.*|<KNOWN_MESSAGE_ID>)/ }
}, (error, i) => console.log(!!error));
```

When a regex does not match any message, the KNOWN_MESSAGE_ID is found instead, so that no error is returned. An `error-action-not-allowed` error only occurs when the regex matched a message that may not be accessed by the requesting client.

The affected code path can be found in [app/message-mark-as-unread/server/unreadMessages.js#L28](https://github.com/RocketChat/Rocket.Chat/blob/2de9b867eee43acfb3012faeb9a2a69f62f54776/app/message-mark-as-unread/server/unreadMessages.js#L28):

```javascript
const originalMessage = Messages.findOneById(firstUnreadMessage._id, {
	fields: {
		u: 1,
		rid: 1,
		file: 1,
		ts: 1,
	},
});
if (originalMessage == null || userId === originalMessage.u._id) {
	throw new Meteor.Error('error-action-not-allowed', 'Not allowed', {
		method: 'unreadMessages',
		action: 'Unread_messages',
	});
}
```

## Releases Affected:

  * 3.9.3 / develop

## Steps To Reproduce (from initial installation to vulnerability):

  1. Login to Rocket.Chat
  2. Open Web Inspector
  3. Call `unreadMessages`
  4. Repeat 3. with more specific regular expression until full message ID is known

## Suggested mitigation

  * Ensure input data `firstUnreadMessage._id` is a String

## Impact

Unauthorized clients can leak existing messages unique identifiers.

## Attachments
No attachments
