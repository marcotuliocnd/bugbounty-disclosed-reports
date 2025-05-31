# Memory leak in CURLOPT_XOAUTH2_BEARER

## Report Details
- **Report ID**: 1567257
- **URL**: https://hackerone.com/reports/1567257
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-05-12T14:53:29.389Z
- **Disclosed**: 2022-05-13T07:51:23.154Z

## Reporter
- **Username**: pappacoda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
Once a bearer token is set with `CURLOPT_XOAUTH2_BEARER`, each HTTP request done with the same handler leaks the token itself.

## Steps To Reproduce:

Given the following code:

```c
#include <curl/curl.h>

int main(void) {
  curl_global_init(CURL_GLOBAL_ALL);

  CURL* curl = curl_easy_init();

  curl_easy_setopt(curl, CURLOPT_HTTPAUTH, CURLAUTH_BEARER);
  curl_easy_setopt(curl, CURLOPT_XOAUTH2_BEARER, "c4e448d652a961fda0ab64f882c8c161d5985f805d45d80c9ddca108f8e2fde3");
  curl_easy_setopt(curl, CURLOPT_HTTPGET, 1L);
  curl_easy_setopt(curl, CURLOPT_URL, "https://andrea.pappacoda.it");

  for (int i = 0; i < 5; i++) {
    curl_easy_perform(curl);
  }

  curl_easy_cleanup(curl);

  curl_global_cleanup();
}
```

AddressSanitizer reports a memory leak:

```text
$ cc -g -fsanitize=address main.c $(pkg-config --cflags --libs libcurl) -o asan && ./asan
=================================================================
==41730==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 260 byte(s) in 4 object(s) allocated from:
    #0 0x7f52f54d97a7 in __interceptor_strdup ../../../../src/libsanitizer/asan/asan_interceptors.cpp:454
    #1 0x7f52f54423cd  (/lib/x86_64-linux-gnu/libcurl.so.4+0x673cd)

SUMMARY: AddressSanitizer: 260 byte(s) leaked in 4 allocation(s).
```

and valgrind does too:

```text
$ cc -g main.c $(pkg-config --cflags --libs libcurl) -o valgrind && valgrind --leak-check=full ./valgrind
==41878== 
==41878== HEAP SUMMARY:
==41878==     in use at exit: 3,710 bytes in 12 blocks
==41878==   total heap usage: 32,937 allocs, 32,925 frees, 3,397,085 bytes allocated
==41878== 
==41878== 260 bytes in 4 blocks are definitely lost in loss record 5 of 8
==41878==    at 0x483F7B5: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==41878==    by 0x499331A: strdup (strdup.c:42)
==41878==    by 0x48CB3CD: ??? (in /usr/lib/x86_64-linux-gnu/libcurl.so.4.8.0)
==41878==    by 0x48AB9B7: ??? (in /usr/lib/x86_64-linux-gnu/libcurl.so.4.8.0)
==41878==    by 0x48AC81D: curl_multi_perform (in /usr/lib/x86_64-linux-gnu/libcurl.so.4.8.0)
==41878==    by 0x4884AE2: curl_easy_perform (in /usr/lib/x86_64-linux-gnu/libcurl.so.4.8.0)
==41878==    by 0x1092FB: main (main.c:15)
==41878== 
==41878== LEAK SUMMARY:
==41878==    definitely lost: 260 bytes in 4 blocks
==41878==    indirectly lost: 0 bytes in 0 blocks
==41878==      possibly lost: 0 bytes in 0 blocks
==41878==    still reachable: 3,450 bytes in 8 blocks
==41878==         suppressed: 0 bytes in 0 blocks
==41878== Reachable blocks (those to which a pointer was found) are not shown.
==41878== To see them, rerun with: --leak-check=full --show-leak-kinds=all
==41878== 
==41878== For lists of detected and suppressed errors, rerun with: -s
==41878== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```


## Supporting Material/References:

As mentioned in curl's SECURITY-PROCESS.md, "small memory leaks" do not account for vulnerabilities, but as I describe below this leak can be triggered multiple times very easily. I thus preferred reporting this in private form to be on the safe side.

