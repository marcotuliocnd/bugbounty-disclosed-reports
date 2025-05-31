# Missing rel=noreferrer tag allows link in list to change url of currently open tab

## Report Details
- **Report ID**: 158002
- **URL**: https://hackerone.com/reports/158002
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-09T22:40:36.532Z
- **Disclosed**: 2016-09-12T19:59:15.545Z

## Reporter
- **Username**: cablej
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Hi,

When adding links to lists, there is no rel=noreferrer tag present, allowing a linked page to change the url of the currently open tab. This can open the doors for phishing attacks, as users trust the tab that contained instacart.

As an example, see my list at https://inst.cr/t/1QmLPG. Clicking the link, which opens in a new tab, will change the url of the currently open tab to http://example.com.

Thank you for your time, and please let me know if you have any questions.

## Attachments
No attachments
