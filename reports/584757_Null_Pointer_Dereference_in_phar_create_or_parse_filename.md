# Null Pointer Dereference in phar_create_or_parse_filename

## Report Details
- **Report ID**: 584757
- **URL**: https://hackerone.com/reports/584757
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-05-20T01:29:57.192Z
- **Disclosed**: 2020-10-10T18:47:55.880Z

## Reporter
- **Username**: chihuahua
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The original report is here https://bugs.php.net/bug.php?id=77396

```
Description:
------------
Please use these poc file:
https://drive.google.com/file/d/1bzw-j4FtV7PEf6SW2GYmDVKtMybmbKnl/view?usp=sharing

Test script:
---------------
USE_ZEND_ALLOC=0 ../../php-7.1.25/sapi/cli/php -r '$phar=new PharData(file_get_contents("id:000005,sig:06,src:000230,op:havoc,rep:8"));'


Actual result:
--------------
USE_ZEND_ALLOC=0 ../../php-7.1.25/sapi/cli/php -r '$phar=new PharData(file_get_contents("id:000005,sig:06,src:000230,op:havoc,rep:8"));'
ASAN:SIGSEGV
=================================================================
==78112==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7f0a8ff9a746 bp 0x7ffc3694f6c0 sp 0x7ffc3694ee48 T0)
    #0 0x7f0a8ff9a745 in strlen (/lib/x86_64-linux-gnu/libc.so.6+0x8b745)
    #1 0x7f0a90e2c1a5 in __interceptor_strlen (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x701a5)
    #2 0x105a1fe in phar_create_or_parse_filename /home/hackyzh/Desktop/php-7.1.25/ext/phar/phar.c:1388
    #3 0x105b94d in phar_open_or_create_filename /home/hackyzh/Desktop/php-7.1.25/ext/phar/phar.c:1328
    #4 0x1075f65 in zim_Phar___construct /home/hackyzh/Desktop/php-7.1.25/ext/phar/phar_object.c:1195
    #5 0x1f740b8 in ZEND_DO_FCALL_SPEC_RETVAL_UNUSED_HANDLER /home/hackyzh/Desktop/php-7.1.25/Zend/zend_vm_execute.h:970
    #6 0x1eb6a66 in execute_ex /home/hackyzh/Desktop/php-7.1.25/Zend/zend_vm_execute.h:429
    #7 0x1f87f14 in zend_execute /home/hackyzh/Desktop/php-7.1.25/Zend/zend_vm_execute.h:474
    #8 0x189ed80 in zend_eval_stringl /home/hackyzh/Desktop/php-7.1.25/Zend/zend_execute_API.c:1120
    #9 0x189f2d0 in zend_eval_stringl_ex /home/hackyzh/Desktop/php-7.1.25/Zend/zend_execute_API.c:1161
    #10 0x1f94de8 in do_cli /home/hackyzh/Desktop/php-7.1.25/sapi/cli/php_cli.c:1024
    #11 0x45f880 in main /home/hackyzh/Desktop/php-7.1.25/sapi/cli/php_cli.c:1381
    #12 0x7f0a8ff2f82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #13 0x45feb8 in _start (/home/hackyzh/Desktop/php-7.1.25/sapi/cli/php+0x45feb8)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV ??:0 strlen
==78112==ABORTING
```

## Impact

Denial of service

## Attachments
No attachments
