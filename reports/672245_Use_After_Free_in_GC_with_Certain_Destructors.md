# Use After Free in GC with Certain Destructors

## Report Details
- **Report ID**: 672245
- **URL**: https://hackerone.com/reports/672245
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-13T13:17:43.075Z
- **Disclosed**: 2020-11-09T01:45:39.148Z

## Reporter
- **Username**: ryat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The bug submitted at: https://bugs.php.net/bug.php?id=72530
The fix committed at: http://git.php.net/?p=php-src.git;a=commit;h=60a7e60b61b8e4a3d455974c83f76a26546ce117

## Impact

The bug can be abused for leaking arbitrary memory blocks or execute arbitrary code remotely via PHP’s object deserializing. ex: unserialize/phar/session

## Attachments
No attachments
