# Heap overflow due to off-by-one when expanding stack

## Report Details
- **Report ID**: 194906
- **URL**: https://hackerone.com/reports/194906
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-31T02:16:16.664Z
- **Disclosed**: 2017-02-07T01:23:21.041Z

## Reporter
- **Username**: titanous
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
This program triggers a heap buffer overflow while zeroing a new stack allocation due to an off-by-one while expanding the stack. It doesn't appear to be exploitable and the fix is extremely simple so I didn't try to simplify the failing test case too much:

```ruby
class A
yield ensure 0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g>>=0.g
end.g>>=g>>=s0>>=e=_=0.g>>=0>p>>=sg>>=0..0>u>>=0..0>a>>=ab|=0..0>r>>=0>e0>>=i>>=0..0>r0>>=a00>ry>>=u0>>=0..0>x>>=0.g>>=0>0|ü|=0..0>r00>>=y>>=t>>=up=sy>>=s00>>=0..0>ug>>=f>>=0>0>>0.g>>=0>a0>>=0.g>>=0>s>>=0..0>0.g>>=0>0.g>>=super
```

ASAN report:

```text
=================================================================
==7397==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x621000017900 at pc 0x0000004ae8ac bp 0x7fff42c9a9d0 sp 0x7fff42c9a180
WRITE of size 16 at 0x621000017900 thread T0
    #0 0x4ae8ab in __asan_memcpy (/vagrant/bin/mruby+0x4ae8ab)
    #1 0x64b513 in stack_clear /vagrant/src/vm.c:68:15
    #2 0x64b1ea in init_new_stack_space /vagrant/src/vm.c:127:5
    #3 0x617dc0 in stack_extend /vagrant/src/vm.c:174:3
    #4 0x61e214 in mrb_vm_run /vagrant/src/vm.c:770:3
    #5 0x618344 in mrb_run /vagrant/src/vm.c:2481:10
    #6 0x647f5b in ecall /vagrant/src/vm.c:297:3
    #7 0x62f830 in mrb_vm_exec /vagrant/src/vm.c:1561:15
    #8 0x61e2eb in mrb_vm_run /vagrant/src/vm.c:772:10
    #9 0x64a628 in mrb_top_run /vagrant/src/vm.c:2491:12
    #10 0x674229 in mrb_load_exec /vagrant/mrbgems/mruby-compiler/core/parse.y:5755:7
    #11 0x674ec5 in mrb_load_file_cxt /vagrant/mrbgems/mruby-compiler/core/parse.y:5764:10
    #12 0x4f3af5 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #13 0x7f2d32996f44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287
    #14 0x41a505 in _start (/vagrant/bin/mruby+0x41a505)

0x621000017900 is located 0 bytes to the right of 4096-byte region [0x621000016900,0x621000017900)
allocated by thread T0 here:
    #0 0x4c4c0d in realloc (/vagrant/bin/mruby+0x4c4c0d)
    #1 0x5bfde5 in mrb_default_allocf /vagrant/src/state.c:60:12
    #2 0x550396 in mrb_realloc_simple /vagrant/src/gc.c:201:8
    #3 0x5509e4 in mrb_realloc /vagrant/src/gc.c:215:8
    #4 0x64ade2 in stack_extend_alloc /vagrant/src/vm.c:155:33
    #5 0x617db1 in stack_extend /vagrant/src/vm.c:172:5
    #6 0x61e214 in mrb_vm_run /vagrant/src/vm.c:770:3
    #7 0x618344 in mrb_run /vagrant/src/vm.c:2481:10
    #8 0x647f5b in ecall /vagrant/src/vm.c:297:3
    #9 0x62f830 in mrb_vm_exec /vagrant/src/vm.c:1561:15
    #10 0x61e2eb in mrb_vm_run /vagrant/src/vm.c:772:10
    #11 0x64a628 in mrb_top_run /vagrant/src/vm.c:2491:12
    #12 0x674229 in mrb_load_exec /vagrant/mrbgems/mruby-compiler/core/parse.y:5755:7
    #13 0x674ec5 in mrb_load_file_cxt /vagrant/mrbgems/mruby-compiler/core/parse.y:5764:10
    #14 0x4f3af5 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #15 0x7f2d32996f44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287

SUMMARY: AddressSanitizer: heap-buffer-overflow (/vagrant/bin/mruby+0x4ae8ab) in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c427fffaed0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c427fffaee0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c427fffaef0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c427fffaf00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c427fffaf10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c427fffaf20:[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c427fffaf30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c427fffaf40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c427fffaf50: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c427fffaf60: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c427fffaf70: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==7397==ABORTING
```

Patch:

```patch
From 7a197ff7c87a4c1db1a686bad49c5d42f9044c12 Mon Sep 17 00:00:00 2001
From: Jonathan Rudenberg <jonathan@titanous.com>
Date: Fri, 30 Dec 2016 21:15:23 -0500
Subject: [PATCH] Fix off-by-one when expanding stack with keep>0

---
 src/vm.c | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/src/vm.c b/src/vm.c
index 368b75a9..051c3b83 100644
--- a/src/vm.c
+++ b/src/vm.c
@@ -124,7 +124,7 @@ init_new_stack_space(mrb_state *mrb, int room, int keep)
 {
   if (room > keep) {
     /* do not leave uninitialized malloc region */
-    stack_clear(&(mrb->c->stack[keep]), room - keep);
+    stack_clear(&(mrb->c->stack[keep]), room - keep - 1);
   }
 }
 
-- 
2.11.0


```

## Attachments
No attachments
