# Garbage collector crash

## Report Details
- **Report ID**: 215854
- **URL**: https://hackerone.com/reports/215854
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-24T14:38:27.607Z
- **Disclosed**: 2017-04-15T14:45:02.271Z

## Reporter
- **Username**: dgaletic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
This github [issue](https://github.com/mruby/mruby/issues/3063] seems to have been reintroduced.

    f = Fiber.new do
        m = Fiber.current
        Fiber.yield Proc.new {}
    end

    f = f.resume
    GC.start
    
It causes mruby to abort due to a failed assertion.    
    
    $ mruby poc
    mruby: /home/user/repos/mruby/src/gc.c:698: mrb_gc_mark: Assertion `(obj)->tt != MRB_TT_FREE' failed.
    Aborted

The issue was reintroduced in ecee8c51b0ad8cddd9e422a3e5105f902d7e2781 and is still present in 051e40c0493f2de332f5439e3230c9fe6958bf1a.

The issue is fixed by reverting ecee8c51b0ad8cddd9e422a3e5105f902d7e2781.

Thank you,
Dinko Galetic
Denis Kasak

## Attachments
No attachments
