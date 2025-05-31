# [serve-here.js] List any file in the folder by using path traversal.

## Report Details
- **Report ID**: 569966
- **URL**: https://hackerone.com/reports/569966
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-05-07T08:29:07.633Z
- **Disclosed**: 2019-06-24T08:22:44.018Z

## Reporter
- **Username**: toannc123
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Path Traversal in **serve-here.js**. It allows to list any file in another folder of web root.

# Module

**module name:** serve-here.js
**version:** 1.1.3
**npm page:** `https://www.npmjs.com/package/serve-here.js`

## Module Description

Serve static files over HTTP

# Vulnerability

## Vulnerability Description

serve-here.js is simply get the path name of url and add it to the web root. it means if you input ../, it will happy add it to web root and you can list the folder you choose. But the trick is web browser or curl are also to try rebuild the url containing ../. I used the burp to make a raw url and send it to server.

## Steps To Reproduce:

install `serve-here.js`
`$ npm install serve-here.js -g`

start program
`$ serve-here

start burpsuite and enter the url contain ../. you should see the files in the folder.
{F485810}

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



**Note:** This is the module `serve-here.js` not the module `serve-here`

## Impact

This vulnerability allows malicious user to list file in the folder. This might expose vectors to attack system with Remote Code Execution, reveals files with usernames and passwords and many other possibilities.

## Attachments
- Capture.PNG
