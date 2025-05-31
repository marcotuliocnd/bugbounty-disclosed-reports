# Int Overflow lead to Heap OverFlow in exif_thumbnail_extract of exif.c

## Report Details
- **Report ID**: 384477
- **URL**: https://hackerone.com/reports/384477
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-20T07:20:20.464Z
- **Disclosed**: 2019-10-21T05:19:46.535Z

## Reporter
- **Username**: md4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This bug was reported to PHP last month and a fix was public last week:https://bugs.php.net/bug.php?id=76423
Heap OverFlow in exif_thumbnail_extract of exif.c
This vulnerability can be triggered by exif_read_data in any 32-bit system.
exif.c:2947:
```
if ((ImageInfo->Thumbnail.offset + ImageInfo->Thumbnail.size) > length) {
	EXIF_ERRLOG_THUMBEOF(ImageInfo)
	return;
}
ImageInfo->Thumbnail.data = estrndup(offset + ImageInfo->Thumbnail.offset, ImageInfo->Thumbnail.size);
```

`ImageInfo->Thumbnail.offset` is in range(0xffffffff) and `ImageInfo->Thumbnail.size` is in range(0xffff). In 32 bit system, `ImageInfo->Thumbnail.offset + ImageInfo->Thumbnail.size` can be an int overflow, which can bypass the check of length and lead to heap overflow in `estrndup`.


Test script:
---------------
https://gist.github.com/yough3rt/f03920196a3bb9cec03e08e02079309a

USE_ZEND_ALLOC=0 /home/youghurt/php-llvm/bin/php IDF_tag.php



Expected result:
----------------
No Error.

Actual result:
--------------
```
When running the test script with an ASAN enabled PHP interpreter with USE_ZEND_ALLOC=0, the following ASAN report/backtrace is generated:
=================================================================
==29132==ERROR: AddressSanitizer: heap-buffer-overflow on address 0xb2500000 at pc 0x0814a6cd bp 0xbfd1f388 sp 0xbfd1ef60
READ of size 65535 at 0xb2500000 thread T0
    #0 0x814a6cc in __asan_memcpy /home/youghurt/llvm-src/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23
    #1 0x95f1eaa in _estrndup /home/youghurt/php-7.2.6/Zend/zend_alloc.c:2538:2
    #2 0x899a435 in exif_thumbnail_extract /home/youghurt/php-7.2.6/ext/exif/exif.c:2951:30
    #3 0x899665e in exif_process_IFD_in_JPEG /home/youghurt/php-7.2.6/ext/exif/exif.c:3619:5
    #4 0x8995c06 in exif_process_TIFF_in_JPEG /home/youghurt/php-7.2.6/ext/exif/exif.c:3665:2
    #5 0x8995586 in exif_process_APP1 /home/youghurt/php-7.2.6/ext/exif/exif.c:3690:2
    #6 0x89918f4 in exif_scan_JPEG_header /home/youghurt/php-7.2.6/ext/exif/exif.c:3835:6
    #7 0x8990433 in exif_scan_FILE_header /home/youghurt/php-7.2.6/ext/exif/exif.c:4224:8
    #8 0x898ff1f in exif_read_from_impl /home/youghurt/php-7.2.6/ext/exif/exif.c:4365:8
    #9 0x8989e8a in exif_read_from_stream /home/youghurt/php-7.2.6/ext/exif/exif.c:4382:8
    #10 0x898a3cf in exif_read_from_file /home/youghurt/php-7.2.6/ext/exif/exif.c:4409:8
    #11 0x89829b7 in zif_exif_read_data /home/youghurt/php-7.2.6/ext/exif/exif.c:4482:9
    #12 0x9cb0053 in ZEND_DO_ICALL_SPEC_RETVAL_USED_HANDLER /home/youghurt/php-7.2.6/Zend/zend_vm_execute.h:617:2
    #13 0x999e521 in execute_ex /home/youghurt/php-7.2.6/Zend/zend_vm_execute.h:59723:7
    #14 0x999fb57 in zend_execute /home/youghurt/php-7.2.6/Zend/zend_vm_execute.h:63760:2
    #15 0x972f63e in zend_execute_scripts /home/youghurt/php-7.2.6/Zend/zend.c:1496:4
    #16 0x9438e0c in php_execute_script /home/youghurt/php-7.2.6/main/main.c:2590:14
    #17 0x9f844cc in do_cli /home/youghurt/php-7.2.6/sapi/cli/php_cli.c:1011:5
    #18 0x9f81245 in main /home/youghurt/php-7.2.6/sapi/cli/php_cli.c:1404:18
    #19 0xb7a06636 in __libc_start_main /build/glibc-mUak1Y/glibc-2.23/csu/../csu/libc-start.c:291
    #20 0x807bd77 in _start (/home/youghurt/php-llvm/bin/php+0x807bd77)

0xb2500000 is located 128 bytes to the left of 896-byte region [0xb2500080,0xb2500400)
allocated by thread T0 here:
    #0 0x814b887 in __interceptor_malloc /home/youghurt/llvm-src/projects/compiler-rt/lib/asan/asan_malloc_linux.cc:121
    #1 0x95f1626 in __zend_malloc /home/youghurt/php-7.2.6/Zend/zend_alloc.c:2829:14
    #2 0x980736c in zend_hash_do_resize /home/youghurt/php-7.2.6/Zend/zend_hash.c:860:14
    #3 0x97fa7df in _zend_hash_add_or_update_i /home/youghurt/php-7.2.6/Zend/zend_hash.c:591:2
    #4 0x97fa7df in _zend_hash_merge /home/youghurt/php-7.2.6/Zend/zend_hash.c:1888
    #5 0x88f7353 in zm_startup_dom /home/youghurt/php-7.2.6/ext/dom/php_dom.c:755:2
    #6 0x9755ecc in zend_startup_module_ex /home/youghurt/php-7.2.6/Zend/zend_API.c:1873:7
    #7 0x97577ff in zend_startup_module_zval /home/youghurt/php-7.2.6/Zend/zend_API.c:1888:10
    #8 0x97ee717 in zend_hash_apply /home/youghurt/php-7.2.6/Zend/zend_hash.c:1506:12
    #9 0x9757121 in zend_startup_modules /home/youghurt/php-7.2.6/Zend/zend_API.c:1999:2
    #10 0x9432549 in php_module_startup /home/youghurt/php-7.2.6/main/main.c:2309:2
    #11 0x9f86e8b in php_cli_startup /home/youghurt/php-7.2.6/sapi/cli/php_cli.c:431:6
    #12 0x9f81027 in main /home/youghurt/php-7.2.6/sapi/cli/php_cli.c:1371:6
    #13 0xb7a06636 in __libc_start_main /build/glibc-mUak1Y/glibc-2.23/csu/../csu/libc-start.c:291

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/youghurt/llvm-src/projects/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23 in __asan_memcpy
Shadow bytes around the buggy address:
  0x3649ffb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x3649ffc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x3649ffd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x3649ffe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x3649fff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x364a0000:[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x364a0010: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x364a0020: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x364a0030: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x364a0040: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x364a0050: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
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
  Shadow gap:              cc
==29132==ABORTING
```

## Impact

A context dependent attacker could potentially gain sensitive information about a PHP environment or cause segmentation faults. This could be used as part of a larger exploit chain to achieve code execution through another vulnerability.

## Attachments
No attachments
