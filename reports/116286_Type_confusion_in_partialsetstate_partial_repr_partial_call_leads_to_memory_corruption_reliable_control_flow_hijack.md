# Type confusion in partial.setstate, partial_repr, partial_call leads to memory corruption, reliable control flow hijack

## Report Details
- **Report ID**: 116286
- **URL**: https://hackerone.com/reports/116286
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-13T19:23:44.612Z
- **Disclosed**: 2016-09-20T04:01:06.202Z

## Reporter
- **Username**: nedw
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
See my official writeups here:

http://bugs.python.org/issue25944
http://bugs.python.org/issue25945

The maintainers merged these bug reports.
In one case, the type confusion leads to a reliable control of the instruction pointer as calling `repr` on a corrupted partial calls a function pointer that is controlled reliably by the user. I've uploaded that case here as well.

## Attachments
- partialpoc.py
