# The Custom Emoji Page has a Reflected XSS

## Report Details
- **Report ID**: 258198
- **URL**: https://hackerone.com/reports/258198
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-08-09T09:03:33.645Z
- **Disclosed**: 2017-09-24T06:40:12.327Z

## Reporter
- **Username**: co3k
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
The Custom Emoji Page has a Reflected XSS in building flash message.

The following is the PoC.
https://{team}.slack.com/customize/emoji?added=1&name=vuln"><script>alert(0);<%2Fscript>

## Attachments
No attachments
