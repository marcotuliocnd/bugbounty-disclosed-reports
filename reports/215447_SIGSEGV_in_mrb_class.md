# SIGSEGV in mrb_class

## Report Details
- **Report ID**: 215447
- **URL**: https://hackerone.com/reports/215447
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-22T20:33:14.464Z
- **Disclosed**: 2017-05-13T21:30:24.381Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
-------------------

Attached as test_mrb_class.rb):

Debug - mirb
-------------------

	Program received signal SIGSEGV, Segmentation fault.
	0x0000000000402ef2 in mrb_class (mrb=0x6b0010, v=...) at /home/x/Desktop/test/mruby/include/mruby/class.h:50
	50	    return mrb_obj_ptr(v)->c;
	(gdb) l
	45	  case MRB_TT_CPTR:
	46	    return mrb->object_class;
	47	  case MRB_TT_ENV:
	48	    return NULL;
	49	  default:
	50	    return mrb_obj_ptr(v)->c;
	51	  }
	52	}
	53	
	54	// TODO: figure out where to put user flags
	9
	(gdb) info reg
	rax            0x20	32
	rbx            0x6c3360	7091040
	rcx            0x21	33
	rdx            0x21	33
	rsi            0x20	32
	rdi            0x6b0010	7012368
	rbp            0x7fffffffba90	0x7fffffffba90
	rsp            0x7fffffffba90	0x7fffffffba90
	r8             0x3	3
	r9             0x6ee1e0	7266784
	r10            0x7fff0000000e	140733193388046
	r11            0x7ffff7895770	140737346361200
	r12            0x401ca0	4201632
	r13            0x7fffffffdf40	140737488346944
	r14            0x0	0
	r15            0x0	0
	rip            0x402ef2	0x402ef2 <mrb_class+151>
	eflags         0x10212	[ AF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) x/x $rax
	0x20:	Cannot access memory at address 0x20
	
Backtrace - mirb
-------------------

	(gdb) bt
	#0  0x0000000000402ef2 in mrb_class (mrb=0x6b0010, v=...) at /home/x/Desktop/test/mruby/include/mruby/class.h:50
	#1  0x0000000000406ccf in mrb_vm_exec (mrb=0x6b0010, proc=0x6b8050, pc=0x471dbc <mrblib_irep+3588>) at /home/x/Desktop/test/mruby/src/vm.c:1209
	#2  0x000000000040542c in mrb_vm_run (mrb=0x6b0010, proc=0x6b30d0, self=..., stack_keep=2) at /home/x/Desktop/test/mruby/src/vm.c:823
	#3  0x000000000040d7c1 in mrb_run (mrb=0x6b0010, proc=0x6b30d0, self=...) at /home/x/Desktop/test/mruby/src/vm.c:2603
	#4  0x0000000000404550 in mrb_funcall_with_block (mrb=0x6b0010, self=..., mid=43, argc=0, argv=0x0, blk=...) at /home/x/Desktop/test/mruby/src/vm.c:451
	#5  0x00000000004045ef in mrb_funcall_argv (mrb=0x6b0010, self=..., mid=43, argc=0, argv=0x0) at /home/x/Desktop/test/mruby/src/vm.c:461
	#6  0x00000000004170b6 in mrb_method_missing (mrb=0x6b0010, name=116, self=..., args=...) at /home/x/Desktop/test/mruby/src/kernel.c:926
	#7  0x0000000000406e3d in mrb_vm_exec (mrb=0x6b0010, proc=0x746d60, pc=0x752614) at /home/x/Desktop/test/mruby/src/vm.c:1225
	#8  0x000000000040542c in mrb_vm_run (mrb=0x6b0010, proc=0x746d60, self=..., stack_keep=4) at /home/x/Desktop/test/mruby/src/vm.c:823
	#9  0x0000000000402b90 in main (argc=2, argv=0x7fffffffdf48) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:54

