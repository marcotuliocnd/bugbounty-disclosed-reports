# Use of uninitialized value in networkstatus_parse_vote_from_string (src/or/routerparse.c:3533)

## Report Details
- **Report ID**: 276253
- **URL**: https://hackerone.com/reports/276253
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-10-11T04:47:19.502Z
- **Disclosed**: 2017-10-31T18:53:02.105Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Triggered in `22139c0`, compiled with `-fsanitize=memory` and clang 6.0.0-trunk.

`./fuzz-consense < test000bbb`

```
==9293==WARNING: MemorySanitizer: use-of-uninitialized-value
    #0 0x5611f7f7e4de in networkstatus_parse_vote_from_string /root/tor/src/or/routerparse.c:3533:23
    #1 0x5611f75bbbd1 in fuzz_main /root/tor/src/test/fuzz/fuzz_consensus.c:66:8
    #2 0x5611f75bb29d in main /root/tor/src/test/fuzz/fuzzing_common.c:179:3
    #3 0x7f9914298b44 in __libc_start_main /build/glibc-6V9RKT/glibc-2.19/csu/libc-start.c:287
    #4 0x5611f75488ce in _start (/root/tor/src/test/fuzz/fuzz-consensus+0x3bc8ce)

SUMMARY: MemorySanitizer: use-of-uninitialized-value /root/tor/src/or/routerparse.c:3533:23 in networkstatus_parse_vote_from_string
```

## Attachments
- test000bbb.gz
