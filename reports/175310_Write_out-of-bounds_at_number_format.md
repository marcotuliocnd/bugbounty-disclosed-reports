# Write out-of-bounds at number_format

## Report Details
- **Report ID**: 175310
- **URL**: https://hackerone.com/reports/175310
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-12T06:41:36.940Z
- **Disclosed**: 2017-02-07T17:56:36.717Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Upstream Bug
---
https://bugs.php.net/bug.php?id=73240

Summary
--
When the *number_format* function receives  *decimals* parameter and *dec_point* length parameter equal or close to 0x7fffffff,  integer overflow occurs in *reslen* variable, this causes a write heap overflow. 

```
USE_ZEND_ALLOC=0 ASAN_OPTIONS=detect_leaks=0 gdb -q --args /home/operac/build4/bin/php -n poc.php
...
gdb-peda$ b math.c:1168
Breakpoint 2 at 0x1497c0c: file /home/operac/build4/php-src/ext/standard/math.c, line 1168.
gdb-peda$ r
Starting program: /home/operac/build4/bin/php -n poc.php
...
Breakpoint 2, _php_math_number_format_ex (d=<optimized out>, dec=0x7fffffff, dec_point=0x7fff6f3c1818 '/' <repeats 200 times>..., dec_point_len=0x7fffffff, thousand_sep=0x60300006e758 ",", thousand_sep_len=0x1)
    at /home/operac/build4/php-src/ext/standard/math.c:1168
1168                    reslen += dec;
gdb-peda$ p reslen
$1 = 0x5
gdb-peda$ p dec
$2 = 0x7fffffff
gdb-peda$ p/d reslen+dec
$4 = -2147483644              /* Integer overflow */
gdb-peda$ b math.c:1176
Breakpoint 3 at 0x1497460: file /home/operac/build4/php-src/ext/standard/math.c, line 1176.
gdb-peda$ c
Continuing.
...
Breakpoint 3, _php_math_number_format_ex (d=<optimized out>, dec=0x7fffffff, dec_point=0x7fff6f3c1818 '/' <repeats 200 times>..., dec_point_len=0x7fffffff, thousand_sep=0x60300006e758 ",", thousand_sep_len=0x1)
    at /home/operac/build4/php-src/ext/standard/math.c:1177
1177                    reslen++;
gdb-peda$ p reslen
$5 = 0x3                  /* reslen decreases*/
gdb-peda$ b math.c:1193
Breakpoint 4 at 0x1497c5b: file /home/operac/build4/php-src/ext/standard/math.c, line 1193.
gdb-peda$ c
...
Breakpoint 4, _php_math_number_format_ex (d=<optimized out>, dec=<optimized out>, dec_point=0x7fff6f3c1818 '/' <repeats 200 times>..., dec_point_len=0x7fffffff, thousand_sep=0x60300006e758 ",", thousand_sep_len=0x1)
    at /home/operac/build4/php-src/ext/standard/math.c:1193
1193                    while (topad--) {
1194                            *t-- = '0';
1195                    }
gdb-peda$ p/d topad
$6 = 2147483329           /* NULL write out of bounds */
```

Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=8259130b6bc752968856b352c9e7f8e03a8c0a8e
```

Fixed for PHP 5.6.27, PHP 7.0.12
--
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php#7.0.12


## Attachments
No attachments
