#  The VTP parser in tcpdump before 4.9.2 has a buffer over-read in print-vtp.c:vtp_print()

## Report Details
- **Report ID**: 802846
- **URL**: https://hackerone.com/reports/802846
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-02-23T15:03:56.348Z
- **Disclosed**: 2021-08-22T03:56:50.541Z

## Reporter
- **Username**: bags
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hello,

The vulnerable code portion is linked below. The linked function is responsible for printing VTP packet payload information to the terminal (e.g., stdout)

https://github.com/the-tcpdump-group/tcpdump/commit/ae83295915d08a854de27a88efac5dd7353e6d3f#diff-8c6895b252e6da31d60a7866973d5787L262-L268

The issue may be reproduced as follows

Check out vulnerable tcpdump commit (< 4.9.2) as follows

```
$ git clone -b e0d8ee571438c755ff988f70886f8c4f5e9a8434 https://github.com/the-tcpdump-group/tcpdump
Build it with afl and AddressSanitizer as follows (please install libpcap before this step)
$ CC=afl-gcc
$ AFL_USE_ASAN=1 make -j
```

Run tcpdump against linked payload (link: https://github.com/the-tcpdump-group/tcpdump/blob/ae83295915d08a854de27a88efac5dd7353e6d3f/tests/vtp_asan-3.pcap?raw=true)

```
$ tcpdump -nvr <payload>
reading from file /tmp/vtp_asan-3.pcap, link-type MFR (FRF.16 Frame Relay)
=================================================================
==3747==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x61200000015c at pc 0x562e64fcc5d2 bp 0x7ffdd3033300 sp 0x7ffdd30332f0
READ of size 1 at 0x61200000015c thread T0
    #0 0x562e64fcc5d1 in fn_printzp util-print.c:217
    #1 0x562e64fb757e in vtp_print print-vtp.c:262
    #2 0x562e64ea3aae in snap_print print-llc.c:493
    #3 0x562e64e0cba5 in fr_print print-fr.c:336
    #4 0x562e64e0dc9e in mfr_print print-fr.c:563
    #5 0x562e64d57e1e in pretty_print_packet print.c:332
    #6 0x562e64d30d8d in print_packet tcpdump.c:2590
    #7 0x562e65003a78 in pcap_offline_read savefile.c:561
    #8 0x562e64ff29ee in pcap_loop pcap.c:2737
    #9 0x562e64d2474d in main tcpdump.c:2093
    #10 0x7f9726cb6b96 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b96)
    #11 0x562e64d2c769 in _start (/home/bhargava/work/github/tcpdump/tcpdump+0x17b769)

0x61200000015c is located 0 bytes to the right of 284-byte region [0x612000000040,0x61200000015c)
allocated by thread T0 here:
    #0 0x7f972737ab50 in __interceptor_malloc (/usr/lib/x86_64-linux-gnu/libasan.so.4+0xdeb50)
    #1 0x562e6500480a in pcap_check_header sf-pcap.c:404

SUMMARY: AddressSanitizer: heap-buffer-overflow util-print.c:217 in fn_printzp
Shadow bytes around the buggy address:
  0x0c247fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c247fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c247fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c247fff8000: fa fa fa fa fa fa fa fa 00 00 00 00 00 00 00 00
  0x0c247fff8010: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c247fff8020: 00 00 00 00 00 00 00 00 00 00 00[04]fa fa fa fa
  0x0c247fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fff8060: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c247fff8070: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
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
==3747==ABORTING
```

It is acknowledged here(link: https://github.com/the-tcpdump-group/tcpdump/commit/ae83295915d08a854de27a88efac5dd7353e6d3f) that I (Bhargava Shastry) am the original reporter of the issue.

To prove that this hackerone account belongs to me, I have hosted a file with the following message on my github page(link: https://bshastry.github.io/.well-known/hackerone.txt)

hello @turtle_shell @hackerone

If you have any further queries, please let me know.

## Impact

I believe that information disclosure is possible.

## Attachments
No attachments
