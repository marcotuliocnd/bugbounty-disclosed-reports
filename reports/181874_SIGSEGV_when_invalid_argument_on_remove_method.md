# SIGSEGV when invalid argument on remove_method

## Report Details
- **Report ID**: 181874
- **URL**: https://hackerone.com/reports/181874
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-13T05:35:56.082Z
- **Disclosed**: 2016-12-17T02:30:48.759Z

## Reporter
- **Username**: jpenalbae
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
There is an invalid memory read on mruby when calling to `remove_method` with invalid arguments which causes a SIGSEGV which leads into denial of service.

## Sample

The following code tries to remove a method using a `nil` as argument
```ruby
class Child
   remove_method nil
end
```

There are many other variants, such as using a float, an integer, a string, a Class, etc... Which obviously are non valid method symbols.
```ruby
class Child
   remove_method 1
   remove_method 2.123
   remove_method 'aaaa'
   remove_method Child
end
```

## Crash

Here we can see the crash (full crash output attached)
```
$ ruby bin/sandbox ../triage/uniq/min/segv/mrb_type > /tmp/full-crash.log
bin/sandbox:20: [BUG] Segmentation fault at 0x0000000000000e
ruby 2.3.1p112 (2016-04-26) [x86_64-linux-gnu]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:001e48 EVAL   bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:001e00 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
bin/sandbox:20:in `<main>'
bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 RIP: 0x00007f8c4d77d554 RBP: 0x00007f8c4c2fe4e0 RSP: 0x00007f8c4c2fc898
 RAX: 0x000000000000008f RBX: 0x0000000000000006 RCX: 0x00007f8c4d7fbf83
 RDX: 0x000000000000008f RDI: 0x00007f8c4c2fe4e0 RSI: 0x0000000000000006
  R8: 0x00007f8c4d7f842f  R9: 0x00007f8c4c2fe010 R10: 0x0000000000000191
 R11: 0x00007f8c4d77d540 R12: 0x0000000000000010 R13: 0x000000000000008f
 R14: 0x00007f8c4c306160 R15: 0x00007f8c4c306100 EFL: 0x0000000000010246

-- C level backtrace information -------------------------------------------
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f8c51a96ea5]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f8c51a970dc]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f8c51971364]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f8c51a22dbe]
/lib/x86_64-linux-gnu/libpthread.so.0 [0x7f8c516f5ed0]
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_respond_to+0x14) [0x7f8c4d77d554] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/include/mruby/boxing_word.h:71
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_check_convert_type+0x6b) [0x7f8c4d78c63b] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/object.c:310
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_check_string_type+0x1c) [0x7f8c4d7897cc] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/string.c:1743
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(join_ary+0xad) [0x7f8c4d78fe0d] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/array.c:1007
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_ary_join+0x2e) [0x7f8c4d790dbe] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/array.c:1031
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vformat+0x14b) [0x7f8c4d7a28cb] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/error.c:345
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_name_error+0x92) [0x7f8c4d7a2ae2] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/error.c:382
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_mod_remove_method+0x137) [0x7f8c4d77c3c7] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1985
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x762) [0x7f8c4d795cf2] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x57) [0x7f8c4d79b567] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mruby_engine_monitored_eval+0x113) [0x7f8c4d76f173] ../../../../ext/mruby_engine/eval_monitored.c:68
/lib/x86_64-linux-gnu/libpthread.so.0 [0x7f8c516ec464]
/lib/x86_64-linux-gnu/libc.so.6(__clone+0x6d) [0x7f8c50a6830d]

```

## Crash debug

```
(gdb) r
Starting program: /usr/bin/ruby bin/sandbox /tmp/crasher.rb
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff7ff5700 (LWP 21707)]
[New Thread 0x7ffff2348700 (LWP 21758)]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff2348700 (LWP 21758)]
mrb_class (v=..., mrb=mrb@entry=0x7ffff23494e0) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/include/mruby/class.h:50
50          return mrb_obj_ptr(v)->c;
(gdb) x/1i $rip
=> 0x7ffff37c8554 <mrb_respond_to+20>:  mov    rsi,QWORD PTR [rsi+0x8]
(gdb) i r rsi
rsi            0x6      6
(gdb) x/1xg $rsi+0x8
0xe:    Cannot access memory at address 0xe
```

The crash happens at `ext/mruby_engine/mruby/include/mruby/class.h:50`
```c
static inline struct RClass*
mrb_class(mrb_state *mrb, mrb_value v)
{
  switch (mrb_type(v)) {
  case MRB_TT_FALSE:
    if (mrb_fixnum(v))
      return mrb->false_class;
    return mrb->nil_class;
  case MRB_TT_TRUE:
    return mrb->true_class;
  case MRB_TT_SYMBOL:
    return mrb->symbol_class;
  case MRB_TT_FIXNUM:
    return mrb->fixnum_class;
  case MRB_TT_FLOAT:
    return mrb->float_class;
  case MRB_TT_CPTR:
    return mrb->object_class;
  case MRB_TT_ENV:
    return NULL;
  default:
    return mrb_obj_ptr(v)->c;  /* BUG: Bad memory access */
  }
}
```

If we check the vale `v`:
```
(gdb) print v
$1 = {
  value = {
    p = 0x6,
    {
      i_flag = 0,
      i = 3
    },
    {
      sym_flag = 6,
      sym = 0
    },
    bp = 0x6,
    fp = 0x6,
    vp = 0x6
  },
  w = 6
}
```
`mrb_obj_ptr` is the following macro
```c
#define mrb_obj_ptr(v)   ((struct RObject*)(mrb_ptr(v)))
```

So `mrb_obj_ptr(v)->c` would be equivalent to this:
```
(gdb) print ((struct RObject*)v)->c
Cannot access memory at address 0xe
(gdb) print &((struct RObject*)v)->c
$2 = (struct RClass **) 0xe
```

If we check the backtrace:
```
(gdb) bt
#0  mrb_class (v=..., mrb=mrb@entry=0x7ffff23494e0) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/include/mruby/class.h:50
#1  mrb_respond_to (mrb=mrb@entry=0x7ffff23494e0, obj=obj@entry=..., mid=mid@entry=143)
    at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1492
