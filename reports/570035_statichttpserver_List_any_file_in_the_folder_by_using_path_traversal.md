# [statichttpserver] List any file in the folder by using path traversal.

## Report Details
- **Report ID**: 570035
- **URL**: https://hackerone.com/reports/570035
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-05-07T08:52:48.264Z
- **Disclosed**: 2019-08-25T10:58:00.858Z

## Reporter
- **Username**: toannc123
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Path Traversal in statichttpserver. It allows to list any file in another folder of web root.

# Module

**module name:** statichttpserver
**version:** 0.9.7
**npm page:** https://www.npmjs.com/package/statichttpserver

## Module Description

'statichttpserver' is inspired by SimpleHTTPServer.py and is intended to be a fast and easy to use static file server.

# Vulnerability

## Vulnerability Description

statichttpserver is simply get the path name of url and add it to the web root. it means if you input ../, it will happy add it to web root and you can list the folder you choose. But the trick is web browser or curl are also to try rebuild the url containing ../. I used the burp to make a raw url and send it to server.

## Steps To Reproduce:

install `statichttpserver`
`$ npm install -g statichttpserver`

start program
`$ StaticHTTPServer --ip 192.168.220.132`

start burpsuite and enter the url contain ../. you should see the files in the folder.
{F485830}

## Patch

filter .. in the path name.

## Supporting Material/References:

Configuration I've used to find this vulnerability:

- kali linux 4.15.0
- nodejs v8.9.3
- npm 6.4.1
- Burpsuite

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

This vulnerability allows malicious user to list file in the folder. This might expose vectors to attack system with Remote Code Execution, reveals files with usernames and passwords and many other possibilities.

## Attachments
- Capture.PNG
