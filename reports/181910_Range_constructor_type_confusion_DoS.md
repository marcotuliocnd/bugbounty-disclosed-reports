# Range constructor type confusion DoS

## Report Details
- **Report ID**: 181910
- **URL**: https://hackerone.com/reports/181910
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-13T12:41:55.264Z
- **Disclosed**: 2016-12-17T01:03:07.728Z

## Reporter
- **Username**: h72
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
It's possible to crash mruby by redefining the `Range` class and then using the range literal syntax:

    Range = Array
    (1..2).inspect

The `mrb_range_new` function allocates and initializes a range object backed by the `RRange` struct, however it uses runtime constant lookup to find the `Range` class object. Redefining the `Range` constant to point to a different class and calling an instance method causes a segfault, as the `RRange::edges` field is confused for the `iv` field on other structs.

It may be possible to achieve RCE through this vulnerability, but there are significant complicating factors and I have not spent the time trying to develop an RCE PoC.

I have attached a patch which fixes this bug. My patch adds a `range_class` field to `mrb_state`, following the pattern other core classes use to avoid runtime constant lookups.

## Attachments
- mruby-range-dos.patch
