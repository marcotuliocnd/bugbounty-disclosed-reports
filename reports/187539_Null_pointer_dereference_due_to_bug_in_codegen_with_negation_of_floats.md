# Null pointer dereference due to bug in codegen with negation of floats

## Report Details
- **Report ID**: 187539
- **URL**: https://hackerone.com/reports/187539
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-02T00:35:38.948Z
- **Disclosed**: 2016-12-17T20:49:37.414Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Similar to bug #187536 but with floats, not ints.

Crash is:

```
p *case
  when nil
    -0.0
    nil
end
```

```
$ ./dev/bin/mruby crash.rb
crash.rb:1:3: '*' interpreted as argument prefix
Segmentation fault: 11
```

```
$ lldb ./dev/bin/mruby crash.rb
(lldb) target create "./dev/bin/mruby"
Current executable set to './dev/bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "crash.rb"
(lldb) r
Process 95703 launched: './dev/bin/mruby' (x86_64)
crash.rb:1:3: '*' interpreted as argument prefix
Process 95703 stopped
* thread #1: tid = 0x85d077b, 0x000000010000278b mruby`ary_concat + 27, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x18)
    frame #0: 0x000000010000278b mruby`ary_concat + 27
mruby`ary_concat:
->  0x10000278b <+27>: movl   0x18(%rdx), %ecx
    0x10000278e <+30>: addl   -0x1c(%rbp), %ecx
    0x100002791 <+33>: movl   %ecx, -0x20(%rbp)
    0x100002794 <+36>: movq   -0x8(%rbp), %rdi
(lldb) bt
* thread #1: tid = 0x85d077b, 0x000000010000278b mruby`ary_concat + 27, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x18)
  * frame #0: 0x000000010000278b mruby`ary_concat + 27
    frame #1: 0x0000000100002766 mruby`mrb_ary_concat + 70
    frame #2: 0x000000010004451f mruby`mrb_vm_exec + 25439
    frame #3: 0x000000010003e1a7 mruby`mrb_vm_run + 135
    frame #4: 0x0000000100046604 mruby`mrb_top_run + 100
    frame #5: 0x0000000100071adf mruby`load_exec + 1183
    frame #6: 0x0000000100071623 mruby`mrb_load_file_cxt + 67
    frame #7: 0x00000001000017d8 mruby`main + 904
    frame #8: 0x00007fff8a9db5ad libdyld.dylib`start + 1
(lldb) register read
General Purpose Registers:
       rax = 0x000000010100f030
       rbx = 0x0000000000000000
       rcx = 0x0000000000000000
       rdx = 0x0000000000000000
       rdi = 0x0000000100400390
       rsi = 0x0000000000000000
       rbp = 0x00007fff5fbfca00
       rsp = 0x00007fff5fbfc9e0
        r8 = 0x0000000000000000
        r9 = 0x000000000000010e
       r10 = 0x0000000000000002
       r11 = 0x0000000000f83160
       r12 = 0x0000000000000000
       r13 = 0x0000000000000000
       r14 = 0x0000000000000000
       r15 = 0x0000000000000000
       rip = 0x000000010000278b  mruby`ary_concat + 27
    rflags = 0x0000000000010202
        cs = 0x000000000000002b
        fs = 0x0000000000000000
        gs = 0x0000000000000000

(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y

```

```
$ ./bin/sandbox crash.rb
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
c:0003 p:---- s:0011 e:000010 CFUNC  :sandbox_eval
c:0002 p:0214 s:0006 E:0007f0 EVAL   ./bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:001680 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
./bin/sandbox:20:in `<main>'
./bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 rax: 0x000000010adab0f0 rbx: 0x000000010ae02c28 rcx: 0x0000000000000003
 rdx: 0x000000010adab0f0 rdi: 0x000000010ada3440 rsi: 0x0000000000000000
 rbp: 0x00007fff558abf50 rsp: 0x00007fff558abf20  r8: 0x0000000000000000
  r9: 0x000000010ada4d60 r10: 0x000000010adb5a88 r11: 0x0000000000000020
 r12: 0x000000010ada3460 r13: 0x0000000000000000 r14: 0x0000000000000000
 r15: 0x0000000000000000 rip: 0x000000010ac7d97d rfl: 0x0000000000010206

-- C level backtrace information -------------------------------------------
0   ruby                                0x000000010a4f05d4 rb_vm_bugreport + 388
1   ruby                                0x000000010a392023 rb_bug_context + 483
2   ruby                                0x000000010a465653 sigsegv + 83
3   libsystem_platform.dylib            0x00007fff9826d52a _sigtramp + 26
4   mruby_engine.bundle                 0x000000010ac7d97d mrb_ary_concat + 29
5   ???                                 0x000000010ada3440 0x0 + 4477039680

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

Abort trap: 6

```

Patch to fix is:

```
diff --git a/mrbgems/mruby-compiler/core/codegen.c b/mrbgems/mruby-compiler/core/codegen.c
index 553baa1..9d0b979 100644
--- a/mrbgems/mruby-compiler/core/codegen.c
+++ b/mrbgems/mruby-compiler/core/codegen.c
@@ -2227,7 +2227,7 @@ codegen(codegen_scope *s, node *tree, int val)
           int off = new_lit(s, mrb_float_value(s->mrb, -f));
 
           genop(s, MKOP_ABx(OP_LOADL, cursp(), off));
-          push();
+          if (val) push();
         }
         break;
 
```

Cheers,

Hugh

## Attachments
No attachments
