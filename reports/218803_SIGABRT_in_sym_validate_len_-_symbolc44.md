# SIGABRT in sym_validate_len - symbol.c:44

## Report Details
- **Report ID**: 218803
- **URL**: https://hackerone.com/reports/218803
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-05T16:41:18.484Z
- **Disclosed**: 2017-05-02T22:09:02.427Z

## Reporter
- **Username**: ilsani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
File [2] as input causes a sigabrt in mruby.

mruby raise an exception in sym_validate_len (symbol.c:44)
```
#0  0x00000000005d3908 in raise ()
#1  0x00000000005d3b3a in abort ()
#2  0x0000000000415b52 in mrb_exc_raise (mrb=<optimized out>, exc=...) at /tmp/mruby/src/error.c:310
#3  0x0000000000415c81 in mrb_raise (mrb=0x94fc10, c=<optimized out>, msg=<optimized out>) at /tmp/mruby/src/error.c:318
#4  0x000000000041afdd in sym_validate_len (mrb=0x94fc10, len=65535) at /tmp/mruby/src/symbol.c:44
```

## Attachments
- stacktrace.txt
- input.txt