Clang - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ ../../clang/mruby/bin/mirb test_mrb_class.rb 
	mirb - Embeddable Interactive Ruby Shell

	 => nil
	NoMethodError: undefined method 't' for main
	NoMethodError: undefined method 'l' for main
	NoMethodError: undefined method 's' for main
	NoMethodError: undefined method 's' for main
	NoMethodError: undefined method 'd' for main
	 => #<Class:0x62f000000c10>
	(mirb):8: uninitialized constant E (NameError)
	NoMethodError: undefined method 't' for main
	 => nil
	NoMethodError: undefined method 't' for main
	NoMethodError: undefined method 'l' for main
	 => nil
	 => #<struct x=nil, y=nil>
	 => #<struct x=nil, y=nil>
	 => #<struct x=nil, y=nil>
	 => #<struct x=#<struct x=nil, y=nil>, y=nil>
	 => nil
	NoMethodError: undefined method 'y' for main
	(mirb):20: uninitialized constant A (NameError)
	NoMethodError: undefined method 'y' for main
	NoMethodError: undefined method 'h' for main
	 => [0, ""]
	 => [0]
	 => nil
	 => nil
	/home/x/Desktop/test/clang/mruby/mrblib/compar.rb:55: comparison of Fixnum with String failed (ArgumentError)
	 => nil
	 => [""]
	 => [0]
	 => nil
	 => {0=>0}
	 => [0]
	NoMethodError: undefined method 's' for #<struct x=#<struct x=nil, y=nil>, y=nil>
	 => [""]
	 => [0]
	NoMethodError: undefined method 'e' for main
	 => [0, ""]
	NoMethodError: undefined method '>' for [0, ""]
	(mirb):40: wrong number of arguments (ArgumentError)
	NoMethodError: undefined method 't' for main
	NoMethodError: undefined method 't' for main
	 => [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]]
	NoMethodError: undefined method '[]' for nil
	 => nil
	 => [0]
	NoMethodError: undefined method 'l' for main
	 => [0]
	NoMethodError: undefined method 'l' for main
	NoMethodError: undefined method 'l' for main
	 => #<struct x=nil, y=nil>
	 => #<struct x=nil, y=nil>
	 => #<struct x=nil, y=nil>
	 => [0]
	 => ""
	NoMethodError: undefined method 'call' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'call' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'call' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'i' for main
	 => #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'n' for main
	NoMethodError: undefined method 'd' for main
	NoMethodError: undefined method 's' for main
	 => nil
	 => [0, "", 0]
	NoMethodError: undefined method 'l' for main
	 => #<struct x=nil, y=nil>
	NoMethodError: undefined method 'e' for main
	NoMethodError: undefined method 'h' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'l' for main
	NoMethodError: undefined method 'h' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'l' for main
	NoMethodError: undefined method 'call' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'call' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'i' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'call' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'call' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'call' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'r' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'e' for main
	NoMethodError: undefined method 'e' for #<Array:0x62f0000354a0>
	NoMethodError: undefined method 's' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'call' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	NoMethodError: undefined method 'call' for #<struct x=#<struct x=nil, y=nil>, y=[0]>
	ASAN:DEADLYSIGNAL
	=================================================================
	==4052==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x0000004f4bae bp 0x7fff6379a8e0 sp 0x7fff6379a8e0 T0)
		#0 0x4f4bad  (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4f4bad)
		#1 0x4f73dc  (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4f73dc)
		#2 0x4f5bae  (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4f5bae)
		#3 0x4f4e33  (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4f4e33)
		#4 0x4f47fa  (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4f47fa)
		#5 0x4f3fa8  (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4f3fa8)
		#6 0x508e45  (/home/x/Desktop/test/clang/mruby/bin/mirb+0x508e45)
		#7 0x4f753a  (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4f753a)
		#8 0x4f5bae  (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4f5bae)
		#9 0x4f3010  (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4f3010)
		#10 0x7fad0f4a6ec4  (/lib/x86_64-linux-gnu/libc.so.6+0x21ec4)
		#11 0x41a575  (/home/x/Desktop/test/clang/mruby/bin/mirb+0x41a575)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4f4bad) 
	==4052==ABORTING

System information
-------------------

	SHA hash - 051e40c0493f2de332f5439e3230c9fe6958bf1a
	Linux 14.04 x86_64
	gcc version 4.8.4

## Attachments
- test_mrb_class.rb