#2  0x00007ffff37d763b in convert_type (raise=0 '\000', method=0x7ffff384342f "to_str", tname=0x7ffff3844446 "String", val=..., mrb=0x7ffff23494e0)
    at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/object.c:310
#3  mrb_check_convert_type (mrb=mrb@entry=0x7ffff23494e0, val=..., type=type@entry=MRB_TT_STRING, tname=tname@entry=0x7ffff3844446 "String",
    method=method@entry=0x7ffff384342f "to_str") at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/object.c:352
#4  0x00007ffff37d47cc in mrb_check_string_type (mrb=mrb@entry=0x7ffff23494e0, str=..., str@entry=...)
    at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/string.c:1743
#5  0x00007ffff37dae0d in join_ary (mrb=mrb@entry=0x7ffff23494e0, ary=ary@entry=..., sep=sep@entry=..., list=...)
    at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/array.c:1007
#6  0x00007ffff37dbdbe in mrb_ary_join (mrb=mrb@entry=0x7ffff23494e0, ary=ary@entry=..., sep=...)
    at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/array.c:1031
#7  0x00007ffff37ed8cb in mrb_vformat (mrb=mrb@entry=0x7ffff23494e0, format=0x7ffff3843547 "method '%S' not defined in %S", ap=ap@entry=0x7ffff23479a8)
    at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/error.c:345
#8  0x00007ffff37edae2 in mrb_name_error (mrb=mrb@entry=0x7ffff23494e0, id=id@entry=0, fmt=fmt@entry=0x7ffff3843547 "method '%S' not defined in %S")
    at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/error.c:382
#9  0x00007ffff37c73c7 in remove_method (mid=0, mod=..., mrb=0x7ffff23494e0)
    at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1985
#10 mrb_mod_remove_method (mrb=0x7ffff23494e0, mod=...) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/class.c:2006
#11 0x00007ffff37e0cf2 in mrb_vm_exec (mrb=mrb@entry=0x7ffff23494e0, proc=<optimized out>, proc@entry=0x7ffff2351520, pc=<optimized out>)
    at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1165
#12 0x00007ffff37e6567 in mrb_vm_run (mrb=0x7ffff23494e0, proc=0x7ffff2351520, self=..., stack_keep=stack_keep@entry=0)
    at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:766
#13 0x00007ffff37ba173 in mruby_engine_monitored_eval (data=0x7ffff23493e0) at ../../../../ext/mruby_engine/eval_monitored.c:68
#14 0x00007ffff7737464 in start_thread (arg=0x7ffff2348700) at pthread_create.c:333
#15 0x00007ffff6ab330d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
(gdb)
```

We can see that whenever the desired method to delete is not found, mruby will raise an error. This is handled by `remove_method()` at `ext/mruby_engine/mruby/src/class.c:1985`:
```c
static void
remove_method(mrb_state *mrb, mrb_value mod, mrb_sym mid)
{
  struct RClass *c = mrb_class_ptr(mod);
  khash_t(mt) *h = find_origin(c)->mt;
  khiter_t k;

  if (h) {
    k = kh_get(mt, mrb, h, mid);
    if (k != kh_end(h)) {
      kh_del(mt, mrb, h, k);
      mrb_funcall(mrb, mod, "method_removed", 1, mrb_symbol_value(mid));
      return;
    }
  }

  mrb_name_error(mrb, mid, "method '%S' not defined in %S",
    mrb_sym2str(mrb, mid), mod);  /* <--- Raise an error */
}
```

Later on, mruby tries to convert the symbol in order to print it which is what causes the crash.

## Proposed fix

As the arguments for `remove_method()` should at least be a method type symbol. I propose the following check at `mrb_mod_remove_method()`
```diff
diff --git a/src/class.c b/src/class.c
index 47a6c84..a898b46 100644
--- a/src/class.c
+++ b/src/class.c
@@ -2003,6 +2003,11 @@ mrb_mod_remove_method(mrb_state *mrb, mrb_value mod)

   mrb_get_args(mrb, "*", &argv, &argc);
   while (argc--) {
+
+    /* Crash fix. Ignore invalid types */
+    if ((!argv->value.sym) || (argv->value.sym_flag != MRB_SYMBOL_FLAG))
+      mrb_raise(mrb, E_TYPE_ERROR, "Invalid type for remove_method");
+
     remove_method(mrb, mod, mrb_symbol(*argv));
     argv++;
   }
```

mruby with the fix applied stops the crash:
```
$ bin/sandbox /tmp/crasher.rb
bin/sandbox:20:in `sandbox_eval': Invalid type for remove_method (MRubyEngine::EngineRuntimeError)
        from bin/sandbox:20:in `<main>'
```

## Impact
This is not exploitable and its impact its limited to DoS of the service running the ruby sandbox.

## Attachments
- crasher.rb
- full-crash.log
- proposed-fix.patch
