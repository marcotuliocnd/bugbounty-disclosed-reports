# wddx_deserialize null dereference

## Report Details
- **Report ID**: 161216
- **URL**: https://hackerone.com/reports/161216
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-19T03:57:00.501Z
- **Disclosed**: 2019-10-31T06:17:34.375Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream Bug
---
https://bugs.php.net/bug.php?id=72750

Summary
--
When wddx deserialize tries to parse an invalid base64 binary value, php_base64_decode return NULL. The return value is not checked and used.
```
https://github.com/php/php-src/blob/master/ext/wddx/wddx.c#L896

                if (!strcmp((char *)name, EL_BINARY)) {
                        zend_string *new_str = php_base64_decode(
                                (unsigned char *)Z_STRVAL(ent1->data), Z_STRLEN(ent1->data));
                        zval_ptr_dtor(&ent1->data);
                        ZVAL_STR(&ent1->data, new_str);
                }
```

Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=698a691724c0a949295991e5df091ce16f899e02
```

Fixed for PHP 5.6.25, PHP 7.0.10
--
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php


## Attachments
No attachments
