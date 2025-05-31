# Denial of service (segfault) due to null pointer dereference in mrb_vm_exec

## Report Details
- **Report ID**: 202584
- **URL**: https://hackerone.com/reports/202584
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-01T10:07:23.015Z
- **Disclosed**: 2017-02-28T05:40:05.236Z

## Reporter
- **Username**: d4nny
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Introduction
============

Provided PoC segfaults at mrb_vm_exec due to null pointer dereference.

Proof of concept
================
Attached the poc.

Crash report
============
```
./sandbox vm_exec.rb 
./sandbox:20: [BUG] Segmentation fault at 0x00000000000000
ruby 2.3.1p112 (2016-04-26) [x86_64-linux-gnu]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:001568 EVAL   ./sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:001270 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
./sandbox:20:in `<main>'
./sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 RIP: 0x00007fe9d813e6ed RBP: 0x00007fe9d6cd4fd0 RSP: 0x00007fe9d6cbf0d0
 RAX: 0x0000000000000000 RBX: 0x00007fe9d6cc9170 RCX: 0x00007fe9d6cd4f80
 RDX: 0x00007fe9d6cd4b30 RDI: 0x00007fe9d6d28a80 RSI: 0x00007fe9d6ce57b0
  R8: 0x00007fe9d6cc23e0  R9: 0x0000000000000000 R10: 0x000000000000001f
 R11: 0x00007fe9d6cee1c0 R12: 0x0000000000000000 R13: 0x00007fe9d6cc24e0
 R14: 0x00007fe9d6cc9f80 R15: 0x0000000000804029 EFL: 0x0000000000010297

-- C level backtrace information -------------------------------------------
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7fe9dc3c9ca5]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7fe9dc3c9edc]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7fe9dc2a3944]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7fe9dc355c3e]
/lib/x86_64-linux-gnu/libc.so.6 [0x7fe9dbeab4b0]
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x7cd) [0x7fe9d813e6ed] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1592
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x55) [0x7fe9d8144445] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:772
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_run+0x17) [0x7fe9d813c3f7] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:2480
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_with_block+0x2fc) [0x7fe9d813c6fc] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:422
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_argv+0xc) [0x7fe9d813cc5c] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:432
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall+0x258) [0x7fe9d813cec8] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:323
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_no_method_error+0x13b) [0x7fe9d816526b] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/error.c:510
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_method_missing+0x95) [0x7fe9d815f445] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1477
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_bob_missing+0x5b) [0x7fe9d815f50b] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1522
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_with_block+0x263) [0x7fe9d813c663] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:415
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_argv+0xc) [0x7fe9d813cc5c] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:432
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall+0x258) [0x7fe9d813cec8] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:323
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_range_new+0x75) [0x7fe9d814cee5] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/range.c:40
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x28ea) [0x7fe9d814080a] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:2414
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x55) [0x7fe9d8144445] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:772
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_run+0x17) [0x7fe9d813c3f7] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:2480
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_with_block+0x2fc) [0x7fe9d813c6fc] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:422
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_argv+0xc) [0x7fe9d813cc5c] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:432
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall+0x258) [0x7fe9d813cec8] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:323
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_no_method_error+0x13b) [0x7fe9d816526b] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/error.c:510
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_method_missing+0x95) [0x7fe9d815f445] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1477
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_bob_missing+0x5b) [0x7fe9d815f50b] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1522
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x680) [0x7fe9d813e5a0] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1174
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x55) [0x7fe9d8144445] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:772
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_run+0x17) [0x7fe9d813c3f7] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:2480
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_with_block+0x2fc) [0x7fe9d813c6fc] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:422
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_argv+0xc) [0x7fe9d813cc5c] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:432
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall+0x258) [0x7fe9d813cec8] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:323
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_no_method_error+0x13b) [0x7fe9d816526b] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/error.c:510
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_method_missing+0x95) [0x7fe9d815f445] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1477
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_bob_missing+0x5b) [0x7fe9d815f50b] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/class.c:1522
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x680) [0x7fe9d813e5a0] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1174
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x55) [0x7fe9d8144445] /home/dan/shpy/mruby-engine/ext/mruby_engine/mruby/src/vm.c:772
/home/dan/shpy/mruby-engine/lib/mruby_engine/mruby_engine.so(mruby_engine_monitored_eval+0x113) [0x7fe9d812f203] ../../../../ext/mruby_engine/eval_monitored.c:68
/lib/x86_64-linux-gnu/libpthread.so.0(start_thread+0xca) [0x7fe9dbc606ba]
/lib/x86_64-linux-gnu/libc.so.6(clone+0x6d) [0x7fe9dbf7c82d] ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

