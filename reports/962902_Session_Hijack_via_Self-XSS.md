# Session Hijack via Self-XSS

## Report Details
- **Report ID**: 962902
- **URL**: https://hackerone.com/reports/962902
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-20T03:22:37.033Z
- **Disclosed**: 2021-01-17T16:51:18.491Z

## Reporter
- **Username**: jcardona
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:** It's possible to hijack a session by tricking the user to perform a Self-XSS on the drag and drop functionality in the chat.

**Description:** Self-XSS is an underrated vulnerability that can have a harmful impact on the users of the application like here, after we get access to the user's session we can read chats, change (some) info and lock the account by activating the 2FA.  

## Releases Affected:

  * Tested on 3.5.2 and 3.5.3 (current version)

## Steps To Reproduce:

  1. Serve the image (payload) using Python's HTTP server.
  1. Trick the user to drag and drop the image inside a chat.
  1. Get the **Meteor.loginToken** from the server logs.
  1. Open that instance of Rocket Chat in a browser.
  1. Add the **Meteor.loginToken** as an item in the local storage.
  1. The site automatically redirects to the session.
  1. Profit!

## Supporting Material/References:

  * GIF file explaining the PoC.
  * HTML file with the payload.

## Suggested mitigation

  * Sanitize the drag and drop functionality of chat text box striping the tags.

## Impact

The attacker can gain access to the user session and read chats, change (some) info and lock the account by activating the Two-Factor Authentication, even alter the server configuration depending on the account privileges.

## Attachments
No attachments
