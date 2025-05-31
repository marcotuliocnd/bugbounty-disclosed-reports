# Port and service scanning on localhost due to improper URL validation.

## Report Details
- **Report ID**: 773313
- **URL**: https://hackerone.com/reports/773313
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-13T09:25:45.926Z
- **Disclosed**: 2020-01-15T07:38:19.186Z

## Reporter
- **Username**: vshmuk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
Generally web masters and developers protect user-accessible CURL from requesting forbidden domains so that the attacker is not able to access internal resources. It is usually done using regular expressions.
Mostly addresses like 127.x.x.x, 192.168.x.x and "integer" notation of IP addresses (like 2130706433 = 127.0.0.1) are filtered out before executing curl using wrapper scripts.
But the ' * ' symbol is valid for CURL, allowing to request localhost's internal web resources and to scan ports. Unfortunately, since http0.9 is turned off by default now, it's harder to easily scan ports (without accessing stderr by the attacker). But if FTP protocol is not disabled, port scanning can still be achieved using time-based attack: active refusal of a closed port takes much less time than connecting by FTP to any other open port.
As far as i see, ' * ' and 'localhost' are not synonyms, and ' * ' string should be filtered out not on the webmaster's side but from inside of CURL.

## Steps To Reproduce:
```
$ ./src/curl -V
curl 7.69.0-DEV (x86_64-pc-linux-gnu) libcurl/7.69.0-DEV OpenSSL/1.1.1d

$ ./src/curl -v "*"
*   Trying ::1:80...
* TCP_NODELAY set
* connect to ::1 port 80 failed: Connection refused
*   Trying 127.0.0.1:80...
* TCP_NODELAY set
* connect to 127.0.0.1 port 80 failed: Connection refused
* Failed to connect to * port 80: Connection refused
* Closing connection 0
curl: (7) Failed to connect to * port 80: Connection refused

$ ./src/curl -v "*:8888"
*   Trying ::1:8888...
* TCP_NODELAY set
* connect to ::1 port 8888 failed: Connection refused
*   Trying 127.0.0.1:8888...
* TCP_NODELAY set
* Connected to * (127.0.0.1) port 8888 (#0)
> GET / HTTP/1.1
> Host: *:8888
> User-Agent: curl/7.69.0-DEV
> Accept: */*
> 
<skip>
Hello world!
* Closing connection 0

$ ./src/curl -v "ftp://*:8888"
*   Trying ::1:8888...
* TCP_NODELAY set
* connect to ::1 port 8888 failed: Connection refused
*   Trying 127.0.0.1:8888...
* TCP_NODELAY set
* Connected to * (127.0.0.1) port 8888 (#0)
^C

./src/curl -v "ftp://*:80"
*   Trying ::1:80...
* TCP_NODELAY set
* connect to ::1 port 80 failed: Connection refused
*   Trying 127.0.0.1:80...
* TCP_NODELAY set
* connect to 127.0.0.1 port 80 failed: Connection refused
* Failed to connect to * port 80: Connection refused
* Closing connection 0
curl: (7) Failed to connect to * port 80: Connection refused
```

## Supporting Material/References:

According to https://tools.ietf.org/html/rfc1034, wildcards are special symbols in DNS and should not be used as domain names..

## Impact

The vulnerability allows attacker to at least access internal web resources restricted to localhost, or at most to scan locally opened ports and expose services running on the machine.

## Attachments
No attachments
