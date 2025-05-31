# HTTP/2 PUSH_PROMISE DoS

## Report Details
- **Report ID**: 2402853
- **URL**: https://hackerone.com/reports/2402853
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-03-05T17:05:32.731Z
- **Disclosed**: 2024-03-27T10:53:44.183Z

## Reporter
- **Username**: w0x42
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
In `discard_newhandle` the condition in the `if` statement is always `false` for http transfer due to a negation.
As a result `http2_data_done` will never be called.
```
static void discard_newhandle(struct Curl_cfilter *cf,
                              struct Curl_easy *newhandle)
{
  if(!newhandle->req.p.http) {
    http2_data_done(cf, newhandle, TRUE);
    newhandle->req.p.http = NULL;
  }
  (void)Curl_close(&newhandle);
}
```

`discard_newhandle` is supposed to close stream and free resources allocated in `http2_data_setup` 
as well as close `Curl_easy` handle when some error occurs in `push_promise`.
For example if `PUSH_PROMISE` frame has invailid `:scheme` pseudo header `set_transfer_url` in `push_promise` will return an error.
```
    rv = set_transfer_url(newhandle, &heads);
    if(rv) {
      discard_newhandle(cf, newhandle);
      rv = CURL_PUSH_DENY;
      goto fail;
    }
```
An attacker could send specially crafted `PUSH_PROMISE` frames to trigger the error.
This would result in a memory leak for every malformed frame received, consequently using all available memory. 



## Steps To Reproduce:

  1. compile `nghttp2` with {F3099706} applied
  1. compile {F3099707}
  1. run `nghttpd -p/=/foo.bar --no-tls 8181`
  1. run `valgrind --leak-check=full ./http2_push_headers`

for each `-p` option `nghttpd` will send 200 `PUSH_PROMISE` frames with invalid `:scheme` header

## Supporting Material/References:

`valgrind --leak-check=full ./http2_push_headers` output:
```
==5247== 
==5247== HEAP SUMMARY:
==5247==     in use at exit: 162,946 bytes in 873 blocks
==5247==   total heap usage: 7,170 allocs, 6,297 frees, 1,696,049 bytes allocated
==5247== 
==5247== 70,400 bytes in 200 blocks are definitely lost in loss record 6 of 7
==5247==    at 0x48485EF: calloc (vg_replace_malloc.c:1340)
==5247==    by 0x48ADC29: http2_data_setup (http2.c:249)
==5247==    by 0x48AF154: h2_duphandle (http2.c:789)
==5247==    by 0x48AF420: push_promise (http2.c:877)
==5247==    by 0x48AFCF6: on_stream_frame (http2.c:1065)
==5247==    by 0x48B08C7: on_frame_recv (http2.c:1265)
==5247==    by 0x4C36AE3: nghttp2_session_mem_recv (in /usr/lib64/libnghttp2.so.14.26.0)
==5247==    by 0x48AE851: h2_process_pending_input (http2.c:551)
==5247==    by 0x48B294F: h2_progress_ingress (http2.c:1930)
==5247==    by 0x48B2B54: cf_h2_recv (http2.c:1969)
==5247==    by 0x4877F03: Curl_conn_recv (cfilters.c:183)
==5247==    by 0x48DB1B3: Curl_read (sendf.c:813)
==5247== 
==5247== LEAK SUMMARY:
==5247==    definitely lost: 70,400 bytes in 200 blocks
==5247==    indirectly lost: 0 bytes in 0 blocks
==5247==      possibly lost: 0 bytes in 0 blocks
==5247==    still reachable: 92,546 bytes in 673 blocks
==5247==         suppressed: 0 bytes in 0 blocks
==5247== Reachable blocks (those to which a pointer was found) are not shown.
==5247== To see them, rerun with: --leak-check=full --show-leak-kinds=all
==5247== 
==5247== For lists of detected and suppressed errors, rerun with: -s
==5247== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```

## Impact

denial of service

## Attachments
- nghttp_v1.59.patch
- http2_push_promise.c
