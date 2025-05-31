# Read beyond bounds via ap_rwrite() [zhbug_httpd_47.2]

## Report Details
- **Report ID**: 1595299
- **URL**: https://hackerone.com/reports/1595299
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-08T23:34:50.838Z
- **Disclosed**: 2022-07-09T13:54:56.102Z

## Reporter
- **Username**: tdp3kel9g
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Greetings. I have found that ap_rwrite() (/server/protocol.c) can cause a read beyond bounds with the extra data sent to an attacker.

The bug is that ap_rwrite() passes its |int nbyte| argument to buffer_output(), where buffer_output()'s corresponding |len| argument isa |apr_size_t|. Thus, a negative |nbyte| value gets sign-extended into a gigantic |len|, causing the creation of a gigantic bucket (`0xffffffffnnnnnnnn bytes`) pointing to a buffer whose actual length is `0xnnnnnnnn`, causing a large read beyond bounds and thus a leak of heap information to an attacker.

The bug is still present in trunk.

Attached is a POC that demonstrates the vulnerability. Use it thusly:

   1. Copy bug47.2.lua into /bug47.2/bug47.2.lua .
   2. Enable LUA.

   3. Copy httpd_lines.txt from this report into httpd.conf (this adds a DATA filter to the output filter chain so that httpd sends data in small chunks).

   4. Run httpd and attach a debugger to it.
   5. Set a BP on ap_rwrite().
   6. Go on to step 7.
   7. Create a file `0x80000000` bytes long filled with 'a' characters, named /<somepath>/bug47.2.bin .
   8. Run the command

      `curl -v -i -o <somepath>/response.txt -X POST -k -T /<somepath>/bug47.2.bin http://127.0.0.1/bug47.2/bug47.2.lua`

   which POSTs the file to httpd.

    9. When the ap_rwrite() BP fires, notice that |int nbyte| == `0x80000000`. Also note the address of the end of the buffer |buf + 0x80000000|.

    10. Trace into buffer_output(). Notice how |len| == `0xffffffff80000000`. Trace into ap_fwrite() and notice how it creates a transient bucket with this length.

    11. Set a BP on data_out_filter() (modules/filters/mod_data.c) on the loop that repeatedly reads <= `6000` bytes of data to be turned into data: URLs.

    12. Proceed. When the BP fires, examine data_out_filter()'s normal behavior.

    13. Disable the BP and proceed. Wait until the debugger pops up an read-beyond-bounds exception, most likely in apr_base64_encode_binary() (apr-util/encoding/apr_base64.c). Examine |string| (the beginning of the buffer that apr_base64_encode_binary() is reading from), and notice that it's already beyond the end of the buffer that you calculated in step 9, showing that some previous iteration of data_out_filter()'s loop sent beyond-bounds data to the attacking host.

    14. If curl hasn't exited by itself, hit ctrl/c.

    15. Examine the beginning of <somepath>/response.txt and notice how its response payload section contains the repeating pattern ("YWFh"), which is the base64 encoding of 'aaa' (which is what you filled bug47.2.bin with).

    16. Examine the end of <somepath>/response.txt and notice how it containsa block of something other than "YWFh", indicating that httpd sent back something other than the base64-encoded value of repeating 'a's. What gets sent back depends on the arrangement of the heap, which depends upon your httpd build (mine is debug), platform, timing, and server loading.
```
-------- bug47.2.lua ----------------------------------------------------
function handle(r)
    local s = r:requestbody()
    r:puts(s)
end
-------- bug47.2.lua ----------------------------------------------------
```
```
-------- httpd_lines.txt ----------------------------------------------------
<Location /bug47.2>
   SetOutputFilter DATA
</Location>
-------- httpd_lines.txt ----------------------------------------------------
```

## Impact

The attacker could exfiltrate data from the victim site's heap. In mitigation, the victim site must run a suitable LUA program (the POC just reads data from the attacker and echoes it back to her, but a more-realistic program would transform the data in some way).

Use of this attack is likely to cause an access violation and consequent crash, which is useful for a DoS attack.

## Attachments
No attachments
