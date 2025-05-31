# Struct type confusion RCE

## Report Details
- **Report ID**: 181879
- **URL**: https://hackerone.com/reports/181879
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-11-13T07:21:17.397Z
- **Disclosed**: 2016-12-17T01:03:22.530Z

## Reporter
- **Username**: h72
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Heya!

I've been poking at mruby a bit more and I've found a vulnerability that allows an attacker to take control of the instruction pointer.

I've attached a proof of concept script that when run in mruby will jump to `0x0000133713371337` and segfault.

While the proof of concept script just jumps to an attacker controlled address and crashes, it would almost certainly be possible to achieve full remote code execution, especially given an arbitrary read/write primitive (which is easily created using the same techniques as in the proof of concept)

The proof of concept script has detailed annotations throughout about how it works, but I'm also happy to clarify anything if need be :)

Cheers,

███████

## Attachments
No attachments
