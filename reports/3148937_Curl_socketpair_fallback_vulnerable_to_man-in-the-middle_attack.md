# `Curl_socketpair()` fallback vulnerable to man-in-the-middle attack

## Report Details
- **Report ID**: 3148937
- **URL**: https://hackerone.com/reports/3148937
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2025-05-15T16:59:22.955Z
- **Disclosed**: 2025-05-20T06:51:27.112Z

## Reporter
- **Username**: jmanojlovich
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
In `Curl_socketpair()` in `curl/lib/socketpair.c` if the operating system lacks a native `socketpair()` function, libcurl will create its own pair of sockets. To do this, libcurl first creates a listening socket, then it creates a client socket, which it then connects to the listening socket. During the time between when the listening socket is bound and set to listen, and when the client socket tries to connect, there is a gap where any process could connect to the listening socket first. As this is an obvious invitation to a man-in-the-middle attack, libcurl generates a 9 byte secret which it writes out of the listening socket, and then subsequently reads the secret back from the client socket for verification. 

```
  listener = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
  if(listener == CURL_SOCKET_BAD)
    return -1;

  memset(&a, 0, sizeof(a));
  a.inaddr.sin_family = AF_INET;
  a.inaddr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
  a.inaddr.sin_port = 0;

  socks[0] = socks[1] = CURL_SOCKET_BAD;

#if defined(_WIN32) || defined(__CYGWIN__)
  /* do not set SO_REUSEADDR on Windows */
  (void)reuse;
#ifdef SO_EXCLUSIVEADDRUSE
  {
    int exclusive = 1;
    if(setsockopt(listener, SOL_SOCKET, SO_EXCLUSIVEADDRUSE,
                  (char *)&exclusive, (curl_socklen_t)sizeof(exclusive)) == -1)
      goto error;
  }
#endif
#else
  if(setsockopt(listener, SOL_SOCKET, SO_REUSEADDR,
                (char *)&reuse, (curl_socklen_t)sizeof(reuse)) == -1)
    goto error;
#endif
  if(bind(listener, &a.addr, sizeof(a.inaddr)) == -1)
    goto error;
  if(getsockname(listener, &a.addr, &addrlen) == -1 ||
     addrlen < (int)sizeof(a.inaddr))
    goto error;
  if(listen(listener, 1) == -1)
    goto error;
  socks[0] = socket(AF_INET, SOCK_STREAM, 0);
  if(socks[0] == CURL_SOCKET_BAD)
    goto error;
  if(connect(socks[0], &a.addr, sizeof(a.inaddr)) == -1)
    goto error;

  /* use non-blocking accept to make sure we do not block forever */
  if(curlx_nonblock(listener, TRUE) < 0)
    goto error;
  pfd[0].fd = listener;
  pfd[0].events = POLLIN;
  pfd[0].revents = 0;
  (void)Curl_poll(pfd, 1, 1000); /* one second */
  socks[1] = accept(listener, NULL, NULL);
  if(socks[1] == CURL_SOCKET_BAD)
    goto error;
  else {
    struct curltime start = curlx_now();
    char rnd[9];
    char check[sizeof(rnd)];
    char *p = &check[0];
    size_t s = sizeof(check);

    if(Curl_rand(NULL, (unsigned char *)rnd, sizeof(rnd)))
      goto error;

    /* write data to the socket */
    swrite(socks[0], rnd, sizeof(rnd));
    /* verify that we read the correct data */
    do {
      ssize_t nread;

      pfd[0].fd = socks[1];
      pfd[0].events = POLLIN;
      pfd[0].revents = 0;
      (void)Curl_poll(pfd, 1, 1000); /* one second */

      nread = sread(socks[1], p, s);
      if(nread == -1) {
        int sockerr = SOCKERRNO;
        /* Do not block forever */
        if(curlx_timediff(curlx_now(), start) > (60 * 1000))
          goto error;
        if(
#ifdef USE_WINSOCK
          /* This is how Windows does it */
          (SOCKEWOULDBLOCK == sockerr)
#else
          /* errno may be EWOULDBLOCK or on some systems EAGAIN when it
             returned due to its inability to send off data without
             blocking. We therefore treat both error codes the same here */
          (SOCKEWOULDBLOCK == sockerr) || (EAGAIN == sockerr) ||
          (SOCKEINTR == sockerr) || (SOCKEINPROGRESS == sockerr)
#endif
          ) {
          continue;
        }
        goto error;
      }
      s -= nread;
      if(s) {
        p += nread;
        continue;
      }
      if(memcmp(rnd, check, sizeof(check)))
        goto error;
      break;
    } while(1);
  }
```

