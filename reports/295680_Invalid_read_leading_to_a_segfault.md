# Invalid read leading to a segfault

## Report Details
- **Report ID**: 295680
- **URL**: https://hackerone.com/reports/295680
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-06T13:49:53.358Z
- **Disclosed**: 2017-12-28T12:02:30.059Z

## Reporter
- **Username**: dgaletic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
===
The attached POC demonstrates invalid reads leading to a segfault.

Debug info
==========

gdb report:

    423│ dispatch_linked(codegen_scope *s, int pc)
    424│ {
    425│   mrb_code i;
    426│   int pos;
    427│
    428│   if (!pc) return;
    429│   for (;;) {
    430├───> i = s->iseq[pc];

    (gdb) p pc
    $1 = -32730

valgrind report:

    ==21952== Memcheck, a memory error detector
    ==21952== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
    ==21952== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
    ==21952== Command: mruby 2.rb
    ==21952== 
    ==21952== Invalid read of size 4
    ==21952==    at 0x17E1C2: dispatch_linked (codegen.c:430)
    ==21952==    by 0x177D68: codegen (codegen.c:1374)
    ==21952==    by 0x17F988: lambda_body (codegen.c:738)
    ==21952==    by 0x17D635: codegen (codegen.c:2767)
    ==21952==    by 0x17792C: codegen (codegen.c:1314)
    ==21952==    by 0x17E72E: scope_body (codegen.c:767)
    ==21952==    by 0x178B40: codegen (codegen.c:1624)
    ==21952==    by 0x1770BC: mrb_generate_code (codegen.c:3049)
    ==21952==    by 0x14C353: mrb_load_exec (parse.y:5815)
    ==21952==    by 0x14C8F6: mrb_load_file_cxt (parse.y:5849)
    ==21952==    by 0x10CD82: main (mruby.c:227)
    ==21952==  Address 0x5df11a8 is 65,816 bytes inside a block of size 131,072 free'd
    ==21952==    at 0x4C2F13F: realloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    ==21952==    by 0x140295: mrb_default_allocf (state.c:55)
    ==21952==    by 0x10D6BC: mrb_realloc_simple (gc.c:206)
    ==21952==    by 0x17DAF7: codegen_realloc (codegen.c:136)
    ==21952==    by 0x17DCA1: genop (codegen.c:154)
    ==21952==    by 0x17CC20: codegen (codegen.c:2600)
    ==21952==    by 0x17FE50: gen_call (codegen.c:893)
    ==21952==    by 0x178B65: codegen (codegen.c:1629)
    ==21952==    by 0x179180: codegen (codegen.c:1729)
    ==21952==    by 0x177ADF: codegen (codegen.c:1350)
    ==21952==    by 0x17F988: lambda_body (codegen.c:738)
    ==21952==    by 0x17D635: codegen (codegen.c:2767)
    ==21952==  Block was alloc'd at
    ==21952==    at 0x4C2F13F: realloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    ==21952==    by 0x140295: mrb_default_allocf (state.c:55)
    ==21952==    by 0x10D6BC: mrb_realloc_simple (gc.c:206)
    ==21952==    by 0x17DAF7: codegen_realloc (codegen.c:136)
    ==21952==    by 0x17DCA1: genop (codegen.c:154)
    ==21952==    by 0x177B11: codegen (codegen.c:1351)
    ==21952==    by 0x17F988: lambda_body (codegen.c:738)
    ==21952==    by 0x17D635: codegen (codegen.c:2767)
    ==21952==    by 0x17792C: codegen (codegen.c:1314)
    ==21952==    by 0x17E72E: scope_body (codegen.c:767)
    ==21952==    by 0x178B40: codegen (codegen.c:1624)
    ==21952==    by 0x1770BC: mrb_generate_code (codegen.c:3049)
    ==21952== 
    ==21952== Invalid read of size 4
    ==21952==    at 0x17DEEC: dispatch (codegen.c:399)
    ==21952==    by 0x17E1E8: dispatch_linked (codegen.c:432)
    ==21952==    by 0x177D68: codegen (codegen.c:1374)
    ==21952==    by 0x17F988: lambda_body (codegen.c:738)
    ==21952==    by 0x17D635: codegen (codegen.c:2767)
    ==21952==    by 0x17792C: codegen (codegen.c:1314)
    ==21952==    by 0x17E72E: scope_body (codegen.c:767)
    ==21952==    by 0x178B40: codegen (codegen.c:1624)
    ==21952==    by 0x1770BC: mrb_generate_code (codegen.c:3049)
    ==21952==    by 0x14C353: mrb_load_exec (parse.y:5815)
    ==21952==    by 0x14C8F6: mrb_load_file_cxt (parse.y:5849)
    ==21952==    by 0x10CD82: main (mruby.c:227)
    ==21952==  Address 0x5df11a8 is 65,816 bytes inside a block of size 131,072 free'd
    ==21952==    at 0x4C2F13F: realloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    ==21952==    by 0x140295: mrb_default_allocf (state.c:55)
    ==21952==    by 0x10D6BC: mrb_realloc_simple (gc.c:206)
    ==21952==    by 0x17DAF7: codegen_realloc (codegen.c:136)
    ==21952==    by 0x17DCA1: genop (codegen.c:154)
    ==21952==    by 0x17CC20: codegen (codegen.c:2600)
    ==21952==    by 0x17FE50: gen_call (codegen.c:893)
    ==21952==    by 0x178B65: codegen (codegen.c:1629)
    ==21952==    by 0x179180: codegen (codegen.c:1729)
    ==21952==    by 0x177ADF: codegen (codegen.c:1350)
    ==21952==    by 0x17F988: lambda_body (codegen.c:738)
    ==21952==    by 0x17D635: codegen (codegen.c:2767)
    ==21952==  Block was alloc'd at
    ==21952==    at 0x4C2F13F: realloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    ==21952==    by 0x140295: mrb_default_allocf (state.c:55)
    ==21952==    by 0x10D6BC: mrb_realloc_simple (gc.c:206)
    ==21952==    by 0x17DAF7: codegen_realloc (codegen.c:136)
    ==21952==    by 0x17DCA1: genop (codegen.c:154)
    ==21952==    by 0x177B11: codegen (codegen.c:1351)
    ==21952==    by 0x17F988: lambda_body (codegen.c:738)
    ==21952==    by 0x17D635: codegen (codegen.c:2767)
    ==21952==    by 0x17792C: codegen (codegen.c:1314)
    ==21952==    by 0x17E72E: scope_body (codegen.c:767)
    ==21952==    by 0x178B40: codegen (codegen.c:1624)
    ==21952==    by 0x1770BC: mrb_generate_code (codegen.c:3049)
    ==21952== 
    bug: dispatch on non JMP op
    ==21952== 
    ==21952== HEAP SUMMARY:
    ==21952==     in use at exit: 1,785,001 bytes in 4,587 blocks
    ==21952==   total heap usage: 4,691 allocs, 104 frees, 2,301,641 bytes allocated
    ==21952== 
    ==21952== LEAK SUMMARY:
    ==21952==    definitely lost: 0 bytes in 0 blocks
    ==21952==    indirectly lost: 0 bytes in 0 blocks
    ==21952==      possibly lost: 1,495,096 bytes in 87 blocks
    ==21952==    still reachable: 289,905 bytes in 4,500 blocks
    ==21952==         suppressed: 0 bytes in 0 blocks
    ==21952== Rerun with --leak-check=full to see details of leaked memory
    ==21952== 
    ==21952== For counts of detected and suppressed errors, rerun with: -v
    ==21952== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 0 from 0)


Test platform
=============
* Arch Linux

mruby SHA: 0e46b14b9e8cece4fd75b003a7a3391116dd6eee

Thank you,
Dinko Galetic
Denis Kasak

## Impact

Denial of service by causing segfaults.

## Attachments
- 2.rb
