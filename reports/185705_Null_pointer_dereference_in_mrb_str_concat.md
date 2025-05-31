# Null pointer dereference in mrb_str_concat

## Report Details
- **Report ID**: 185705
- **URL**: https://hackerone.com/reports/185705
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-11-27T04:42:23.451Z
- **Disclosed**: 2016-12-17T20:50:12.192Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Hi,

The following file causes a segmentation fault due to a null pointer in `mrb_str_concat` which calls `mrb_str_modify` then `check_frozen` which tries to dereference it.

```
"#{*O=0}"
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
Process 97806 launched: './dev/bin/mruby' (x86_64)
Process 97806 stopped
* thread #1: tid = 0x6d723b5, 0x000000010002de04 mruby`check_frozen + 20, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x0)
    frame #0: 0x000000010002de04 mruby`check_frozen + 20
mruby`check_frozen:
->  0x10002de04 <+20>: movl   (%rsi), %eax
    0x10002de06 <+22>: shrl   $0xb, %eax
    0x10002de09 <+25>: andl   $0x4, %eax
    0x10002de0c <+28>: cmpl   $0x0, %eax
(lldb) bt
* thread #1: tid = 0x6d723b5, 0x000000010002de04 mruby`check_frozen + 20, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x0)
  * frame #0: 0x000000010002de04 mruby`check_frozen + 20
    frame #1: 0x000000010002daa0 mruby`mrb_str_modify + 32
    frame #2: 0x000000010002e353 mruby`mrb_str_concat + 51
    frame #3: 0x0000000100044cc4 mruby`mrb_vm_exec + 27396
    frame #4: 0x000000010003e1a7 mruby`mrb_vm_run + 135
    frame #5: 0x0000000100046604 mruby`mrb_top_run + 100
    frame #6: 0x0000000100071adf mruby`load_exec + 1183
    frame #7: 0x0000000100071623 mruby`mrb_load_file_cxt + 67
    frame #8: 0x00000001000017d8 mruby`main + 904
    frame #9: 0x00007fff8a9db5ad libdyld.dylib`start + 1
(lldb) register read
General Purpose Registers:
       rax = 0x0000000000000003
       rbx = 0x0000000000000000
       rcx = 0x0000000000000000
       rdx = 0x0000000000000003
       rdi = 0x0000000100600000
       rsi = 0x0000000000000000
       rbp = 0x00007fff5fbfc8a0
       rsp = 0x00007fff5fbfc880
        r8 = 0x000000000000000e
        r9 = 0x0000000000000000
       r10 = 0x0000000000000004
       r11 = 0x0000000100600000
       r12 = 0x0000000000000000
       r13 = 0x0000000000000000
       r14 = 0x0000000000000000
       r15 = 0x0000000000000000
       rip = 0x000000010002de04  mruby`check_frozen + 20
    rflags = 0x0000000000010202
        cs = 0x000000000000002b
        fs = 0x0000000000000000
        gs = 0x0000000000000000

(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y

```

This also affects mruby-engine.

```
./bin/sandbox:20: [BUG] Segmentation fault at 0x00000000000001
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
c:0002 p:0201 s:0005 E:002358 EVAL   ./bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:001bf0 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
./bin/sandbox:20:in `<main>'
./bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 rax: 0x0000000000000002 rbx: 0x0000000000000001 rcx: 0x0000000108feea60
 rdx: 0x0000000108fe4090 rdi: 0x0000000108fdc440 rsi: 0x0000000000000001
 rbp: 0x00007fff57672f10 rsp: 0x00007fff57672ee0  r8: 0x000000000000007f
  r9: 0x0000000108f5f5d0 r10: 0x000000010900a3e0 r11: 0xfffffffffffdaa02
 r12: 0x0000000108fdc460 r13: 0x0000000108fdc5a8 r14: 0x0000000000000001
 r15: 0x0000000108fdc440 rip: 0x0000000108ed8ed1 rfl: 0x0000000000010206

-- C level backtrace information -------------------------------------------
0   ruby                                0x00000001087295d4 rb_vm_bugreport + 388
1   ruby                                0x00000001085cb023 rb_bug_context + 483
2   ruby                                0x000000010869e653 sigsegv + 83
3   libsystem_platform.dylib            0x00007fff9826d52a _sigtramp + 26
4   mruby_engine.bundle                 0x0000000108ed8ed1 mrb_str_modify + 17
5   ???                                 0x0000000000000002 0x0 + 2

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

The following patch fixes this, though a better solution could be done while parsing the file.

```
diff --git a/src/string.c b/src/string.c
index f472942..7c89711 100644
--- a/src/string.c
+++ b/src/string.c
@@ -752,6 +752,10 @@ mrb_str_to_cstr(mrb_state *mrb, mrb_value str0)
 MRB_API void
 mrb_str_concat(mrb_state *mrb, mrb_value self, mrb_value other)
 {
+  if (!mrb_string_p(self)) {
+    mrb_raisef(mrb, E_TYPE_ERROR, "expecting String, got %S", mrb_obj_value(mrb_obj_class(mrb, self)));
+    return;
+  }
   struct RString *s1 = mrb_str_ptr(self), *s2;
   mrb_int len;
 
```

Applying the above patch to mruby itself fixes it there, and in `ext/mruby-engine/mruby` fixes the sandbox crash.

Cheers,

Hugh

## Attachments
No attachments
