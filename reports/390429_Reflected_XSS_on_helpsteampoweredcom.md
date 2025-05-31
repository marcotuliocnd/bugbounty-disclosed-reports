# Reflected XSS on help.steampowered.com

## Report Details
- **Report ID**: 390429
- **URL**: https://hackerone.com/reports/390429
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-08-04T08:13:15.999Z
- **Disclosed**: 2019-01-07T20:14:15.601Z

## Reporter
- **Username**: xpaw
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
URL: https://help.steampowered.com/en/wizard/HelpWithGameIssue/?appid=704740&issueid=125&option=%3Ch1%3Eunfiltered

It puts `option` option into a translation token `<div class="help_page_title">#Help_Game_MissingItemsTitle{user controlled string here}`

And if there's no such translation token, it just prints out the entire user input unescaped.

## Impact

XSS.

## Attachments
- 04-081217004.png
