# openssl_seal() uninitialized memory usage

## Report Details
- **Report ID**: 114414
- **URL**: https://hackerone.com/reports/114414
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-03T13:01:11.393Z
- **Disclosed**: 2019-11-12T09:38:26.105Z

## Reporter
- **Username**: 51201
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
openssl_seal() is prone to use uninitialized memory that can be turned into a code execution.

Details about bug: https://bugs.php.net/bug.php?id=71475 (already fixed)
Details about exploitation: http://akat1.pl/?id=1 (released after bug was fixed)

## Attachments
No attachments
