# CRLF Injection in urllib

## Report Details
- **Report ID**: 590020
- **URL**: https://hackerone.com/reports/590020
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-25T10:16:29.801Z
- **Disclosed**: 2020-05-06T02:15:20.166Z

## Reporter
- **Username**: push0ebp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hi. I found CRLF Injection a few months ago.
Please refer my bug issue.
https://bugs.python.org/issue35906

Thank you

## Impact

lead to SSRF. 
e.g. can exploit a internal redis server to send arbitrary packet data including ascii and non-ascii.

## Attachments
No attachments
