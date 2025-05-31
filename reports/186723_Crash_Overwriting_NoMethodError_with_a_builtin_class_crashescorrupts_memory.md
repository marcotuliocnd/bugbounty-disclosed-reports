# Crash: Overwriting NoMethodError with a builtin class crashes/corrupts memory

## Report Details
- **Report ID**: 186723
- **URL**: https://hackerone.com/reports/186723
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-30T03:14:56.540Z
- **Disclosed**: 2017-03-01T10:15:16.157Z

## Reporter
- **Username**: brakhane
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Uhm, while testing this I seem to have broken `https://mruby.science`.. Ooops, sorry about that!

Anyway, here's the bug:
Overwriting (at least, not sure about other triggers) `NoMethodError` with a builtin class like `Fixnum` or `Integer` leads to a rather interesting behavior. `https://mruby.science` didn't crash all the times (reads: it sometimes does report a `MRubyEngine::EngineTimeQuotaError`), but sometimes it does report the 'Application Error' page after a long time. My local sandbox behaves somewhat like this: it prints the `MRubyEngine::EngineTimeQuotaError` error but crashes anyway.

The root cause is that triggering the `NoMethodError` triggers another `NoMethodError` when `mrb_no_method_error in error.c` tries to call `new` on the new `NoMethodError`, which has no new.

# PoC
```
NoMethodError = Fixnum
boom!
```



# Fix
I've attached a fix similar to #186719, this time moving the `NoMethodError` into `mrb_state`

# Traces
sandbox:

$ bin/sandbox new_crashes/fixnum_exception.mrb       
```                                        
bin/sandbox:20: [BUG] Segmentation fault at 0x0000000000000a
ruby 2.3.3p222 (2016-11-21 revision 56859) [x86_64-linux]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:000f78 EVAL   bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:000670 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
bin/sandbox:20:in `<main>'
bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 RIP: 0x00007f4ff550b25f RBP: 0x00000000000003bc RSP: 0x00007f4ff4043720
 RAX: 0x00007f4ff40c0290 RBX: 0x0000000000000384 RCX: 0x00007f4ff40c2290
 RDX: 0x0000000000000400 RDI: 0x00007f4ff40684e0 RSI: 0x000000000000000a
  R8: 0x00007f4ff40c2070  R9: 0x00007f4ff40dcab0 R10: 0x0000000000000007
 R11: 0x00007f4ff4076510 R12: 0x00007f4ff4074a10 R13: 0x00007f4ff40684e0
 R14: 0x0000000000000000 R15: 0x00007f4ff5569dd2 EFL: 0x0000000000010246

-- C level backtrace information -------------------------------------------
/usr/lib/libruby.so.2.3 [0x7f4ff95cc455]
/usr/lib/libruby.so.2.3 [0x7f4ff95cc68c]
/usr/lib/libruby.so.2.3 [0x7f4ff94a6e34]
/usr/lib/libruby.so.2.3 [0x7f4ff95586ce]
/usr/lib/libc.so.6 [0x7f4ff90cc0b0]
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mark_context_stack+0x8f) [0x7f4ff550b25f] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/include/mruby/boxing_word.h:83
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(incremental_gc.part.11+0x5a2) [0x7f4ff550bd92] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/gc.c:938
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_incremental_gc+0x1f3) [0x7f4ff550c3a3] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/gc.c:1062
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_obj_alloc+0xfd) [0x7f4ff550cb8d] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/gc.c:486
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_str_new+0x24) [0x7f4ff54e61c4] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/string.c:59
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vformat+0x123) [0x7f4ff550db83] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/error.c:344
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_no_method_error+0x9a) [0x7f4ff550e33a] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/error.c:508
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_method_missing+0x95) [0x7f4ff54fd3b5] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1468
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_bob_missing+0x4d) [0x7f4ff54fd46d] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1513
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_with_block+0x27f) [0x7f4ff54f0c1f] 
[......]
/home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:407
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_argv+0xc) [0x7f4ff54f11dc] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:424
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall+0x240) [0x7f4ff54f1430] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:319
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_no_method_error+0x12d) [0x7f4ff550e3cd] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/error.c:508
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_method_missing+0x95) [0x7f4ff54fd3b5] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1468
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_bob_missing+0x4d) [0x7f4ff54fd46d] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1513
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_with_block+0x27f) [0x7f4ff54f0c1f] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:407
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_argv+0xc) [0x7f4ff54f11dc] /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:424
/home/simon/git/shopify/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall+0x240) bin/sandbox:20:in `sandbox_eval': exceeded quota of 100 ms. (MRubyEngine::EngineTimeQuotaError)
	from bin/sandbox:20:in `<main>'
```

gdb:
```
$ gdb attach 5534
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
Attaching to process 5534
Reading symbols from /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/build/host/bin/mirb...done.
Reading symbols from /usr/lib/libm.so.6...(no debugging symbols found)...done.
Reading symbols from /usr/lib/libreadline.so.7...(no debugging symbols found)...done.
Reading symbols from /usr/lib/libncursesw.so.6...(no debugging symbols found)...done.
Reading symbols from /usr/lib/libc.so.6...(no debugging symbols found)...done.
Reading symbols from /lib64/ld-linux-x86-64.so.2...(no debugging symbols found)...done.
0x00007fcacf29b131 in pselect () from /usr/lib/libc.so.6
(gdb) c
Continuing.

