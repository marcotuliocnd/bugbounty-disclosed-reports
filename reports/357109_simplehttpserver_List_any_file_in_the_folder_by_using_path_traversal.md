# [simplehttpserver] List any file in the folder by using path traversal.

## Report Details
- **Report ID**: 357109
- **URL**: https://hackerone.com/reports/357109
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-05-24T17:10:48.144Z
- **Disclosed**: 2018-08-30T04:39:27.163Z

## Reporter
- **Username**: n0n4me
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Path Traversal in simplehttpserver. It allows to list any file in another folder of web root.

# Module

**module name:** simplehttpserver
**version:** 0.1.1
**npm page:** `https://www.npmjs.com/package/simplehttpserver`

## Module Description

'simpehttpserver' is an simple imitation of python's SimpleHTTPServer and is intended for testing, development and debugging purposes

## Module Stats

[444] downloads in the last week

# Vulnerability

## Vulnerability Description

simpehttpserver is simply get the path name of url and add it to the web root. it means if you input ../, it will happy add it to web root and you can list the folder you choose. But the trick is web browser or curl are also to try rebuild the url containing ../. I used the burp to make a raw url and send it to server.

## Steps To Reproduce:

install `simplehttpserver`
`$ npm install simplehttpserver -g`

start program
`$ simplehttpserver ./`

start burpsuite and enter the url contain ../. you should see the files in the folder.
{F301226}

## Patch

filter .. in the path name.

## Supporting Material/References:

Configuration I've used to find this vulnerability:

- kali linux 4.15.0
- nodejs v8.11.2
- npm 6.1.0
- Burpsuite community

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

This vulnerability allows malicious user to list file in the folder. This might expose vectors to attack system with Remote Code Execution, reveals files with usernames and passwords and many other possibilites.

## Attachments
- 1._POC_simplehttpserver.png
