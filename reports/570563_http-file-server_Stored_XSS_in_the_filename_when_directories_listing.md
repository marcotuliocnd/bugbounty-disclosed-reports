# [http-file-server] Stored XSS in the filename when directories listing

## Report Details
- **Report ID**: 570563
- **URL**: https://hackerone.com/reports/570563
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-07T19:53:36.580Z
- **Disclosed**: 2019-07-24T05:50:58.218Z

## Reporter
- **Username**: lightangel1412
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Stored XSS in module "http-file-server".
It allows to inject malicious scripts in the file name, store them on the server, then execute these scripts in the browser via the XSS vulnerability.

# Module

**module name:** http-file-server
**version:** 0.2.6
**npm page:** `https://www.npmjs.com/package/http-file-server

## Module Description

Simple HTTP file server (Node.JS)

## Module Stats

[0] downloads in the last day
[1] downloads in the last week
[47] downloads in week 02-08 Apr 2019
[40] downloads in week 09-15 Apr 2019
[120+] downloads in the last month

# Vulnerability

## Vulnerability Description

This XSS vulnerability occurs due to the module represents filename(s) in HTML without any sanitization in listing directory page. In a result, any malicious scripts which are injected and stored on the server, would be executed in the client's browser.

## Steps To Reproduce:

- Install the module
```
npm install -g http-file-server
```

- In the directory which will be served via http-file-server, create file with following names in directories ~/Desktop/:
```
" onmouseover=alert(1) "
```
{F486137}

- Run 'http-file-server in "~/Desktop" directory :
```
http-file-server
```
or 
```
nodejs /usr/lib/node_modules/http-file-server/http-file-server.js
```

- Open http://localhost:8080/
{F486135}

- When mouseover event is trigger, a message will be popup via XSS vulnerability.
{F486136}

## Patch

User input should be properly sanitized and filtered both at the client and server side. Dangerous characters such as < > ' " % ; ) ( & + should either be disallowed or HTML encoded before displaying them on screen. 

## Supporting Material/References:

- Linux kali 4.15.0-kali2-amd64
- node 10.15.3
- npm 6.9
- Firefox ESR 52.7.3 (64-bit)

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows to inject malicious scripts in the file name, store them on the server, then execute these scripts in the browser via the XSS vulnerability.

## Attachments
- http-file-server_-_XSS0.PNG
- http-file-server_-_XSS.PNG
- http-file-server_-_XSS2.PNG
