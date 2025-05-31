# List any file in the folder by using path traversal

## Report Details
- **Report ID**: 403703
- **URL**: https://hackerone.com/reports/403703
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-01T03:35:12.717Z
- **Disclosed**: 2018-11-23T08:03:07.307Z

## Reporter
- **Username**: vulzzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Path Traversal in simplehttpserver. It allows to list any file in another folder of web root.

# Module

**module name:** simplehttpserver
**version:** v0.2.1
**npm page:** `https://www.npmjs.com/package/simplehttpserver`

## Module Description

 'simpehttpserver' is an simple imitation of python's SimpleHTTPServer and is intended for testing, development and debugging purposes

## Module Stats

 [319] downloads in the last week

# Vulnerability

## Vulnerability Description

 simpehttpserver is simply get the path name of url and add it to the web root.If there is a symlink file in the directory. You can access files outside the web root directory.

## Steps To Reproduce:
 create symlink file 
$ ln -s ../../ symdir

 install simplehttpserver
$ npm install simplehttpserver -g

start program
$ simplehttpserver ./

{F340863}

## Patch

Disable symlink file access in webserver.

## Supporting Material/References:

Configuration I've used to find this vulnerability:

macos 10.13.6
nodejs v10.9.0
npm 6.4.1
chrome 68.0.3440.106

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

This vulnerability allows malicious user to list file in the folder. This might expose vectors to attack system with Remote Code Execution, reveals files with usernames and passwords and many other possibilites.

## Attachments
- Nodejs_simpleHTTPServer.png
