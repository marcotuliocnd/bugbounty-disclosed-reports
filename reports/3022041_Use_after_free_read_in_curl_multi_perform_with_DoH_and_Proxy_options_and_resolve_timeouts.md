# Use after free (read) in curl_multi_perform with DoH and Proxy options, and resolve timeouts

## Report Details
- **Report ID**: 3022041
- **URL**: https://hackerone.com/reports/3022041
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2025-03-04T06:24:58.089Z
- **Disclosed**: 2025-03-06T09:58:10.619Z

## Reporter
- **Username**: catenacyber
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
[summary of the vulnerability]

There is a use after free in `curl_multi_perform` when DoH resolver timeouts and `CURLOPT_PROXY` is used (see reproducer and stack trace)

I found it via fuzzing with https://github.com/catenacyber/curl-fuzzer/tree/proxy (after fixing a small memory leak in curl)
Another reproducer was found with curl_fuzzer_mqtt
(I have other fuzzers reports)

## Affected version
[Which curl/libcurl version are you using to reproduce? On which platform? `curl -V` typically generates good output to include]

Master at commit 7b0240c07799c28dc84272f9e38e1092ce4cc498
```
curl 8.13.0-DEV (x86_64-apple-darwin23.6.0) libcurl/8.13.0-DEV OpenSSL/1.0.2n zlib/1.2.11 libidn2/2.0.4 libpsl/0.19.1 nghttp2/1.55.1 librtmp/2.3
Release-Date: [unreleased]
Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt pop3 pop3s rtmp rtsp smb smbs smtp smtps telnet tftp ws wss
Features: alt-svc AsynchDNS HSTS HTTP2 HTTPS-proxy IDN IPv6 Largefile libz NTLM PSL SSL threadsafe TLS-SRP UnixSockets
```

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Run the following example

```c
#include <stdio.h>
#include <curl/curl.h>

int main(void)
{
  CURL *curl;
  int still_running;

  curl = curl_easy_init();
  if(curl) {
    CURLM *multi_handle = curl_multi_init();
    curl_multi_add_handle(multi_handle, curl);
    curl_easy_setopt(curl, CURLOPT_DOH_URL, "doh");
    curl_easy_setopt(curl, CURLOPT_PROXY, "proxy");
    curl_easy_setopt(curl, CURLOPT_URL, "tftp://curl.se/");
    curl_easy_setopt(curl, CURLOPT_TIMEOUT_MS, 50L);
    curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);
    curl_easy_setopt(curl, CURLOPT_SERVER_RESPONSE_TIMEOUT, 1L);
    curl_easy_setopt(curl, CURLOPT_PROTOCOLS_STR, "tftp");

    curl_multi_perform(multi_handle, &still_running);
      while (still_running > 0) {
          printf("still_running %d\n", still_running);
          struct timespec remaining, request = { 0, 60000000 };
          // We should do a select, but let's just wait for timeout for reproducibility
          nanosleep(&request, &remaining);
          curl_multi_perform(multi_handle, &still_running);
    }
    curl_multi_remove_handle(multi_handle, curl);
    curl_multi_cleanup(multi_handle);
    curl_easy_cleanup(curl);
  }
  return 0;
}

```

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

Output when curl is compiled with `--enable-debug` and stack trace from ASAN is 

```
* Added connection 0. The cache now contains 1 members
* Resolving timed out after 61 milliseconds
* Curl_disconnect(conn #0, aborted=1)
* closing connection #0
=================================================================
==47284==ERROR: AddressSanitizer: heap-use-after-free on address 0x622000003148 at pc 0x00010e3a3397 bp 0x7ff7b25cf1c0 sp 0x7ff7b25cf1b8
READ of size 4 at 0x622000003148 thread T0
    #0 0x10e3a3396 in Curl_node_elem llist.c:248
    #1 0x10e3c5cba in curl_multi_perform multi.c:2604
    #2 0x10d931c46 in main pocuaf.c:29
    #3 0x7ff8011a4344 in start+0x774 (dyld:x86_64+0xfffffffffff5c344)

0x622000003148 is located 72 bytes inside of 5760-byte region [0x622000003100,0x622000004780)
freed by thread T0 here:
    #0 0x10ecacdb6 in free+0xa6 (libclang_rt.asan_osx_dynamic.dylib:x86_64h+0xe0db6)
    #1 0x10e3a47fd in curl_dbg_free memdebug.c:297
    #2 0x10e436f30 in Curl_close url.c:337
    #3 0x10e31d12a in Curl_doh_close doh.c:1305
    #4 0x10e3e5ea4 in Curl_req_done request.c:110
    #5 0x10e3c2308 in multi_done multi.c:597
    #6 0x10e3ce6ff in multi_handle_timeout multi.c:1583
    #7 0x10e3c72d3 in multi_runsingle multi.c:2242
    #8 0x10e3c5c8e in curl_multi_perform multi.c:2620
    #9 0x10d931c46 in main pocuaf.c:29
    #10 0x7ff8011a4344 in start+0x774 (dyld:x86_64+0xfffffffffff5c344)

previously allocated by thread T0 here:
    #0 0x10ecad042 in calloc+0xa2 (libclang_rt.asan_osx_dynamic.dylib:x86_64h+0xe1042)
    #1 0x10e3a424d in curl_dbg_calloc memdebug.c:175
    #2 0x10e4380fb in Curl_open url.c:499
    #3 0x10e319c09 in doh_run_probe doh.c:272
    #4 0x10e319445 in Curl_doh doh.c:436
    #5 0x10e357a63 in Curl_resolv hostip.c:813
    #6 0x10e44445c in resolve_server url.c:3250
    #7 0x10e43e70c in Curl_connect url.c:3803
    #8 0x10e3c76e2 in multi_runsingle multi.c:2275
    #9 0x10e3c5c8e in curl_multi_perform multi.c:2620
    #10 0x10d931bb9 in main pocuaf.c:22
    #11 0x7ff8011a4344 in start+0x774 (dyld:x86_64+0xfffffffffff5c344)
```

## Impact

## Summary:

I am not sure if this UAF can be used to gain RCE, or as it is a UAF read to bypass ASLR

## Attachments
No attachments
