# Out of bound read in exif_process_IFD_in_MAKERNOTE

## Report Details
- **Report ID**: 152231
- **URL**: https://hackerone.com/reports/152231
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-19T07:52:42.525Z
- **Disclosed**: 2016-08-30T18:48:55.696Z

## Reporter
- **Username**: hoangnguyen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I have found some vulnerable code that lacks check size of buffer may lead to memory out of read or write.

Take a look at : 
```
static int exif_process_IFD_in_MAKERNOTE(image_info_type *ImageInfo, char * value_ptr, int value_len, char *offset_base, size_t IFDlength, size_t displacement)
{
*****SNIP*******
	switch (maker_note->offset_mode) {
		case MN_OFFSET_MAKER:
			offset_base = value_ptr;
			break;
		case MN_OFFSET_GUESS:
			offset_diff = 2 + NumDirEntries*12 + 4 - php_ifd_get32u(dir_start+10, ImageInfo->motorola_intel);
#ifdef EXIF_DEBUG
			exif_error_docref(NULL EXIFERR_CC, ImageInfo, E_NOTICE, "Using automatic offset correction: 0x%04X", ((int)dir_start-(int)offset_base+maker_note->offset+displacement) + offset_diff);
#endif
			offset_base = value_ptr + offset_diff;
			break;
		default:
		case MN_OFFSET_NORMAL:
			break;
	}

	if ((2+NumDirEntries*12) > value_len)
*****SNIP*******
}
```
As you can see this line while processing markernote of "Cannon"
```
offset_diff = 2 + NumDirEntries*12 + 4 - php_ifd_get32u(dir_start+10, ImageInfo->motorola_intel);
```
Because no checking the value return from php_ifd_get32u(dir_start+10, ImageInfo->motorola_intel); and weak check value of NumDirEntries, so attacker can control both value to make offset_diff may out of size offset_base.

That result may lead to information leak or memory corruption.

Here jpeg image link to lead to this problem : https://drive.google.com/file/d/0B0D1DYQpkA9UZmVOMzYwQlBnSGM/view?usp=sharing

