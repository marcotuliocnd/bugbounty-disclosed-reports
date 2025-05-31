# Broken handling of maximum number of method call arguments leads to segfault

## Report Details
- **Report ID**: 182484
- **URL**: https://hackerone.com/reports/182484
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-16T10:57:28.825Z
- **Disclosed**: 2016-12-21T08:04:12.624Z

## Reporter
- **Username**: dkasak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Introduction
============

Improper logic for handling of maximum number of method call arguments leads to dereferencing an invalid pointer in some cases, which causes a segfault in both mruby and mruby_engine (and the parent MRI).

The crash only happens when the number of arguments, `n == CALL_MAXARGS`, which is 127. If a larger number of arguments are supplied, mruby doesn't crash but it doesn't appear to work as intended either. The intent of the design seems to had been to support a larger number of arguments than CALL_MAXARGS, but that they should then be passed as an array. However, calls with more than CALL_MAXARGS don't succeed, raising an ArgumentError instead.

Proof of Concept
================

crash.rb
--------

    x 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, \
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, \
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, \
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, \
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, \
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

The above POC is written with line continuations for readability only; the crash doesn't depend on the line continuations, only on there being exactly 127 arguments.

1. Save the above code as crash.rb
2. Run either:
   a) mruby crash.rb
   b) sandbox crash.rb
3. Both cause a segmentation fault.

Discussion
==========

Everything below assumes the latest master of the mruby repository as of Nov 16th, which is commit `1685eff2a5e672173d67916a1c96648df92b7271`.

The crash happens on line 473 of `ext/mruby_engine/mruby/src/array.c`

    if (ARY_SHARED_P(a)

because `a` is a null pointer and the macro `ARY_SHARED_P` tries accessing its `flags` member (`(a)->flags`).

The underlying cause is located in `ext/mruby_engine/mruby/mrbgems/mruby-compiler/core/codegen.c`, in the function `gen_values`. Inside the `while` loop on line 779, there is a special check for handling both array "splat" mode and more than 126 arguments. This code creates an array as the first argument of the method call which is supposed to contain all the arguments for a method call with more than 126 arguments. Since the rest of the code expects that the first argument is an array when `n == CALL_MAXARGS`, it is vital for this check to happen.

However, when there are exactly 127 arguments, `n` becomes 127 exactly when `t` becomes null at the end of the loop in the assignment `t = t->cdr`. This is expected, because we have reached the last AST node, but then the loop exits early and the special case never happens. This leads to the rest of the code treating the first argument (a `0` fixnum) as an array, leading to the crash.

At first it seemed to us that this is a simple botched check and that shuffling things around a bit in this function should fix it, but it seems there is a deeper problem with the design in multiple places. In particular, calling functions with more than 127 arguments doesn't work at all (even though the special case is triggered in those cases and an array is created):

more_than_127.rb
----------------

    def x(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16,
          x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30,
          x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44,
          x45, x46, x47, x48, x49, x50, x51, x52, x53, x54, x55, x56, x57, x58,
          x59, x60, x61, x62, x63, x64, x65, x66, x67, x68, x69, x70, x71, x72,
          x73, x74, x75, x76, x77, x78, x79, x80, x81, x82, x83, x84, x85, x86,
          x87, x88, x89, x90, x91, x92, x93, x94, x95, x96, x97, x98, x99, x100,
          x101, x102, x103, x104, x105, x106, x107, x108, x109, x110, x111, x112,
          x113, x114, x115, x116, x117, x118, x119, x120, x121, x122, x123, x124,
          x125, x126, x127, x128)
    end

    x 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, \
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, \
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, \
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, \
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, \
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, \
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, \
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

This raises a cryptic error message:

    trace:
            [1] more_than_127.rb:1:in Object.x
            [0] more_than_127.rb:20
    ArgumentError: 'x': wrong number of arguments (-1 for 0)

Solution
========

Because of design issues described above, it might be a good idea to patch the security flaw first (if mruby is already deployed somewhere) by limiting the number of arguments to 126:

127_arguments_crash_provisionary.patch
--------------------------------------

    diff --git a/mrbgems/mruby-compiler/core/codegen.c b/mrbgems/mruby-compiler/core/codegen.c
    index 9b064b8..36a6d5f 100644
    --- a/mrbgems/mruby-compiler/core/codegen.c
    +++ b/mrbgems/mruby-compiler/core/codegen.c
    @@ -770,6 +770,8 @@ attrsym(codegen_scope *s, mrb_sym a)
    return mrb_intern(s->mrb, name2, len+1);
    }
    
    +#define CALL_MAXARGS 127
    +
    static int
    gen_values(codegen_scope *s, node *t, int val)
    {
    @@ -824,13 +826,15 @@ gen_values(codegen_scope *s, node *t, int val)
        /* normal (no splat) mode */
        codegen(s, t->car, val);
        n++;
    +    if (n >= CALL_MAXARGS-1) {
    +        raise_error(s, "Too many arguments");
    +        return -1;
    +    }
        t = t->cdr;
    }
    return n;
    }
    
    -#define CALL_MAXARGS 127
    -
    static void
    gen_call(codegen_scope *s, node *tree, mrb_sym name, int sp, int val, int safe)
    {

This makes one test fail at the moment ("Array (Longish inline array)"). We will investigate the issue further and try to come up with a patch that also fixes support for a larger number of arguments.

## Attachments
- crash.rb
- more_than_127.rb
- 127_arguments_crash_provisionary.patch