```
MRuby analysis
==============
Code downloaded: 31-Jan-2017
Build: x64 Linux GCC with ASAN

```
Program received signal SIGSEGV, Segmentation fault.
──────────────────────────────────────────────────────────────────────────[registers]──
$rax     0x0000000000000000 $rbx     0x00007fffffff87d0 
$rcx     0x000061d00001e000 $rdx     0x0000000000000000 
$rsp     0x00007fffffff79f0 $rbp     0x00007fffffff87f0 
$rsi     0x0000000000000003 $rdi     0x000061400000fe40 
$rip     0x0000000000427fbf $r8      0x0000000000000000 
$r9      0x00007fffffff8c40 $r10     0x0000000000000009 
$r11     0x00007ffff692d550 $r12     0x00007fffffff8d80 
$r13     0x00007fffffff8be0 $r14     0x00007fffffff8be0 

0x427fae	 <mrb_vm_exec+44316>     je   0x427fb8 <mrb_vm_exec+44326>
0x427fb0	 <mrb_vm_exec+44318>     mov   rdi,rax
0x427fb3	 <mrb_vm_exec+44321>     call   0x401e10 <__asan_report_load4@plt>
0x427fb8	 <mrb_vm_exec+44326>     mov   rax,QWORD PTR [rbp-0xdd8]
0x427fbf	 <mrb_vm_exec+44333>     mov   eax,DWORD PTR [rax] 		  <-  $pc
0x427fc1	 <mrb_vm_exec+44335>     mov   DWORD PTR [rbp-0xdb4],eax
0x427fc7	 <mrb_vm_exec+44341>     mov   eax,DWORD PTR [rbp-0xdb4]
0x427fcd	 <mrb_vm_exec+44347>     and   eax,0x7f
0x427fd0	 <mrb_vm_exec+44350>     movsxd   rdx,eax

g> bt
#0  0x0000000000427fbf in mrb_vm_exec ()
#1  0x000000000041d290 in mrb_vm_run ()
#2  0x0000000000432e75 in mrb_run ()
#3  0x000000000041a328 in mrb_funcall_with_block ()
#4  0x000000000041a4ef in mrb_funcall_argv ()
#5  0x0000000000418e9e in mrb_funcall ()
#6  0x000000000047f240 in mrb_no_method_error ()
#7  0x0000000000476e75 in mrb_method_missing ()
#8  0x0000000000476fc6 in mrb_bob_missing ()
#9  0x000000000041a1c5 in mrb_funcall_with_block ()
#10 0x000000000041a4ef in mrb_funcall_argv ()
#11 0x0000000000418e9e in mrb_funcall ()
#12 0x0000000000443840 in range_check ()
#13 0x0000000000443934 in mrb_range_new ()
#14 0x000000000043250c in mrb_vm_exec ()
#15 0x000000000041d290 in mrb_vm_run ()
#16 0x0000000000432e75 in mrb_run ()
#17 0x000000000041a328 in mrb_funcall_with_block ()
#18 0x000000000041a4ef in mrb_funcall_argv ()
#19 0x0000000000418e9e in mrb_funcall ()
#20 0x000000000047f240 in mrb_no_method_error ()
#21 0x0000000000476e75 in mrb_method_missing ()
#22 0x0000000000476fc6 in mrb_bob_missing ()
#23 0x00000000004222bc in mrb_vm_exec ()
#24 0x000000000041d290 in mrb_vm_run ()
#25 0x0000000000432e75 in mrb_run ()
#26 0x000000000041a328 in mrb_funcall_with_block ()
#27 0x000000000041a4ef in mrb_funcall_argv ()
#28 0x0000000000418e9e in mrb_funcall ()
#29 0x000000000047f240 in mrb_no_method_error ()
#30 0x0000000000476e75 in mrb_method_missing ()
#31 0x0000000000476fc6 in mrb_bob_missing ()
#32 0x00000000004222bc in mrb_vm_exec ()
#33 0x000000000041d290 in mrb_vm_run ()
#34 0x0000000000433007 in mrb_top_run ()
#35 0x00000000004a2431 in mrb_load_exec ()
#36 0x00000000004a2592 in mrb_load_file_cxt ()
#37 0x0000000000403758 in main ()

```

This looks pretty similar to dreaded `lines break` issue (https://github.com/mruby/mruby/issues/3359). I thought of submitting this as it doesn't have `mrb_yield_argv`. Though I guess the issue is another `break` not supported inside `NoMethodError`.

## Attachments
- vm_exec.rb
