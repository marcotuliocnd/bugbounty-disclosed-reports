# heap-buffer-overflow (READ of size 11) in Perl 5.25.x

## Report Details
- **Report ID**: 232150
- **URL**: https://hackerone.com/reports/232150
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-26T06:38:31.405Z
- **Disclosed**: 2017-05-28T19:23:48.944Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This issue was first reported to the Perl security mailing list on 19 August 2016. It was inadvertently made public in another bug report on 23 August 2016. It was finally marked fixed around 23 January 2017. 

[Original bug report](https://rt.perl.org/Ticket/Display.html?id=128998):

```
perl -e 'v300&O|0' triggers a heap-buffer-overflow in Perl_my_atof2 (numeric.c:1349). This was found with AFL, ASAN and libdislocator.so and affects v5.25.4 (v5.25.3-305-g8c6b0c7). Perl 5.20.2 returns errors, doesn't crash.

==23567==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60200000e1ba at pc 0x0000004abd02 bp 0x7ffced70a210 sp 0x7ffced7099d0
READ of size 11 at 0x60200000e1ba thread T0
    #0 0x4abd01 in __interceptor_strlen (/root/perl/perl+0x4abd01)
    #1 0xc2edf7 in Perl_my_atof2 /root/perl/numeric.c:1349:28
    #2 0xc2e7a5 in Perl_my_atof /root/perl/numeric.c:1244:13
    #3 0x99bbfc in S_sv_setnv /root/perl/sv.c:2113:9
    #4 0x8fd5fe in S_sv_2iuv_common /root/perl/sv.c:2298:13
    #5 0x900fd5 in Perl_sv_2uv_flags /root/perl/sv.c:2574:6
    #6 0x9c7738 in Perl_pp_bit_or /root/perl/pp.c:2463:35
    #7 0x7f1d93 in Perl_runops_debug /root/perl/dump.c:2234:23
    #8 0x5a11d6 in S_run_body /root/perl/perl.c:2524:2
    #9 0x5a11d6 in perl_run /root/perl/perl.c:2447
    #10 0x4de85d in main /root/perl/perlmain.c:123:9
    #11 0x7ff026dedb44 in __libc_start_main /build/glibc-uPj9cH/glibc-2.19/csu/libc-start.c:287
    #12 0x4de4cc in _start (/root/perl/perl+0x4de4cc)

0x60200000e1ba is located 0 bytes to the right of 10-byte region [0x60200000e1b0,0x60200000e1ba)
allocated by thread T0 here:
    #0 0x4c0e4b in malloc (/root/perl/perl+0x4c0e4b)
    #1 0x7f5bd7 in Perl_safesysmalloc /root/perl/util.c:153:21
```

Reason for the bug:

```
The UTF-8 string path of bit-and in do_vop() doesn't NUL terminate the resulting string. The bit-or op then attempts to or the result of that and a number, so attempts to convert that result into a number and strlen() attempts to access the undefined bytes following the result of the bit-and. 
```

[First mention of it being a security issue](https://rt.perl.org/Ticket/Attachment/1418970/767269/) - 19 August 2016

[... proper to treat this as a security issue.](https://rt.perl.org/Ticket/Attachment/1418980/767280/) - 23 August 2016

It was eventually decided that this didn't warrant a release or CVE assignment and that the fix would just be [committed](https://perl5.git.perl.org/perl.git/commit/b43665fffa48dd179eba1b5616d4ca35b4def876) and a perldelta entry created. 



## Attachments
No attachments
