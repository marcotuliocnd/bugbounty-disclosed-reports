# IRC-Bot exposes information

## Report Details
- **Report ID**: 222870
- **URL**: https://hackerone.com/reports/222870
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-21T19:35:58.500Z
- **Disclosed**: 2017-04-21T20:36:32.951Z

## Reporter
- **Username**: luke081515
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
You can setup the IRC-Bot, and set it into private channels, so that it posts only information about tasks into private channels. Example:
<Human> T698
<Bot> T698: Task title - https://url.example.org/T698

The problem is, that, if the bot is online in IRC, you can send him task numbers via private messages, and then he exposes the title of tasks without access control.

## Attachments
No attachments
