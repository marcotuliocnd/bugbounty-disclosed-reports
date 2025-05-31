# Segfault and/or potential unwanted (byte)code execution with "break" and "||=" inside a loop

## Report Details
- **Report ID**: 183356
- **URL**: https://hackerone.com/reports/183356
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-18T19:23:38.371Z
- **Disclosed**: 2016-12-16T21:42:19.613Z

## Reporter
- **Username**: dkasak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Introduction
============

Certain invalid inputs (invalid Ruby programs) crash mruby and mruby_engine (including the parent MRI VM). The programs always involve the `||=` operator, loops and the `break` keyword.

Proof of Concept
================

crash.rb
--------

    A ||= break while break

1. Save the above code as crash.rb
2. Run either:
    a) mruby crash.rb
    b) sandbox crash.rb
3. Both cause a segmentation fault.

Discussion
==========

Everything below assumes the latest master of the mruby repository as of Nov 18th, which is commit `0ff3ae1fbaed62010c54c43235e29cdc85da2f78`.

The above crashing example isn't the only one that we've managed to produce but is the minimal one so far. An infinite family of programs is able to exploit this bug to crash the interpreter, execute spurious bytecode that wasn't generated for the current program or even set the machine instruction pointer to some junk value (making this a limited form of unwated code execution, even though the executed code isn't arbitrary).

The generated AST and bytecode for the crashing case is as follows:

    mruby 1.2.0 (2015-11-17)
    00001 NODE_SCOPE:
    00001   NODE_BEGIN:
    00001     NODE_WHILE:
    00001       cond:
    00001         NODE_BREAK:
    00001       body:
    00001         NODE_OP_ASGN:
    00001           lhs:
    00001             NODE_CONST A
    00001           op='||' (666)
    00001           NODE_BREAK:
    irep 0x16b2970 nregs=2 nlocals=1 pools=0 syms=1 reps=0
    file: crash.rb
        1 000 OP_JMP    010
        1 001 OP_ONERR  005
        1 002 OP_GETCONST       R1      :A
        1 003 OP_POPERR 1
        1 004 OP_JMP    007
        1 005 OP_RESCUE R1
        1 006 OP_LOADF  R1
        1 007 OP_JMPIF  R1      010
        1 008 OP_JMP    008
        1 009 OP_SETCONST       :A      R1
        1 010 OP_JMP    018
        1 011 OP_JMPIF  R1      001
        1 012 OP_LOADNIL        R1
        1 013 OP_STOP

The odd thing to notice here is that the `OP_JMP` at 010 jumps beyond the last instruction. This is what leads to a potential execution of spurious bytecode since there may be valid opcodes beyond the end of the `iseq` array of the current `irep` (and indeed, we've seen this happen).

Furthermore, the index of the instruction onto which the invalid `OP_JMP` jumps to is equal I + A where I is the index of the instruction the `OP_JMP` at 000 jumps to (in this case 010) and A is the index of an `OP_JMP` instruction located prior to the invalid one (so in this case 010 + 008 = 018). Since each additional `break` inserted into the code inserts an additional `OP_JMP` instruction, this implies that the argument of the invalid `OP_JMP` can be increased almost without bounds (limited only by memory consumption and/or the maximum argument to `OP_JMP` instructions, which is `0xffff >> 1` = 32767).

As an example, the code:

larger.rb
---------

    A ||= break break break break while break

Yields the following bytecode:

file: larger.rb
    1 000 OP_JMP        013
    1 001 OP_ONERR      005
    1 002 OP_GETCONST   R1      :A
    1 003 OP_POPERR     1
    1 004 OP_JMP        007
    1 005 OP_RESCUE     R1
    1 006 OP_LOADF      R1
    1 007 OP_JMPIF      R1      013
    1 008 OP_JMP        008
    1 009 OP_JMP        017
    1 010 OP_JMP        019
    1 011 OP_JMP        021
    1 012 OP_SETCONST   :A      R1
    1 013 OP_JMP        024
    1 014 OP_JMPIF      R1      001
    1 015 OP_LOADNIL    R1
    1 016 OP_STOP

After the jump is made, the memory location might contain a valid mruby instruction or even something with an opcode larger than the number of opcodes contained in the `optable` in `vm.c`. Since the code in `mrb_vm_exec` jumps to addresses contained in the `optable`, indexed by the opcode number, this leads to a limited form of unwanted code execution, since memory locations after the `optable` may contain pointers to executable code by accident.

It is interesting to note that a very similar program doesn't cause a crash:

non-crash.rb
------------

    a ||= break while break

The only difference from the crashing case is the use of a lowercase variable name instead of an uppercase (so a non-constant, in Ruby terms).

Another non-crashing case is the following:

non-crash-other.rb
------------------

    A &&= break while break

The only difference here is the use of another assignment operator — `&&`, instead of `||`.

This gives us a hint as to where the problem is. The invalid jump length is ultimately set during code generation for the `NODE_WHILE` node of the AST in `codegen.c`, line 1426. Specifically, the jump lengths are adjusted *after* the loop is generated, on line 1438 of the same file, during the call of the function `loop_pop()`.

When this function is executed in the debugger when run on the `crash.rb` case, it may be noticed that the `s->loop` variable, which contains the loop context, contains two loops inside one another instead of only one: a `LOOP_NORMAL` (which is generated by the `while`) and a `LOOP_RESCUE`. The latter is generated during code generation for `NODE_OP_ASGN`, starting at line 1724 of `codegen.c`. Here we encounter this interesting special case:

      if ((len == 2 && name[0] == '|' && name[1] == '|') &&
          ((intptr_t)tree->car->car == NODE_CONST ||
           (intptr_t)tree->car->car == NODE_CVAR)) {

This explains why the problem only happens only when using the `||=` operator on Ruby constants. It is here that an additional `LOOP_RESCUE` loop context is created, and it is using this context that is used later on by `loop_pop`/`dispatch_linked` to generate the final arguments to the jump instructions.

Since this "loop" is generated simply to catch potential `NameError` exceptions generated when an unexisting constant is reference, it seems that this loop context shouldn't escape the generation of the code for the assignment operator.

Solution
========

Therefore, the solution we chose was to pop this loop context after the assignment code is generated. This makes the `loop_pop`/`dispatch_linked` function calls inside the `while` code generation operate on the loop context for the `while` loop instead and fixes the generated jump.

undef-constant-or-assign.patch
------------------------------
    diff --git a/mrbgems/mruby-compiler/core/codegen.c b/mrbgems/mruby-compiler/core/codegen.c
    index 9b064b8..bbe0f51 100644
    --- a/mrbgems/mruby-compiler/core/codegen.c
    +++ b/mrbgems/mruby-compiler/core/codegen.c
    @@ -1746,6 +1746,7 @@ codegen(codegen_scope *s, node *tree, int val)
            genop(s, MKOP_A(OP_RESCUE, exc));
            genop(s, MKOP_A(OP_LOADF, exc));
            dispatch(s, noexc);
    +        loop_pop(s, val);
        }
        else if ((intptr_t)tree->car->car == NODE_CALL) {
            node *n = tree->car->cdr;

With the above patch, we were unable to crash the VM through this bug nor generated any more jumps with invalid jump lengths. Furthermore, all tests pass successfully.

## Attachments
- crash.rb
- non-crash.rb
- larger.rb
- undef-constant-or-assign.patch
- non-crash-other.rb
