# Heap-buffer-overflow in Perl__byte_dump_string (utf8.c) could lead to memory leak

## Report Details
- **Report ID**: 480778
- **URL**: https://hackerone.com/reports/480778
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-01-16T08:31:57.672Z
- **Disclosed**: 2019-10-24T20:57:47.575Z

## Reporter
- **Username**: tmnt53
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
With crafted regex match, I have found a heap-over-flow in function Perl__byte_dump_string, which would lead to memory leak.
* Reported to the [Perl security mailing list](https://rt.perl.org/Public/Bug/Display.html?id=132063) on 11 Sep 2017.
* Confirmed as a security flaw by TonyC on 24 Feb 2018
* CVE-2018-6797 assigned to this flaw on 7 Feb 2018
* [Public security advisory](https://github.com/Perl/perl5/blob/blead/pod/perl5262delta.pod) released on 14 April 2018
```
=================================================================
==2895==ERROR: AddressSanitizer: heap-buffer-overflow on address 0xb610081c at pc 0x08a72387 bp 0xbfea6038 sp 0xbfea602c
WRITE of size 4 at 0xb610081c thread T0
    #0 0x8a72386 in S_pack_rec /root/karas/perl5-blead/pp_pack.c:2703:17
    #1 0x8a42706 in Perl_packlist /root/karas/perl5-blead/pp_pack.c:1980:11
    #2 0x8a73626 in Perl_pp_pack /root/karas/perl5-blead/pp_pack.c:3135:5
    #3 0x84dc7ac in Perl_runops_debug /root/karas/perl5-blead/dump.c:2465:23
    #4 0x818858a in S_fold_constants /root/karas/perl5-blead/op.c:4557:2
    #5 0x8186c5a in Perl_op_convert_list /root/karas/perl5-blead/op.c:4896:12
    #6 0x8363e7e in Perl_yyparse /root/karas/perl5-blead/perly.y:889:23
    #7 0x8232350 in S_parse_body /root/karas/perl5-blead/perl.c:2401:9
    #8 0x82285e3 in perl_parse /root/karas/perl5-blead/perl.c:1719:2
    #9 0x81494a6 in main /root/karas/perl5-blead/perlmain.c:121:18
    #10 0xb74d5636 in __libc_start_main /build/glibc-KM3i_a/glibc-2.23/csu/../csu/libc-start.c:291
    #11 0x8075847 in _start (/root/karas/perl5-blead/perl+0x8075847)

0xb610081c is located 2 bytes to the right of 10-byte region [0xb6100810,0xb610081a)
allocated by thread T0 here:
    #0 0x8119b84 in malloc (/root/karas/perl5-blead/perl+0x8119b84)
    #1 0x84e2987 in Perl_safesysmalloc /root/karas/perl5-blead/util.c:153:21

SUMMARY: AddressSanitizer: heap-buffer-overflow /root/karas/perl5-blead/pp_pack.c:2703:17 in S_pack_rec
Shadow bytes around the buggy address:
  0x36c200b0: fa fa fd fd fa fa fd fd fa fa fd fd fa fa 00 04
  0x36c200c0: fa fa fd fd fa fa 00 04 fa fa 00 04 fa fa 00 04
  0x36c200d0: fa fa 00 04 fa fa 00 04 fa fa 00 04 fa fa 00 04
  0x36c200e0: fa fa 00 04 fa fa 00 04 fa fa 00 04 fa fa 00 04
  0x36c200f0: fa fa fd fa fa fa fd fd fa fa 00 02 fa fa 01 fa
=>0x36c20100: fa fa 00[02]fa fa 00 02 fa fa fd fd fa fa 00 04
  0x36c20110: fa fa 02 fa fa fa 00 02 fa fa 07 fa fa fa 00 02
  0x36c20120: fa fa 00 02 fa fa 00 00 fa fa 00 05 fa fa 00 01
  0x36c20130: fa fa 00 07 fa fa 00 fa fa fa 00 02 fa fa 05 fa
  0x36c20140: fa fa 00 02 fa fa 06 fa fa fa 00 02 fa fa 05 fa
  0x36c20150: fa fa 00 05 fa fa 04 fa fa fa 05 fa fa fa 05 fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:       fa
  Heap right redzone:      fb
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack partial redzone:   f4
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==2895==ABORTING
```

## Impact

Depending on the heap implementation a remote attacker could leak heap information to bypass ASLR.

## Attachments
No attachments
