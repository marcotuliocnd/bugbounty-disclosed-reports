# SIGABRT - mirb - Double Free

## Report Details
- **Report ID**: 214576
- **URL**: https://hackerone.com/reports/214576
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-18T23:26:46.437Z
- **Disclosed**: 2017-05-13T21:31:12.187Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
-------------------

Attached as test.rb

Debug - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ gdb -q ./mirb
	r Reading symbols from ./mirb...done.
	(gdb) r test.rb 
	Starting program: /home/x/Desktop/test/mruby/bin/mirb test.rb
	mirb - Embeddable Interactive Ruby Shell

	NoMethodError: undefined method 'n' for main
	NoMethodError: undefined method 'b' for main
	 => nil
	(mirb):4: uninitialized constant Fo (NameError)
	 => nil
	 => [8, 2]
	NoMethodError: undefined method '>>' for nil
	NoMethodError: undefined method 'n' for main
	NoMethodError: undefined method '�' for main
	 => 1
	NoMethodError: undefined method 't' for main
	NoMethodError: undefined method 'e' for main
	 => ""
	NoMethodError: undefined method '�' for main
	NoMethodError: undefined method 'nit' for main
	NoMethodError: undefined method ' for main
	NoMethodError: undefined method 'r' for nil
	NoMethodError: undefined method '�' for main
	 => #<Fiber:0x704fc0>
	NoMethodError: undefined method 'r' for nil
	 => nil
	NoMethodError: undefined method 's' for #<Proc:0x704b10@(mirb):22 (lambda)>
	 => nil
	 => nil
	NoMethodError: super called outside of method
	 => nil
	line 29: syntax error, unexpected tAMPER, expecting keyword_end
	 => #<Module:0x7045a0>
	 => nil
	 => [#<Module:0x7045a0>]
	 => nil
	NoMethodError: undefined method 'array' for main
	NoMethodError: undefined method 'it' for main
	 => nil
	NoMethodError: undefined method 'block' for main
	line 41: syntax error, unexpected keyword_end
	NoMethodError: super called outside of method
	 => nil
	 => :b
	 => nil
	NoMethodError: undefined method 'it' for main
	line 48: syntax error, unexpected keyword_end
	 => nil
	 => nil
	 => nil
	NoMethodError: undefined method 'attr_reader' for main
	 => nil
	 => [#<Module:0x702c50>]
	 => nil
	line 68: syntax error, unexpected tCONSTANT, expecting keyword_end
	 => [#<Module:0x7025c0>]
	 => nil
	 => [#<Module:0x701f30>]
	 => #<Fiber:0x701990>
	*** Error in `/home/x/Desktop/test/mruby/bin/mirb': corrupted double-linked list: 0x00000000007b8360 ***

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.

Backtrace - mirb
-------------------

	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff77821d4 in __libc_message (do_abort=do_abort@entry=1, fmt=fmt@entry=0x7ffff7890a10 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:175
	#3  0x00007ffff778cf37 in malloc_printerr (action=<optimized out>, str=0x7ffff788cae6 "corrupted double-linked list", ptr=<optimized out>) at malloc.c:4996
	#4  0x00007ffff778e5e7 in _int_free (av=0x7ffff7acd760 <main_arena>, p=<optimized out>, have_lock=1) at malloc.c:3996
	#5  0x00007ffff77906d0 in _int_realloc (av=0x7ffff7acd760 <main_arena>, oldp=0x7b1f50, oldsize=25616, nb=27664) at malloc.c:4340
	#6  0x00007ffff7791e09 in __GI___libc_realloc (oldmem=0x7b1f60, bytes=27648) at malloc.c:3029
	#7  0x000000000042ce50 in mrb_default_allocf (mrb=0x6b0010, p=0x7b1f60, size=27648, ud=0x0) at /home/x/Desktop/test/mruby/src/state.c:60
	#8  0x0000000000434ff2 in mrb_realloc_simple (mrb=0x6b0010, p=0x7b1f60, len=27648) at /home/x/Desktop/test/mruby/src/gc.c:201
	#9  0x0000000000435074 in mrb_realloc (mrb=0x6b0010, p=0x7b1f60, len=27648) at /home/x/Desktop/test/mruby/src/gc.c:215
	#10 0x0000000000406489 in stack_extend_alloc (mrb=0x6b0010, room=2, keep=0) at /home/x/Desktop/test/mruby/src/vm.c:161
	#11 0x000000000040659d in stack_extend (mrb=0x6b0010, room=2, keep=0) at /home/x/Desktop/test/mruby/src/vm.c:181
	#12 0x00000000004072a6 in mrb_funcall_with_block (mrb=0x6b0010, self=..., mid=8, argc=0, argv=0x7fffffffbb40, blk=...) at /home/x/Desktop/test/mruby/src/vm.c:409
	#13 0x0000000000432a75 in mrb_class_new_class (mrb=0x6b0010, cv=...) at /home/x/Desktop/test/mruby/src/class.c:1459
	#14 0x000000000040a162 in mrb_vm_exec (mrb=0x6b0010, proc=0x6b7300, pc=0x7322e8) at /home/x/Desktop/test/mruby/src/vm.c:1264
	#15 0x000000000040847f in mrb_vm_run (mrb=0x6b0010, proc=0x6b7300, self=..., stack_keep=3) at /home/x/Desktop/test/mruby/src/vm.c:820
	#16 0x000000000041084a in mrb_run (mrb=0x6b0010, proc=0x6b7300, self=...) at /home/x/Desktop/test/mruby/src/vm.c:2606
	#17 0x000000000040802b in mrb_yield_with_class (mrb=0x6b0010, b=..., argc=1, argv=0x7fffffffc260, self=..., c=0x6b71e0) at /home/x/Desktop/test/mruby/src/vm.c:701
	#18 0x0000000000431d5e in mrb_mod_initialize (mrb=0x6b0010, mod=...) at /home/x/Desktop/test/mruby/src/class.c:1148
	#19 0x0000000000407567 in mrb_funcall_with_block (mrb=0x6b0010, self=..., mid=8, argc=0, argv=0x0, blk=...) at /home/x/Desktop/test/mruby/src/vm.c:444
	#20 0x0000000000432842 in mrb_instance_new (mrb=0x6b0010, cv=...) at /home/x/Desktop/test/mruby/src/class.c:1413
	#21 0x000000000040a162 in mrb_vm_exec (mrb=0x6b0010, proc=0x702d40, pc=0x7278ec) at /home/x/Desktop/test/mruby/src/vm.c:1264
	#22 0x000000000040847f in mrb_vm_run (mrb=0x6b0010, proc=0x7018d0, self=..., stack_keep=8) at /home/x/Desktop/test/mruby/src/vm.c:820
	#23 0x0000000000402b90 in main (argc=2, argv=0x7fffffffe088) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549
	
Clang - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../clang/mruby/bin/mirb test.rb 
	mirb - Embeddable Interactive Ruby Shell

	NoMethodError: undefined method 'n' for main
	NoMethodError: undefined method 'b' for main
	 => nil
	(mirb):4: uninitialized constant Fo (NameError)
	 => nil
	 => [8, 2]
	NoMethodError: undefined method '>>' for nil
	NoMethodError: undefined method 'n' for main
	NoMethodError: undefined method '�' for main
	 => 1
	NoMethodError: undefined method 't' for main
	NoMethodError: undefined method 'e' for main
	 => ""
	NoMethodError: undefined method '�' for main
	NoMethodError: undefined method 'nit' for main
	NoMethodError: undefined method ' for main
	NoMethodError: undefined method 'r' for nil
	NoMethodError: undefined method '�' for main
	 => #<Fiber:0x62f000018ed0>
	NoMethodError: undefined method 'r' for nil
	 => nil
	NoMethodError: undefined method 's' for #<Proc:0x62f000018a80@(mirb):22 (lambda)>
	 => nil
	 => nil
	NoMethodError: super called outside of method
	 => nil
	line 29: syntax error, unexpected tAMPER, expecting keyword_end
	 => #<Module:0x62f000018570>
	 => nil
	 => [#<Module:0x62f000018570>]
	 => nil
	NoMethodError: undefined method 'array' for main
	NoMethodError: undefined method 'it' for main
	 => nil
	NoMethodError: undefined method 'block' for main
	line 41: syntax error, unexpected keyword_end
	NoMethodError: super called outside of method
	 => nil
	 => :b
	 => nil
	NoMethodError: undefined method 'it' for main
	line 48: syntax error, unexpected keyword_end
	 => nil
	 => nil
	 => nil
	NoMethodError: undefined method 'attr_reader' for main
	 => nil
	 => [#<Module:0x62f000016e00>]
	 => nil
	line 68: syntax error, unexpected tCONSTANT, expecting keyword_end
	 => [#<Module:0x62f000016770>]
	 => nil
	 => [#<Module:0x62f0000160e0>]
	 => #<Fiber:0x62f000015b40>
	=================================================================
	==23545==ERROR: AddressSanitizer: attempting double-free on 0x62b00000e200 in thread T0:
		#0 0x4c4c7d in realloc (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4c4c7d)
		#1 0x526295 in mrb_default_allocf /home/x/Desktop/test/clang/mruby/src/state.c:60:12
		#2 0x53056c in mrb_realloc_simple /home/x/Desktop/test/clang/mruby/src/gc.c:201:8
		#3 0x530724 in mrb_realloc /home/x/Desktop/test/clang/mruby/src/gc.c:215:8
		#4 0x50272c in stack_extend_alloc /home/x/Desktop/test/clang/mruby/src/vm.c:161:33
		#5 0x4f8bcb in stack_extend /home/x/Desktop/test/clang/mruby/src/vm.c:181:5
		#6 0x4f96e3 in mrb_yield_with_class /home/x/Desktop/test/clang/mruby/src/vm.c:689:5
		#7 0x52e1fe in mrb_class_initialize /home/x/Desktop/test/clang/mruby/src/class.c:1440:5
		#8 0x4f85e9 in mrb_funcall_with_block /home/x/Desktop/test/clang/mruby/src/vm.c:444:13
		#9 0x52e076 in mrb_class_new_class /home/x/Desktop/test/clang/mruby/src/class.c:1460:5
		#10 0x4fb6ca in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1267:18
		#11 0x4f9a1e in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:823:10
		#12 0x4f8ca3 in mrb_run /home/x/Desktop/test/clang/mruby/src/vm.c:2611:12
		#13 0x4f9846 in mrb_yield_with_class /home/x/Desktop/test/clang/mruby/src/vm.c:704:11
		#14 0x52e787 in mrb_mod_initialize /home/x/Desktop/test/clang/mruby/src/class.c:1149:5
		#15 0x4f85e9 in mrb_funcall_with_block /home/x/Desktop/test/clang/mruby/src/vm.c:444:13
		#16 0x52c16c in mrb_instance_new /home/x/Desktop/test/clang/mruby/src/class.c:1414:3
		#17 0x4fb6ca in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1267:18
		#18 0x4f9a1e in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:823:10
		#19 0x4f3010 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#20 0x7f58dcc91ec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#21 0x41a575 in _start (/home/x/Desktop/test/clang/mruby/bin/mirb+0x41a575)

	0x62b00000e200 is located 0 bytes inside of 27648-byte region [0x62b00000e200,0x62b000014e00)
	freed by thread T0 here:
		#0 0x4c4590 in free (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4c4590)
		#1 0x52627b in mrb_default_allocf /home/x/Desktop/test/clang/mruby/src/state.c:56:5
		#2 0x5309dc in mrb_free /home/x/Desktop/test/clang/mruby/src/gc.c:268:3
		#3 0x526923 in mrb_free_context /home/x/Desktop/test/clang/mruby/src/state.c:226:3
		#4 0x530e9c in obj_free /home/x/Desktop/test/clang/mruby/src/gc.c:769:9
		#5 0x532ce7 in incremental_sweep_phase /home/x/Desktop/test/clang/mruby/src/gc.c:1030:11
		#6 0x532651 in incremental_gc /home/x/Desktop/test/clang/mruby/src/gc.c:1096:20
		#7 0x5319a6 in incremental_gc_until /home/x/Desktop/test/clang/mruby/src/gc.c:1112:5
		#8 0x53167e in mrb_incremental_gc /home/x/Desktop/test/clang/mruby/src/gc.c:1163:5
		#9 0x531508 in mrb_obj_alloc /home/x/Desktop/test/clang/mruby/src/gc.c:507:5
		#10 0x507207 in mrb_proc_new /home/x/Desktop/test/clang/mruby/src/proc.c:22:22
		#11 0x5072bc in mrb_closure_new /home/x/Desktop/test/clang/mruby/src/proc.c:69:21
		#12 0x500d1e in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:2403:13
		#13 0x4f9a1e in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:823:10
		#14 0x4f3010 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#15 0x7f58dcc91ec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287

	previously allocated by thread T0 here:
		#0 0x4c4c7d in realloc (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4c4c7d)
		#1 0x526295 in mrb_default_allocf /home/x/Desktop/test/clang/mruby/src/state.c:60:12
		#2 0x53056c in mrb_realloc_simple /home/x/Desktop/test/clang/mruby/src/gc.c:201:8
		#3 0x530724 in mrb_realloc /home/x/Desktop/test/clang/mruby/src/gc.c:215:8
		#4 0x50272c in stack_extend_alloc /home/x/Desktop/test/clang/mruby/src/vm.c:161:33
		#5 0x4f8bcb in stack_extend /home/x/Desktop/test/clang/mruby/src/vm.c:181:5
		#6 0x4f8314 in mrb_funcall_with_block /home/x/Desktop/test/clang/mruby/src/vm.c:409:7
		#7 0x52e076 in mrb_class_new_class /home/x/Desktop/test/clang/mruby/src/class.c:1460:5
		#8 0x4fb6ca in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1267:18
		#9 0x4f9a1e in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:823:10
		#10 0x4f8ca3 in mrb_run /home/x/Desktop/test/clang/mruby/src/vm.c:2611:12
		#11 0x4f9846 in mrb_yield_with_class /home/x/Desktop/test/clang/mruby/src/vm.c:704:11
		#12 0x52e787 in mrb_mod_initialize /home/x/Desktop/test/clang/mruby/src/class.c:1149:5
		#13 0x4f85e9 in mrb_funcall_with_block /home/x/Desktop/test/clang/mruby/src/vm.c:444:13
		#14 0x52c16c in mrb_instance_new /home/x/Desktop/test/clang/mruby/src/class.c:1414:3
		#15 0x4fb6ca in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1267:18
		#16 0x4f9a1e in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:823:10
		#17 0x4f3010 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#18 0x7f58dcc91ec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287

	SUMMARY: AddressSanitizer: double-free (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4c4c7d) in realloc
	==23545==ABORTING

## Attachments
- test.rb
