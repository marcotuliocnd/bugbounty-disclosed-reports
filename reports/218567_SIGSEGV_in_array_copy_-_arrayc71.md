# SIGSEGV in array_copy - array.c:71

## Report Details
- **Report ID**: 218567
- **URL**: https://hackerone.com/reports/218567
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-04T16:56:10.017Z
- **Disclosed**: 2017-04-13T22:44:41.115Z

## Reporter
- **Username**: ilsani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
File [2] as input causes a segfault in mruby.

mruby crashes in ary_copy (array.c:71):
```
Program received signal SIGSEGV, Segmentation fault.
0x000000000040e088 in array_copy (src=<optimized out>, size=<optimized out>, dst=<optimized out>) at /tmp/mruby/src/array.c:71
71          dst[i] = src[i];
```

Test platform:
Linux 3.16.0-4-amd64 #1 SMP Debian 3.16.39-1+deb8u1 x86_64 GNU/Linux

## Attachments
- backtrace.txt
- input.txt