Some more info about my environment:

```text
$ curl -V
curl 7.83.0 (x86_64-pc-linux-gnu) libcurl/7.83.0 OpenSSL/1.1.1o zlib/1.2.11 brotli/1.0.9 zstd/1.5.2 libidn2/2.3.2 libpsl/0.21.0 (+libidn2/2.3.0) libssh2/1.10.0 nghttp2/1.43.0 librtmp/2.3 OpenLDAP/2.5.11
Release-Date: 2022-04-27
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp 
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM NTLM_WB PSL SPNEGO SSL TLS-SRP UnixSockets zstd

$ uname -a
Linux debian 5.17.0-1-amd64 #1 SMP PREEMPT Debian 5.17.3-1 (2022-04-18) x86_64 GNU/Linux
```

I can also confirm that the issue is still present in the latest master (commit 1ddc8aefb2e45def02dfe02973a3afd2fbdf09c3) - and this time as curl has been built from source AddressSanitizer is able to provide a more helpful error message:

```text
==18021==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 260 byte(s) in 4 object(s) allocated from:
    #0 0x7f535c4317a7 in __interceptor_strdup ../../../../src/libsanitizer/asan/asan_interceptors.cpp:454
    #1 0x557a76fce6c7 in create_conn ../subprojects/curl-master/lib/url.c:3655
    #2 0x557a76fd11df in Curl_connect ../subprojects/curl-master/lib/url.c:4152
    #3 0x557a76f7fe55 in multi_runsingle ../subprojects/curl-master/lib/multi.c:1858
    #4 0x557a76f83d54 in curl_multi_perform ../subprojects/curl-master/lib/multi.c:2636
    #5 0x557a76f60c0c in easy_transfer ../subprojects/curl-master/lib/easy.c:599
    #6 0x557a76f61169 in easy_perform ../subprojects/curl-master/lib/easy.c:689
    #7 0x557a76f61239 in curl_easy_perform ../subprojects/curl-master/lib/easy.c:708
    #8 0x557a76f5ff8d in main ../exe/main.cpp:76
    #9 0x7f535bc0c7fc in __libc_start_main ../csu/libc-start.c:332

SUMMARY: AddressSanitizer: 260 byte(s) leaked in 4 allocation(s).
```

## Impact

As bearer tokens don't have a standardized length, applications usually don't impose limits on it. If a user is able to set a big bearer token and perform an arbitrary number of meaningless requests it could slowly eat up all system's memory.

In particular, substituting the bearer string literal with a user-supplied input (let's say `argv[1]`) an attacker could pass in a token as large as roughly 45 kilobytes, which would result in 45 kilobytes of leaked memory on each request that could sum up to hundreds or thousands of megabytes on long-running services. This could eventually lead to the service being killed by the OOM killer, as well as slow downs of overall system performance, especially in constrained environments.

The example reported above, if substituting `argv[1]` to the literal and simulating a high number of requests with a for loop, leads to the following memory usage:

```text
$ cc -g -fsanitize=address main_args.c $(pkg-config --cflags --libs libcurl) -o asan_args && time ./asan_args $(openssl rand -hex 23000)
=================================================================
==9608==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 45954999 byte(s) in 999 object(s) allocated from:
    #0 0x7f55142917a7 in __interceptor_strdup ../../../../src/libsanitizer/asan/asan_interceptors.cpp:454
    #1 0x7f55141fa3cd  (/lib/x86_64-linux-gnu/libcurl.so.4+0x673cd)

SUMMARY: AddressSanitizer: 45954999 byte(s) leaked in 999 allocation(s).
./asan_args $(openssl rand -hex 23000)  7,62s user 0,74s system 8% cpu 1:36,56 total
```

This example is taken to the extreme, but 40 MiB in one minute and a half is a big amount of leaked memory nonetheless.

It is also worth noting that the leaked data is fairly sensitive, as bearer tokens are widely used for authentication in a variety of places (e.g. REST APIs).

## Attachments
No attachments
