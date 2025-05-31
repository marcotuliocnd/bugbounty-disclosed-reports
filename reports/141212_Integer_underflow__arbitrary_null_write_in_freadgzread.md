# Integer underflow / arbitrary null write in fread/gzread

## Report Details
- **Report ID**: 141212
- **URL**: https://hackerone.com/reports/141212
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-26T15:11:35.123Z
- **Disclosed**: 2019-10-13T18:35:12.621Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://bugs.php.net/bug.php?id=72114

Integer underflow in the  fread/gzread length parameter allows to write an arbitrary null byte on 64 bit platforms. This was identified with the help of ASAN and a custom fuzzer.

```
(gdb) run gzread2.php 
Starting program: /home/operac/php/php-56/sapi/cli/php gzread2.php

Program received signal SIGSEGV, Segmentation fault.
0x0000000000727b66 in zif_fread (ht=2, return_value=0x7ffff7fd7d00, return_value_ptr=0x7ffff7fa21c8, this_ptr=0x0, return_value_used=0)
    at /home/operac/php/php-56/ext/standard/file.c:1769
1769            Z_STRVAL_P(return_value)[Z_STRLEN_P(return_value)] = 0;
(gdb) print (*return_value)
$2 = {value = {lval = 140735140003952, dval = 6,9532397838610798e-310, str = {val = 0x7fff74070070 "", len = -2147483648}, ht = 0x7fff74070070, 
    obj = {handle = 1946615920, handlers = 0x5a5a5a5a80000000}, ast = 0x7fff74070070}, refcount__gc = 1, type = 0 '\000', is_ref__gc = 0 '\000'}
(gdb) print (*return_value).value.str.len
$1 = -2147483648
```
Len has got a negative value here and it will be later used to write the null terminator
```
 /* needed because recv/read/gzread doesnt put a null at the end*/
 Z_STRVAL_P(return_value)[Z_STRLEN_P(return_value)] = 0; 

```

This affected PHP version 5.5, 5.6 and 7.0, patch released today:

http://php.net/ChangeLog-5.php#5.5.36

## Attachments
No attachments
