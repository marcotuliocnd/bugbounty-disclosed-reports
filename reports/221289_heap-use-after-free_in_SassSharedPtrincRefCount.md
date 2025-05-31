# heap-use-after-free in Sass::SharedPtr::incRefCount()

## Report Details
- **Report ID**: 221289
- **URL**: https://hackerone.com/reports/221289
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-15T20:31:06.780Z
- **Disclosed**: 2017-08-10T21:38:35.540Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: libsass

## Vulnerability Information
Feeding `@P#{()if(0,0<0,0)}` to `./sassc -s` triggers this use after free.

```
==10210==ERROR: AddressSanitizer: heap-use-after-free on address 0x60c00000a908 at pc 0x000000610a0f bp 0x7fff12af40d0 sp 0x7fff12af40c8
READ of size 8 at 0x60c00000a908 thread T0
    #0 0x610a0e in Sass::SharedPtr::incRefCount() /home/geeknik/libsass/src/memory/SharedPtr.cpp:75:7
    #1 0x610a0e in Sass::SharedPtr::SharedPtr(Sass::SharedObj*) /home/geeknik/libsass/src/memory/SharedPtr.cpp:93
    #2 0x9820a2 in Sass::SharedImpl<Sass::Expression>::SharedImpl(Sass::Expression*) /home/geeknik/libsass/src/memory/SharedPtr.hpp:141:23
    #3 0x9820a2 in Sass::Eval::operator()(Sass::Function_Call*) /home/geeknik/libsass/src/eval.cpp:1018
    #4 0x951b36 in Sass::Eval::operator()(Sass::List*) /home/geeknik/libsass/src/eval.cpp:502:18
    #5 0x9a0042 in Sass::Eval::operator()(Sass::String_Schema*) /home/geeknik/libsass/src/eval.cpp:1236:27
    #6 0x9a0042 in Sass::Eval::operator()(Sass::String_Schema*) /home/geeknik/libsass/src/eval.cpp:1236:27
    #7 0x9cc301 in Sass::Expand::operator()(Sass::Directive*) /home/geeknik/libsass/src/expand.cpp:226:18
    #8 0x9f964c in Sass::Expand::append_block(Sass::Block*) /home/geeknik/libsass/src/expand.cpp:788:27
    #9 0x9c2379 in Sass::Expand::operator()(Sass::Block*) /home/geeknik/libsass/src/expand.cpp:81:5
    #10 0x656973 in Sass::Context::compile() /home/geeknik/libsass/src/context.cpp:658:12
    #11 0x651bc7 in Sass::Data_Context::parse() /home/geeknik/libsass/src/context.cpp:629:12
    #12 0x5d0650 in Sass::sass_parse_block(Sass_Compiler*) /home/geeknik/libsass/src/sass_context.cpp:227:22
    #13 0x5d0650 in sass_compiler_parse /home/geeknik/libsass/src/sass_context.cpp:476
    #14 0x5cf1d1 in sass_compile_context(Sass_Context*, Sass::Context*) /home/geeknik/libsass/src/sass_context.cpp:364:7
    #15 0x5ceaf6 in sass_compile_data_context /home/geeknik/libsass/src/sass_context.cpp:449:12
    #16 0x5b9a54 in compile_stdin /home/geeknik/sassc/sassc.c:125:5
    #17 0x5bab3d in main /home/geeknik/sassc/sassc.c:340:18
    #18 0x7f202f310b44 in __libc_start_main /build/glibc-qK83Be/glibc-2.19/csu/libc-start.c:287
    #19 0x5b92fc in _start (/home/geeknik/sassc/bin/sassc+0x5b92fc)

0x60c00000a908 is located 8 bytes inside of 128-byte region [0x60c00000a900,0x60c00000a980)
freed by thread T0 here:
    #0 0x59b9fb in free (/home/geeknik/sassc/bin/sassc+0x59b9fb)
    #1 0x6106d2 in Sass::SharedPtr::decRefCount() /home/geeknik/libsass/src/memory/SharedPtr.cpp:67:11
    #2 0x6106d2 in Sass::SharedPtr::~SharedPtr() /home/geeknik/libsass/src/memory/SharedPtr.cpp:86
    #3 0x982065 in Sass::Eval::operator()(Sass::Function_Call*) /home/geeknik/libsass/src/eval.cpp:1018:18
    #4 0x951b36 in Sass::Eval::operator()(Sass::List*) /home/geeknik/libsass/src/eval.cpp:502:18
    #5 0x9a0042 in Sass::Eval::operator()(Sass::String_Schema*) /home/geeknik/libsass/src/eval.cpp:1236:27
    #6 0x9a0042 in Sass::Eval::operator()(Sass::String_Schema*) /home/geeknik/libsass/src/eval.cpp:1236:27
    #7 0x9cc301 in Sass::Expand::operator()(Sass::Directive*) /home/geeknik/libsass/src/expand.cpp:226:18
    #8 0x9f964c in Sass::Expand::append_block(Sass::Block*) /home/geeknik/libsass/src/expand.cpp:788:27
    #9 0x9c2379 in Sass::Expand::operator()(Sass::Block*) /home/geeknik/libsass/src/expand.cpp:81:5
    #10 0x656973 in Sass::Context::compile() /home/geeknik/libsass/src/context.cpp:658:12
    #11 0x651bc7 in Sass::Data_Context::parse() /home/geeknik/libsass/src/context.cpp:629:12
    #12 0x5d0650 in Sass::sass_parse_block(Sass_Compiler*) /home/geeknik/libsass/src/sass_context.cpp:227:22
    #13 0x5d0650 in sass_compiler_parse /home/geeknik/libsass/src/sass_context.cpp:476
    #14 0x5cf1d1 in sass_compile_context(Sass_Context*, Sass::Context*) /home/geeknik/libsass/src/sass_context.cpp:364:7
    #15 0x5b9a54 in compile_stdin /home/geeknik/sassc/sassc.c:125:5
    #16 0x5bab3d in main /home/geeknik/sassc/sassc.c:340:18
    #17 0x7f202f310b44 in __libc_start_main /build/glibc-qK83Be/glibc-2.19/csu/libc-start.c:287

previously allocated by thread T0 here:
    #0 0x59bc7b in __interceptor_malloc (/home/geeknik/sassc/bin/sassc+0x59bc7b)
    #1 0x7f202fd342e7 in operator new(unsigned long) (/usr/lib/x86_64-linux-gnu/libstdc++.so.6+0x5f2e7)
    #2 0x9c00a9 in Sass::Expand::Expand(Sass::Context&, Sass::Environment<Sass::SharedImpl<Sass::AST_Node> >*, Sass::Backtrace*, std::vector<Sass::SharedImpl<Sass::Selector_List>, std::allocator<Sass::SharedImpl<Sass::Selector_List> > >*) /home/geeknik/libsass/src/expand.cpp:32:3
    #3 0x72900a in Sass::Functions::sass_if(Sass::Environment<Sass::SharedImpl<Sass::AST_Node> >&, Sass::Environment<Sass::SharedImpl<Sass::AST_Node> >&, Sass::Context&, char const*, Sass::ParserState, Sass::Backtrace*, std::vector<Sass::SharedImpl<Sass::Selector_List>, std::allocator<Sass::SharedImpl<Sass::Selector_List> > >) /home/geeknik/libsass/src/functions.cpp:1720:14
    #4 0x982065 in Sass::Eval::operator()(Sass::Function_Call*) /home/geeknik/libsass/src/eval.cpp:1018:18
    #5 0x951b36 in Sass::Eval::operator()(Sass::List*) /home/geeknik/libsass/src/eval.cpp:502:18
    #6 0x9a0042 in Sass::Eval::operator()(Sass::String_Schema*) /home/geeknik/libsass/src/eval.cpp:1236:27
    #7 0x9a0042 in Sass::Eval::operator()(Sass::String_Schema*) /home/geeknik/libsass/src/eval.cpp:1236:27
    #8 0x9cc301 in Sass::Expand::operator()(Sass::Directive*) /home/geeknik/libsass/src/expand.cpp:226:18
    #9 0x9f964c in Sass::Expand::append_block(Sass::Block*) /home/geeknik/libsass/src/expand.cpp:788:27
    #10 0x9c2379 in Sass::Expand::operator()(Sass::Block*) /home/geeknik/libsass/src/expand.cpp:81:5
    #11 0x656973 in Sass::Context::compile() /home/geeknik/libsass/src/context.cpp:658:12
    #12 0x651bc7 in Sass::Data_Context::parse() /home/geeknik/libsass/src/context.cpp:629:12
    #13 0x5d0650 in Sass::sass_parse_block(Sass_Compiler*) /home/geeknik/libsass/src/sass_context.cpp:227:22
    #14 0x5d0650 in sass_compiler_parse /home/geeknik/libsass/src/sass_context.cpp:476
    #15 0x5cf1d1 in sass_compile_context(Sass_Context*, Sass::Context*) /home/geeknik/libsass/src/sass_context.cpp:364:7
    #16 0x5b9a54 in compile_stdin /home/geeknik/sassc/sassc.c:125:5
    #17 0x5bab3d in main /home/geeknik/sassc/sassc.c:340:18
    #18 0x7f202f310b44 in __libc_start_main /build/glibc-qK83Be/glibc-2.19/csu/libc-start.c:287

SUMMARY: AddressSanitizer: heap-use-after-free /home/geeknik/libsass/src/memory/SharedPtr.cpp:75 Sass::SharedPtr::incRefCount()
```

## Attachments
No attachments
