# use after free in cookie.c

## Report Details
- **Report ID**: 707006
- **URL**: https://hackerone.com/reports/707006
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-10-03T09:46:43.827Z
- **Disclosed**: 2021-02-08T07:54:25.821Z

## Reporter
- **Username**: pauldreik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
I ran fuzzing with the internal fuzzer at https://github.com/pauldreik/curl-fuzzer/blob/paul/localfuzz_public0/intree_fuzzer/src/insidefuzzers/fuzz_cookies.cc

It seems like the following sequence of events trigger the use after free:

```c
        #include "cookie.h"
        #include <curl/curl.h>
        curl_global_init(CURL_GLOBAL_DEFAULT);
        CURL*  handle=curl_easy_init();
        CookieInfo* info=Curl_cookie_init(handle,NULL,NULL,false);
        curl_easy_setopt(handle, CURLOPT_COOKIEJAR, "/dev/null");
        Curl_flush_cookies(handle, true);
        Curl_cookie_cleanup(info);
        curl_easy_cleanup(handle); // <--------- this is where it happens
        curl_global_cleanup();
```
Even if the program above is a "fuzz only" type of use case, I am not sure
if a real user would be able to trigger this situation.
Anyway, the following seems to fix it:
```diff
diff --git a/lib/cookie.c b/lib/cookie.c
index f6b52df2f..c17340029 100644
--- a/lib/cookie.c
+++ b/lib/cookie.c
@@ -1646,6 +1646,7 @@ void Curl_flush_cookies(struct Curl_easy *data, int cleanup)
 
   if(cleanup && (!data->share || (data->cookies != data->share->cookies))) {
     Curl_cookie_cleanup(data->cookies);
+    data->cookies=NULL;
   }
   Curl_share_unlock(data, CURL_LOCK_DATA_COOKIE);
 }

```

Address sanitizer gets this output, without the fix (line numbers are not accurate, they refer to a temporary branch):
```
==31195==ERROR: AddressSanitizer: heap-use-after-free on address 0x61d000001e88 at pc 0x0000005d64c4 bp 0x7ffc983b1b00 sp 0x7ffc983b1af8
READ of size 8 at 0x61d000001e88 thread T0
    #0 0x5d64c3 in remove_expired /home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/../lib/cookie.c:386:10
    #1 0x5e49c5 in cookie_output /home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/../lib/cookie.c:1516:3
    #2 0x5e379a in Curl_flush_cookies /home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/../lib/cookie.c:1635:8
    #3 0x95b602 in Curl_close /home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/../lib/url.c:377:3
    #4 0x61d7ee in curl_easy_cleanup /home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/../lib/easy.c:734:3
    #5 0x5b0e12 in CurlInitializer::~CurlInitializer() /home/paul/code/delaktig/curl-fuzzer/intree_fuzzer/src/insidefuzzers/CurlInitializer.h:18:5
    #6 0x5afa57 in LLVMFuzzerTestOneInput /home/paul/code/delaktig/curl-fuzzer/intree_fuzzer/src/insidefuzzers/fuzz_cookies.cc:97:1
    #7 0x47be0d in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/tests/internalfuzzer_fuzz_cookies+0x47be0d)
    #8 0x46b87a in fuzzer::RunOneTest(fuzzer::Fuzzer*, char const*, unsigned long) (/home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/tests/internalfuzzer_fuzz_cookies+0x46b87a)
    #9 0x4767b8 in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/tests/internalfuzzer_fuzz_cookies+0x4767b8)
    #10 0x4684e2 in main (/home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/tests/internalfuzzer_fuzz_cookies+0x4684e2)
    #11 0x7f9bfc727b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310
    #12 0x468519 in _start (/home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/tests/internalfuzzer_fuzz_cookies+0x468519)

0x61d000001e88 is located 8 bytes inside of 2096-byte region [0x61d000001e80,0x61d0000026b0)
freed by thread T0 here:
    #0 0x568e48 in __interceptor_free (/home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/tests/internalfuzzer_fuzz_cookies+0x568e48)
    #1 0x63636d in curl_dbg_free /home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/../lib/memdebug.c:328:5
    #2 0x5d78e4 in Curl_cookie_cleanup /home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/../lib/cookie.c:1463:5
    #3 0x5e4907 in Curl_flush_cookies /home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/../lib/cookie.c:1650:5
    #4 0x5afa10 in LLVMFuzzerTestOneInput /home/paul/code/delaktig/curl-fuzzer/intree_fuzzer/src/insidefuzzers/fuzz_cookies.cc:92:5
    #5 0x47be0d in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/tests/internalfuzzer_fuzz_cookies+0x47be0d)
    #6 0x46b87a in fuzzer::RunOneTest(fuzzer::Fuzzer*, char const*, unsigned long) (/home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/tests/internalfuzzer_fuzz_cookies+0x46b87a)
    #7 0x4767b8 in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/tests/internalfuzzer_fuzz_cookies+0x4767b8)
    #8 0x4684e2 in main (/home/paul/code/delaktig/curl/build-fuzz-clang7-asan-ubsan/tests/internalfuzzer_fuzz_cookies+0x4684e2)
    #9 0x7f9bfc727b96 in __libc_start_main /build/glibc-OTsEL5/glibc-2.27/csu/../csu/libc-start.c:310


```

## Impact

No idea.

## Attachments
No attachments
