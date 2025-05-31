# Pinning leaks message content

## Report Details
- **Report ID**: 1062538
- **URL**: https://hackerone.com/reports/1062538
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-19T15:38:36.886Z
- **Disclosed**: 2024-08-10T21:53:50.125Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:** Improper input validation allows pinning of arbitrary messages (in private channels), leaking the message content back to the sender.

**Description:**

Message pinning was found to lack input data validation, so that arbitrary messages can be pinned and leaked back to an unauthorized client.

```javascript
Meteor.methods({
	pinMessage(message) {
		if (!Meteor.userId()) {
			toastr.error(TAPi18n.__('error-not-authorized'));
			return false;
		}
		if (!settings.get('Message_AllowPinning')) {
			toastr.error(TAPi18n.__('pinning-not-allowed'));
			return false;
		}
		if (Subscriptions.findOne({ rid: message.rid }) == null) {
			toastr.error(TAPi18n.__('error-pinning-message'));
			return false;
		}
		toastr.success(TAPi18n.__('Message_has_been_pinned'));
		return ChatMessage.update({
			_id: message._id,
		}, {
			$set: {
				pinned: true,
			},
		});
	},
	// ...
});
```

The Meteor.method `pinMessage` accepts a message object as input with `_id` and `rid` keys.

With a known Message ID and any Room ID that is accessible by the attacker, the check room subscriptions can be circumvented, because the target chat message is not validated to be in the same room as validated with `Subscriptions.findOne({ rid: message.rid }`.

In addition to that the `pinMessage` function accepts JavaScript objects that are then directly forwarded to the MongoDB model, allowing attackers to use regular expressions to improve guessing of message IDs.

```javascript
Meteor.call("pinMessage", {
  _id: { $regex: /.*/ },
  rid: "<ACCESSIBLE_ROOM_ID>" 
}, (...args) => console.log(...args));
```

The Meteor.call return data contains the message content, so that an arbitrary user with access to any channel can leak individual messages outside of their accessible channels.

## Releases Affected:

  * 3.9.10 / develop

## Steps To Reproduce (from initial installation to vulnerability):

(Add details for how we can reproduce the issue)

  1. Open Rocket.Chat
  2. Find any accessible Room ID (for instance from channel avatar URL)
  3. Open Web Inspector
  4. Execute pinMessage Meteor.call and receive message content in return callback

## Suggested mitigation

  * Check message object data types
  * Query the target `rid` along with the updated message `_id`.

```diff
diff --git a/app/message-pin/client/pinMessage.js b/app/message-pin/client/pinMessage.js
index 9fbc2f778..c360c5d9c 100644
--- a/app/message-pin/client/pinMessage.js
+++ b/app/message-pin/client/pinMessage.js
@@ -1,4 +1,5 @@
 import { Meteor } from 'meteor/meteor';
+import { check } from 'meteor/check';
 import toastr from 'toastr';
 import { TAPi18n } from 'meteor/rocketchat:tap-i18n';
 
@@ -7,6 +8,8 @@ import { ChatMessage, Subscriptions } from '../../models';
 
 Meteor.methods({
        pinMessage(message) {
+               check(message._id, String);
+               check(message.rid, String);
                if (!Meteor.userId()) {
                        toastr.error(TAPi18n.__('error-not-authorized'));
                        return false;
@@ -22,6 +25,7 @@ Meteor.methods({
                toastr.success(TAPi18n.__('Message_has_been_pinned'));
                return ChatMessage.update({
                        _id: message._id,
+                       rid: message.rid
                }, {
                        $set: {
                                pinned: true,
@@ -29,6 +33,8 @@ Meteor.methods({
                });
        },
        unpinMessage(message) {
+               check(message._id, String);
+               check(message.rid, String);
                if (!Meteor.userId()) {
                        toastr.error(TAPi18n.__('error-not-authorized'));
                        return false;
@@ -44,6 +50,7 @@ Meteor.methods({
                toastr.success(TAPi18n.__('Message_has_been_unpinned'));
                return ChatMessage.update({
                        _id: message._id,
+                       rid: message.rid
                }, {
                        $set: {
                                pinned: false,
```

## Impact

Content of arbitrary (private) messages can be leaked by any client with access to at least one room.

## Attachments
No attachments
