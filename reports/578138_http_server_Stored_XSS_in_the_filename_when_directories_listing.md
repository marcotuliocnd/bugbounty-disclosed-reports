# [http_server] Stored XSS in the filename when directories listing

## Report Details
- **Report ID**: 578138
- **URL**: https://hackerone.com/reports/578138
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-05-12T20:10:40.121Z
- **Disclosed**: 2019-09-13T10:49:27.689Z

## Reporter
- **Username**: lightangel1412
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Stored XSS in module "http_server".
It allows to inject malicious scripts in the file name, store them on the server, then execute these scripts in the browser via the XSS vulnerability.

# Module
- module name: http_server
- version: 1.0.12
- npm page: https://www.npmjs.com/package/http_server

## Module Description
一个静态服务器 means "a static server"

## Module Stats
- [14] downloads in the last week
- [116] downloads in the last month

# Vulnerability
##Vulnerability Description
This XSS vulnerability occurs due to the module represents filename(s) in HTML without any sanitization in listing directory page. In a result, any malicious scripts which are injected and stored on the server, would be executed in the client's browser.

##Steps To Reproduce:
- Install the module
```
npm install -g http_server
```
- In the directory which will be served via http_server, create file with following names in directories ~/Desktop/:

```
" onmouseover=alert(1) "
```

or

```
<img src=x onmouseover=alert(1)>
```

{F489070}
- Run 'http_server in "~/Desktop" directory :

```
root@kali:~/Desktop# http_server
server running is :http://localhost:8888
```

- Open http://localhost:8888/
{F489069}
- When mouseover event is triggered on BOTH 2 payloads, a message will be popup via XSS vulnerability.
{F489071}

##Patch
User input should be properly sanitized and filtered both at the client and server side. Dangerous characters such as < > ' " % ; ) ( & + should either be disallowed or HTML encoded before displaying them on screen.

##Supporting Material/References:
- Linux kali 4.15.0-kali2-amd64
- node 10.15.3
- npm 6.9
- Firefox ESR 52.7.3 (64-bit)

##Wrap up
- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows to inject malicious scripts in the file name, store them on the server, then execute these scripts in the browser via the XSS vulnerability.

## Attachments
- http_server_-_XSS1.PNG
- http_server_-_XSS0.PNG
- http_server_-_XSS2.PNG
