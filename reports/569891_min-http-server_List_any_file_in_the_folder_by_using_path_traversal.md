# [min-http-server] List any file in the folder by using path traversal.

## Report Details
- **Report ID**: 569891
- **URL**: https://hackerone.com/reports/569891
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-05-07T07:51:07.269Z
- **Disclosed**: 2020-08-26T02:20:09.724Z

## Reporter
- **Username**: toannc123
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Path Traversal in min-http-server. It allows to list any file in another folder of web root.

# Module

**module name:** min-http-server
**version:** 1.0.6
**npm page:** `https://www.npmjs.com/package/min-http-server`

## Module Description

'min-http-server' is a zero-configuration, lightweight http static resource server.

# Vulnerability

## Vulnerability Description

min-http-server is simply get the path name of url and add it to the web root. it means if you input ../, it will happy add it to web root and you can list the folder you choose. But the trick is web browser or curl are also to try rebuild the url containing ../. I used the burp to make a raw url and send it to server.

## Steps To Reproduce:

install `min-http-server`
`$ npm install min-http-server -g`

start program
`$ min-http-server`

start burpsuite and enter the url contain ../. you should see the files in the folder.
{F485794}

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

This vulnerability allows malicious user to list file in the folder. This might expose vectors to attack system with Remote Code Execution, reveals files with usernames and passwords and many other possibilites.

## Attachments
- Capture.PNG
