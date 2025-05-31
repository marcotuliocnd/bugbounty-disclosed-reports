# Certain inputs cause tight C-level recursion leading to process stack overflow

## Report Details
- **Report ID**: 189633
- **URL**: https://hackerone.com/reports/189633
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-08T22:16:40.299Z
- **Disclosed**: 2017-03-14T22:22:39.902Z

## Reporter
- **Username**: dkasak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Introduction
============

Certain legal Ruby programs can cause a tight recursion on the C-level (without using `eval`) while spending very little of the Ruby-level stack. This precludes triggering a Ruby stack overflow exception and eventually leads to a process stack overflow and a segfault. Both vanilla mruby and mruby running inside mruby-engine are vulnerable.

Proof of concept
================

recursive_to_i.rb:
------------------

    def to_i
        '' * self
    end

    to_i

1. Save the above code as `recursive_to_i.rb`.
2. Run either:
   a) `mruby recursive_to_i.rb`
   b) `sandbox recursive_to_i.rb`
3. Both cause a segfault due to a process stack overflow.

Discussion
==========

Everything below assumes the latest master of the mruby repository as of Dec 08th, which is commit `b84e005fc36a3c669586cc66ab3c87630d7a5509`.

Since the above POC redefines `to_i` on `Object`, it is very easy to trigger the crash afterwards, for instance, by trying to use any subclass of `Object` without its own `to_i` in an integer context.

Incidentally, that mruby uses `to_i` for implicit conversion to an `Integer` seems wrong (the offending code being in object.c, line 561). For instance, MRI Ruby gives the following for the above POC:

    recursive_to_i.rb:2:in `*': no implicit conversion of Object into Integer (TypeError)
            from recursive_to_i.rb:2:in `to_i'
            from recursive_to_i.rb:5:in `<main>'<Paste>

However, the problem isn't limited to overriding `to_i`. Some other inputs that exploit the same bug:

nil_method_ensure.rb
--------------------

    def nil.m
        m a ensure m + a
    end

    nil.m

This one crashes only mruby and not the sandbox:

module_new_do.rb
----------------

    def a
        Module.new do
            a
        end
    end

    a

There are probably others since the underlying cause is the same.

Solution
========

While there may be a way to fix these cases individually, it is our opinion that the C-level recursion depth should be tracked and, ideally, limited according to the size of the process stack.

We managed to produce recursions that spend as much as 3200 bytes of the process stack between two recursive `mrb_vm_run` calls while only spending 80 bytes of the Ruby stack. Based on some testing, we've derived a loose upper limit of the number of recursions needed to crash the interpreter in this scenario:

    (stack_size * 0.98) / 3200

Tightening the factors up a bit, we arrive at the following formula that should give a good safety margin (assumptions: 10% of the stack used before first call to `mrb_vm_run`, 4096 bytes of the process stack used between two recursive calls):

    (stack_size * 0.9) / 4096 - 1

We supply a patch where we've implemented C-level recursion depth tracking based on this formula, hardcoded to a stack size of 8 MiB (defined as a macro constant). Ideally, the process stack size should be determined using a method appropriate for the OS (for instance, `getrlimit` on POSIX).

--
Denis Kasak
Damir Jelić

## Attachments
- recursive_to_i.rb
- nil_method_ensure.rb
- module_new_do.rb
- recursion_limit.patch
