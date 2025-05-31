# Use after free and out of bounds read in xmlrpc_decode()

## Report Details
- **Report ID**: 477896
- **URL**: https://hackerone.com/reports/477896
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-01-11T10:10:08.276Z
- **Disclosed**: 2020-11-09T01:48:05.244Z

## Reporter
- **Username**: hanno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Malformed input can lead to use after free and out of bounds memory errors.

This has been fixed with the latest updates of PHP (7.1.26/7.2.14/7.3.1).

(Note: I reported those as separate bugs to PHP, but they had the same underlying bug and were fixed by the same commit. The release notes only mention "out of bounds read", but this is misleading, as a use after free error is potentially more severe.)

Bugs reported to PHP:
https://bugs.php.net/bug.php?id=77242
https://bugs.php.net/bug.php?id=77249

## Impact

If the xmlrpc functionality of PHP is used to parse untrusted input from a public API point it can potentially be used to gain code execution.

## Attachments
No attachments
