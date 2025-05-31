# memcpy negative size parameter in php_resolve_path

## Report Details
- **Report ID**: 175311
- **URL**: https://hackerone.com/reports/175311
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-12T06:48:50.127Z
- **Disclosed**: 2017-02-07T17:56:44.527Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream Bug
---
https://bugs.php.net/bug.php?id=73189

Summary
--
Multiple PHP functions are vulnerable to negative size parameter in *memcpy* call through *php_resolve_path*. Some of the affected functions are: *file_get_contents, file_put_contents, file, readfile, get_meta_tags, gzopen, readgzfile, gzfile, tidy_repair_file, php_strip_whitespace, parse_ini_file, highlight_file*.

When *filename* parameter size is equal to 0x7fffffff, memcpy function will receive a negative size value in php_resolve_path. This was identified on a 64 bits linux build.

```
GDB output:

gdb -q --args /home/operac/build4/bin/php -n poc.php
No symbol table is loaded.  Use the "file" command.
Breakpoint 1 (__asan_report_error) pending.
Reading symbols from /home/operac/build4/bin/php...done.
gdb-peda$ b fopen_wrappers.c:555
Breakpoint 2 at 0x17333ac: file /home/operac/build4/php-src/main/fopen_wrappers.c, line 555.
gdb-peda$ r
Starting program: /home/operac/build4/bin/php -n poc.php
...
Breakpoint 2, php_resolve_path (filename=0x7fff6ec00018 'A' <repeats 200 times>..., filename_length=<optimized out>, 
    path=<optimized out>) at /home/operac/build4/php-src/main/fopen_wrappers.c:556
556				ptr = NULL;
gdb-peda$ b memcpy
Breakpoint 3 at 0x455469: memcpy. (43 locations)
gdb-peda$ c
...
Breakpoint 3, 0x00007ffff6ef6aa0 in memcpy () from /usr/lib/x86_64-linux-gnu/libasan.so.2
gdb-peda$ p/d $rdx
$1 = -2147483648

````

Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=da7e89cde880c66887caacd0a3eae7ecdacf9b2a
```

Fixed for PHP 5.6.27, PHP 7.0.12
--
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php#7.0.12


## Attachments
No attachments
