# Arbitrary modification value "session" (Cookie) in badoo.com

## Report Details
- **Report ID**: 178567
- **URL**: https://hackerone.com/reports/178567
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-28T10:08:27.732Z
- **Disclosed**: 2017-06-25T01:26:40.316Z

## Reporter
- **Username**: ahiezer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
Users who log on through https://m.badoo.com/ receive a session cookie named "session" whose value represents the user identifier.

I have found a way to change the value of the cookie, this error can be used to:

Leave off the application to a particular user to log on again, the attacker would have to cause the victim to visit a particular link.
https://mus1.badoo.com/es/help?platform=4&sessionId=Not_Valid

- Tricking a user to perform a certain action (eg buy credits) believe that this action is for your profile when in fact it is a profile of the attacker.

Proof of Concept
a document is attached to the PoC


## Attachments
- PoC.docx
