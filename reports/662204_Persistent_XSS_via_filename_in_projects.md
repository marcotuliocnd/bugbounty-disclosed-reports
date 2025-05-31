# Persistent XSS via filename in projects

## Report Details
- **Report ID**: 662204
- **URL**: https://hackerone.com/reports/662204
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-28T10:22:56.058Z
- **Disclosed**: 2020-03-01T13:18:39.631Z

## Reporter
- **Username**: foobar7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
CVSS
----

Medium 5.4 [CVSS:3.0/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N)

Description
-----------

Affected: Talk / Spreed 6.0.3

The name of a file is echoed without encoding when moving the mouse onto it in the projects tab of a conversation, leading to persistent XSS.

A successful attack requires an account with low-level permissions as well as a usual amount of user interaction (interacting with the project of a talk in a usual manner).

Successful exploitation allows the attacker to take over the account of the attacked user. If the attacked user is an administrator, this would allow a user full access to the application & files.

POC
--- 

To place the payload as the attacker:

- create a file named `test'"><img src=x onerror=alert(document.location)>.txt`. Share the file with the victim. 
- Create a new conversation: Talk -> new conversation -> enter a name.
- Invite the victim: Participants -> Add participant -> select the user
- Add a project: Projects -> Add a project -> Link to a file -> select the file from step 1. 

To trigger the payload as the victim: 

- open the conversation -> projects -> hover over the file symbol to trigger the payload.

## Impact

Successful exploitation allows an attacker to read any data the attacked user has access to, or to perform arbitrary requests the user can perform.

## Attachments
No attachments
