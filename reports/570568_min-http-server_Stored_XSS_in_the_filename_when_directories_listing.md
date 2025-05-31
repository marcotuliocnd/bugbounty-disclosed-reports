# [min-http-server] Stored XSS in the filename when directories listing

## Report Details
- **Report ID**: 570568
- **URL**: https://hackerone.com/reports/570568
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-07T20:16:36.004Z
- **Disclosed**: 2019-07-24T05:49:38.304Z

## Reporter
- **Username**: lightangel1412
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Stored XSS in module "min-http-server".
It allows to inject malicious scripts in the file name, store them on the server, then execute these scripts in the browser via the XSS vulnerability.

# Module

**module name:** min-http-server
**version:** 1.0.6
**npm page:** `https://www.npmjs.com/package/min-http-server`

## Module Description
一个零配置、轻量级的 http 静态资源服务器 means 
A zero-configuration, lightweight http static resource server

## Module Stats

[0] downloads in the last day
[4] downloads in the last week
[35] downloads in the last month

# Vulnerability

## Vulnerability Description

This XSS vulnerability occurs due to the module represents filename(s) in HTML without any sanitization in listing directory page. In a result, any malicious scripts which are injected and stored on the server, would be executed in the client's browser.

## Steps To Reproduce:

- Install the module
```
npm install -g min-http-server
```
- In the directory which will be served via min-http-server, create file with following names in directories ~/Desktop/:
```
" onmouseover=alert(1) "
```
{F486143}

- Run 'min-http-server in "~/Desktop" directory :
```
min-http-server

    [tiny-http-server] static-server is starting at port 1138
    [tiny-http-server] please enter localhost:1138 in the browser
```

- Open http://localhost:1138/
{F486143}

- When mouseover event is trigger, a message will be popup via XSS vulnerability.
{F486145}

## Patch

User input should be properly sanitized and filtered both at the client and server side. Dangerous characters such as < > ' " % ; ) ( & + should either be disallowed or HTML encoded before displaying them on screen.

## Supporting Material/References:

- Linux kali 4.15.0-kali2-amd64
- node 10.15.3
- npm 6.9
- Firefox ESR 60.5.1esr (64-bit)

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows to inject malicious scripts in the file name, store them on the server, then execute these scripts in the browser via the XSS vulnerability.

## Attachments
- min-http-server_-_XSS1.PNG
- min-file-server_-_XSS0_.PNG
- min-http-server_-_XSS2.PNG
