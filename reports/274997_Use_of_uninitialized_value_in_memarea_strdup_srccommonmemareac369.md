# Use of uninitialized value in memarea_strdup (src/common/memarea.c:369)

## Report Details
- **Report ID**: 274997
- **URL**: https://hackerone.com/reports/274997
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-10-06T09:20:30.540Z
- **Disclosed**: 2017-10-25T20:40:43.658Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Triggered in `51e4748 `, compiled with clang 6.0.0-trunk and -fsanitize=memory.

`./fuzz-hsdescv2 < test001`

```
Uninitialized bytes in __interceptor_strlen at offset 0 inside [0x7fff5525ff80, 51)
==19693==WARNING: MemorySanitizer: use-of-uninitialized-value
    #0 0x5570edfe5fbd in memarea_strdup /root/tor/src/common/memarea.c:369:14
    #1 0x5570edc4d77c in get_next_token /root/tor/src/or/parsecommon.c
    #2 0x5570edc4a097 in tokenize_string /root/tor/src/or/parsecommon.c:72:11
    #3 0x5570edda67f7 in rend_parse_v2_service_descriptor /root/tor/src/or/routerparse.c:5197:7
    #4 0x5570ed946d02 in fuzz_main /root/tor/src/test/fuzz/fuzz_hsdescv2.c:40:10
    #5 0x5570ed94677a in main /root/tor/src/test/fuzz/fuzzing_common.c:179:3
    #6 0x7fee60f8a3f0 in __libc_start_main /build/glibc-mXZSwJ/glibc-2.24/csu/../csu/libc-start.c:291
    #7 0x5570ed8d47d9 in _start (/root/tor/src/test/fuzz/fuzz-hsdescv2+0x717d9)

SUMMARY: MemorySanitizer: use-of-uninitialized-value /root/tor/src/common/memarea.c:369:14 in memarea_strdup
```

## Attachments
- test001.gz
