# Self XSS when pasting HTML into Text app with Ctrl+Shift+V

## Report Details
- **Report ID**: 2211561
- **URL**: https://hackerone.com/reports/2211561
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-10-16T15:13:18.814Z
- **Disclosed**: 2023-12-21T05:24:53.202Z

## Reporter
- **Username**: max_nextcloud
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
ctrl-shift-v is meant to paste plaintext as is. However it will paste it into a dom elements `innerHtml` and can thus be used to inject malicious html.

## Steps To Reproduce:

  1. copy "<h1>html</h1>"
  1. use ctrl-shift-v to paste it into a .md file
  1. See the heading getting added.

## Supporting Material/References:
https://github.com/nextcloud/text/blob/main/src/extensions/Markdown.js#L97

  * [attachment / reference]

## Impact

If you can trick someone into using ctrl-shift-v to paste content you control you can insert html into the page leading to a possible xss attack.

The html will be inserted into the editors schema - but before that happens it's already pasted into the innerHtml of a dom element.

## Attachments
No attachments
