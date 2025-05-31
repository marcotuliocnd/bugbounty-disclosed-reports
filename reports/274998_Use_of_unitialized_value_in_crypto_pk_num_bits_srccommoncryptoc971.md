# Use of unitialized value in crypto_pk_num_bits (src/common/crypto.c:971)

## Report Details
- **Report ID**: 274998
- **URL**: https://hackerone.com/reports/274998
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-10-06T09:25:44.100Z
- **Disclosed**: 2023-11-28T09:02:03.777Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Triggered in `51e4748`, compiled with clang 6.0.0-trunk and -fsanitize=memory.

`./fuzz-hsdescv2 < test002`

```
==20245==WARNING: MemorySanitizer: use-of-uninitialized-value
    #0 0x558a63e2d816 in crypto_pk_num_bits /root/tor/src/common/crypto.c:971:3
    #1 0x558a63b8f66a in token_check_object /root/tor/src/or/parsecommon.c:212:23
    #2 0x558a63b8f66a in get_next_token /root/tor/src/or/parsecommon.c:397
    #3 0x558a63b8d097 in tokenize_string /root/tor/src/or/parsecommon.c:72:11
    #4 0x558a63ce97f7 in rend_parse_v2_service_descriptor /root/tor/src/or/routerparse.c:5197:7
    #5 0x558a63889d02 in fuzz_main /root/tor/src/test/fuzz/fuzz_hsdescv2.c:40:10
    #6 0x558a6388977a in main /root/tor/src/test/fuzz/fuzzing_common.c:179:3
    #7 0x7fa41c9773f0 in __libc_start_main /build/glibc-mXZSwJ/glibc-2.24/csu/../csu/libc-start.c:291
    #8 0x558a638177d9 in _start (/root/tor/src/test/fuzz/fuzz-hsdescv2+0x717d9)

SUMMARY: MemorySanitizer: use-of-uninitialized-value /root/tor/src/common/crypto.c:971:3 in crypto_pk_num_bits
```

## Attachments
- test002.gz
