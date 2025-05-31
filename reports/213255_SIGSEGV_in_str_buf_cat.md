# SIGSEGV in str_buf_cat

## Report Details
- **Report ID**: 213255
- **URL**: https://hackerone.com/reports/213255
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-14T00:01:24.059Z
- **Disclosed**: 2017-04-27T21:18:22.638Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
-------------------

Attached as test_str_buf_cat.rb

Debug - mirb
-------------------

	Program received signal SIGSEGV, Segmentation fault.
	__memcpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S:36
	36	../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S: No such file or directory.
	(gdb) info reg
	rax            0xffff80000955aee1	-140737331745055
	rbx            0xe	14
	rcx            0xd640a0	14041248
	rdx            0x6b2050	7020624
	rsi            0x719f50	7446352
	rdi            0x7ffff6b0d01f	140737332170783
	rbp            0x7fffffffc130	0x7fffffffc130
	rsp            0x7fffffffc0e8	0x7fffffffc0e8
	r8             0xffffffff	4294967295
	r9             0x0	0
	r10            0x22	34
	r11            0xf7acd701	4155299585
	r12            0x401ca0	4201632
	r13            0x7fffffffe070	140737488347248
	r14            0x0	0
	r15            0x0	0
	rip            0x7ffff77a6e3e	0x7ffff77a6e3e <__memcpy_sse2_unaligned+46>
	eflags         0x10206	[ PF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0
	(gdb) up
	#1  0x00000000004158a1 in str_buf_cat (mrb=0x6b0010, s=0x6b9af0, ptr=0x719f50 "", len=7020624) at /home/x/Desktop/test/mruby/src/string.c:183
	183	  memcpy(RSTR_PTR(s) + RSTR_LEN(s), ptr, len);
	(gdb) up
	#2  0x000000000041b9cf in mrb_str_cat (mrb=0x6b0010, str=..., ptr=0x719f50 "", len=7020624) at /home/x/Desktop/test/mruby/src/string.c:2586
	2586	  str_buf_cat(mrb, mrb_str_ptr(str), ptr, len);
	(gdb) up
	#3  0x000000000041bac0 in mrb_str_cat_str (mrb=0x6b0010, str=..., str2=...) at /home/x/Desktop/test/mruby/src/string.c:2599
	2599	  return mrb_str_cat(mrb, str, RSTRING_PTR(str2), RSTRING_LEN(str2));


Backtrace - mirb
-------------------

	(gdb) bt
	#0  __memcpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S:36
	#1  0x00000000004158a1 in str_buf_cat (mrb=0x6b0010, s=0x6b9af0, ptr=0x719f50 "", len=7020624) at /home/x/Desktop/test/mruby/src/string.c:183
	#2  0x000000000041b9cf in mrb_str_cat (mrb=0x6b0010, str=..., ptr=0x719f50 "", len=7020624) at /home/x/Desktop/test/mruby/src/string.c:2586
	#3  0x000000000041bac0 in mrb_str_cat_str (mrb=0x6b0010, str=..., str2=...) at /home/x/Desktop/test/mruby/src/string.c:2599
	#4  0x0000000000429a4b in exc_inspect (mrb=0x6b0010, exc=...) at /home/x/Desktop/test/mruby/src/error.c:170
	#5  0x0000000000407567 in mrb_funcall_with_block (mrb=0x6b0010, self=..., mid=43, argc=0, argv=0x0, blk=...) at /home/x/Desktop/test/mruby/src/vm.c:444
	#6  0x0000000000407693 in mrb_funcall_argv (mrb=0x6b0010, self=..., mid=43, argc=0, argv=0x0) at /home/x/Desktop/test/mruby/src/vm.c:461
	#7  0x0000000000413570 in mrb_method_missing (mrb=0x6b0010, name=117, self=..., args=...) at /home/x/Desktop/test/mruby/src/kernel.c:926
	#8  0x0000000000409ed1 in mrb_vm_exec (mrb=0x6b0010, proc=0x756ae0, pc=0x756c64) at /home/x/Desktop/test/mruby/src/vm.c:1229
	#9  0x000000000040847f in mrb_vm_run (mrb=0x6b0010, proc=0x756ae0, self=..., stack_keep=11) at /home/x/Desktop/test/mruby/src/vm.c:820
	#10 0x0000000000402b90 in main (argc=2, argv=0x7fffffffe078) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549

Clang - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../clang/mruby/bin/mirb test_str_buf_cat.rb 
	mirb - Embeddable Interactive Ruby Shell

	NoMethodError: undefined method 'o' for main
	NoMethodError: undefined method 'e' for main
	NoMethodError: undefined method '�' for main
	NoMethodError: undefined method 'd' for main
	 => nil
	 => nil
	NoMethodError: undefined method 'd' for main
	 => nil
	 => [{""=>0}]
	NoMethodError: undefined method 'r' for main
	NoMethodError: undefined method 's' for 0
	NoMethodError: undefined method 'h' for [0]
	 => ""
	NoMethodError: undefined method 'd' for 0
	NoMethodError: undefined method 'd' for [0]
	 => [0]
	NoMethodError: undefined method 's' for [0]
	NoMethodError: undefined method 'd' for main
	NoMethodError: undefined method 'k' for main
	NoMethodError: undefined method 'x' for 0
	NoMethodError: undefined method 't' for main
	NoMethodError: undefined method 't' for main
	 => nil
	NoMethodError: undefined method 't' for main
	NoMethodError: undefined method 't' for main
	NoMethodError: undefined method 'e' for main
	 => nil
	NoMethodError: undefined method 'd' for [[0], 0, 0]
	 => nil
	NoMethodError: undefined method 'nd' for main
	NoMethodError: undefined method 'o' for main
	NoMethodError: undefined method 't' for main
	NoMethodError: undefined method 't' for main
	 => nil
	NoMethodError: undefined method 't' for main
	NoMethodError: undefined method 't' for main
	 => nil
	 => nil
	NoMethodError: undefined method 't' for main
	 => nil
	NoMethodError: undefined method 't' for main
	 => nil
	 => [0]
	NoMethodError: undefined method 'k' for main
	NoMethodError: undefined method 'a' for nil
	NoMethodError: undefined method 's' for [0]
	NoMethodError: undefined method 'h' for [[0]]
	NoMethodError: undefined method 't' for main
	NoMethodError: undefined method 'i' for main
	NoMethodError: undefined method 'd0' for main
	NoMethodError: undefined method 'k' for main
	NoMethodError: undefined method 'i' for main
	NoMethodError: undefined method 'o' for main
	NoMethodError: undefined method 'd0' for main
	NoMethodError: undefined method 't' for main
	 => nil
	NoMethodError: undefined method 't' for main
	 => nil
	 => nil
	NoMethodError: undefined method 'i' for main
	 => nil
	NoMethodError: undefined method 'i' for main
	 => [0, 0]
	NoMethodError: undefined method 's' for [0, 0]
	NoMethodError: undefined method 'u' for [0, 0]
	NoMethodError: undefined method 'call' for [0, 0]
	NoMethodError: undefined method 'h' for [0, 0]
	NoMethodError: undefined method 's' for [0, 0]
	 => ""
	NoMethodError: undefined method 's' for [0, 0]
	 => ""
	NoMethodError: undefined method 'x' for main
	NoMethodError: undefined method '[]' for nil
	 => [{""=>0}]
	 => nil
	NoMethodError: undefined method 's' for [0, 0]
	NoMethodError: undefined method '[]' for 0
	 => nil
	 => nil
	NoMethodError: undefined method 'x' for main
	NoMethodError: undefined method 'x' for main
	 => nil
	NoMethodError: undefined method 'k' for main
	 => [{""=>0}]
	 => nil
	NoMethodError: undefined method 't' for main
	 => nil
	NoMethodError: undefined method 'i' for main
	 => nil
	 => nil
	 => nil
	NoMethodError: undefined method 'y' for main
	NoMethodError: undefined method 'o' for [{""=>0}]
	 => [{""=>0}]
	NoMethodError: undefined method 'call' for [0, 0]
	NoMethodError: undefined method 'd=' for [[0, 0]]
	 => nil
	NoMethodError: undefined method 't' for main
	NoMethodError: undefined method '[]' for 0
	 => [0, 0]
	 => nil
	 => [{""=>0}]
	 => nil
	NoMethodError: undefined method 'call' for [{""=>0}]
	NoMethodError: undefined method 's' for [0, [{""=>0}]]
	NoMethodError: undefined method 's' for [[0, 0], [0, [{""=>0}]]]
	 => nil
	NoMethodError: undefined method 'call' for nil
	 => [{""=>0}]
	NoMethodError: undefined method 's' for [[0, 0], [0, [{""=>0}]], [0], 0]
	NoMethodError: undefined method 'o' for main
	NoMethodError: undefined method 'i' for main
	NoMethodError: undefined method 'n' for main
	 => nil
	NoMethodError: undefined method 'k' for main
	NoMethodError: undefined method 'call' for [{""=>0}]
	 => nil
	NoMethodError: undefined method 'm' for [{""=>0}]
	NoMethodError: undefined method 'h' for [[0, 0], [0, [{""=>0}]]]
	 => ""
	NoMethodError: undefined method 'call' for [{""=>0}]
	 => [{""=>0}]
	 => [[{""=>0}], [0, [{""=>0}]]]
	NoMethodError: undefined method '�' for main
	(mirb):132: uninitialized constant M (NameError)
	 => [0]
	 => nil
	=================================================================
	==8172==ERROR: AddressSanitizer: heap-use-after-free on address 0x60d00000b980 at pc 0x00000045d032 bp 0x7ffffe05cb20 sp 0x7ffffe05c2d0
	READ of size 8032 at 0x60d00000b980 thread T0
		#0 0x45d031 in __interceptor_memcpy (/home/x/Desktop/test/clang/mruby/bin/mirb+0x45d031)
		#1 0x50c963 in str_buf_cat /home/x/Desktop/test/clang/mruby/src/string.c:183:3
		#2 0x50c56e in mrb_str_cat /home/x/Desktop/test/clang/mruby/src/string.c:2586:3
		#3 0x50cbaf in mrb_str_cat_str /home/x/Desktop/test/clang/mruby/src/string.c:2599:10
		#4 0x5238b4 in exc_inspect /home/x/Desktop/test/clang/mruby/src/error.c:170:7
		#5 0x4f8539 in mrb_funcall_with_block /home/x/Desktop/test/clang/mruby/src/vm.c:444:13
		#6 0x4f7d68 in mrb_funcall_argv /home/x/Desktop/test/clang/mruby/src/vm.c:461:10
		#7 0x504b55 in mrb_method_missing /home/x/Desktop/test/clang/mruby/src/kernel.c:926:12
		#8 0x4fb0ce in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1193:11
		#9 0x4f98ee in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:820:10
		#10 0x4f3010 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#11 0x7fddf073bec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#12 0x41a575 in _start (/home/x/Desktop/test/clang/mruby/bin/mirb+0x41a575)

	0x60d00000ba01 is located 0 bytes to the right of 129-byte region [0x60d00000b980,0x60d00000ba01)
	freed by thread T0 here:
		#0 0x4c4590 in free (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4c4590)
		#1 0x525ecb in mrb_default_allocf /home/x/Desktop/test/clang/mruby/src/state.c:56:5
		#2 0x5306bc in mrb_free /home/x/Desktop/test/clang/mruby/src/gc.c:268:3
		#3 0x50828a in mrb_gc_free_str /home/x/Desktop/test/clang/mruby/src/string.c:247:5
		#4 0x530bfd in obj_free /home/x/Desktop/test/clang/mruby/src/gc.c:787:5
		#5 0x5329c7 in incremental_sweep_phase /home/x/Desktop/test/clang/mruby/src/gc.c:1030:11
		#6 0x532331 in incremental_gc /home/x/Desktop/test/clang/mruby/src/gc.c:1096:20
		#7 0x5316fd in incremental_gc_step /home/x/Desktop/test/clang/mruby/src/gc.c:1122:15
		#8 0x531370 in mrb_incremental_gc /home/x/Desktop/test/clang/mruby/src/gc.c:1166:5
		#9 0x5311e8 in mrb_obj_alloc /home/x/Desktop/test/clang/mruby/src/gc.c:507:5
		#10 0x507ef3 in str_new /home/x/Desktop/test/clang/mruby/src/string.c:59:7
		#11 0x5080e5 in mrb_str_new_cstr /home/x/Desktop/test/clang/mruby/src/string.c:215:7
		#12 0x523842 in exc_inspect /home/x/Desktop/test/clang/mruby/src/error.c:167:11
		#13 0x4f8539 in mrb_funcall_with_block /home/x/Desktop/test/clang/mruby/src/vm.c:444:13
		#14 0x4f7d68 in mrb_funcall_argv /home/x/Desktop/test/clang/mruby/src/vm.c:461:10
		#15 0x504b55 in mrb_method_missing /home/x/Desktop/test/clang/mruby/src/kernel.c:926:12
		#16 0x4fb0ce in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1193:11
		#17 0x4f98ee in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:820:10
		#18 0x4f3010 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#19 0x7fddf073bec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287

	previously allocated by thread T0 here:
		#0 0x4c4c7d in realloc (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4c4c7d)
		#1 0x525ee5 in mrb_default_allocf /home/x/Desktop/test/clang/mruby/src/state.c:60:12
		#2 0x53024c in mrb_realloc_simple /home/x/Desktop/test/clang/mruby/src/gc.c:201:8
		#3 0x530404 in mrb_realloc /home/x/Desktop/test/clang/mruby/src/gc.c:215:8
		#4 0x5305b3 in mrb_malloc /home/x/Desktop/test/clang/mruby/src/gc.c:236:10
		#5 0x507d32 in mrb_str_buf_new /home/x/Desktop/test/clang/mruby/src/string.c:115:28
		#6 0x513735 in join_ary /home/x/Desktop/test/clang/mruby/src/array.c:1031:12
		#7 0x51362e in mrb_ary_join /home/x/Desktop/test/clang/mruby/src/array.c:1075:10
		#8 0x521c07 in mrb_vformat /home/x/Desktop/test/clang/mruby/src/error.c:362:12
		#9 0x522d6d in mrb_no_method_error /home/x/Desktop/test/clang/mruby/src/error.c:526:13
		#10 0x504cb0 in mrb_method_missing /home/x/Desktop/test/clang/mruby/src/kernel.c:935:3
		#11 0x4fb0ce in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1193:11
		#12 0x4f98ee in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:820:10
		#13 0x4f3010 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:549:18
		#14 0x7fddf073bec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287

	SUMMARY: AddressSanitizer: heap-use-after-free (/home/x/Desktop/test/clang/mruby/bin/mirb+0x45d031) in __interceptor_memcpy
	Shadow bytes around the buggy address:
	  0x0c1a7fff96e0: fa fa fd fd fd fd fd fd fd fd fd fd fd fd fd fd
	  0x0c1a7fff96f0: fd fd fd fa fa fa fa fa fa fa fa fa fd fd fd fd
	  0x0c1a7fff9700: fd fd fd fd fd fd fd fd fd fd fd fd fd fa fa fa
	  0x0c1a7fff9710: fa fa fa fa fa fa fd fd fd fd fd fd fd fd fd fd
	  0x0c1a7fff9720: fd fd fd fd fd fd fd fa fa fa fa fa fa fa fa fa
	=>0x0c1a7fff9730:[fd]fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd
	  0x0c1a7fff9740: fd fa fa fa fa fa fa fa fa fa fd fd fd fd fd fd
	  0x0c1a7fff9750: fd fd fd fd fd fd fd fd fd fd fd fa fa fa fa fa
	  0x0c1a7fff9760: fa fa fa fa fd fd fd fd fd fd fd fd fd fd fd fd
	  0x0c1a7fff9770: fd fd fd fd fd fa fa fa fa fa fa fa fa fa fd fd
	  0x0c1a7fff9780: fd fd fd fd fd fd fd fd fd fd fd fd fd fd fd fa
	Shadow byte legend (one shadow byte represents 8 application bytes):
	  Addressable:           00
	  Partially addressable: 01 02 03 04 05 06 07 
	  Heap left redzone:       fa
	  Heap right redzone:      fb
	  Freed heap region:       fd
	  Stack left redzone:      f1
	  Stack mid redzone:       f2
	  Stack right redzone:     f3
	  Stack partial redzone:   f4
	  Stack after return:      f5
	  Stack use after scope:   f8
	  Global redzone:          f9
	  Global init order:       f6
	  Poisoned by user:        f7
	  Container overflow:      fc
	  Array cookie:            ac
	  Intra object redzone:    bb
	  ASan internal:           fe
	  Left alloca redzone:     ca
	  Right alloca redzone:    cb
	==8172==ABORTING

## Attachments
- test_str_buf_cat.rb