Test script:
---------------
```
<?php
	$exif = exif_read_data('exif/gen.jpg');
	var_dump($exif);
?>
```
I will show you the variable of offset_diff, offset_base before and after hitting that code path.
```
[----------------------------------registers-----------------------------------]
RAX: 0x0
RBX: 0x18
RCX: 0x0
RDX: 0x7ffff3e7607e --> 0x29286fffffa92
RSI: 0x0
RDI: 0x7ffff3e7607e --> 0x29286fffffa92
RBP: 0x7fffffffa8a0 --> 0x7fffffffa9d0 --> 0x7fffffffaa30 --> 0x7fffffffab60 --> 0x7fffffffabc0 --> 0x7fffffffac00 --> 0x7fffffffac30 --> 0x7fffffffacd0 --> 0x7fffffffad10 --> 0x7fffffffadf0 --> 0x7fffffffb0d0 --> 0x7fffffffb100 --> 0x7fffffffb130 --> 0x7fffffffb170 --> 0x7fffffffb280 --> 0x7fffffffd580 --> 0x7fffffffe900 --> 0x7fffffffea50 --> 0xa15f90 (<__libc_csu_init>:	push   r15)
RSP: 0x7fffffffa830 --> 0xc ('\x0c')
RIP: 0x613c3d (<exif_process_IFD_in_MAKERNOTE+489>:	call   0x610603 <php_ifd_get32u>)
R8 : 0x594
R9 : 0xc ('\x0c')
R10: 0x1c
R11: 0x206
R12: 0x42c170 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffeb30 --> 0x2
R14: 0x7ffff3e14030 --> 0x7ffff3e5fb80 --> 0x9a28f2 (<ZEND_DO_ICALL_SPEC_HANDLER>:	push   rbp)
R15: 0x7ffff3e5fb80 --> 0x9a28f2 (<ZEND_DO_ICALL_SPEC_HANDLER>:	push   rbp)
EFLAGS: 0x206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x613c34 <exif_process_IFD_in_MAKERNOTE+480>:	add    rdx,0xa
   0x613c38 <exif_process_IFD_in_MAKERNOTE+484>:	mov    esi,eax
   0x613c3a <exif_process_IFD_in_MAKERNOTE+486>:	mov    rdi,rdx
=> 0x613c3d <exif_process_IFD_in_MAKERNOTE+489>:	call   0x610603 <php_ifd_get32u>
   0x613c42 <exif_process_IFD_in_MAKERNOTE+494>:	sub    ebx,eax
   0x613c44 <exif_process_IFD_in_MAKERNOTE+496>:	mov    eax,ebx
   0x613c46 <exif_process_IFD_in_MAKERNOTE+498>:	add    eax,0x6
   0x613c49 <exif_process_IFD_in_MAKERNOTE+501>:	mov    DWORD PTR [rbp-0x24],eax
Guessed arguments:
arg[0]: 0x7ffff3e7607e --> 0x29286fffffa92
arg[1]: 0x0
arg[2]: 0x7ffff3e7607e --> 0x29286fffffa92
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffa830 --> 0xc ('\x0c')
0008| 0x7fffffffa838 --> 0x594
0016| 0x7fffffffa840 --> 0x7ffff3e76008 --> 0x8002a4949
0024| 0x7fffffffa848 --> 0x1c006117bc
0032| 0x7fffffffa850 --> 0x7ffff3e76074 --> 0x1000202080002
0040| 0x7fffffffa858 --> 0x7fffffffae50 --> 0x7ffff3e5fa00 --> 0x12b9700 --> 0x8d43d1 (<php_stdiop_write>:	push   rbp)
0048| 0x7fffffffa860 --> 0x7fffffffa8a0 --> 0x7fffffffa9d0 --> 0x7fffffffaa30 --> 0x7fffffffab60 --> 0x7fffffffabc0 --> 0x7fffffffac00 --> 0x7fffffffac30 --> 0x7fffffffacd0 --> 0x7fffffffad10 --> 0x7fffffffadf0 --> 0x7fffffffb0d0 --> 0x7fffffffb100 --> 0x7fffffffb130 --> 0x7fffffffb170 --> 0x7fffffffb280 --> 0x7fffffffd580 --> 0x7fffffffe900 --> 0x7fffffffea50 --> 0xa15f90 (<__libc_csu_init>:	push   r15)
0056| 0x7fffffffa868 --> 0x5
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 5, 0x0000000000613c3d in exif_process_IFD_in_MAKERNOTE (
    ImageInfo=0x7fffffffae50, value_ptr=0x7ffff3e76074 "\002", value_len=0x1c,
    offset_base=0x7ffff3e76008 "II*", IFDlength=0x594, displacement=0xc)
    at /home/vagrant/Sources_Ext/audit/src/php7.0-7.0.4/ext/exif/exif.c:2754
2754				offset_diff = 2 + NumDirEntries*12 + 4 - php_ifd_get32u(dir_start+10, ImageInfo->motorola_intel);
gdb-peda$ x/80gx offset_base
0x7ffff3e76008:	0x00000008002a4949	0x00010005011a0002
0x7ffff3e76018:	0x8769000004000000	0x0022000000010004
0x7ffff3e76028:	0x0005829a00060000	0x0000041200000001
0x7ffff3e76038:	0x000000010005829d	0x0002928600000444
0x7ffff3e76048:	0x00000da6000000a8	0x0000002c00028298
0x7ffff3e76058:	0x0002010f00000e4e	0x00000e7a00000005
0x7ffff3e76068:	0x000000070004927c	0x020800020000006c
0x7ffff3e76078:	0xfa92000000010002	0x00ff00029286ffff
0x7ffff3e76088:	0x5252000000000000	0x5252525252525252
0x7ffff3e76098:	0x5252525252525252	0x5252525252525252
0x7ffff3e760a8:	0x5252525252525252	0x5252525252525252
0x7ffff3e760b8:	0x5252525252525252	0x5252525252525252
0x7ffff3e760c8:	0x5252525252525252	0x5252525252525252
0x7ffff3e760d8:	0x5252525252525252	0x5252525252525252
0x7ffff3e760e8:	0x5252525252525252	0x00f2525252525252
.....
0x7ffff3e76568:	0x5454545454545454	0x5454545454545454
0x7ffff3e76578:	0x5454545454545454	0x5454545454545454
0x7ffff3e76588:	0x5454545454545454	0x5454545454545454
0x7ffff3e76598:	0x00000000d9ff5454	0x0000000000000000
0x7ffff3e765a8:	0x0000000000000000	0x0000000000000000
0x7ffff3e765b8:	0x0000000000000000	0x0000000000000000
0x7ffff3e765c8:	0x0000000000000000	0x0000000000000000
0x7ffff3e765d8:	0x0000000000000000	0x000000000000059d
0x7ffff3e765e8:	0x0000000000b12b88	0x0000000000f774a0
0x7ffff3e765f8:	0x000009ce00000646	0x00007ffff3e76c00
```
As you see above at address *0x7ffff3e76598* is the end of offset_base.
Next i hit next to execute *offset_base = value_ptr + offset_diff;*
```
[----------------------------------registers-----------------------------------]
RAX: 0x7ffff3e76600 --> 0x7ffff3e76c00 --> 0x7ffff3e77200 --> 0x7ffff3e77800 --> 0x7ffff3e77e00 --> 0x7ffff3e78400 --> 0x7ffff3e78a00 --> 0x0
RBX: 0x586
RCX: 0x0
RDX: 0x58c
RSI: 0x0
RDI: 0x7ffff3e7607e --> 0x29286fffffa92
RBP: 0x7fffffffa8a0 --> 0x7fffffffa9d0 --> 0x7fffffffaa30 --> 0x7fffffffab60 --> 0x7fffffffabc0 --> 0x7fffffffac00 --> 0x7fffffffac30 --> 0x7fffffffacd0 --> 0x7fffffffad10 --> 0x7fffffffadf0 --> 0x7fffffffb0d0 --> 0x7fffffffb100 --> 0x7fffffffb130 --> 0x7fffffffb170 --> 0x7fffffffb280 --> 0x7fffffffd580 --> 0x7fffffffe900 --> 0x7fffffffea50 --> 0xa15f90 (<__libc_csu_init>:	push   r15)
RSP: 0x7fffffffa830 --> 0xc ('\x0c')
RIP: 0x613c5d (<exif_process_IFD_in_MAKERNOTE+521>:	nop)
R8 : 0x594
R9 : 0xc ('\x0c')
R10: 0x1c
R11: 0x206
R12: 0x42c170 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffeb30 --> 0x2
R14: 0x7ffff3e14030 --> 0x7ffff3e5fb80 --> 0x9a28f2 (<ZEND_DO_ICALL_SPEC_HANDLER>:	push   rbp)
R15: 0x7ffff3e5fb80 --> 0x9a28f2 (<ZEND_DO_ICALL_SPEC_HANDLER>:	push   rbp)
EFLAGS: 0x216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x613c52 <exif_process_IFD_in_MAKERNOTE+510>:	mov    rax,QWORD PTR [rbp-0x50]
   0x613c56 <exif_process_IFD_in_MAKERNOTE+514>:	add    rax,rdx
   0x613c59 <exif_process_IFD_in_MAKERNOTE+517>:	mov    QWORD PTR [rbp-0x60],rax
=> 0x613c5d <exif_process_IFD_in_MAKERNOTE+521>:	nop
   0x613c5e <exif_process_IFD_in_MAKERNOTE+522>:	mov    edx,DWORD PTR [rbp-0x28]
   0x613c61 <exif_process_IFD_in_MAKERNOTE+525>:	mov    eax,edx
   0x613c63 <exif_process_IFD_in_MAKERNOTE+527>:	add    eax,eax
   0x613c65 <exif_process_IFD_in_MAKERNOTE+529>:	add    eax,edx
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffa830 --> 0xc ('\x0c')
0008| 0x7fffffffa838 --> 0x594
0016| 0x7fffffffa840 --> 0x7ffff3e76600 --> 0x7ffff3e76c00 --> 0x7ffff3e77200 --> 0x7ffff3e77800 --> 0x7ffff3e77e00 --> 0x7ffff3e78400 --> 0x7ffff3e78a00 --> 0x0
0024| 0x7fffffffa848 --> 0x1c006117bc
0032| 0x7fffffffa850 --> 0x7ffff3e76074 --> 0x1000202080002
0040| 0x7fffffffa858 --> 0x7fffffffae50 --> 0x7ffff3e5fa00 --> 0x12b9700 --> 0x8d43d1 (<php_stdiop_write>:	push   rbp)
0048| 0x7fffffffa860 --> 0x7fffffffa8a0 --> 0x7fffffffa9d0 --> 0x7fffffffaa30 --> 0x7fffffffab60 --> 0x7fffffffabc0 --> 0x7fffffffac00 --> 0x7fffffffac30 --> 0x7fffffffacd0 --> 0x7fffffffad10 --> 0x7fffffffadf0 --> 0x7fffffffb0d0 --> 0x7fffffffb100 --> 0x7fffffffb130 --> 0x7fffffffb170 --> 0x7fffffffb280 --> 0x7fffffffd580 --> 0x7fffffffe900 --> 0x7fffffffea50 --> 0xa15f90 (<__libc_csu_init>:	push   r15)
0056| 0x7fffffffa868 --> 0x5
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
2759				break;
gdb-peda$ p offset_base
$86 = 0x7ffff3e76600 ""
gdb-peda$ x/40gx offset_base
0x7ffff3e76600:	0x00007ffff3e76c00	0x0000000000000000
0x7ffff3e76610:	0x0000000000000000	0x0000000000000000
0x7ffff3e76620:	0x0000000000000000	0x0000000000000000
```
After calculate offset_base, you can see that address is out of own buffer

## Attachments
No attachments
