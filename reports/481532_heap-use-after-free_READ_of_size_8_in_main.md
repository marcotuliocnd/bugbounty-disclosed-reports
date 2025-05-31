# heap-use-after-free (READ of size 8) in main()

## Report Details
- **Report ID**: 481532
- **URL**: https://hackerone.com/reports/481532
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-17T17:27:05.196Z
- **Disclosed**: 2019-11-03T16:42:50.258Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: putty_h1c

## Vulnerability Information
**Summary:** 
After downloading putty-0.70-2019-01-17.53747ad.tar.gz, I compiled it on Debian 9 with Clang-8.0.0 and AddressSanitizer and while trying to extract a public key from a crafted key, I triggered a heap-use-after-free in main().

**Description:** [add more details about this vulnerability]

## Steps To Reproduce:

1. Compile putty without GTK and with AddressSanitizer.
```
CC=clang CXX=clang++ CFLAGS=-fsanitize=address CXXFLAGS=-fsanitize=address ./configure --without-gtk && make --j2
```

2. `./puttygen -L test0025.ppk`

```
==24482==ERROR: AddressSanitizer: heap-use-after-free on address 0x604000000018 at pc 0x0000004f9271 bp 0x7ffe82ceee30 sp 0x7ffe82ceee28
READ of size 8 at 0x604000000018 thread T0
    #0 0x4f9270 in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:979:45
    #1 0x7f019934a2e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)
    #2 0x41db89 in _start (/root/putty-0.70-2019-01-17.53747ad/puttygen+0x41db89)

0x604000000018 is located 8 bytes inside of 48-byte region [0x604000000010,0x604000000040)
freed by thread T0 here:
    #0 0x4c5fb2 in __interceptor_free /b/swarming/w/ir/kitchen-workdir/src/third_party/llvm/compiler-rt/lib/asan/asan_malloc_linux.cc:124:3
    #1 0x4f7e68 in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:819:21
    #2 0x7f019934a2e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)

previously allocated by thread T0 here:
    #0 0x4c6333 in malloc /b/swarming/w/ir/kitchen-workdir/src/third_party/llvm/compiler-rt/lib/asan/asan_malloc_linux.cc:146:3
    #1 0x51971d in safemalloc /root/putty-0.70-2019-01-17.53747ad/memory.c:23:6
    #2 0x5bf67f in strbuf_new /root/putty-0.70-2019-01-17.53747ad/utils.c:431:31
    #3 0x4f7a4e in main /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:809:28
    #4 0x7f019934a2e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)

SUMMARY: AddressSanitizer: heap-use-after-free /root/putty-0.70-2019-01-17.53747ad/cmdgen.c:979:45 in main
```

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

1) The use of previously freed memory may corrupt valid data, if the memory area in question has been allocated and used properly elsewhere.  

2) If chunk consolidation occurs after the use of previously freed data, the process may crash when invalid data is used as chunk information. 

3) If malicious data is entered before chunk consolidation can take place, it may be possible to take advantage of a write-what-where primitive to execute arbitrary code.

## Attachments
- test0025.ppk.gz
