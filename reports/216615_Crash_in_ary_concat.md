# Crash in ary_concat() 

## Report Details
- **Report ID**: 216615
- **URL**: https://hackerone.com/reports/216615
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-28T06:59:01.773Z
- **Disclosed**: 2017-05-13T21:29:14.531Z

## Reporter
- **Username**: mg36
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The code above raises a segmentation fault both in mruby and mruby-engine
```
N *case
when nil
->()do end
def e()end
end#
````

ASAN report :
```
line 1:3: '*' interpreted as argument prefix
ASAN:SIGSEGV
=================================================================
==111090==ERROR: AddressSanitizer: SEGV on unknown address 0x0000000c (pc 0x08449c8e sp 0xfffd4e20 bp 0x0000000c T0)
    #0 0x8449c8d in ary_concat /root/fuzzing/mruby/src/array.c:260
    #1 0x8449c8d in mrb_ary_concat /root/fuzzing/mruby/src/array.c:279
    #2 0x850bfe1 in mrb_vm_exec /root/fuzzing/mruby/src/vm.c:2288
    #3 0x852f901 in mrb_vm_run /root/fuzzing/mruby/src/vm.c:823
    #4 0x852f901 in mrb_top_run /root/fuzzing/mruby/src/vm.c:2614
    #5 0x82e3a4b in mrb_load_exec /root/fuzzing/mruby/mrbgems/mruby-compiler/core/parse.y:5760
    #6 0x82e6b9b in mrb_load_nstring_cxt /root/fuzzing/mruby/mrbgems/mruby-compiler/core/parse.y:5782
    #7 0x82e6b9b in mrb_load_string_cxt /root/fuzzing/mruby/mrbgems/mruby-compiler/core/parse.y:5794
    #8 0x82e6dc4 in mrb_load_string /root/fuzzing/mruby/mrbgems/mruby-compiler/core/parse.y:5800
    #9 0x80d22e8 in main /root/fuzzing/mruby/bin/fuzz.c:13
    #10 0xf74e5636 in __libc_start_main (/lib/i386-linux-gnu/libc.so.6+0x18636)
    #11 0x80d1fc4 in _start (/home/simo/test/news/xx/bin/zz+0x80d1fc4)
```

Sandbox crash report :
```
home/simo/mruby-engine-normal/bin/sandbox:20: [BUG] Segmentation fault at 0x00000000000018
ruby 2.3.1p112 (2016-04-26) [x86_64-linux-gnu]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:0009d8 EVAL   /home/simo/mruby-engine-normal/bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:002180 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
/home/simo/mruby-engine-normal/bin/sandbox:20:in `<main>'
/home/simo/mruby-engine-normal/bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 RIP: 0x00007f2932c2aa7e RBP: 0x00007f29317b8a00 RSP: 0x00007f29317aaac0
 RAX: 0x1fffffffffffffff RBX: 0x00007f29317ac4e0 RCX: 0x0000000000000003
 RDX: 0x00007f29317b40d0 RDI: 0x00007f29317ac4e0 RSI: 0x0000000000000000
  R8: 0x0000000000000010  R9: 0x0000000000000000 R10: 0x000000000000001f
 R11: 0x00007f29317bb520 R12: 0x0000000000000000 R13: 0x00007f29317ac4e0
 R14: 0x00007f29317ac4e0 R15: 0x0000000001810038 EFL: 0x0000000000010206
```

Thanks

## Attachments
No attachments