Program received signal SIGSEGV, Segmentation fault.
mark_context_stack (mrb=mrb@entry=0xb1e010, c=c@entry=0xb2a540) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/gc.c:532
532	    if (!mrb_immediate_p(v)) {
(gdb) bt
#0  mark_context_stack (mrb=mrb@entry=0xb1e010, c=c@entry=0xb2a540) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/gc.c:532
#1  0x0000000000428a2c in mark_context (c=0xb2a540, mrb=0xb1e010) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/gc.c:550
#2  root_scan_phase (mrb=0xb1e010, gc=0xb1e0e8) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/gc.c:820
#3  0x0000000000429793 in incremental_gc (limit=18446744073709551615, gc=0xb1e0e8, mrb=0xb1e010) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/gc.c:1022
#4  incremental_gc_until (to_state=<optimized out>, gc=<optimized out>, mrb=<optimized out>) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/gc.c:1053
#5  mrb_incremental_gc (mrb=0xb1e010) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/gc.c:1104
#6  0x0000000000429f4d in mrb_obj_alloc (mrb=mrb@entry=0xb1e010, ttype=ttype@entry=MRB_TT_STRING, cls=0xb28550) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/gc.c:486
#7  0x0000000000406404 in str_new (len=0, p=0x48c0a2 "", mrb=mrb@entry=0xb1e010) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/string.c:59
#8  mrb_str_new (mrb=mrb@entry=0xb1e010, p=0x48c0a2 "", len=0) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/string.c:185
#9  0x000000000042af43 in mrb_vformat (mrb=mrb@entry=0xb1e010, format=format@entry=0x48c086 "undefined method '%S' for %S", ap=ap@entry=0x7ffe576cfe88) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/error.c:344
#10 0x000000000042b8ba in mrb_no_method_error (mrb=mrb@entry=0xb1e010, id=id@entry=11, args=..., args@entry=..., fmt=fmt@entry=0x48c086 "undefined method '%S' for %S") at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/error.c:508
#11 0x000000000041d5f5 in mrb_method_missing (mrb=mrb@entry=0xb1e010, name=11, self=self@entry=..., args=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1468
#12 0x000000000041d6ad in mrb_bob_missing (mrb=0xb1e010, mod=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1513
#13 0x0000000000410e5f in mrb_funcall_with_block (mrb=mrb@entry=0xb1e010, self=..., mid=<optimized out>, argc=<optimized out>, argc@entry=3, argv=argv@entry=0x7ffe576d01c0, blk=..., blk@entry=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:407
#14 0x000000000041141c in mrb_funcall_argv (mrb=mrb@entry=0xb1e010, self=..., self@entry=..., mid=<optimized out>, argc=argc@entry=3, argv=argv@entry=0x7ffe576d01c0) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:424
#15 0x0000000000411670 in mrb_funcall (mrb=mrb@entry=0xb1e010, self=..., name=name@entry=0x48a81f "new", argc=argc@entry=3) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:319

[......]
#1822 0x000000000042b94d in mrb_no_method_error (mrb=mrb@entry=0xb1e010, id=id@entry=11, args=args@entry=..., fmt=fmt@entry=0x48c086 "undefined method '%S' for %S") at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/error.c:508
#1823 0x000000000041d5f5 in mrb_method_missing (mrb=mrb@entry=0xb1e010, name=11, self=self@entry=..., args=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1468
#1824 0x000000000041d6ad in mrb_bob_missing (mrb=0xb1e010, mod=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1513
#1825 0x0000000000410e5f in mrb_funcall_with_block (mrb=mrb@entry=0xb1e010, self=..., mid=<optimized out>, argc=<optimized out>, argc@entry=3, argv=argv@entry=0x7ffe5771df80, blk=..., blk@entry=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:407
#1826 0x000000000041141c in mrb_funcall_argv (mrb=mrb@entry=0xb1e010, self=..., self@entry=..., mid=<optimized out>, argc=argc@entry=3, argv=argv@entry=0x7ffe5771df80) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:424
#1827 0x0000000000411670 in mrb_funcall (mrb=mrb@entry=0xb1e010, self=..., name=name@entry=0x48a81f "new", argc=argc@entry=3) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:319
#1828 0x000000000042b94d in mrb_no_method_error (mrb=mrb@entry=0xb1e010, id=id@entry=11, args=args@entry=..., fmt=fmt@entry=0x48c086 "undefined method '%S' for %S") at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/error.c:508
#1829 0x000000000041d5f5 in mrb_method_missing (mrb=mrb@entry=0xb1e010, name=11, self=self@entry=..., args=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1468
#1830 0x000000000041d6ad in mrb_bob_missing (mrb=0xb1e010, mod=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1513
#1831 0x0000000000410e5f in mrb_funcall_with_block (mrb=mrb@entry=0xb1e010, self=..., mid=<optimized out>, argc=<optimized out>, argc@entry=3, argv=argv@entry=0x7ffe5771e3a0, blk=..., blk@entry=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:407
#1832 0x000000000041141c in mrb_funcall_argv (mrb=mrb@entry=0xb1e010, self=..., self@entry=..., mid=<optimized out>, argc=argc@entry=3, argv=argv@entry=0x7ffe5771e3a0) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:424
#1833 0x0000000000411670 in mrb_funcall (mrb=mrb@entry=0xb1e010, self=..., name=name@entry=0x48a81f "new", argc=argc@entry=3) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:319
#1834 0x000000000042b94d in mrb_no_method_error (mrb=mrb@entry=0xb1e010, id=id@entry=11, args=args@entry=..., fmt=fmt@entry=0x48c086 "undefined method '%S' for %S") at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/error.c:508
#1835 0x000000000041d5f5 in mrb_method_missing (mrb=mrb@entry=0xb1e010, name=11, self=self@entry=..., args=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1468
#1836 0x000000000041d6ad in mrb_bob_missing (mrb=0xb1e010, mod=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1513
#1837 0x0000000000410e5f in mrb_funcall_with_block (mrb=mrb@entry=0xb1e010, self=..., mid=<optimized out>, argc=<optimized out>, argc@entry=3, argv=argv@entry=0x7ffe5771e7c0, blk=..., blk@entry=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:407
#1838 0x000000000041141c in mrb_funcall_argv (mrb=mrb@entry=0xb1e010, self=..., self@entry=..., mid=<optimized out>, argc=argc@entry=3, argv=argv@entry=0x7ffe5771e7c0) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:424
#1839 0x0000000000411670 in mrb_funcall (mrb=mrb@entry=0xb1e010, self=..., name=name@entry=0x48a81f "new", argc=argc@entry=3) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:319
#1840 0x000000000042b94d in mrb_no_method_error (mrb=mrb@entry=0xb1e010, id=id@entry=11, args=args@entry=..., fmt=fmt@entry=0x48c086 "undefined method '%S' for %S") at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/error.c:508
#1841 0x000000000041d5f5 in mrb_method_missing (mrb=mrb@entry=0xb1e010, name=11, self=self@entry=..., args=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1468
#1842 0x000000000041d6ad in mrb_bob_missing (mrb=0xb1e010, mod=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1513
#1843 0x0000000000410e5f in mrb_funcall_with_block (mrb=mrb@entry=0xb1e010, self=..., mid=<optimized out>, argc=<optimized out>, argc@entry=3, argv=argv@entry=0x7ffe5771ebe0, blk=..., blk@entry=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:407
#1844 0x000000000041141c in mrb_funcall_argv (mrb=mrb@entry=0xb1e010, self=..., self@entry=..., mid=<optimized out>, argc=argc@entry=3, argv=argv@entry=0x7ffe5771ebe0) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:424
#1845 0x0000000000411670 in mrb_funcall (mrb=mrb@entry=0xb1e010, self=..., name=name@entry=0x48a81f "new", argc=argc@entry=3) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:319
#1846 0x000000000042b94d in mrb_no_method_error (mrb=mrb@entry=0xb1e010, id=id@entry=627, args=args@entry=..., fmt=fmt@entry=0x48c086 "undefined method '%S' for %S") at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/error.c:508
#1847 0x000000000041d5f5 in mrb_method_missing (mrb=mrb@entry=0xb1e010, name=627, self=self@entry=..., args=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1468
#1848 0x000000000041d6ad in mrb_bob_missing (mrb=0xb1e010, mod=...) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/class.c:1513
#1849 0x0000000000412d62 in mrb_vm_exec (mrb=mrb@entry=0xb1e010, proc=<optimized out>, proc@entry=0xb20e70, pc=<optimized out>) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
#1850 0x0000000000418a47 in mrb_vm_run (mrb=mrb@entry=0xb1e010, proc=proc@entry=0xb20e70, self=..., stack_keep=stack_keep@entry=1) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
#1851 0x0000000000402b7e in main (argc=<optimized out>, argv=<optimized out>) at /home/simon/git/shopify/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549
(gdb) info registers
rax            0xc43420	12858400
rbx            0x384	900
rcx            0xc47820	12875808
rdx            0x880	2176
rsi            0xa	10
rdi            0xb1e010	11657232
rbp            0x862	0x862
rsp            0x7ffe576cfd50	0x7ffe576cfd50
r8             0xc47730	12875568
r9             0x30	48
r10            0x7	7
r11            0xb2c040	11714624
r12            0xb2a540	11707712
r13            0xb1e010	11657232
r14            0x7ffe576cfe88	140730365181576
r15            0x48c0a2	4767906
rip            0x42861f	0x42861f <mark_context_stack+143>
eflags         0x10246	[ PF ZF IF RF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0
(gdb) 
```


## Attachments
No attachments
