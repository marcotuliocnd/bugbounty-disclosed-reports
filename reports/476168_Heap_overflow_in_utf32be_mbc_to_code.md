# Heap overflow in utf32be_mbc_to_code

## Report Details
- **Report ID**: 476168
- **URL**: https://hackerone.com/reports/476168
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-01-07T20:15:56.831Z
- **Disclosed**: 2020-11-09T01:48:51.477Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://bugs.php.net/bug.php?id=77418

Buffer overflow in mbc_to_code functions for UTF32BE, UTF32LE, UTF16BE, and UTF16LE due to incorrect length assumptions of a buffer. Provided a patch that was adapted to check the length of the buffer prior to using it.

## Impact

Memory leakage and/or corruption

## Attachments
No attachments
