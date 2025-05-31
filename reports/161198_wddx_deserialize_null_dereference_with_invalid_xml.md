# wddx_deserialize null dereference with invalid xml

## Report Details
- **Report ID**: 161198
- **URL**: https://hackerone.com/reports/161198
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-19T03:08:05.446Z
- **Disclosed**: 2019-10-13T18:35:24.387Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream Bug
---
2016-08-09 02:53 UTC
https://bugs.php.net/bug.php?id=72790


Summary
--
wddx_deserialize allows to unserializes a WDDX packet that usually comes from external input, php interpreter crashes while processing invalid XML input with wddx_deserialize
```
https://github.com/php/php-src/blob/PHP-5.6/ext/wddx/wddx.c#L1170

 wddx_stack_top(&stack, (void**)&ent);
 *return_value = *(ent->data);
```
ent value is null but is not checked and then used to assign the return value. This doesn't happen with PHP-7.0, but the code here changed a little, I guess some of these macro check the value and prevent it from happening:

```
https://github.com/php/php-src/blob/PHP-7.0.9/ext/wddx/wddx.c#L1075

 wddx_stack_top(&stack, (void**)&ent);
 ZVAL_COPY(return_value, &ent->data);
````

Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=1f6078e4a5c67733bfdbd20bb2706501ac56a344
```

Fixed for PHP 5.6.25,
--
http://php.net/ChangeLog-5.php


## Attachments
No attachments
