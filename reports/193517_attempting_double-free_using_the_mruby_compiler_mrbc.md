# attempting double-free using the mruby compiler `mrbc`

## Report Details
- **Report ID**: 193517
- **URL**: https://hackerone.com/reports/193517
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-23T00:13:38.306Z
- **Disclosed**: 2017-02-07T01:26:49.578Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
I cloned the mruby git 4 days ago, started fuzzing with American Fuzzy Lop. This is the 1st crash. 

./mrbc test000
```
codegen error:test000:1: too complex expression
=================================================================
==12142==ERROR: AddressSanitizer: attempting double-free on 0x60200000d750 in thread T0:
    #0 0x7f2fd1fd0527 in __interceptor_free (/usr/lib/x86_64-linux-gnu/libasan.so.1+0x54527)
    #1 0x425788 in mrb_default_allocf /root/mruby/src/state.c:56
    #2 0x4af31b in mrb_free_symtbl /root/mruby/src/symbol.c:166
    #3 0x4285b1 in mrb_close /root/mruby/src/state.c:249
    #4 0x404d48 in cleanup /root/mruby/mrbgems/mruby-bin-mrbc/tools/mrbc/mrbc.c:165
    #5 0x404d48 in main /root/mruby/mrbgems/mruby-bin-mrbc/tools/mrbc/mrbc.c:314
    #6 0x7f2fd18f1b44 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b44)
    #7 0x4061c9 (/root/mruby/bin/mrbc+0x4061c9)

0x60200000d750 is located 0 bytes inside of 8-byte region [0x60200000d750,0x60200000d758)
freed by thread T0 here:
    #0 0x7f2fd1fd0527 in __interceptor_free (/usr/lib/x86_64-linux-gnu/libasan.so.1+0x54527)
    #1 0x425788 in mrb_default_allocf /root/mruby/src/state.c:56
    #2 0x426867 in mrb_irep_free /root/mruby/src/state.c:162
    #3 0x4267a9 in mrb_irep_decref /root/mruby/src/state.c:133
    #4 0x4267a9 in mrb_irep_free /root/mruby/src/state.c:158
    #5 0x687046 in mrb_generate_code /root/mruby/mrbgems/mruby-compiler/core/codegen.c:2960
    #6 0x5df3c1 in mrb_load_exec /root/mruby/mrbgems/mruby-compiler/core/parse.y:5732
    #7 0x5ed6c6 in mrb_load_file_cxt /root/mruby/mrbgems/mruby-compiler/core/parse.y:5764
    #8 0x4041a1 in load_file /root/mruby/mrbgems/mruby-bin-mrbc/tools/mrbc/mrbc.c:220
    #9 0x4041a1 in main /root/mruby/mrbgems/mruby-bin-mrbc/tools/mrbc/mrbc.c:285
    #10 0x7f2fd18f1b44 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b44)

previously allocated by thread T0 here:
    #0 0x7f2fd1fd09f6 in __interceptor_realloc (/usr/lib/x86_64-linux-gnu/libasan.so.1+0x549f6)
    #1 0x488211 in mrb_realloc_simple /root/mruby/src/gc.c:201
    #2 0x488211 in mrb_realloc /root/mruby/src/gc.c:215
    #3 0x488211 in mrb_malloc /root/mruby/src/gc.c:236
    #4 0x4acea8 in sym_intern /root/mruby/src/symbol.c:81
    #5 0x4acea8 in mrb_intern /root/mruby/src/symbol.c:95
    #6 0x4acea8 in mrb_intern_cstr /root/mruby/src/symbol.c:107
    #7 0x5de18b in mrb_parser_set_filename /root/mruby/mrbgems/mruby-compiler/core/parse.y:5639
    #8 0x5eb623 in parser_init_cxt /root/mruby/mrbgems/mruby-compiler/core/parse.y:5467
    #9 0x5eb623 in mrb_parser_parse /root/mruby/mrbgems/mruby-compiler/core/parse.y:5520
    #10 0x5ed680 in mrb_parse_file /root/mruby/mrbgems/mruby-compiler/core/parse.y:5679
    #11 0x5ed680 in mrb_load_file_cxt /root/mruby/mrbgems/mruby-compiler/core/parse.y:5764
    #12 0x4041a1 in load_file /root/mruby/mrbgems/mruby-bin-mrbc/tools/mrbc/mrbc.c:220
    #13 0x4041a1 in main /root/mruby/mrbgems/mruby-bin-mrbc/tools/mrbc/mrbc.c:285
    #14 0x7f2fd18f1b44 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b44)

SUMMARY: AddressSanitizer: double-free ??:0 __interceptor_free
==12142==ABORTING
```



## Attachments
- test000.gz
