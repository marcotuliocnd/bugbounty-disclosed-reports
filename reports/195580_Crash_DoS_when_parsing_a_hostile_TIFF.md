# Crash (DoS) when parsing a hostile TIFF

## Report Details
- **Report ID**: 195580
- **URL**: https://hackerone.com/reports/195580
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-03T20:22:13.683Z
- **Disclosed**: 2019-10-13T09:30:35.525Z

## Reporter
- **Username**: aerodudrizzt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The issue was reported and resolved by PHP's security team:
* Ticket #73737: https://bugs.php.net/bug.php?id=73737
* Git Commit: http://git.php.net/?p=php-src.git;a=commit;h=1cda0d7c2ffb62d8331c64e703131d9cabdc03ea

The EXIF module in all PHP versions (5.6.9 and below, 7.1.0 and below) is vulnerable to a DoS attack when parsing a hostile EXIF file of type TIFF. Here are the technical details:
* File: ext\exif\exif.c
* Function:  exif_convert_any_to_int
* Vulnerable tag: TAG_FMT_SRATIONAL

The relevant code is:
```
	case TAG_FMT_SRATIONAL:
		s_den = php_ifd_get32s(4+(char *)value, motorola_intel);
		if (s_den == 0) {
			return 0;
		} else {
			return php_ifd_get32s(value, motorola_intel) / s_den;
		}
```
On intel chipsets this division can trigger an exception in this edge case: -1 / MIN_INT (see link: http://x86.renejeschke.de/html/file_module_x86_id_72.html):

When tested with a simple PHP script and a specially crafted TIFF file (with an .exif extension), it triggered the following segmentation fault:
```
<?php
	$e = exif_thumbnail("example_hostile.exif");
	echo "Loaded the exif picture\n";
?>
```

And here is the trace:
Program terminated with signal SIGFPE, Arithmetic exception.
```
#0  0xb4fd9d74 in ?? () from /usr/lib/php/20151012/exif.so
(gdb) bt
#0  0xb4fd9d74 in ?? () from /usr/lib/php/20151012/exif.so
#1  0xb4fdb11f in ?? () from /usr/lib/php/20151012/exif.so
#2  0xb4fdbd40 in ?? () from /usr/lib/php/20151012/exif.so
#3  0xb4fdbc11 in ?? () from /usr/lib/php/20151012/exif.so
#4  0xb4fdc134 in ?? () from /usr/lib/php/20151012/exif.so
#5  0xb4fdc886 in zif_exif_thumbnail () from /usr/lib/php/20151012/exif.so
#6  0x802f8662 in execute_internal ()
#7  0x80251dce in dtrace_execute_internal ()
#8  0x802e9f65 in ?? ()
#9  0x802a26da in execute_ex ()
#10 0x80251c35 in dtrace_execute_ex ()
#11 0x802fa1b6 in zend_execute ()
#12 0x8026210d in zend_execute_scripts ()
#13 0x80201054 in php_execute_script ()
#14 0x802fc01f in ?? ()
#15 0x800db64f in main ()
(gdb) info reg
eax            0x80000000	-2147483648
ecx            0x1	1
edx            0xffffffff	-1
ebx            0x0	0
esp            0xbff4c188	0xbff4c188
ebp            0xb525d302	0xb525d302
esi            0xb525d30a	-1255812342
edi            0xffffffff	-1
eip            0xb4fd9d74	0xb4fd9d74
eflags         0x210202	[ IF RF ID ]
cs             0x73	115
ss             0x7b	123
ds             0x7b	123
es             0x7b	123
fs             0x0	0
gs             0x33	51
```
One can see that the registers involved are edx (-1) and eax (MIN_INT), as intel describes in their chipset specs.

## Attachments
No attachments
