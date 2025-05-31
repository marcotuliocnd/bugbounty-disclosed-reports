# stack-buffer-overflow through "ResourceBundle" methods

## Report Details
- **Report ID**: 175316
- **URL**: https://hackerone.com/reports/175316
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-12T07:00:23.006Z
- **Disclosed**: 2019-10-13T18:10:53.259Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream Bug
---
https://bugs.php.net/bug.php?id=73218

Summary
--
ResourceBundle::create and ResourceBundle::getLocales  methods (and their respective functions) are vulnerables to stack buffer overflow when bundlename parameter length is equal or close to 0x7fffffff, due to a type confusion in CharString::ensureCapacity at libicu.

PHP could mitigate this issue by checking that the bundlename parameter is not bigger than PHP_MAXPATHLEN constant before calling libicu.

GDB output:
```

LD_LIBRARY_PATH=/home/operac/icu58/lib USE_ZEND_ALLOC=0 ASAN_OPTIONS=detect_leaks=0 gdb -q --args  /home/operac/build4/bin/php -dextension=/home/operac/build4/lib/php/20151012-debug/intl.so -n poc.php
No symbol table is loaded.  Use the "file" command.
Breakpoint 1 (__asan_report_error) pending.
Reading symbols from /home/operac/build4/bin/php...done.
gdb-peda$ b charstr.cpp:87
No source file named charstr.cpp.
Breakpoint 2 (charstr.cpp:87) pending.
gdb-peda$ b charstr.cpp:135
No source file named charstr.cpp.
Breakpoint 3 (charstr.cpp:135) pending.
gdb-peda$ r
Starting program: /home/operac/build4/bin/php -dextension=/home/operac/build4/lib/php/20151012-debug/intl.so -n poc.php
...
Breakpoint 3, icu::CharString::ensureCapacity (this=0x7fffffff9598, capacity=0x80000000, desiredCapacityHint=0x0, errorCode=@0x7fffffff9e90: U_ZERO_ERROR) at charstr.cpp:135
135         if(capacity>buffer.getCapacity()) {
gdb-peda$ p/d capacity
$1 = -2147483648
gdb-peda$ p/d buffer.getCapacity()
$2 = 40
gdb-peda$ p capacity>buffer.getCapacity()
$3 = 0x0                // !! false
gdb-peda$ c
Continuing.
...
Breakpoint 2, icu::CharString::append (this=0x7fffffff9598, s=0x7ffeec3f9800 '/' <repeats 200 times>..., sLength=0x7fffffff, errorCode=@0x7fffffff9e90: U_ZERO_ERROR) at charstr.cpp:87
87                  uprv_memcpy(buffer.getAlias()+len, s, sLength);
gdb-peda$ p sLength
$4 = 0x7fffffff                    // !! buffer overflow
 ```

Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=d946d102936525bc7dcd01f3827d0a6e0bb971b0
```

Fixed for PHP 5.6.27, PHP 7.0.12
--
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php#7.0.12


## Attachments
No attachments
