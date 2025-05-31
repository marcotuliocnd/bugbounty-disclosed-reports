# CSS Injection in Message Avatar

## Report Details
- **Report ID**: 1031613
- **URL**: https://hackerone.com/reports/1031613
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-11T14:32:55.635Z
- **Disclosed**: 2024-08-10T21:59:25.340Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
## Summary

Custom message avatars can contain inline CSS that influences the resulting HTML element rendering.

## Description

The Meteor.method `sendMessage` allows setting custom avatars. When escaping the input with `none);` further CSS is applied to the elements inline styles. The injected CSS may not contain certain characters, including whitespace.

```
Meteor.call("sendMessage", {
    rid: "<ROOM OR DM ID>",
    avatar: "none);position:fixed;top:0;right:0;bottom:0;left:0;z-index:999;background-color:black;opacity:0.5;pointer-events:none;",
    msg: "Enjoy the Dark Theme!",
    alias: "hacker"
});
```

When the background image is a screenshot of the 2FA message dialog, users could be confused to enter their 2FA token to the chat message field and accidentallty sent it into the currently open channel. A more sophisticated attack would use a second CSS injection overlaying the text input. Although only one CSS element at a time can be influenced, the combination many can lead to the UI being in attacker control.

## Releases Affected:

  * develop

## Steps To Reproduce (from initial installation to vulnerability):

  1. Login to Rocket.Chat
  2. Figure out channel or direct message ID
  3. Open Web Inspector
  4. Send malicious message with Meteor.call `sendMessage`

## Suggested mitigation

  * Verify avatar URLs
  * Sanitize user input

## Impact

Attackers can overlay UI elements and phish for users credentials that are accidentally entered in chat messages.

## Attachments
No attachments
