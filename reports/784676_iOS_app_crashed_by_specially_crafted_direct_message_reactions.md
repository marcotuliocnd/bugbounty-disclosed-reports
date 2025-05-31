# iOS app crashed by specially crafted direct message reactions

## Report Details
- **Report ID**: 784676
- **URL**: https://hackerone.com/reports/784676
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-28T11:08:28.835Z
- **Disclosed**: 2020-02-21T21:09:38.699Z

## Reporter
- **Username**: alexiaya
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** iOS app crashed by specially crafted direct message reactions

**Description:**
Twitter does not properly sanitize direct message reactions, making it possible for arbitrary reaction text to be shown to the user via the message preview in the direct message list. Special characters such as `\r` and `\n` are not stripped, and it is even possible to crash the app by inserting a `\0` character into the reaction text.

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Start a direct message conversation with the victim (this can also be yourself).
  1. Make a request to https://api.twitter.com/1.1/dm/reaction/new.json with an appropriate `conversation_id` and `dm_id` parameter, and `reaction_key` set to `\0` (an actual NUL byte).
  1. Notice that the iOS app crashes, even on any subsequent attempts to reopen it.

## Impact

This makes it trivial for an attacker to make the Twitter iOS app unusable for any user they can send a direct message to. The only recourse for the victim is to log in via twitter.com and delete the affected message or conversation.

## Attachments
No attachments
