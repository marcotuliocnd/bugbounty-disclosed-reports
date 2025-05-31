# wddx_deserialize use-after-free

## Report Details
- **Report ID**: 170144
- **URL**: https://hackerone.com/reports/170144
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-18T02:21:05.690Z
- **Disclosed**: 2019-11-03T01:19:43.702Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream Bug
---
https://bugs.php.net/bug.php?id=72860

Summary
--
wddx_deserialize allows to unserialize a WDDX packet that usually comes from external input.

While WDDX tries to deserialize "recordset" element, use-after-free happens if the close tag for the field is not found. 


Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=780daee62b55995a10f8e849159eff0a25bacb9d
```

Fixed for PHP 5.6.26 and 7.0.11
--
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php


## Attachments
No attachments
