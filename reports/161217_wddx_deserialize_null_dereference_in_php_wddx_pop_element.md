# wddx_deserialize null dereference in php_wddx_pop_element

## Report Details
- **Report ID**: 161217
- **URL**: https://hackerone.com/reports/161217
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-19T04:03:10.173Z
- **Disclosed**: 2019-10-13T18:25:48.192Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream Bug
---
https://bugs.php.net/bug.php?id=72799

Summary
--
If we add an element to boolean leaf of XML struct, a null pointer dereference will happen when the element is popped. 

```
Source code:
https://github.com/php/php-src/blob/PHP-5.6.24/ext/wddx/wddx.c#L985

static void php_wddx_pop_element(void *user_data, const XML_Char *name)
{
...
  if (Z_TYPE_P(ent2->data) == IS_ARRAY || Z_TYPE_P(ent2->data) == IS_OBJECT) {
    target_hash = HASH_OF(ent2->data);
...

```

Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=1f6078e4a5c67733bfdbd20bb2706501ac56a344
```

Fixed for PHP 5.6.25, PHP 7.0.10
--
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php

## Attachments
No attachments
