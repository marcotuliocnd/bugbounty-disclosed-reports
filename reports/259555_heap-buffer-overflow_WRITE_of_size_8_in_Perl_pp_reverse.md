# heap-buffer-overflow (WRITE of size 8) in Perl_pp_reverse()

## Report Details
- **Report ID**: 259555
- **URL**: https://hackerone.com/reports/259555
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-13T22:06:14.989Z
- **Disclosed**: 2018-05-07T18:54:04.232Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
[Reported to the Perl security mailing list on 11 June 2017](https://rt.perl.org/Ticket/Display.html?id=131555).
Fixed pushed to git on [13 June 2017](https://github.com/Perl/perl5/commit/d5d91c1e89a7882099b788fe66dfd438c0eb0a9e). No advisory.

```
==376==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x619000009a80 at pc 0xd1b9c4 bp 0x7ffd21892230 sp 0x7ffd21892228
WRITE of size 8 at 0x619000009a80 thread T0
    #0 0xd1b9c3 in Perl_pp_reverse /root/perl/pp.c:5740
    #1 0x926e76 in Perl_runops_debug /root/perl/dump.c:2451
    #2 0x59f02a in S_run_body /root/perl/perl.c:2543
    #3 0x59f02a in perl_run /root/perl/perl.c:2471
    #4 0x43506d in main /root/perl/perlmain.c:123
    #5 0x7f474413cb44 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b44)
    #6 0x436015 (/root/perl/perl+0x436015)

0x619000009a80 is located 0 bytes to the right of 1024-byte region [0x619000009680,0x619000009a80)
allocated by thread T0 here:
    #0 0x7f474528e73f in malloc (/usr/lib/x86_64-linux-gnu/libasan.so.1+0x5473f)
    #1 0x962c71 in Perl_safesysmalloc /root/perl/util.c:153

SUMMARY: AddressSanitizer: heap-buffer-overflow /root/perl/pp.c:5740 Perl_pp_reverse
```

**What is happening?**
`Scalar context reverse doesn't extend the stack before pushing the result. This is safe unless reverse doesn't have an argument (when it defaults to $_).`

The following code can trigger it:
```
    $_ = "";
    for my $i (1..1000) {
        () = (1..$i, scalar reverse);
    }
```

**Is this a security bug?**
Maybe. Dave Mitchell, one of the main Perl devs says this: `"The attacker would need to find some code that uses argless reverse() in scalar context, where reverse() is called when the args stack is exactly full. In this case, the address of the reverse op's target SV will be written to the 4 or 8 bytes following the malloced stack block. The attacker can't control what is written."`


## Attachments
No attachments
