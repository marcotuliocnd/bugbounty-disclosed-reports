# javascript: and mailto: links are allowed in JIRA integration settings

## Report Details
- **Report ID**: 209917
- **URL**: https://hackerone.com/reports/209917
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-01T20:18:26.269Z
- **Disclosed**: 2017-04-10T17:49:55.366Z

## Reporter
- **Username**: jamesclyde
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
For new feature settings, you accept website URLs like javascript:// or data:// in base urls. Even https://evil.com works, this needs to be stripped, this can be used to create another integrations without 

### Steps To Reproduce

1. https://hackerone.com/(Team)/integrations/jira/edit
2. Try in Base URL: javascript:// or data://
3. It will save and opens it everytime when escalate

### Optional: Your Environment (Browser version, Device, etc)
Works in all browsers

## Attachments
No attachments
