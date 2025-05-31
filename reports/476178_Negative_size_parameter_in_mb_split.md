# Negative size parameter in mb_split

## Report Details
- **Report ID**: 476178
- **URL**: https://hackerone.com/reports/476178
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-01-07T20:25:48.915Z
- **Disclosed**: 2020-11-09T01:48:52.585Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://bugs.php.net/bug.php?id=77367

mb_split doesn't correctly detect the length when the $string has an unfinished multibyte character at the end of the string. This causes a crash due to a negative parameter to add_next_index_stringl, which calls zend_string_init and memcpy.

Could reproduce on master.

## Impact

This could be used to cause memory corruption/leakage.

## Attachments
No attachments
