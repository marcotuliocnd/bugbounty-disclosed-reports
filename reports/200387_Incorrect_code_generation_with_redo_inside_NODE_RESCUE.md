# Incorrect code generation with redo inside NODE_RESCUE.

## Report Details
- **Report ID**: 200387
- **URL**: https://hackerone.com/reports/200387
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-01-22T18:09:42.398Z
- **Disclosed**: 2017-02-28T13:30:14.189Z

## Reporter
- **Username**: dgaletic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The following code causes mruby to use up all available memory:

`class A redo
rescue c
end`

Following the execution, we see the code in codegen.c jumping between
CASE(OP_ONERR) and CASE(OP_JMP). CASE(OP_ONERR) uses realloc to double
the size of mrb->c->rescue, and since it is stuck in an infinite loop
between the two instructions, it runs out of memory.

The problematic jump is visible in the bytcode (emphasis added).

00001 NODE_SCOPE:
00001   NODE_BEGIN:
00001     NODE_CLASS:
00003       :A
00003       body:
00001         NODE_RESCUE:
00003           body:
00001             NODE_BEGIN:
00001               NODE_REDO
00003           rescue:
00003             handle classes:
00002               NODE_FCALL:
00002                 NODE_SELF
00002                 method='c' (670)
00003             rescue body:
00003               NODE_BEGIN:

irep 0x715200 nregs=3 nlocals=1 pools=0 syms=1 reps=1
    1 000 OP_LOADNIL    R1
    1 001 OP_LOADNIL    R2
    1 002 OP_CLASS      R1      :A
    1 003 OP_EXEC       R1      I(+1)
    1 004 OP_STOP

irep 0x71b400 nregs=4 nlocals=1 pools=0 syms=2 reps=0
    **1 000 OP_ONERR      003**   <------- Infinite loop
    **1 001 OP_JMP        000**   <------- created here.
    1 002 OP_JMP        013
    1 003 OP_RESCUE     R1
    2 004 OP_LOADSELF   R2
    2 005 OP_SEND       R2      :c      0
    2 006 OP_MOVE       R3      R1
    2 007 OP_SEND       R2      :===    1
    2 008 OP_JMPIF      R2      010
    2 009 OP_JMP        012
    3 010 OP_LOADNIL    R1
    3 011 OP_JMP        014
    3 012 OP_RAISE      R1
    3 013 OP_POPERR     1
    3 014 OP_RETURN     R1      return

Testing the same code with MRI Ruby shows that MRI Ruby rejects it as a syntax
error. It would seem MRI Ruby forbids the use of `redo` in the context of
`rescue` so the patch below disallows the related LOOP_* types. The test suite
runs successfully with the patch. The bug is mitigated inside the mruby-engine
sandbox because it triggers the instruction quota.

```
--- a/mrbgems/mruby-compiler/core/codegen.c
+++ b/mrbgems/mruby-compiler/core/codegen.c
@@ -2031,7 +2031,7 @@ codegen(codegen_scope *s, node *tree, int val)
     break;
 
   case NODE_REDO:
-    if (!s->loop) {
+    if (!s->loop || s->loop->type == LOOP_BEGIN || s->loop->type == LOOP_RESCUE) {
       raise_error(s, "unexpected redo");
     }
     else {
```


## Attachments
- 0001-Fix-incorrect-code-generation-with-redo-inside-NODE_.patch