This approach is still vulnerable to both a man-in-the-middle attack. It is easy for a user to monitor for new TCP listening sockets on the localhost interface, and it is possible for another user to connect first to the listening socket. Once connected, the attacker could simply send 9 random bytes. While the probability of successfully guessing the generated secret is low, it is not zero. Furthermore, if curl is compiled without SSL, the curl random number generator will fall back to a low entropy mode based on the system clock, and secrets generated while in this mode would be much easier to guess. In `curl/lib/rand.c`

```
  infof(data, "WARNING: using weak random seed");
  {
    static unsigned int randseed;
    static bool seeded = FALSE;
    unsigned int rnd;
    if(!seeded) {
      struct curltime now = curlx_now();
      randseed += (unsigned int)now.tv_usec + (unsigned int)now.tv_sec;
      randseed = randseed * 1103515245 + 12345;
      randseed = randseed * 1103515245 + 12345;
      randseed = randseed * 1103515245 + 12345;
      seeded = TRUE;
    }

    /* Return an unsigned 32-bit pseudo-random number. */
    r = randseed = randseed * 1103515245 + 12345;
    rnd = (r << 16) | ((r >> 16) & 0xFFFF);
    memcpy(entropy, &rnd, length);
  }
```

Also, any user on a system with the capability to capture network traffic on the localhost interface can read the generated 9 byte secret, and then inject the secret into their own connection to the server socket. While non-privileged users do not always have capture permissions, it is not unheard of, particularly in shared computer environments. Yes, this would imply that the attacker would have access to all data sent over the socket pair anyway, but that data could be encrypted at a higher level, whereas the 9 byte secret is essentially sent as plaintext. Here is a screenshot of an interception, with the 9 byte secret highlighted. 

{F4351504}

## Similar Issue

CVE-2024-3219
https://nvd.nist.gov/vuln/detail/CVE-2024-3219
https://github.com/python/cpython/issues/122133

## Suggested fix

Instead of generating, sending, and receiving a sequence of random bytes, I recommend following the example of Python by comparing the TCP ports of both sockets. As the sockets are both on the same localhost interface, matching the TCP ports will guarantee the socket equivalence. This also obviates any concern about the random number generator. In the code below, the port numbers are in network-byte order, but for the purposes of comparison that is irrelevant. 

```
struct sockaddr_in addr;
socklen_t len;
in_port_t ports[4];
len = sizeof(struct sockaddr_in);
memset(&addr, 0, sizeof(struct sockaddr_in));
if(getsockname(socks[0], (struct sockaddr*)&addr, &len))
  goto error;
ports[0] = addr.sin_port;
memset(&addr, 0, sizeof(struct sockaddr_in));
if(getpeername(socks[0], (struct sockaddr*)&addr, &len))
  goto error;
ports[1] = addr.sin_port;
memset(&addr, 0, sizeof(struct sockaddr_in));
if(getsockname(socks[1], (struct sockaddr*)&addr, &len))
  goto error;
ports[2] = addr.sin_port;
memset(&addr, 0, sizeof(struct sockaddr_in));
if(getpeername(socks[1], (struct sockaddr*)&addr, &len))
  goto error;
ports[3] = addr.sin_port;
if(ports[0] != ports[3] || ports[1] != ports[2])
  goto error;
```

## Impact

Any user on a system using a version of libcurl built without native `socketpair()` support can attempt to impersonate libcurl by hijacking the socket pair creation.

## Attachments
- image.png
