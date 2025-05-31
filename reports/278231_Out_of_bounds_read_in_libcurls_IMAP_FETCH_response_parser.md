# Out of bounds read in libcurl's IMAP FETCH response parser

## Report Details
- **Report ID**: 278231
- **URL**: https://hackerone.com/reports/278231
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-10-17T16:41:52.850Z
- **Disclosed**: 2018-05-16T15:39:22.187Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Reported to the curl security mailing list on 6 October 2017.
Acknowledged on 6 October 2017.
Patched on 8 October 2017.
Reported to distros@openwall on 17 October 2017.
Public release on 23 October 2017.
CVE Pending.

***Vulnerability***
An IMAP FETCH response line indicates the size of the returned data, in number of bytes. When that response says the data is zero bytes, libcurl would pass on that (non-existing) data with a pointer and the size (zero) to the deliver-data function.

libcurl's deliver-data function treats zero as a magic number and invokes strlen() on the data to figure out the length. The strlen() is called on a heap based buffer that might not be zero terminated so libcurl might read beyond the end of it into whatever memory lies after in memory (or just crash) and then deliver that to the application as if it was actually downloaded.

This flaw was introduced with IMAP support in December 2009 and has been fixed in curl 7.56.1.

```
./curl_fuzzer: Running 1 inputs 1 time(s) each.
Running: ./crash-f6366f72844961fbffdda095eca33cb72d740393
=================================================================
==32295==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60c0000000b3 at pc 0x000000432e75 bp 0x7ffd8b226960 sp 0x7ffd8b226108
READ of size 108 at 0x60c0000000b3 thread T0
    #0 0x432e74 in __interceptor_strlen (/root/fuzz/curl_fuzzer+0x432e74)
    #1 0x5e1bab in Curl_client_write /root/curl/lib/sendf.c:632:11
    #2 0x6eb2a3 in imap_state_fetch_resp /root/curl/lib/imap.c:1129:16
    #3 0x6eb2a3 in imap_statemach_act /root/curl/lib/imap.c:1299
    #4 0x6e6c2d in imap_multi_statemach /root/curl/lib/imap.c:1342:12
    #5 0x6e6f06 in imap_doing /root/curl/lib/imap.c:1645:21
    #6 0x538e66 in multi_runsingle /root/curl/lib/multi.c:1755:16
    #7 0x52dbde in curl_multi_perform /root/curl/lib/multi.c:2160:14
    #8 0x4f93e2 in fuzz_handle_transfer(fuzz_data*) /root/curl-fuzzer/curl_fuzzer.cc:705:5
    #9 0x4f21e5 in LLVMFuzzerTestOneInput /root/curl-fuzzer/curl_fuzzer.cc:89:3
    #10 0x7c550d in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) /root/./Fuzzer/FuzzerLoop.cpp:495:13
    #11 0x7b9322 in fuzzer::RunOneTest(fuzzer::Fuzzer*, char const*, unsigned long) /root/./Fuzzer/FuzzerDriver.cpp:273:6
    #12 0x7bde2a in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) /root/./Fuzzer/FuzzerDriver.cpp:690:9
    #13 0x7b8ff0 in main /root/./Fuzzer/FuzzerMain.cpp:20:10
    #14 0x7f79b5e8bb44 in __libc_start_main /build/glibc-6V9RKT/glibc-2.19/csu/libc-start.c:287
    #15 0x4200eb in _start (/root/fuzz/curl_fuzzer+0x4200eb)

0x60c0000000b3 is located 0 bytes to the right of 115-byte region [0x60c000000040,0x60c0000000b3)
allocated by thread T0 here:
    #0 0x4c3153 in malloc (/root/fuzz/curl_fuzzer+0x4c3153)
    #1 0x50778e in curl_domalloc /root/curl/lib/memdebug.c:175:9
    #2 0x71a797 in Curl_pp_readresp /root/curl/lib/pingpong.c:433:21
    #3 0x6e82b7 in imap_statemach_act /root/curl/lib/imap.c:1257:14
    #4 0x6e6c2d in imap_multi_statemach /root/curl/lib/imap.c:1342:12
    #5 0x6e6f06 in imap_doing /root/curl/lib/imap.c:1645:21
    #6 0x538e66 in multi_runsingle /root/curl/lib/multi.c:1755:16
    #7 0x52dbde in curl_multi_perform /root/curl/lib/multi.c:2160:14
    #8 0x4f93e2 in fuzz_handle_transfer(fuzz_data*) /root/curl-fuzzer/curl_fuzzer.cc:705:5
    #9 0x4f21e5 in LLVMFuzzerTestOneInput /root/curl-fuzzer/curl_fuzzer.cc:89:3
    #10 0x7c550d in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) /root/./Fuzzer/FuzzerLoop.cpp:495:13
    #11 0x7b9322 in fuzzer::RunOneTest(fuzzer::Fuzzer*, char const*, unsigned long) /root/./Fuzzer/FuzzerDriver.cpp:273:6
    #12 0x7bde2a in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) /root/./Fuzzer/FuzzerDriver.cpp:690:9
    #13 0x7b8ff0 in main /root/./Fuzzer/FuzzerMain.cpp:20:10
    #14 0x7f79b5e8bb44 in __libc_start_main /build/glibc-6V9RKT/glibc-2.19/csu/libc-start.c:287

SUMMARY: AddressSanitizer: heap-buffer-overflow (/root/fuzz/curl_fuzzer+0x432e74) in __interceptor_strlen
```

Also, I'd like a determination made on my other CVE-worthy curl bugs [here](https://hackerone.com/reports/255587) and [here](https://hackerone.com/reports/212931), thank you.

## Attachments
No attachments
