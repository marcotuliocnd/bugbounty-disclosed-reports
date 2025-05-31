# Create an Unexpected Object and Don't Invoke __wakeup() in During Deserialization

## Report Details
- **Report ID**: 159943
- **URL**: https://hackerone.com/reports/159943
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-17T06:30:29.105Z
- **Disclosed**: 2019-10-13T11:09:59.593Z

## Reporter
- **Username**: ryat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://bugs.php.net/bug.php?id=72663

the first commit for fix this bug at:
https://github.com/php/php-src/commit/448c9be157f4147e121f1a2a524536c75c9c6059
but this commit lead to type confusion, i reported this bug at comments. then the improve fix commit at:
https://github.com/php/php-src/commit/639f7fde6a51c23d7c670358fbcb777ac1a143f3

## Attachments
No attachments
