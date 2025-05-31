# Restricted file access when it exists in old versions of task or wiki document

## Report Details
- **Report ID**: 203658
- **URL**: https://hackerone.com/reports/203658
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-05T20:01:34.759Z
- **Disclosed**: 2017-02-06T12:04:20.169Z

## Reporter
- **Username**: denispugachev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
mongoose

Hey! I think there is strange access rules for restricted file.

### Steps to reproduce:
1. Load by User1 file and set it access level "No one" (file Id for example 12)
2. Make wiki with text `{F12}` by User1
3. Edit new wiki page (change all text or delete) by User1
4. Try to access file from User2: http://phabricator.dev/F12 - User2 has access to file even if it has "No
 one" access level.

It happens because `{F12}` exists in old versions of wiki page and User1 can't do anything to hide his file only if he will restrict view access to entire wiki page. I think access level to file should be evaluated by current version of document, not older.

It can be reproduced also in tasks.

## Attachments
No attachments
