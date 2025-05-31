# heap-buffer-overflow (READ of size 61) in Perl_re_intuit_start()

## Report Details
- **Report ID**: 233440
- **URL**: https://hackerone.com/reports/233440
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-31T00:07:39.287Z
- **Disclosed**: 2017-06-05T18:54:27.251Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
[Reported to the Perl security mailing list on 25 August 2016](https://rt.perl.org/Ticket/Display.html?id=129085).

```
==17057==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60800000b978 at pc 0x0000004a9201 bp 0x7ffe97551890 sp 0x7ffe97551048
READ of size 61 at 0x60800000b978 thread T0
    #0 0x4a9200 in __interceptor_memcmp (/root/perl/perl+0x4a9200)
    #1 0xb46135 in Perl_re_intuit_start /root/perl/regexec.c:809:37
    #2 0xb3a3e5 in Perl_regexec_flags /root/perl/regexec.c:2988:6
    #3 0x8be7f9 in Perl_pp_match /root/perl/pp_hot.c:1836:10
    #4 0x7f1dd3 in Perl_runops_debug /root/perl/dump.c:2234:23
    #5 0x5a1234 in S_run_body /root/perl/perl.c:2525:2
    #6 0x5a1234 in perl_run /root/perl/perl.c:2448
    #7 0x4de85d in main /root/perl/perlmain.c:123:9
    #8 0x7f8899228b44 in __libc_start_main /build/glibc-uPj9cH/glibc-2.19/csu/libc-start.c:287
    #9 0x4de4cc in _start (/root/perl/perl+0x4de4cc)

0x60800000b978 is located 0 bytes to the right of 88-byte region [0x60800000b920,0x60800000b978)
allocated by thread T0 here:
    #0 0x4c113e in realloc (/root/perl/perl+0x4c113e)
    #1 0x7f6306 in Perl_safesysrealloc /root/perl/util.c:274:18

SUMMARY: AddressSanitizer: heap-buffer-overflow ??:0 __interceptor_memcmp
```

##What is happening?##
```
When a match is anchored against the start of a string, the regexp can be compiled to include a fixed string match against a fixed offset in the string. In some cases, where the matched against string included UTF-8 before the fixed offset, this could result in attempting a memcmp() which overlaps the end of the string and potentially past the end of the allocated memory.
```

##Arguments for:##
On [29 August 2016](https://rt.perl.org/Ticket/Attachment/1420527/768174/), Tony says `It *might* be possible to use this as a hard to trigger denial of service attack, eg. if the memcmp() went past the end of a page into unmapped memory.`

On the same day in [another comment](https://rt.perl.org/Ticket/Attachment/1420627/768230/), Tony says `An attacker that can control the regexp *might* be able to use that to examine the contents of memory beyond the terminating NUL, which would be critical if that previously held a password or anything else sensitive.`

##Arguments Against:##
On [6 September 2016](https://rt.perl.org/Ticket/Attachment/1422020/769144/), Dave says `I don't think this is a security issue any more, and I think your patch should be applied.`

##Fix##
Patch was released on 30 October 2016 and it was released today, 30 May 2017, with Perl 5.26.0. (Worth noting that 52 of the bug fixes in Perl 5.26.0 were from my reports).

## Attachments
No attachments
