# buffer overread in base64 code of the xmlrpc module

## Report Details
- **Report ID**: 477897
- **URL**: https://hackerone.com/reports/477897
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-01-11T10:11:55.189Z
- **Disclosed**: 2020-11-09T01:48:23.671Z

## Reporter
- **Username**: hanno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Malformed input to the xmlrpc_decode function can cause an out of bounds read in the base64 code.

This is fixed in the latest updates of PHP (7.3.1 etc.)

Report:
https://bugs.php.net/bug.php?id=77380

## Impact

If the attacker has access to the decoded output this may leak memory contents.

## Attachments
No attachments
