# puttygen: 160MB memory leak while trying to extract openssh public key from crafted key file

## Report Details
- **Report ID**: 484930
- **URL**: https://hackerone.com/reports/484930
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-24T02:31:51.325Z
- **Disclosed**: 2019-11-03T16:43:06.420Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: putty_h1c

## Vulnerability Information
**Summary:**
After downloading putty-0.70-2019-01-17.53747ad.tar.gz, I compiled it on Debian 9 with Clang-8.0.0 and AddressSanitizer. A 160000844 byte (160MB) memory leak happens while trying to extract an OpenSSH public key from a crafted key file.

**Description:**
puttygen does not sufficiently track and release allocated memory after it has been used, which slowly consumes remaining memory. This is often triggered by improper handling of malformed data or unexpectedly interrupted sessions. 

## Steps To Reproduce:

1) Compile putty without GTK and with AddressSanitizer:
`CC=clang CXX=clang++ CFLAGS=-fsanitize=address CXXFLAGS=-fsanitize=address ./configure --without-gtk && make --j2`

2) Run puttygen against the crafted key file:
`./puttygen -L test0000.ppk`

Result:
```
INVALID-ALGORITHM FmqsPmWL usest

=================================================================
==31861==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 159999984 byte(s) in 1 object(s) allocated from:
    #0 0x4c6333 in malloc /b/swarming/w/ir/kitchen-workdir/src/third_party/llvm/    compiler-rt/lib/asan/asan_malloc_linux.cc:146:3
    #1 0x51971d in safemalloc /root/putty-0.70-2019-01-17.53747ad/memory.c:23:6
    #2 0x587f5f in read_blob /root/putty-0.70-2019-01-17.53747ad/sshpubk.c:535:1    2
    #3 0x589ce0 in ssh2_userkey_loadpub /root/putty-0.70-2019-01-17.53747ad/sshp    ubk.c:1126:10
    #4 0x4f7a73 in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:810:7
    #5 0x7f3c8b9632e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x20    2e0)

Direct leak of 128 byte(s) in 1 object(s) allocated from:
    #0 0x4c6333 in malloc /b/swarming/w/ir/kitchen-workdir/src/third_party/llvm/    compiler-rt/lib/asan/asan_malloc_linux.cc:146:3
    #1 0x51971d in safemalloc /root/putty-0.70-2019-01-17.53747ad/memory.c:23:6
    #2 0x587d1a in read_body /root/putty-0.70-2019-01-17.53747ad/sshpubk.c:504:1    2
    #3 0x589aac in ssh2_userkey_loadpub /root/putty-0.70-2019-01-17.53747ad/sshp    ubk.c:1111:20
    #4 0x4f7a73 in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:810:7
    #5 0x7f3c8b9632e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x20    2e0)

Direct leak of 128 byte(s) in 1 object(s) allocated from:
    #0 0x4c6333 in malloc /b/swarming/w/ir/kitchen-workdir/src/third_party/llvm/    compiler-rt/lib/asan/asan_malloc_linux.cc:146:3
    #1 0x51971d in safemalloc /root/putty-0.70-2019-01-17.53747ad/memory.c:23:6
    #2 0x587d1a in read_body /root/putty-0.70-2019-01-17.53747ad/sshpubk.c:504:1    2
    #3 0x58aa52 in ssh2_userkey_encrypted /root/putty-0.70-2019-01-17.53747ad/ss    hpubk.c:1188:20
    #4 0x4f7389 in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:744:18
    #5 0x7f3c8b9632e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x20    2e0)

Direct leak of 48 byte(s) in 1 object(s) allocated from:
    #0 0x4c6333 in malloc /b/swarming/w/ir/kitchen-workdir/src/third_party/llvm/    compiler-rt/lib/asan/asan_malloc_linux.cc:146:3
    #1 0x51971d in safemalloc /root/putty-0.70-2019-01-17.53747ad/memory.c:23:6
    #2 0x5bf67f in strbuf_new /root/putty-0.70-2019-01-17.53747ad/utils.c:431:31
    #3 0x4f7a4e in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:809:28
    #4 0x7f3c8b9632e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x20    2e0)

Direct leak of 8 byte(s) in 1 object(s) allocated from:
    #0 0x4c6333 in malloc /b/swarming/w/ir/kitchen-workdir/src/third_party/llvm/    compiler-rt/lib/asan/asan_malloc_linux.cc:146:3
    #1 0x51971d in safemalloc /root/putty-0.70-2019-01-17.53747ad/memory.c:23:6
    #2 0x5b8182 in filename_from_str /root/putty-0.70-2019-01-17.53747ad/unix/ux    misc.c:46:21
    #3 0x4f6b5f in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:556:15
    #4 0x7f3c8b9632e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x20    2e0)

Indirect leak of 512 byte(s) in 1 object(s) allocated from:
    #0 0x4c6333 in malloc /b/swarming/w/ir/kitchen-workdir/src/third_party/llvm/    compiler-rt/lib/asan/asan_malloc_linux.cc:146:3
    #1 0x51971d in safemalloc /root/putty-0.70-2019-01-17.53747ad/memory.c:23:6
    #2 0x5bf704 in strbuf_new /root/putty-0.70-2019-01-17.53747ad/utils.c:435:5
    #3 0x4f7a4e in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:809:28
    #4 0x7f3c8b9632e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x20    2e0)

Indirect leak of 36 byte(s) in 1 object(s) allocated from:
    #0 0x4c6333 in malloc /b/swarming/w/ir/kitchen-workdir/src/third_party/llvm/    compiler-rt/lib/asan/asan_malloc_linux.cc:146:3
    #1 0x51971d in safemalloc /root/putty-0.70-2019-01-17.53747ad/memory.c:23:6
    #2 0x5be819 in dupstr /root/putty-0.70-2019-01-17.53747ad/utils.c:235:13
    #3 0x5b818d in filename_from_str /root/putty-0.70-2019-01-17.53747ad/unix/ux    misc.c:47:17
    #4 0x4f6b5f in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:556:15
    #5 0x7f3c8b9632e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x20    2e0)

SUMMARY: AddressSanitizer: 160000844 byte(s) leaked in 7 allocation(s).

```

test0000.ppk SHA256: 0aa3fd97f319bc5ab9fcaafb94a5f6b05a3c3895d8d4256828a4d716e3960776

## Impact

Most memory leaks result in general software reliability problems, but if an attacker can intentionally trigger a memory leak, the attacker might be able to launch a denial of service attack (by crashing or hanging the program) or take advantage of other unexpected program behavior resulting from a low memory condition.

## Attachments
- test0000.ppk
