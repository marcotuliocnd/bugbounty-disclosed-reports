# Stored XSS in "post last edited" option

## Report Details
- **Report ID**: 333507
- **URL**: https://hackerone.com/reports/333507
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-04-04T18:48:34.636Z
- **Disclosed**: 2018-07-09T16:04:37.753Z

## Reporter
- **Username**: luigigubello
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: discourse

## Vulnerability Information
1. There are two users: **Attacker** and **Victim**.
2. **Attacker** starts a private talk via private message with the **Victim**.
3. **Attacker** send a message to **Victim**, then he edits it or deletes it.
4. **Victim** sees the *yellow pencil*, symbol of the edit.
5. **Victim** clicks on *yellow pencil* to see the edit and the XSS runs.

Other info: the XSS also runs on topic (video PoC #2). You can find my XSS message on this URL:
https://try.discourse.org/t/recommended-reading-for-community-and-foss-enthusiasts/278
It is very dangerous because it can hit many users at the same time.

## Impact

XSS can use to steal cookies, password or to run arbitrary code on victim's browser

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://try.discourse.org/t/recommended-reading-for-community-and-foss-enthusiasts/278

**Verified**
Yes



## Attachments
- discourse_stored_xss_2.mp4
- discourse_stored_xss.mp4
