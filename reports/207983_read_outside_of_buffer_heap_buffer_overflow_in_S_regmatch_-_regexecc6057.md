# read outside of buffer (heap buffer overflow) in S_regmatch - regexec.c:6057

## Report Details
- **Report ID**: 207983
- **URL**: https://hackerone.com/reports/207983
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-21T19:06:08.632Z
- **Disclosed**: 2017-05-28T19:23:59.393Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Reported to the Perl security mailing list on 20 August 2016, reported fixed by `khw` on 30 August 2016. 

```
==14086==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61900000a4aa at pc 0x000000b9988f bp 0x7fff325d9630 sp 0x7fff325d9628
READ of size 1 at 0x61900000a4aa thread T0
    #0 0xb9988e in S_regmatch /root/perl/regexec.c:6057:24
    #1 0xb691ec in S_regtry /root/perl/regexec.c:3619:14
    #2 0xb5323c in S_find_byclass /root/perl/regexec.c:2357:9
    #3 0xb41439 in Perl_regexec_flags /root/perl/regexec.c:3368:13
    #4 0xa36982 in Perl_pp_substcont /root/perl/pp_ctl.c:225:18
    #5 0x7f1b53 in Perl_runops_debug /root/perl/dump.c:2234:23
    #6 0x5a0ff6 in S_run_body /root/perl/perl.c:2524:2
    #7 0x5a0ff6 in perl_run /root/perl/perl.c:2447
    #8 0x4de68d in main /root/perl/perlmain.c:123:9
    #9 0x7fdb3ea25b44 in __libc_start_main /build/glibc-uPj9cH/glibc-2.19/csu/libc-start.c:287
    #10 0x4de2fc in _start (/root/perl/perl+0x4de2fc)

0x61900000a4aa is located 2 bytes to the right of 1064-byte region [0x61900000a080,0x61900000a4a8)
allocated by thread T0 here:
    #0 0x4c0c7b in malloc (/root/perl/perl+0x4c0c7b)
    #1 0x7f5997 in Perl_safesysmalloc /root/perl/util.c:153:21

SUMMARY: AddressSanitizer: heap-buffer-overflow /root/perl/regexec.c:6057 S_regmatch
```
In some circumstances, this will just cause a crash (denial of service), in other circumstances, it could read outside of the buffer by up to 12 bytes:

```
That means the maximum it can extend beyond the string is 12 bytes, if the character is \xFF, and a UV is a quad. Otherwise it is 6 bytes or less.
```

The final resting place of this bug is https://rt.perl.org/Public/Bug/Display.html?id=129024 where you can see this mentioned as a security fix for maintenance release 5.22.4/5.24.2. 

## Attachments
No attachments
