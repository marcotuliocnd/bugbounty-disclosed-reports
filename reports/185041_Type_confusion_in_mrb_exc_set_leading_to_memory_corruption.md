# Type confusion in mrb_exc_set leading to memory corruption

## Report Details
- **Report ID**: 185041
- **URL**: https://hackerone.com/reports/185041
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-11-25T09:46:06.737Z
- **Disclosed**: 2016-12-16T20:26:40.161Z

## Reporter
- **Username**: raydot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Similar to #181871, but the bug is more general. The E_*_ERROR macros are not constants, so the exception types can be redefined to not be exceptions:

    #define E_NOTIMP_ERROR              (mrb_class_get(mrb, "NotImplementedError"))

This means that any code calling mrb_raise on an exception macro can instead get a non-exception object, leading to memory corruption and arbitrary code execution. This snippet causes a native crash in mruby-engine:

    NotImplementedError = String
    Module.constants # mrb_raise(mrb, E_NOTIMP_ERROR, "Module.constants not implemented");

This should be fixed by making mrb_exc_set check that it is an exception type. Attached is a patch to mruby to fix this problem.


## Attachments
- patch5.diff
