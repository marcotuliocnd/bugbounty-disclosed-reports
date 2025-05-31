# Invalid parameter in memcpy function trough openssl_pbkdf2

## Report Details
- **Report ID**: 190933
- **URL**: https://hackerone.com/reports/190933
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-13T20:43:44.109Z
- **Disclosed**: 2017-02-08T17:01:52.502Z

## Reporter
- **Username**: emyei
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream: https://bugs.php.net/bug.php?id=72776

Summary:
------------
When key_length parameter is greater than 0x7fffffff, size parameter is interpreted as negative in memcpy, inside PKCS5_PBKDF2_HMAC function (libcrypto.so).

This issue happens only in PHP 5.6 branch. PHP 7.0 avoids this issue trough PHP_OPENSSL_CHECK_NUMBER_CONVERSION macro: https://github.com/php/php-src/blob/PHP-7.0.10/ext/openssl/openssl.c#L541

==11421==ERROR: AddressSanitizer: negative-size-param: (size=-1)
    #0 0x7f919d1029a1 in __asan_memcpy (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x8c9a1)
    #1 0x7f919b2c87e9 in PKCS5_PBKDF2_HMAC (/lib/x86_64-linux-gnu/libcrypto.so.1.0.0+0x1317e9)
    #2 0x5be33e in zif_openssl_pbkdf2 /home/operac/build2/php-src-56/ext/openssl/openssl.c:4080
    #3 0x1d5b393 in zend_do_fcall_common_helper_SPEC /home/operac/build2/php-src-56/Zend/zend_vm_execute.h:558
    #4 0x1c0463c in execute_ex /home/operac/build2/php-src-56/Zend/zend_vm_execute.h:363
    #5 0x194c382 in zend_execute_scripts /home/operac/build2/php-src-56/Zend/zend.c:1341
    #6 0x169a2df in php_execute_script /home/operac/build2/php-src-56/main/main.c:2613
    #7 0x1d64366 in do_cli /home/operac/build2/php-src-56/sapi/cli/php_cli.c:994
    #8 0x4550a0 in main /home/operac/build2/php-src-56/sapi/cli/php_cli.c:1378
    #9 0x7f919ab4482f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #10 0x4556b8 in _start (/home/operac/build2/bin/php+0x4556b8)

Address 0x7ffd544616b0 is located in stack of thread T0
SUMMARY: AddressSanitizer: negative-size-param ??:0 __asan_memcpy
==11421==ABORTING


Patch:  https://github.com/php/php-src/commit/493b2bff02531b0ead233177a2a0846c75e94777


Fixed for PHP 5.6.29

## Attachments
No attachments
