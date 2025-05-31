# Range#initialize_copy null pointer dereference

## Report Details
- **Report ID**: 181685
- **URL**: https://hackerone.com/reports/181685
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-12T01:19:47.017Z
- **Disclosed**: 2016-12-17T01:03:44.537Z

## Reporter
- **Username**: h72
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Heya!

It's possible to segfault mruby through mruby-engine with the following snippet of code:

    Range.remove_method(:initialize_copy)
    (1..2).dup.to_s

This can be triggered through mruby-engine like this:

    MRubyEngine.new(512*1024, 1000, 1000).sandbox_eval("/tmp", %{
      Range.remove_method(:initialize_copy)
      (1..2).dup.to_s
    })

The `dup` and `clone` methods allocate a new object and then call `initialize_copy` on the new object with the old object as an argument to copy over internal state.

Removing `Range#initialize_copy` makes it possible to construct an uninitialized `Range` object. Calling (pretty much) any instance method on the uninitialized `Range` object afterwards causes mruby to dereference a null pointer, leading to a segfault.

I've attached a patch that fixes the bug by copying internal range state before calling `initialize_copy`, similar to what mruby already does for classes and modules.

## Attachments
- range-initialize-copy-segfault.patch
